<template>
	<div class="container">
		<nav class="top-fixed">
			<g-n-b />
		</nav>
		<div class="body-container">
			<router-view />
		</div>
		<footer>
			<service-footer />
		</footer>
	</div>
</template>

<script>
import GNB from '@/components/GNB';
import ServiceFooter from '@/components/ServiceFooter';
export default {
	components: {
		GNB,
		ServiceFooter,
	},
	beforeCreate() {
		this.$store.dispatch('auth/keepLoginToken');
		// this.$store.dispatch('user/setUserProfile');
	},
};
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}

nav {
	z-index: 999;
}

.top-fixed {
	position: sticky;
	top: 0;
}
</style>
