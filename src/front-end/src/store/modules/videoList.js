import http from '@/api/http';

export const videoList = {
	namespaced: true,
	state: {
		filters: {
			providers: [],
			categories: [],
			genres: [],
			ratingMin: 0.5,
			ratingMax: 5,
			releaseDateMin: 1800,
			releaseDateMax: 2022,
			productionCountry: [],
			watched: [],
		},
		videos: [],
		totalResult: 0,
		search: '',
		sort: 'random',
		providers: '',
	},
	getters: {},
	mutations: {
		INIT_FILTERS(state) {
			state.filters.categories.splice(0, state.filters.categories.length);
			state.filters.genres.splice(0, state.filters.genres.length);
			state.filters.productionCountry.splice(
				0,
				state.filters.productionCountry.length,
			);
			state.filters.watched.splice(0, state.filters.watched.length);
			state.filters.ratingMin = 0.5;
			state.filters.releaseDateMax = 5;
			state.filters.releaseDateMin = 1800;
			state.filters.releaseDateMax = 2022;
		},
		SET_CATEGORIES(state, selected) {
			state.filters.categories.splice(0, state.filters.categories.length);
			selected.forEach(cond => {
				state.filters.categories.push(cond);
			});
		},
		SET_GENRES(state, selected) {
			state.filters.genres.splice(0, state.filters.genres.length);
			selected.forEach(cond => {
				state.filters.genres.push(cond);
			});
		},
		SET_COUNTRY(state, selected) {
			state.filters.productionCountry.splice(
				0,
				state.filters.productionCountry.length,
			);
			selected.forEach(cond => {
				state.filters.productionCountry.push(cond);
			});
		},
		SET_WATCHED(state, selected) {
			state.filters.watched.splice(0, state.filters.watched.length);
			selected.forEach(cond => {
				state.filters.watched.push(cond);
			});
		},
		SET_TOTAL_PAGE(state, page) {
			state.totalPage = page;
		},
		SET_TOTAL_RESULT(state, cnt) {
			state.totalResult = cnt;
		},
		ADD_VIDEOS(state, videos) {
			state.videos = [...state.videos, ...videos];
		},
		SET_SEARCH(state, word) {
			state.search = word;
		},
		INIT_VIDEOS(state) {
			state.videos = [];
			state.totalResult = 0;
		},
	},
	actions: {
		async loadVideoList({ state, commit }, offset) {
			let url = `/videos/`;
			const params = {
				offset,
				search: state.search,
				sort: state.sort,
				providers: state.providers,
			};
			if (url !== state.beforeUrl) {
				await http
					.get(url, { params })
					.then(res => {
						const list = res.data.results;
						const total = res.data.page.totalCount;
						commit('SET_TOTAL_RESULT', total - 1);
						commit('ADD_VIDEOS', list);

						if (state.totalResult <= state.videos.length) {
							const maxWidth = 6;
							const lack = maxWidth - (state.totalResult % maxWidth) - 1;
							for (let i = 0; i < lack; i++) {
								commit('ADD_VIDEOS', [{}]);
							}
						}
					})
					.catch(() => {
						commit('SET_TOTAL_RESULT', 0);
					});
			}
		},
		async initSelectCondition({ state, commit, dispatch }) {
			commit('INIT_FILTERS');
			await dispatch('loadVideoList', state.videos.length);
		},
		async selectCondition({ commit, dispatch }, condition) {
			commit(`SET_${condition.name}`, condition.selected);
			dispatch('loadVideoList', 24);
		},
		async searchVideos({ state, commit, dispatch }, word) {
			commit('INIT_VIDEOS');
			commit('SET_SEARCH', word);
			await dispatch('loadVideoList', state.videos.length);
		},
	},
};
