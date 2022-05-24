<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-ma-sm"> </q-card-section>

		<q-card-section class="col text-center q-ma-lg q-mt-none" v-if="isActive">
			<div class="text-h6">{{ $t('join.fail') }}</div>
			<div class="text-grey">{{ $t('join.retry') }}</div>
		</q-card-section>

		<q-card-actions align="right">
			<q-btn flat label="확인" class="text-blue-200" v-close-popup />
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
	},
};
</script>

<style scoped></style>
