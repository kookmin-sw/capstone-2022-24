<template>
	<!-- 1단계 영역 -->
	<div class="step-one-frame row q-ma-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step1') }}</div>
				<div>{{ $t('join.stepTitle1') }}</div>
			</div>
			<div class="row col-gap-12"><!--12가 나은지 16이 나은지 모르겠다... 컨테이너 마진은 48이라 두 값 다 배수이긴 한데..-->
				<q-avatar
					rounded
					color="blue"
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
	<q-separator color="blue" inset />
	<!-- 2단계 영역 -->
	<div class="step-two-frame row q-ma-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step2') }}</div>
				<div>{{ $t('join.stepTitle2') }}</div>
			</div>
			<div class="explanation col text-left">
				<div class="leader-expl col q-mb-md">
					<div
						class="text-weight-bold leader-title"
						:class="{ 'role-select-text': roleSelect.leader }">
						{{ $t('join.leaderGuideTitle') }}
					</div>
					<div>{{ $t('join.leaderGuide') }}</div>
					<div>{{ $t('join.leaderPaymentGuide') }}</div>
				</div>
				<div class="member-expl col q-mb-md">
					<div
						class="text-weight-bold member-title"
						:class="{ 'role-select-text': roleSelect.member }">
						{{ $t('join.memberGuideTitle') }}
					</div>
					<div>{{ $t('join.memberGuide') }}</div>
					<div>{{ $t('join.memberPaymentGuide') }}</div>
				</div>
			</div>
			<q-btn-toggle
				v-model="role"
				spread
				class="role-toggle-button"
				unelevated
				toggle-color="blue"
				text-color="blue"
				:options="[
					{ label: '모임장', value: 'leader' },
					{ label: '모임원', value: 'member' },
				]"
				@click="roleButtonClick(), stepCompletionCheck()" />
		</div>
		<q-space class="col-2" />
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 3단계 영역 -->
	<div class="step-three-frame row q-ma-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step3') }}</div>
				<div>{{ $t('join.stepTitle3') }}</div>
			</div>
			<div class="explanation col text-left q-mb-md">
				<div>OTT 및 결제 비용 안내 ~</div>
			</div>
			<q-btn
				unelevated
				color="blue"
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
export default {
	name: 'Join',
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
		joinBtnClick() {
			alert('모임 신청이 완료되었습니다!');
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
/*.btn-frame * {*/
/*	margin-right: 12px;*/
/*} 현재 페이지에서 쓰이지 않는 스타일*/
/*.ott-icons-frame {*/
/*	column-gap: 16px;*/
/*} col-gap-n css 클래스 적용하기로 변경*/
.ott-select {
	border: 3px solid darkblue;
	border-radius: 7px;
}
.role-toggle-button {
	border: 1px solid #2196f3;
}
.role-select-text {
	color: #2196f3;
}
</style>
