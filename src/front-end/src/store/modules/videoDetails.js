import http from '@/api/http';

export const videoDetails = {
	namespaced: true,
	state: {
		videoDetails: {},
	},
	getters: {},
	mutations: {
		SET_VIDEO_DETAILS(state, details) {
			state.videoDetails = details;
		},
	},
	actions: {
		async loadVideoDetails({ commit }, video) {
			const url = `/videos/${video.category}/${video.videoId}`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
					const details = res.data;
					commit('SET_VIDEO_DETAILS', details);
				})
				.catch(() => {
					console.log('');
				});
		},
		async loadVideoSeason({ commit }, video) {
			const url = `/videos/${video.category}/${video.videoId}/seasons/${video.season}`;
			await http
				.get(url)
				.then(res => {
					const details = res.data;
					commit('SET_VIDEO_DETAILS', details);
				})
				.catch(() => {
					console.log('');
				});
		},
	},
};
