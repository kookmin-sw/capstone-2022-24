<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-ma-sm"></q-card-section>

		<q-card-section
			className="col text-center q-ma-lg q-mt-none"
			v-if="isActive">
			<div class="text-h6">모임 탈퇴에 실패했습니다.</div>
			<div>다시 시도해주세요.</div>
		</q-card-section>

		<q-card-actions align="right">
			<q-btn flat label="확인" v-close-popup />
		</q-card-actions>
	</q-card>
</template>

<script>
export default {
	name: 'LeaveGroupSuccess',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
	methods: {},
};
</script>

<style scoped></style>
