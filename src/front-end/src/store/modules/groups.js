import http from '@/api/http';

export const groups = {
	namespaced: true,
	state: {
		applied: [],
		notApplied: [],
	},
	getters: {},
	mutations: {
		SET_APPLIED(state, providers) {
			state.applied = providers;
		},
		SET_NOT_APPLIED(state, providers) {
			state.notApplied = providers;
		},
	},
	actions: {
		async joinProviders({ commit }) {
			const url = `/providers`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http.get(url, { headers }).then(res => {
				console.log(res.data);
				commit('SET_APPLIED', res.data.appliedProviders);
				commit('SET_NOT_APPLIED', res.data.notAppliedProviders);
			});
		},
		async applyGroup(context, applyer) {
			// TODO: 엔드포인트 변경 예정 (PR중)
			const url = `/applies/${applyer.role}/`;
			console.log(url);
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			const data = {
				providerId: applyer.providerId,
				paymentId: applyer.paymentId,
			};
			return new Promise((resolve, reject) => {
				http
					.post(url, data, { headers })
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},
		async LeaveGroup() {
			console.log('leave group');
		},
	},
};
