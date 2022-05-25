<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-ma-sm"> </q-card-section>

		<q-card-section class="col text-center q-ma-lg q-mt-none" v-if="isActive">
			<div v-if="role === 'leader'">
				<div class="text-h6">
					<span class="text-blue-200 text-bold">{{ provider }}</span> 모임을
					<span class="text-blue-200 text-bold">모임장</span>으로 신청
					하시겠습니까?
				</div>
				<div class="q-mb-md">
					모임 모집 완료 후 {{ provider }} 계정을 등록하면 마일리지가
					환급됩니다.
				</div>
			</div>
			<div v-else>
				<div class="text-h6">
					<span class="text-blue-200 text-bold">{{ provider }}</span> 모임을
					<span class="text-blue-200 text-bold">모임원</span>으로 신청
					하시겠습니까?
				</div>
				<!--        TODO: ott 요금 정보 추가-->
				<div class="q-mb-md text-h6">
					{{ totalCharge }}원이 마일리지에서 차감됩니다.
				</div>
			</div>
		</q-card-section>

		<q-card-actions align="right">
			<q-btn flat label="취소" color="red" v-close-popup />
			<q-btn
				flat
				label="모임 신청"
				class="text-blue-200"
				@click="clickApply"
				v-close-popup />
		</q-card-actions>
	</q-card>
</template>

<script>
export default {
	name: 'JoinFailModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
		provider: {
			require: true,
		},
		role: {
			type: String,
			require: true,
		},
		totalCharge: {
			require: true,
		},
	},
	methods: {
		clickApply() {
			this.$emit('clickOk', true);
		},
	},
};
</script>

<style scoped></style>
