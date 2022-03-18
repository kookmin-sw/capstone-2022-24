<template>
	<!--  <q-separator color="blue" inset />-->
	<div class="footer">
		<div class="footer-menu-frame row text-left">
			<router-link to="/introduction">{{ $t('footer.company') }}</router-link>
			<router-link to="/tos">{{ $t('footer.tos') }}</router-link>
			<router-link to="/privacy">{{ $t('footer.privacyPolicy') }}</router-link>
			<router-link to="/center">{{ $t('footer.cs') }}</router-link>
			<router-link to="/questions">{{ $t('footer.qa') }}</router-link>
		</div>
		<div class="business-info col">
			<div class="row text-left text-grey">{{ $t('footer.businessInfo') }}</div>
			<div class="row text-left text-grey">{{ $t('footer.copyright') }}</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Footer',
};
</script>

<style scoped>
.footer {
	height: 170px;
	padding: 40px 30px 56px 30px;
}

.footer-menu-frame * {
	margin-right: 12px;
}

.business-info {
	margin-top: 16px;
}
</style>
