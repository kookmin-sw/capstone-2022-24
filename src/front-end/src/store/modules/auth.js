export const auth = {
	namespaced: true,
	state: {
		token: null,
		userId: 'abc',
		naver: {
			clientId: `HDyG0cg2DID7bPsLQ4_u`,
			redirectionUri: `${window.location.origin}/login/naver`,
			code: null,
			reqState: Math.random().toString(36).substr(2, 11),
			resState: null,
		},
	},
	getters: {
		isLogin(state) {
			return state.token !== null;
		},
	},
	mutations: {
		SET_TOKEN(state, token) {
			state.token = token;
		},
		SET_NAVER_AUTH(state, { code, naverState }) {
			state.naver.code = code;
			state.naver.resState = naverState;
		},
	},
	actions: {
		setToken({ commit }, token) {
			commit('SET_TOKEN', token);
		},
		setNaverAuth({ commit }, { code, naverState }) {
			commit('SET_NAVER_AUTH', { code, naverState });
		},
		getNaverAuth({ state }) {
			const apiUrl = `https://nid.naver.com/oauth2.0/authorize`;
			window.location.href = `${apiUrl}?response_type=code&client_id=${state.naver.clientId}&redirect_uri=${state.naver.redirectionUri}&state=${state.naver.reqState}`;
		},
		loginWithNaver({ dispatch }) {
			dispatch('getNaverAuth');
		},
	},
};
