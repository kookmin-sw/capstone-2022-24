<template>
	<q-card
		style="width: 480px; max-width: 60vw; height: 100%; max-height: 70vh"
		v-if="isActive">
		<!--    mileage history title    -->
		<q-card-section class="row items-center q-ma-sm">
			<q-icon name="currency_exchange" size="md" class="text-blue-200" />
			<div class="text-h6 text-weight-bold q-ml-sm">
				마일리지(정직 비용) 내역조회
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
				<span class="q-mr-sm text-weight-bold">충전 알림</span>
				<span>정직 비용 2,000원이 추가되었습니다!</span>
				<div class="text-grey q-mt-xs">아마존 프라임 모임 무사 종료금</div>
				<div class="text-right text-grey">5월 26일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 2   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">사용 알림</span>
				<span>?원이 사용되었습니다!</span>
				<div class="text-grey q-mt-xs">라프텔 모임 결제</div>
				<div class="text-right text-grey">5월 1일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 3   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">사용 알림</span>
				<span>?원이 사용되었습니다!</span>
				<div class="text-grey q-mt-xs">아마존 프라임 모임 결제</div>
				<div class="text-right text-grey">4월 28일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
		<!--    msg 4   -->
		<q-card-section class="text-center" v-if="isActive">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg">
				<span class="q-mr-sm text-weight-bold">충전 알림</span>
				<span>?원이 충전되었습니다!</span>
				<div class="text-grey q-mt-xs">우리카드 2056 자동 충전</div>
				<div class="text-right text-grey">4월 21일</div>
			</div>
		</q-card-section>
		<q-separator color="grey-4" />
	</q-card>
</template>

<script>
export default {
	name: 'MileageModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
};
</script>

<style scoped></style>
