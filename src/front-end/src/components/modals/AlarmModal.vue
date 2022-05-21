<template>
	<q-card
		style="width: 480px; max-width: 60vw; height: 100%; max-height: 70vh"
		v-if="isActive">
		<!--    alarm title    -->
		<q-card-section class="row items-center q-ma-sm">
			<q-icon name="notifications" size="md" class="text-blue-200" />
			<div class="text-h6 text-weight-bold q-ml-sm">
				{{ $t('gnb.alarm') }}
			</div>
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
			<div class="q-ma-sm text-blue-200 text-weight-bold">
				모든 알림은 확인 여부와 상관없이 전송 후 30일 뒤 삭제됩니다.
			</div>
		</q-card-section>
		<!-- separator -->
		<q-separator color="blue-4" />
		<q-separator color="blue-4" />

		<!--    msg 1   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">모임 알림</span>
				<span>구독 종료까지 3일 남았습니다!</span>
				<div class="text-grey q-mt-xs">
					넷플릭스 모임 구독 종료일 - 5월 25일
				</div>
				<div class="text-right text-grey">5월 22일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 2   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">결제 알림</span>
				<span>왓챠 구독 후 계정 정보를 등록해주세요!</span>
				<div class="text-grey q-mt-xs">왓챠 모임 결제 요청</div>
				<div class="text-right text-grey">5월 1일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 3   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">모임 알림</span>
				<span>모임 모집이 완료되었습니다!</span>
				<div class="text-grey q-mt-xs">왓챠 모임 모집 완료 - 4월 29일</div>
				<div class="text-right text-grey">4월 29일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 4   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">모임 알림</span>
				<span>넷플릭스 계정 정보가 등록되었습니다!</span>
				<div class="text-grey q-mt-xs">넷플릭스 모임 계정 정보 등록 알림</div>
				<div class="text-right text-grey">4월 27일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
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
