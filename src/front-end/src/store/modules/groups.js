import http from '@/api/http';

export const groups = {
	namespaced: true,
	state: {
		applied: [],
		notApplied: [],
		isLack: false,
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
			// TODO: 모임원 마일리지 사용 api 호출
			// TODO: 현재 마일리지 확인
			const url = `/applies/${applyer.role}/`;
			const data = {
				providerId: applyer.providerId,
			};
			return new Promise((resolve, reject) => {
				http
					.post(url, data)
					.then(() => {
						commit('SET_LACK_MILEAGE', false);
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
	},
};
