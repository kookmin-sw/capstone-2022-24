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
			await http.get(url).then(res => {
				commit('SET_APPLIED', res.data.appliedProviders);
				commit('SET_NOT_APPLIED', res.data.notAppliedProviders);
			});
		},
		async applyGroup(context, applyer) {
			const url = `/applies/${applyer.role}/`;
			const data = {
				providerId: applyer.providerId,
			};
			return new Promise((resolve, reject) => {
				http
					.post(url, data)
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},
		async LeaveGroup(context, id) {
			console.log('leave group', id);
			// TODO: member, leader 변수
			// TODO: 변경된 api requeset 확인, 적용
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			const role = 'member';
			const url = `/applies/${role}/`;
			const data = {
				provideId: id,
			};
			await http.put(url, data, { headers }).then(res => {
				console.log(res);
			});
		},
	},
};
