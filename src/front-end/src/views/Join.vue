<template>
	<!-- 1단계 영역 -->
	<div class="step-one-frame row q-mt-xl q-mb-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step1') }}</div>
				<div>{{ $t('join.stepTitle1') }}</div>
			</div>
			<div class="row q-mb-lg ott-icons-frame">
				<q-avatar
					rounded
					color="blue"
					size="60px"
					v-for="(otts, index) in ottFilters"
					:key="index"
					:class="{ 'ott-select': otts.isSelect }"
					@click="ottFilterClick(index)" />
				확인: {{ selected.ott }}
			</div>
		</div>
		<q-space class="col-2" />
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 2단계 영역 -->
	<div class="step-two-frame row q-mt-xl q-mb-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step2') }}</div>
				<div>{{ $t('join.stepTitle2') }}</div>
			</div>
			<div class="explanation col text-left q-mb-lg">
				<div class="leader-expl col q-mb-md">
					<div class="text-weight-bold">{{ $t('join.leaderGuideTitle') }}</div>
					<div>{{ $t('join.leaderGuide') }}</div>
					<div>{{ $t('join.leaderPaymentGuide') }}</div>
				</div>
				<div class="member-expl col">
					<div class="text-weight-bold">{{ $t('join.memberGuideTitle') }}</div>
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
					]" />
<!--			<div class="btn-frame row">-->
<!--				<q-btn-->
<!--					outline-->
<!--					color="blue"-->
<!--					class="col leader-button"-->
<!--					@click="roleButtonClick"-->
<!--					>{{ $t('leader') }}</q-btn-->
<!--				>-->
<!--				<q-btn-->
<!--					outline-->
<!--					color="blue"-->
<!--					class="col member-button"-->
<!--					@click="roleButtonClick"-->
<!--					>{{ $t('member') }}</q-btn-->
<!--				>-->
<!--				&lt;!&ndash;        <q-space class="col-2" />&ndash;&gt;-->
<!--			</div>-->
		</div>
		<q-space class="col-2" />
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 3단계 영역 -->
	<div class="step-three-frame row q-mt-xl q-mb-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step3') }}</div>
				<div>{{ $t('join.stepTitle3') }}</div>
			</div>
			<div class="explanation col text-left q-mb-lg">
				<div>OTT 및 결제 비용 안내 ~</div>
			</div>
			<q-btn unelevated color="grey" class="full-width" disabled="true">
				신청하기
			</q-btn>
		</div>
		<q-space class="col-2" />
	</div>
</template>

<script>
export default {
	name: 'Home',
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
		};
	},
	methods: {
		ottFilterClick(idx) {
			this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
			if (this.ottFilters[idx].isSelect === true) {
				this.selected.ott.push(this.ottFilters[idx].label);
			} else this.selected.ott.splice(this.ottFilters[idx].label, 1);
		},
		// roleButtonClick() {
		// 	console.log();
		// },
	},
};
</script>

<style scoped>
.guide-text {
	column-gap: 4px;
}
.guide-text div {
	margin-top: auto;
	margin-bottom: auto;
}
.btn-frame * {
	margin-right: 12px;
}
.ott-icons-frame {
	column-gap: 16px;
}
.ott-select {
	border: 3px solid darkblue;
	border-radius: 7px;
}
.role-toggle-button {
  border: 1px solid #2196f3
}
</style>
