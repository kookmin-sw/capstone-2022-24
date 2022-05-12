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
		totalPage: 0,
		totalResult: 0,
		search: '',
	},
	getters: {
		hasResult(state) {
			return state.videos.length;
		},
	},
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
		INIT_VIDEOS(state, videos) {
			videos.forEach(video => {
				state.videos.push(video);
			});
		},
		SET_SEARCH(state, word) {
			state.search = word;
		},
	},
	actions: {
		initSelectCondition({ commit }) {
			commit('INIT_FILTERS');
		},
		async loadVideoList({ state, commit }, size) {
			// Home.vue
			let url = `/videos?page=1&size=${size}`;
			if (state.search) {
				url += `&search=${state.search}`;
			}
			if (state.filters.categories.length !== 0) {
				url += `&category=${state.filters.categories}`;
			}

			await http
				.get(url)
				.then(res => {
					const data = res.data.results;
					commit('SET_TOTAL_PAGE', data.page.totalPage);
					commit('SET_TOTAL_RESULT', data.page.totalResult);
					commit('INIT_VIDEOS', data.videos);
				})
				.catch(() => {
					commit('SET_TOTAL_RESULT', 0);
				});
		},
		async selectCondition({ commit, dispatch }, condition) {
			commit(`SET_${condition.name}`, condition.selected);
			dispatch('loadVideoList', 24);
		},
		async searchVideos({ commit, dispatch }, word) {
			// Home.vue
			commit('SET_SEARCH', word);
			dispatch('loadVideoList', 24);
		},
	},
};
