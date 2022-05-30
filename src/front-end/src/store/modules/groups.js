import http from '@/api/http';

export const groups = {
	namespaced: true,
	state: {
		applied: [],
		notApplied: [],
		isLack: false,
		isChangeFail: false,
	},
	getters: {},
	mutations: {
		SET_APPLIED(state, providers) {
			state.applied = providers;
		},
		SET_NOT_APPLIED(state, providers) {
			state.notApplied = providers;
		},
		SET_LACK_MILEAGE(state, status) {
			state.isLack = status;
		},
		SET_CHANGE_FAIL(state, status) {
			state.isChangeFail = status;
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
			console.log('apply url:', url);
			const data = {
				providerId: applyer.providerId,
			};

			return new Promise((resolve, reject) => {
				http
					.post(url, data)
					.then(res => {
						console.log(url, res.data);
						// commit('SET_LACK_MILEAGE', false);
						// http.patch('/mileages/', { amount: applyer.amount }).then();
						resolve();
					})
					.catch(() => {
						// if (err.response.status === 400 && applyer.role === 'member') {
						// 	commit('SET_LACK_MILEAGE', true);
						// }
						reject();
					});
			});
		},
		async LeaveGroup(context, group) {
			const url = `/applies/${group.role}/`;
			console.log('leaveUrl:', url);
			const data = {
				providerId: group.id,
			};
			return new Promise((resolve, reject) => {
				http
					.put(url, data)
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},

		async editAccount({ commit }, account) {
			let url = `/groups/${account.groupId}/account/id/`;
			let data = {
				identifier: account.identifier,
			};
			await http
				.patch(url, data)
				.then(() => {
					commit('SET_CHANGE_FAIL', false);
				})
				.catch(() => {
					commit('SET_CHANGE_FAIL', true);
				});
			url = `groups/${account.groupId}/account/password/`;
			data = {
				password: account.password,
			};
			await http
				.patch(url, data)
				.then(() => {
					commit('SET_CHANGE_FAIL', false);
				})
				.catch(() => {
					commit('SET_CHANGE_FAIL', true);
				});
		},
	},
};
