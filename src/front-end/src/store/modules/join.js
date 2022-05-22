import http from '@/api/http';

export const join = {
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
				commit('SET_APPLIED', res.data.appliedProviders);
				commit('SET_NOT_APPLIED', res.data.notAppliedProviders);
			});
		},
		async applyMember(context, applyer) {
			const url = `applies/member/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			return new Promise((resolve, reject) => {
				http
					.post(url, applyer, { headers })
					.then(() => {
						console.log('모임원 모임 신청 성공');
						resolve();
					})
					.catch(() => {
						console.log('모임원 모임 신청 실패');
						reject();
					});
			});
		},
		applyLeader() {
			console.log('vuex, applyLeader');
		},
	},
};
