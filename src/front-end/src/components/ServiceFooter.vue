<template>
	<!--  <q-separator color="blue" inset />-->
	<div class="footer">
		<div class="text-menu-frame row text-left text-grey-8">
			<div>{{ $t('footer.company') }}</div>
			<div>{{ $t('footer.tos') }}</div>
			<div>{{ $t('footer.privacyPolicy') }}</div>
			<div>{{ $t('footer.cs') }}</div>
			<div>{{ $t('footer.qa') }}</div>
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
	/*background-color:yellowgreen;*/
}

.text-menu-frame div {
	margin-right: 12px;
}

.business-info {
	margin-top: 16px;
}
</style>
