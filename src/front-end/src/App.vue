<template>
	<div class="container">
		<nav class="top-fixed">
			<g-n-b />
		</nav>
		<div class="body-container">
			<router-view />
		</div>
		<footer>
			<q-separator color="blue" inset />
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
	// created() {
	// 	this.setMsg();
	// },
	// methods: {
	// 	setMsg() {
	// 		this.$store.dispatch('mockTest/setMsg');
	// 	},
	// },
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
