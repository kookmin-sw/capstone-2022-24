import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store/index.js';
import Home from '@/views/Home.vue';

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
				// get naver access token (state)
				social = 'naver';
				const code = url.searchParams.get('code');
				const state = url.searchParams.get('state');
				if (code === null) {
					alert('필수 정보 제공에 동의하지 않아 로그인을 취소합니다.');
					next('/');
				}
				const response = {
					code: code,
					resState: state,
				};
				await store.dispatch('auth/setNaverAuth', response);
			} else if (url.pathname === '/login/google') {
				// get google access token
				social = 'google';
				const href = url.hash;
				const hash = href.split('&')[1];
				const token = hash.split('=')[1];
				await store.dispatch('auth/setGoogleAuth', token);
			}
			await store
				.dispatch('auth/loginWithSocial', social)
				.then(() => {
					next('/');
				})
				.catch(() => {
					next('/register');
				});
		},
	},
	{
		// TODO: beforeEnter: url 입력으로 인한 접근 막기
		path: '/register',
		name: 'Register',
		component: () =>
			import(/* webpackChunkName: "Register" */ '@/views/Register.vue'),
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
		path: '/details/:category/:videoId',
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
		path: '/:userId/expand/:listType',
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
	scrollBehavior() {
		return { top: 0, left: 0 };
	},
});

export default router;
