<template>
	<q-card
		style="width: 480px; max-width: 60vw; height: 100%; max-height: 70vh"
		v-if="isActive">
		<!--    mileage history title    -->
		<q-card-section class="row items-center q-ma-sm">
			<q-icon name="currency_exchange" size="md" class="text-blue-200" />
			<div class="text-h6 text-weight-bold q-ml-sm">
				정직 비용 충천/사용 내역조회
			</div>
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
			<div class="q-ma-sm text-blue-200 text-weight-bold">
				모든 알림은 확인 여부와 상관없이 30일 뒤 삭제됩니다.
			</div>
		</q-card-section>
		<!-- separator -->
		<q-separator color="blue-4" />
		<q-separator color="blue-4" />

		<q-card-section class="text-center" v-if="!histories.length">
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg text-bold">
				최근 30일간 충전/사용 내역이 없습니다.
			</div>
		</q-card-section>

		<!-- TODO: histories, histories[0] 확인-->
		<q-card-section
			class="text-center"
			v-for="history in histories[0]"
			:key="history">
			<!-- 충전 -->
			<div
				class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg"
				v-if="history.amount > 0">
				<span class="q-mr-sm text-weight-bold">충전 알림</span>
				<div class="q-mt-xs">
					정직 비용 {{ history.amount }}원이 추가되었습니다!
				</div>
				<div class="text-right text-grey">{{ history.renewalDateTime }}</div>
			</div>
			<!-- 사용 -->
			<div class="text-left q-mt-sm q-mb-sm q-ml-lg q-mr-lg" v-else>
				<span class="q-mr-sm text-weight-bold">사용 알림</span>
				<div class="q-mt-xs">{{ history.amount }}원이 사용되었습니다!</div>
				<div class="text-right text-grey">{{ history.renewalDateTime }}</div>
			</div>
			<q-separator color="grey-4" />
		</q-card-section>
	</q-card>
</template>

<script>
import { mapState } from 'vuex';

export default {
	name: 'MileageModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
	beforeCreate() {
		this.$store.dispatch('mileage/getMileageHistory');
	},
	computed: {
		...mapState('mileage', ['histories']),
	},
};
</script>

<style scoped></style>
