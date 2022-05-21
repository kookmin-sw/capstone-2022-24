import http from '@/api/http';

export const videoExpands = {
	namespaced: true,
	state: {
		totalWish: 0,
		wishList: [],
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
	},
	actions: {
		async setWishList({ state, commit }) {
			const url = `/users/mypage/wishes`;
			const token = localStorage.getItem('ACCESS_TOKEN');
			const headers = {
				authorization: `Bearer ${token}`,
			};
			const params = {
				videoLimit: 48,
				videoOffset: state.wishList.length,
			};
			await http.get(url, { params, headers }).then(res => {
				commit('SET_TOTAL_WISH', res.data.page.totalCount);
				commit('ADD_WISH_VIDEOS', res.data.results);
				if (state.totalWish <= state.wishList.length) {
					const maxWidth = 6;
					const lack = maxWidth - (state.totalWish % maxWidth) - 1;
					for (let i = 0; i < lack; i++) {
						commit('ADD_WISH_VIDEOS', [{}]);
					}
				}
			});
		},
	},
};
