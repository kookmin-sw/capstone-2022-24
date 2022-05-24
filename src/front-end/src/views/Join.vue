<template>
	<!-- 모임 신청 성공 모달  -->
	<q-dialog v-model="isSuccess">
		<join-success-modal :isActive="isSuccess" />
	</q-dialog>
	<!-- 모임 신청 실패 모달 -->
	<q-dialog v-model="isFail">
		<join-fail-modal :isActive="isFail" />
	</q-dialog>
	<!-- 결제, 신청 확인 모달 -->
	<q-dialog v-model="isPayment" persistent>
		<payment-modal
			@clickOk="applyGroup"
			:isActive="isPayment"
			:provider="selected.ott[0]"
			:role="role" />
	</q-dialog>
	<!-- 모든 ott 신청했을 때 -->
	<div v-if="!notApplied.length" style="height: 50vh">
		<div style="position: relative; top: 45%">
			<div class="text-h6 text-bold">
				신청 가능한 모든 OTT 모임에 참여 중입니다.
			</div>
			<q-btn flat color="blue" @click="this.$router.push({ name: 'My' })">
				<div class="text-underline">내 정보에서 모임 확인하기</div>
				<q-icon name="arrow_right_alt" size="md" />
			</q-btn>
		</div>
	</div>
	<div v-else>
		<!-- 1단계 영역 -->
		<div class="step-one-frame row q-ma-xl">
			<q-space class="col-2" />
			<div class="col-8">
				<div class="guide-text row text-left q-mb-md">
					<div class="text-h6 text-weight-bold">{{ $t('join.step1') }}</div>
					<div class="text-weight-bold">{{ $t('join.stepTitle1') }}</div>
				</div>
				<div class="row col-gap-12">
					<q-avatar
						rounded
						color="grey-4"
						size="60px"
						v-for="(otts, index) in ottFilters"
						:key="index"
						:class="{ 'ott-select': otts.isSelect }"
						@click="ottFilterClick(index), stepCompletionCheck(index)">
						<img :src="otts.logoUrl" :alt="otts.name" />
					</q-avatar>
				</div>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator color="blue-1" size="2px" inset />
		<q-separator color="blue-4" inset />
		<!-- 2단계 영역 -->
		<div class="step-two-frame row q-ma-xl">
			<q-space class="col-2" />
			<div class="col-8">
				<div class="guide-text row text-left q-mb-md">
					<div class="text-h6 text-weight-bold">{{ $t('join.step2') }}</div>
					<div class="text-weight-bold">{{ $t('join.stepTitle2') }}</div>
				</div>
				<div class="explanation col text-left">
					<div class="leader-expl col q-mb-md">
						<div
							class="text-weight-bold leader-title"
							:class="{ 'text-blue-100': roleSelect.leader }">
							{{ $t('join.leaderGuideTitle') }}
						</div>
						<div>{{ $t('join.leaderGuide') }}</div>
						<div>{{ $t('join.leaderPaymentGuide') }}</div>
					</div>
					<div class="member-expl col q-mb-md">
						<div
							class="text-weight-bold member-title"
							:class="{ 'text-blue-100': roleSelect.member }">
							{{ $t('join.memberGuideTitle') }}
						</div>
						<div>{{ $t('join.memberGuide') }}</div>
						<div>{{ $t('join.memberPaymentGuide') }}</div>
					</div>
				</div>
				<q-btn-toggle
					v-model="role"
					spread
					class="border-blue-100 text-blue-100"
					style="border-radius: 4px"
					unelevated
					toggle-color="blue-4"
					:options="[
						{ label: '모임장', value: 'leader' },
						{ label: '모임원', value: 'member' },
					]"
					@click="roleButtonClick(), stepCompletionCheck()" />
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator color="blue-1" size="2px" inset />
		<q-separator color="blue-4" inset />
		<!-- 3단계 영역 -->
		<div class="step-three-frame row q-ma-xl">
			<q-space class="col-2" />
			<div class="col-8">
				<div class="guide-text row text-left q-mb-md">
					<div class="text-h6 text-weight-bold">{{ $t('join.step3') }}</div>
					<div class="text-weight-bold">{{ $t('join.stepTitle3') }}</div>
				</div>
				<div class="explanation col text-left q-mb-md">
					<div v-if="!selected.ott[0]">신청할 OTT 서비스를 선택해주세요.</div>
					<div v-else>
						<div>
							{{ selected.ott.join(' ') }}(을)를 {{ role }}(으)로 신청합니다.
						</div>
						<div>결제 금액은 5,500원 입니다.</div>
					</div>
				</div>
				<q-btn
					unelevated
					color="blue-4"
					class="full-width"
					:disabled="state"
					@click="joinBtnClick">
					신청하기
				</q-btn>
			</div>
			<q-space class="col-2" />
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex';
import JoinSuccessModal from '@/components/modals/JoinSuccessModal';
import PaymentModal from '@/components/modals/PaymentModal';
import JoinFailModal from '@/components/modals/JoinFailModal';
export default {
	name: 'Join',
	components: { JoinFailModal, JoinSuccessModal, PaymentModal },
	data() {
		return {
			ottFilters: {},
			selected: {
				ott: [],
			},
			role: 'leader',
			roleSelect: {
				leader: true,
				member: false,
			},
			state: true,
			isSuccess: false,
			isFail: false,
			isPayment: false,
		};
	},
	async created() {
		await this.$store.dispatch('groups/joinProviders');
		this.notApplied.forEach(provider => {
			this.ottFilters[provider.name] = provider;
			this.ottFilters[provider.name]['isSelect'] = false;
		});
	},
	computed: {
		...mapState('groups', ['notApplied', 'applied']),
	},
	methods: {
		ottFilterClick(idx) {
			this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
			if (this.ottFilters[idx].isSelect === true) {
				this.selected.ott.push(this.ottFilters[idx].name);
				for (let i = 0; i < Object.keys(this.ottFilters).length; i++) {
					if (
						this.ottFilters[idx].name !== Object.values(this.ottFilters)[i].name
					) {
						Object.values(this.ottFilters)[i].isSelect = false;
						this.selected.ott = this.selected.ott.filter(
							element => element === this.ottFilters[idx].name,
						);
					}
				}
			} else this.selected.ott.splice(this.ottFilters[idx].name, 1);
		},
		roleButtonClick() {
			if (this.role === 'member') {
				this.roleSelect.leader = false;
				this.roleSelect.member = true;
			} else {
				this.roleSelect.leader = true;
				this.roleSelect.member = false;
			}
		},
		stepCompletionCheck(idx) {
			this.state = !(
				this.ottFilters[idx].isSelect &&
				(this.roleSelect.leader || this.roleSelect.member)
			);
			return this.state;
		},
		joinBtnClick() {
			this.isPayment = true;
		},
		async applyGroup() {
			const provider = this.selected.ott[0];
			const applyer = {
				providerId: this.ottFilters[provider].id,
				paymentId: null,
				role: this.role,
			};
			this.$store
				.dispatch('groups/applyGroup', applyer)
				.then(() => {
					console.log('성공!');
					this.isSuccess = true;
					window.location.href();
				})
				.catch(() => {
					console.log('실패!');
					this.isFail = true;
				});
		},
	},
};
</script>

<style scoped>
.guide-text {
	column-gap: 8px;
}
.guide-text div {
	margin-top: auto;
	margin-bottom: auto;
}
.ott-select {
	border: 3px solid #449bfe; /*blue-200*/
	border-radius: 4px;
}
</style>
