<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-pb-none q-pt-sm">
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
		</q-card-section>

		<q-card-section
			class="col text-center vertical-middle q-mt-none q-ma-lg"
			v-if="isActive">
			<q-avatar rounded size="60px" color="blue" class="q-mt-none"></q-avatar>
			<div class="text-h6 text-center col-10 q-mt-md">
				익명님은 해당 OTT 모임에 가입되어 있지 않습니다.
			</div>
			<q-btn unelevated color="blue" class="full-width q-mt-md">
				{{ $t('goJoinMsg') }}
			</q-btn>
			<q-btn flat color="blue" class="full-width">
				<div class="text-underline">OTT 홈 페이지로 바로가기</div>
				<q-icon name="arrow_right_alt" size="md" />
			</q-btn>
		</q-card-section>
	</q-card>
</template>

<script>
export default {
	name: 'MakeJoinModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
};
</script>

<style scoped></style>
