<template>
	<div class="container">
		<g-n-b />
		<div class="body-container">
			<router-view />
			<footer>
				<q-separator color="blue" inset />
				<service-footer />
			</footer>
		</div>
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

#nav {
	padding: 30px;
}

#nav a {
	font-weight: bold;
	color: #2c3e50;
}

#nav a.router-link-exact-active {
	color: #42b983;
}

.body-container {
	padding-top: 84px;
}
</style>
