<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-ma-sm"> </q-card-section>

		<q-card-section class="col text-center q-ma-lg q-mt-none" v-if="isActive">
			<div>
				<div class="text-h6">정말 모임을 탈퇴하시겠습니까?</div>
				<div class="q-mb-md">
					탈퇴 예약 상태가 되며, 모임이 종료 후 자동으로 모임에서 탈퇴됩니다.
				</div>
			</div>
		</q-card-section>

		<q-card-actions align="right">
			<q-btn flat label="취소" color="red" v-close-popup />
			<q-btn
				flat
				label="모임 탈퇴"
				class="text-blue-200"
				@click="clickLeave"
				v-close-popup />
		</q-card-actions>
	</q-card>
</template>

<script>
export default {
	name: 'LeaveGroupModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
	methods: {
		clickLeave() {
			this.$emit('clickLeave');
		},
	},
};
</script>

<style scoped></style>
