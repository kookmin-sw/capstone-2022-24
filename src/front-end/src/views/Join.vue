<template>
	<!-- 1단계 영역 -->
	<div class="step-one-frame row q-mt-xl q-mb-xl">
		<q-space class="col-2" />
		<div class="col-8">
			<div class="guide-text row text-left q-mb-md">
				<div class="text-h6 text-weight-bold">{{ $t('join.step1') }}</div>
				<div>{{ $t('join.stepTitle1') }}</div>
			</div>
			<div class="ott-icons-frame row">
				<q-avatar rounded color="blue" size="60px"></q-avatar>
				<q-avatar rounded color="blue" size="60px"></q-avatar>
				<q-avatar rounded color="blue" size="60px"></q-avatar>
				<q-avatar rounded color="blue" size="60px"></q-avatar>
				<q-avatar rounded color="blue" size="60px"></q-avatar>
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
			<div class="btn-frame row">
				<q-btn outline color="blue" class="col">{{ $t('leader') }}</q-btn>
				<q-btn outline color="blue" class="col">{{ $t('member') }}</q-btn>
				<!--        <q-space class="col-2" />-->
			</div>
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
			<div class="explanationn col text-left q-mb-lg">
				<div>OTT 및 결제 비용 안내 ~</div>
			</div>
			<q-btn unelevated color="blue" class="full-width" disabled="true">
				신청하기
			</q-btn>
		</div>
		<q-space class="col-2" />
	</div>
</template>

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
</style>
