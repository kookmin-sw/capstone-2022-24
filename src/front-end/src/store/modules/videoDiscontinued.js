import http from '@/api/http';

export const videoDiscontinued = {
	namespaced: true,
	state: {
		videos: [],
		totalResult: 0,
		loadFail: false,
	},
	getters: {},
	mutations: {
		SET_LOAD_FAIL(state, status) {
			state.loadFail = status;
		},
		INIT_VIDEOS(state) {
			state.videos = [];
			state.totalResult = 0;
		},
		ADD_VIDEOS(state, videos) {
			state.videos = [...state.videos, ...videos];
		},
		SET_TOTAL_RESULT(state, cnt) {
			state.totalResult = cnt;
		},
	},
	actions: {
		async loadVideoList({ commit }, days) {
			let url = `/discontinues/${days}`;
			let params;
			commit('INIT_VIDEOS');
			await http
				.get(url, { params })
				.then(res => {
					const list = res.data.results;
					const total = res.data.page.totalCount;
					commit('SET_TOTAL_RESULT', total - 1);
					commit('ADD_VIDEOS', list);
					commit('SET_LOAD_FAIL', false);
					// const maxWidth = 6;
					// if (params.limit % maxWidth !== 0) {
					// 	const lack = maxWidth - (params.limit % maxWidth);
					// 	for (let i = 0; i < lack; i++) {
					// 		commit('ADD_VIDEOS', [{}]);
					// 	}
					// }
				})
				.catch(() => {
					commit('INIT_VIDEOS');
					commit('SET_LOAD_FAIL', true);
				});
		},
	},
};
