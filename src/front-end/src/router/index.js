import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';

import store from '@/store/index.js';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/home',
		redirect: '/',
	},
	{
		path: '/join',
		name: 'Join',
		component: () => import(/* webpackChunkName: "Join" */ '@/views/Join.vue'),
		beforeEnter: (to, from, next) => {
			if (store.getters['auth/isLogin'] === false) {
				alert('로그인 후 사용하실 수 있습니다.');
				next('/');
			} else {
				next();
			}
		},
	},
	{
		path: '/discontinue',
		name: 'Discontinue',
		component: () =>
			import(/* webpackChunkName: "Join" */ '@/views/Discontinue.vue'),
	},
	{
		path: '/details',
		name: 'Details',
		component: () =>
			import(/* webpackChunkName: "Details" */ '@/views/Details.vue'),
	},
	{
		path: '/introduction',
		name: 'Introduction',
		component: () =>
			import(
				/* webpackChunkName: "Introduction" */ '@/views/footer/Introduction.vue'
			),
	},
	{
		path: '/tos',
		name: 'TermsOfService',
		component: () =>
			import(/* webpackChunkName: "Tos" */ '@/views/footer/Tos.vue'),
	},
	{
		path: '/privacy',
		name: 'PrivacyPolicy',
		component: () =>
			import(
				/* webpackChunkName: "Privacy" */ '@/views/footer/PrivacyPolicy.vue'
			),
	},
	{
		path: '/center',
		name: 'Center',
		component: () =>
			import(/* webpackChunkName: "Center" */ '@/views/footer/Center.vue'),
	},
	{
		path: '/questions',
		name: 'Questions',
		component: () =>
			import(
				/* webpackChunkName: "Questions" */ '@/views/footer/Questions.vue'
			),
	},
	{
		path: '/404',
		name: 'NotFound',
		component: () =>
			import(/* webpackChunkName: "NotFound" */ '@/views/NotFound.vue'),
	},
	{
		path: '/:pathMatch(.*)*',
		redirect: '/404',
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
