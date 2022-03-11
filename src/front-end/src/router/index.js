import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/about',
		name: 'About',
		component: () =>
			import(/* webpackChunkName: "about" */ '@/views/About.vue'),
	},
	{
		path: '/join',
		name: 'Join',
		component: () => import(/* webpackChunkName: "Join" */ '@/views/Join.vue'),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
