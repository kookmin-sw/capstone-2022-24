<template>
	<q-card style="width: 480px; max-width: 60vw; height: 100%; max-height: 70vh;" v-if="isActive">
		<!--    alarm title    -->
		<q-card-section class="row items-center q-pb-none q-pt-sm">
			<div class="text-subtitle1 text-weight-bold q-pt-auto q-pb-auto">
				<q-icon name="notifications_none" size="md" color="blue" />
				{{ $t('gnb.alarm') }}
			</div>
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup class="" />
			<div class="q-ml-sm q-mr-lg text-blue text-weight-bold">
				모든 알림은 확인 여부와 상관없이 전송 후 30일 뒤 삭제됩니다.
			</div>
		</q-card-section>

		<!--    delete button   -->
		<q-card-section class="col text-right q-ma-none q-mr-lg" v-if="isActive">
			<q-btn flat>전체 읽음 표시</q-btn>
			<q-btn flat>읽은 알림 삭제</q-btn>
			<q-btn flat>전체 삭제</q-btn>
		</q-card-section>
		<q-separator color="blue" />

		<!--    msg 1   -->
		<q-separator color="blue" />
		<q-card-section
			class="row text-center q-mt-md q-mr-lg q-mb-sm q-ml-lg"
			v-if="isActive">
			<div class="text-left col-11">
				<span class="q-mr-sm text-weight-bold">모임 알림</span>
				<span>구독 종료까지 3일 남았습니다!</span>
				<div class="text-grey-8">넷플릭스 모임 구독 종료일 - 6월 30일</div>
				<q-space />
				<div class="text-right q-mt-sm text-grey">6월 28일</div>
			</div>
			<div class="col-1">
				<q-btn icon="close" flat round dense color="blue" size="sm" />
			</div>
		</q-card-section>
		<!--    msg 2   -->
		<q-separator color="grey" />
		<q-card-section
			class="row text-center q-mt-md q-mr-lg q-mb-sm q-ml-lg"
			v-if="isActive">
			<div class="text-left col-11">
				<span class="q-mr-sm text-weight-bold">결제 알림</span>
				<span>왓챠 구독 후 계정 정보를 등록해주세요!</span>
				<div class="text-grey-8">왓챠 모임 결제 요청</div>
				<q-space />
				<div class="text-right q-mt-sm text-grey">5월 31일</div>
			</div>
			<div class="col-1">
				<q-btn icon="close" flat round dense color="blue" size="sm" />
			</div>
		</q-card-section>
	</q-card>
</template>
<script>
export default {
	name: 'AlarmModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
};
</script>

<style scoped></style>
