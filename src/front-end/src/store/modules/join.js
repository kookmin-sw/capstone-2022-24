import http from '@/api/http';

export const join = {
	namespaced: true,
	state: {},
	getters: {},
	mutations: {},
	actions: {
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
