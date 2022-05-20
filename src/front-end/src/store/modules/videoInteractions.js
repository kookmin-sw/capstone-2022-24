import http from '@/api/http';

export const videoInteractions = {
	namespaced: true,
	state: {},
	getters: {},
	mutations: {},
	actions: {
		async addWish(context, videoId) {
			console.log('vuex, addWish', videoId);
			const url = `videos/${videoId}/wishes/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				Authorization: `Bearer ${token}`,
			};
			console.log(url, headers);
			await http
				.post(url, {}, { headers })
				.then(res => {
					console.log(res);
				})
				.catch(err => {
					console.log(err);
				});
		},
		cancleWish(context, videoId) {
			console.log('vuex, cancleWish', videoId);
		},
	},
};
