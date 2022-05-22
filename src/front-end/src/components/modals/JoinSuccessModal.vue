<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-pb-none q-pt-sm">
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
		</q-card-section>

		<q-card-section class="col text-center q-ma-lg q-mt-none" v-if="isActive">
			<div class="text-h6">{{ $t('join.success') }}</div>
			<q-btn flat color="blue" @click="this.$router.push({ name: 'My' })">
				<div class="text-underline">{{ $t('join.goGroupState') }}</div>
				<q-icon name="arrow_right_alt" size="md" />
			</q-btn>
		</q-card-section>
	</q-card>
</template>

<script>
export default {
	name: 'JoinSuccessModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
};
</script>

<style scoped></style>
