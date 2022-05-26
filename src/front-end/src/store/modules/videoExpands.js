import http from '@/api/http';

export const videoExpands = {
	namespaced: true,
	state: {
		totalResult: 0,
		videos: [],
		loadFail: false,
	},
	getters: {},
	mutations: {
		INIT_VIDEOS(state) {
			state.totalResult = 0;
			state.videos = [];
		},
		SET_TOTAL_RESULT(state, total) {
			state.totalResult = total;
		},
		ADD_VIDEOS(state, videoList) {
			state.videos = [...state.videos, ...videoList];
		},
		SET_LOAD_FAIL(state, status) {
			state.loadFail = status;
		},
	},
	actions: {
		async loadVideoList({ state, commit }, { offset, type }) {
			const url = `/mypage/${type}`;
			const params = {
				videoLimit: 48,
				videoOffset: offset,
			};
			await http
				.get(url, { params })
				.then(res => {
					commit('SET_TOTAL_RESULT', res.data.page.totalCount - 1);
					commit('ADD_VIDEOS', res.data.results);
					commit('SET_LOAD_FAIL', false);
					if (state.totalResult + 1 <= state.videos.length) {
						const maxWidth = 6;
						const lack = maxWidth - (state.totalResult % maxWidth) - 1;
						for (let i = 0; i < lack; i++) {
							commit('ADD_VIDEOS', [{}]);
						}
					}
				})
				.catch(() => {
					commit('SET_LOAD_FAIL', true);
				});
		},
	},
};
