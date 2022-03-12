<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-pb-none">
			<div class="text-h6">{{ $t('gnb.login') }}</div>
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
		</q-card-section>

		<q-card-section class="col q-ma-lg" v-if="isActive">
			<h3 class="text-center">온갖</h3>
			<q-btn unelevated class="kakao-btn full-width" size="md">
				<q-icon
					class="q-ma-sm"
					name="fas fa-solid fa-comment"
					size="24px"
					color="#191919" />
				{{ $t('login.kakao') }}
			</q-btn>
			<q-btn unelevated class="naver-btn full-width q-mt-md" size="md">
				<img src="@/assets/naver-circle-logo.png" class="q-mr-xs" alt="" />
				{{ $t('login.naver') }}
			</q-btn>
		</q-card-section>
	</q-card>
</template>

<script>
export default {
	name: 'LoginModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
};
</script>

<style scoped>
.kakao-btn {
	background: #fee500;
	color: #191919;
	border-radius: 6px;
}

.naver-btn {
	background: #03c75a;
	color: white;
}
.naver-btn img {
	width: 36px;
	height: 36px;
}
</style>
