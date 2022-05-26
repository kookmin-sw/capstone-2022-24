import http from '@/api/http';

export const user = {
	namespaced: true,
	state: {
		profile: {
			nickname: 'tmp',
		},
		groupList: [],
		groupsInfo: [],
		selectGroup: {},
		recentList: {},
		wishList: [],
		starList: {},
		watchList: {},
		totalWish: 0,
	},
	getters: {
		getGroupList(state) {
			return state.groupList;
		},
		getSelectGroup(state) {
			return state.selectGroup;
		},
		getRecentList(state) {
			return state.recentList;
		},
		getWishList(state) {
			return state.wishList;
		},
		getStarList(state) {
			return state.starList;
		},
		getWatchList(state) {
			return state.watchList;
		},
	},
	mutations: {
		INIT_GROUP(state) {
			state.groupList = [];
		},
		SET_PROFILE(state, profile) {
			state.profile = profile;
		},
		SET_GROUP_LIST(state, groupList) {
			state.groupList = [...state.groupList, ...groupList];
		},
		SET_SELECT_GROUP(state, group) {
			state.selectGroup = group;
		},
		INIT_VIDEOS(state) {
			state.wishList = [];
		},
		SET_TOTAL_WISH(state, total) {
			state.totalWish = total;
		},
		PUSH_WISH_LIST(state, videoList) {
			state.wishList.push(videoList);
		},
	},
	actions: {
		async initProfile({ state, commit, dispatch }) {
			commit('INIT_GROUP');
			commit('SET_PROFILE', {});
			const url = `/mypage/`;
			const params = {
				videoLimit: 6,
				videoOffset: 0,
			};

			await http
				.get(url, { params })
				.then(res => {
					// init profile
					const user = res.data.profile;
					const userProfile = {
						nickname: user.nickname,
						phone: user.cellPhoneNumber,
						email: user.email,
						profileImg: user.profileImageUrl,
						birthday: user.birthday,
						isActive: user.isActive,
						isVerified: user.isVerified,
						mileages: user.totalMileages,
					};
					commit('SET_PROFILE', userProfile);

					// set videos
					const videos = res.data.videos;
					commit('SET_TOTAL_WISH', videos.wishes.page.totalCount);
					commit('INIT_VIDEOS');
					commit('PUSH_WISH_LIST', videos.wishes.results);

					// init groups
					const groups = res.data.groups;
					commit('SET_SELECT_GROUP', groups.default);
					commit('SET_GROUP_LIST', [groups.default]);
					commit('SET_GROUP_LIST', groups.others);
				})
				.catch(err => {
					alert(err);
				});

			if (state.selectGroup) {
				dispatch('selectGroup', state.selectGroup.provider.id);
			}
		},
		async selectGroup({ state, commit }, groupId) {
			// 사용자가 선택한 모임 정보가 존재하는지 확인
			const selected = state.groupList.find(group => {
				return group.provider.id === groupId;
			});

			if (selected) {
				const url = `/providers/${selected.provider.id}`;
				await http.get(url).then(res => {
					commit('SET_SELECT_GROUP', res.data);
				});
			}
		},
		async pushWishList({ state, commit }) {
			const url = `/mypage/wishes`;
			const params = {
				videoLimit: 6,
				videoOffset: state.wishList.length * 6,
			};
			http
				.get(url, { params })
				.then(res => {
					commit('PUSH_WISH_LIST', res.data.results);
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
