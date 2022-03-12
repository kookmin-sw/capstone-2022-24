<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-pb-none q-pt-sm">
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
		</q-card-section>

		<q-card-section class="col text-center q-mb-lg" v-if="isActive">
			<div class="text-h6">{{ $t('afterLoginMsg') }}</div>
			<q-btn flat color="blue">
				<div class="text-underline">{{ $t('goLoginMsg') }}</div>
				<q-icon name="arrow_right_alt" size="md" />
			</q-btn>
		</q-card-section>
	</q-card>
</template>

<script>
export default {
	name: 'AfterLoginModal',
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
