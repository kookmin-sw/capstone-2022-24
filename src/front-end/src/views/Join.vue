<template>
	<!-- 모임 신청 성공 모달  -->
	<q-dialog v-model="isSuccess">
		<join-success-modal :isActive="isSuccess" />
	</q-dialog>
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
					@click="ottFilterClick(index), stepCompletionCheck(index)" />
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
				<div>OTT 및 결제 비용 안내 ~</div>
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
</template>

<script>
import JoinSuccessModal from '@/components/modals/JoinSuccessModal';
export default {
	name: 'Join',
	components: { JoinSuccessModal },
	data() {
		return {
			ottFilters: {
				netflix: { label: '넷플릭스', isSelect: false },
				watcha: { label: '왓챠', isSelect: false },
				disneyPlus: { label: '디즈니플러스', isSelect: false },
				tving: { label: '티빙', isSelect: false },
				wavve: { label: '웨이브', isSelect: false },
			},
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
		};
	},
	methods: {
		ottFilterClick(idx) {
			this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
			if (this.ottFilters[idx].isSelect === true) {
				this.selected.ott.push(this.ottFilters[idx].label);
				for (let i = 0; i < Object.keys(this.ottFilters).length; i++) {
					if (
						this.ottFilters[idx].label !==
						Object.values(this.ottFilters)[i].label
					) {
						Object.values(this.ottFilters)[i].isSelect = false;
						this.selected.ott = this.selected.ott.filter(
							element => element === this.ottFilters[idx].label,
						);
					}
				}
			} else this.selected.ott.splice(this.ottFilters[idx].label, 1);
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
			if (
				this.ottFilters[idx].isSelect &&
				(this.roleSelect.leader || this.roleSelect.member)
			) {
				this.state = false;
			} else this.state = true;
			return this.state;
		},
		async joinBtnClick() {
			const applyer = {
				// TODO: provider Id 수정
				providerId: 1,
				paymentId: null,
			};
			if (this.roleSelect.leader) {
				await this.$store.dispatch('join/applyLeader', applyer);
			} else {
				await this.$store.dispatch('join/applyMember', applyer).then(() => {
					this.isSuccess = true;
				});
			}
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
