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
			productionCountry: 'KR',
			watched: false,
		},
	},
	getters: {},
	mutations: {},
	actions: {
		selectCondition(context, condition) {
			console.log(condition);
		},
	},
};
