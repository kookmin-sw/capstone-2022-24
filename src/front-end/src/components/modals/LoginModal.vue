<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-pb-none q-pt-sm">
			<q-space />
			<q-btn icon="close" flat round dense v-close-popup />
		</q-card-section>

		<q-card-section class="col q-ma-lg" v-if="isActive">
			<h3 class="text-center">온갖</h3>

			<q-btn
				unelevated
				size="md"
				class="full-width google-btn"
				@click="loginWithGoogle">
				<q-icon class="q-ma-sm" name="fas fa-brands fa-google" size="24px" />
				{{ $t('login.google') }}
			</q-btn>
			<q-btn
				unelevated
				size="md"
				class="q-mt-md full-width naver-btn"
				@click="loginWithNaver">
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
	created() {
		window.onSignIn = this.onSignIn;
	},
	methods: {
		loginWithNaver() {
			this.$store.dispatch('auth/requestNaverAuth');
		},
		loginWithGoogle() {
			this.$store.dispatch('auth/requestGoogleAuth');
		},
	},
};
</script>

<style scoped>
.google-btn {
	background: white;
	color: #191919;
	border-radius: 6px;
	border: solid 1px lightgrey;
}

.naver-btn {
	background: #03c75a;
	color: white;
	border: solid 1px #03c75a;
}
.naver-btn img {
	width: 36px;
	height: 36px;
}
</style>
