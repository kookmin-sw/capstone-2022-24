export const auth = {
	namespaced: true,
	state: {
		token: null,
		userId: 'abc',
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
	},
	actions: {
		setToken({ commit }, token) {
			commit('SET_TOKEN', token);
		},
	},
};
