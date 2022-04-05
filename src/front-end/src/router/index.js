import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';

import store from '@/store/index.js';

const onlyAuthUser = (to, from, next) => {
	if (store.getters['auth/isLogin'] === false) {
		alert('로그인 후 사용하실 수 있습니다.');
		next('/');
	} else {
		next();
	}
};

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/login/:social',
		name: 'LoginCallback',
		async beforeEnter(to, from, next) {
			const url = new URL(window.location.href);
			let social = null;
			if (url.pathname === '/login/naver') {
				// 네이버가 url로 넘겨준 code, state를 vuex 변수에 저장
				social = 'naver';
				const code = url.searchParams.get('code');
				const state = url.searchParams.get('state');
				const response = {
					code: code,
					resState: state,
				};
				await store.dispatch('auth/setNaverAuth', response);
			} else if (url.pathname === '/login/google') {
				// 구글이 hash로 넘겨준 token을 vuex 변수에 저장
				social = 'google';
				const href = url.hash;
				const hash = href.split('&')[1];
				const token = hash.split('=')[1];
				await store.dispatch('auth/setGoogleAuth', token);
			}
			await store.dispatch('auth/loginWithSocial', social);
			next('/');
		},
	},
	{
		path: '/join/:userId',
		name: 'Join',
		component: () => import(/* webpackChunkName: "Join" */ '@/views/Join.vue'),
		beforeEnter: onlyAuthUser,
	},
	{
		path: '/discontinue',
		name: 'Discontinue',
		component: () =>
			import(/* webpackChunkName: "Join" */ '@/views/Discontinue.vue'),
	},
	{
		path: '/details/:videoId',
		name: 'Details',
		component: () =>
			import(/* webpackChunkName: "Details" */ '@/views/Details.vue'),
	},
	{
		path: '/my/:userId',
		name: 'My',
		component: () => import(/* webpackChunkName: "My" */ '@/views/My.vue'),
		beforeEnter: onlyAuthUser,
	},
	{
		path: '/expand',
		name: 'Expand',
		component: () =>
			import(/* webpackChunkName: "Expand" */ '@/views/Expand.vue'),
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
