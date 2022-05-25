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
		async getMileageHistory({ state, commit }) {
			const url = `/mileages/`;
			await http.get(url).then(res => {
				console.log(res.data);
				commit('SET_MILEAGE_HISTORY', res.data);
				console.log(state.histories);
			});
		},
	},
};
