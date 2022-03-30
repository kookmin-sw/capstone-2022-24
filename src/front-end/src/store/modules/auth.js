import http from '@/api/http';

export const auth = {
	namespaced: true,
	state: {
		token: null,
		userId: 'abc',
		isRegister: null,
		naver: {
			clientId: `HDyG0cg2DID7bPsLQ4_u`,
			redirectionUri: `${window.location.origin}/login/naver`,
			code: null,
			resState: null,
		},
		google: {
			clientId: `111000957224-lu56fk9cgkavoika3b1b9872vv0lri8q.apps.googleusercontent.com`,
			redirectionUri: `${window.location.origin}/login/google`,
			token: null,
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
		SET_REGISTER(state, isRegister) {
			state.isRegister = isRegister;
		},
		SET_NAVER_AUTH(state, response) {
			state.naver.code = response.code;
			state.naver.resState = response.resState;
		},
		SET_GOOGLE_AUTH(state, token) {
			state.google.token = token;
		},
	},
	actions: {
		setToken({ commit }, token) {
			commit('SET_TOKEN', token);
		},
		setNaverAuth({ commit }, response) {
			commit('SET_NAVER_AUTH', response);
		},
		setGoogleAuth({ commit }, response) {
			commit('SET_GOOGLE_AUTH', response);
		},
		async requestNaverAuth({ state }) {
			// 네이버 로그인 호출
			const reqState = Math.random().toString(36).substr(2, 11);
			const apiUrl = `https://nid.naver.com/oauth2.0/authorize`;
			// 로그인 성공 후 리디렉션 (로그인 버튼 클릭한 페이지로 이동하게끔 라우터에서 처리)
			window.location.href = `${apiUrl}?response_type=code&client_id=${state.naver.clientId}&redirect_uri=${state.naver.redirectionUri}&state=${reqState}`;
		},
		async requestGoogleAuth({ state }) {
			const reqState = Math.random().toString(36).substr(2, 11);
			const apiUrl = `https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly&include_granted_scopes=true&response_type=token`;
			window.location.href = `${apiUrl}&state=${reqState}&redirect_uri=${state.google.redirectionUri}&client_id=${state.google.clientId}`;
		},
		async loginWithSocial({ state, commit }, social) {
			const url = `/login/oauth/${social}`;
			http
				.post(url, { code: state.naver.code })
				.then(res => {
					// 로그인 성공
					const token = res.data.accessToken;
					commit('SET_REGISTER', true);
					commit('SET_TOKEN', token);
					// TODO: access token 저장해서 로그인 유지
				})
				.catch(err => {
					// 최초 로그인 시도 (회원가입)
					if (err.response.status === 301) {
						commit('SET_REGISTER', false);
					}
				});
		},
	},
};
