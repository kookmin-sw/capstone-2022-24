import http from '@/api/http';

export const mileage = {
	namespaced: true,
	state: {
		histories: [],
	},
	getters: {},
	mutations: {
		SET_MILEAGE_HISTORY(state, history) {
			state.histories = history;
		},
	},
	actions: {
		async getMileageHistory({ commit }) {
			const url = `/mileages/`;
			await http.get(url).then(res => {
				commit('SET_MILEAGE_HISTORY', res.data);
			});
		},
	},
};
