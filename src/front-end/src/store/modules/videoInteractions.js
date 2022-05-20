import http from '@/api/http';

export const videoInteractions = {
	namespaced: true,
	state: {},
	getters: {},
	mutations: {},
	actions: {
		async addWish(context, videoId) {
			const url = `videos/${videoId}/wishes/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				Authorization: `Bearer ${token}`,
			};
			return new Promise((resolve, reject) => {
				http
					.post(url, {}, { headers })
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},
		async cancleWish(context, videoId) {
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				Authorization: `Bearer ${token}`,
			};

			const url = `videos/${videoId}/wishes/`;
			return new Promise((resolve, reject) => {
				http
					.delete(url, { headers })
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},
	},
};
