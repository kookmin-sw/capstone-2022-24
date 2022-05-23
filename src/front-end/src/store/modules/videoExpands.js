import http from '@/api/http';

export const videoExpands = {
	namespaced: true,
	state: {
		totalWish: 0,
		wishList: [],
		loadFail: false,
	},
	getters: {},
	mutations: {
		INIT_VIDEOS(state) {
			state.totalWish = 0;
			state.wishList = [];
		},
		SET_TOTAL_WISH(state, total) {
			state.totalWish = total;
		},
		ADD_WISH_VIDEOS(state, videoList) {
			state.wishList = [...state.wishList, ...videoList];
		},
		SET_LOAD_FAIL(state, status) {
			state.loadFail = status;
		},
	},
	actions: {
		async loadWishList({ state, commit }, offset) {
			const url = `/mypage/wishes`;
			const token = localStorage.getItem('ACCESS_TOKEN');
			const headers = {
				authorization: `Bearer ${token}`,
			};
			const params = {
				videoLimit: 48,
				videoOffset: offset,
			};
			await http
				.get(url, { params, headers })
				.then(res => {
					commit('SET_TOTAL_WISH', res.data.page.totalCount - 1);
					commit('ADD_WISH_VIDEOS', res.data.results);
					commit('SET_LOAD_FAIL', false);
					if (state.totalWish + 1 <= state.wishList.length) {
						const maxWidth = 6;
						const lack = maxWidth - (state.totalWish % maxWidth) - 1;
						for (let i = 0; i < lack; i++) {
							commit('ADD_WISH_VIDEOS', [{}]);
						}
					}
				})
				.catch(() => {
					commit('SET_LOAD_FAIL', true);
				});
		},
	},
};
