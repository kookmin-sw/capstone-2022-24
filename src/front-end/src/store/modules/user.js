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
		SET_PROFILE(state, profile) {
			state.profile = profile;
		},
		SET_GROUP_LIST(state, groupList) {
			state.groupList = [...state.groupList, ...groupList];
		},
		ADD_GROUP_INFO(state, group) {
			state.groupsInfo.push(group);
		},
		SET_SELECT_GROUP(state, group) {
			state.selectGroup = group;
		},
		INIT_VIDEOS(state) {
			state.wishList = [];
		},
		SET_RECENT_LIST(state, videoList) {
			state.recentList = videoList;
		},
		PUSH_RECENT_LIST(state, videoList) {
			state.recentList.results.push(videoList);
		},
		SET_TOTAL_WISH(state, total) {
			state.totalWish = total;
		},
		PUSH_WISH_LIST(state, videoList) {
			state.wishList.push(videoList);
		},
		SET_STAR_LIST(state, videoList) {
			state.starList = videoList;
		},
		PUSH_STAR_LIST(state, videoList) {
			state.starList.results.push(videoList);
		},
		SET_WATCH_LIST(state, videoList) {
			state.watchList = videoList;
		},
		PUSH_WATCH_LIST(state, videoList) {
			state.watchList.results.push(videoList);
		},
	},
	actions: {
		async initProfile({ commit }) {
			commit('SET_PROFILE', {});
			const url = `/users/mypage/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
					// init profile
					const user = res.data.profile;
					const userProfile = {
						nickname: user.nickname,
						phone: user.cellPhoneNumber,
						email: user.email,
						profileImg: user.profileImgUrl,
						birthday: user.birthday,
						isActive: user.isActive,
						isVerified: user.isVerified,
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
		},
		async selectGroup({ state, commit }, groupId) {
			// 사용자가 선택한 모임 정보가 존재하는지 확인
			const selected = state.groupList.find(group => {
				return group.provider.id === groupId;
			});
			if (selected) {
				// TODO: 모임 상세 api 호출 (PR중)
				commit('SET_SELECT_GROUP', selected);
			}
		},
		async pushRecentList({ commit }, { page, size }) {
			const url = `/users/mypage/recent-views?page=${page}&size=${size}`;
			http
				.get(url)
				.then(res => {
					const videoList = {
						videos: res.data.results,
					};
					commit('PUSH_RECENT_LIST', videoList);
				})
				.catch(err => {
					alert(err);
				});
		},
		async pushWishList({ commit }) {
			const url = `/users/mypage/wishes`;
			http
				.get(url)
				.then(res => {
					const videoList = {
						videos: res.data.results,
					};
					commit('PUSH_WISH_LIST', videoList);
				})
				.catch(err => {
					alert(err);
				});
		},
		async pushStarList({ commit }, { page, size }) {
			const url = `/users/mypage/stars?page=${page}&size=${size}`;
			http
				.get(url)
				.then(res => {
					const videoList = {
						videos: res.data.results,
					};
					commit('PUSH_STAR_LIST', videoList);
				})
				.catch(err => {
					alert(err);
				});
		},
		async pushWatchList({ commit }, { page, size }) {
			const url = `/users/mypage/watch-marks?page=${page}&size=${size}`;
			http
				.get(url)
				.then(res => {
					const videoList = {
						videos: res.data.results,
					};
					commit('PUSH_WATCH_LIST', videoList);
				})
				.catch(err => {
					alert(err);
				});
		},
	},
};
