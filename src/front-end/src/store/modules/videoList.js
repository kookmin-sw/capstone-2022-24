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
		loadFail: false,
	},
	getters: {},
	mutations: {
		SET_LOAD_FAIL(state, status) {
			state.loadFail = status;
		},
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
		SET_PROVIDERS(state, selected) {
			state.filters.providers.splice(0, state.filters.providers.length);
			selected.forEach(cond => {
				state.filters.providers.push(cond);
			});
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
		SET_SEARCH(state, word) {
			state.search = word;
		},
		SET_SORT(state, sort) {
			state.sort = sort;
		},
	},
	actions: {
		initSetting({ commit }) {
			commit('INIT_FILTERS');
			commit('INIT_VIDEOS');
			commit('SET_SEARCH', '');
			commit('SET_SORT', 'random');
		},
		async loadVideoList({ state, commit }, offset) {
			let url = `/videos/`;
			const params = {
				offset,
				search: state.search,
				sort: state.sort,
				providers: state.filters.providers.join(','),
				category: state.filters.categories.join(','),
			};

			await http
				.get(url, { params })
				.then(res => {
					const list = res.data.results;
					const total = res.data.page.totalCount;
					commit('SET_TOTAL_RESULT', total - 1);
					commit('ADD_VIDEOS', list);
					commit('SET_LOAD_FAIL', false);
					if (state.totalResult <= state.videos.length) {
						const maxWidth = 6;
						const lack = maxWidth - (state.totalResult % maxWidth) - 1;
						for (let i = 0; i < lack; i++) {
							commit('ADD_VIDEOS', [{}]);
						}
					}
				})
				.catch(() => {
					commit('INIT_VIDEOS');
					commit('SET_LOAD_FAIL', true);
				});
		},
		async initSelectCondition({ state, commit, dispatch }) {
			commit('INIT_FILTERS');
			await dispatch('loadVideoList', state.videos.length);
		},
		async filterVideos({ commit, dispatch }, condition) {
			commit(`SET_${condition.name}`, condition.selected);
			commit('INIT_VIDEOS');
			dispatch('loadVideoList', 0);
		},
		async searchVideos({ commit, dispatch }, word) {
			commit('INIT_VIDEOS');
			commit('SET_SEARCH', word);
			await dispatch('loadVideoList', 0);
		},
		async sortVideos({ commit, dispatch }, sort) {
			commit('INIT_VIDEOS');
			commit('SET_SORT', sort);
			await dispatch('loadVideoList', 0);
		},
	},
};
