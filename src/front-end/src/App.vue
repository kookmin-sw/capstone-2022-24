<template>
	<div class="container">
		<g-n-b></g-n-b>
		<div class="body-container">
			<div id="nav">
				<router-link to="/">Home</router-link> |
				<router-link to="/about">About</router-link>
			</div>
			<router-view />
		</div>
	</div>
</template>

<script>
import GNB from '@/components/GNB';
export default {
	components: {
		GNB,
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
