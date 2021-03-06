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
		async applyGroup({ commit }, applyer) {
			const url = `/applies/${applyer.role}/`;
			const data = {
				providerId: applyer.providerId,
			};

			return new Promise((resolve, reject) => {
				http
					.post(url, data)
					.then(() => {
						commit('SET_LACK_MILEAGE', false);
						http.patch('/mileages/', { amount: applyer.amount }).then();
						resolve();
					})
					.catch(err => {
						if (err.response.status === 400 && applyer.role === 'member') {
							commit('SET_LACK_MILEAGE', true);
						}
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
