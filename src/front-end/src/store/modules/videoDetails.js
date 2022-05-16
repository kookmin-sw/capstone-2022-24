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
			await http
				.get(url)
				.then(res => {
					const details = res.data;
					console.log(details);
					commit('SET_VIDEO_DETAILS', details);
				})
				.catch(() => {
					console.log('');
				});
		},
	},
};
