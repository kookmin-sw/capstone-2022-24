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
	},
	getters: {},
	mutations: {
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
	},
	actions: {
		selectCondition(context, condition) {
			context.commit(`SET_${condition.name}`, condition.selected);
			console.log(context.state.filters);
		},
	},
};
