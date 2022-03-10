<template>
	<!--  <q-separator color="blue" inset />-->
	<div class="footer">
		<div class="text-menu-frame row text-left text-grey-8">
			<div>{{ $t('company') }}</div>
			<div>{{ $t('tos') }}</div>
			<div>{{ $t('privacyPolicy') }}</div>
			<div>{{ $t('cs') }}</div>
			<div>{{ $t('qa') }}</div>
		</div>
		<div class="business-info col">
			<div class="row text-left text-grey">{{ $t('businessInfo') }}</div>
			<div class="row text-left text-grey">{{ $t('copyright') }}</div>
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
