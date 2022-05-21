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
		wishList: {},
		starList: {},
		watchList: {},
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
		SET_RECENT_LIST(state, videoList) {
			state.recentList = videoList;
		},
		PUSH_RECENT_LIST(state, videoList) {
			state.recentList.results.push(videoList);
		},
		SET_WISH_LIST(state, videoList) {
			state.wishList = videoList;
		},
		PUSH_WISH_LIST(state, videoList) {
			state.wishList.results.push(videoList);
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
		async initProfile({ state, commit }) {
			commit('SET_PROFILE', {});
			const url = `/users/mypage/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
					console.log(res);
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
					const wishes = {
						total: videos.wishes.totalCount,
						results: videos.wishes.results,
					};
					commit('SET_WISH_LIST', wishes);

					// init groups
					const groups = res.data.groups;
					commit('SET_SELECT_GROUP', groups.default);
					commit('SET_GROUP_LIST', [groups.default]);
					commit('SET_GROUP_LIST', groups.others);
					console.log(state.groupList, state.selectGroup);
					console.log(groups);
				})
				.catch(err => {
					alert(err);
				});
		},
		async selectGroup({ state, commit }, groupId) {
			// 사용자가 선택한 모임 정보가 존재하는지 확인
			console.log(groupId);
			console.log(state.groupList);
			const selected = state.groupList.find(group => {
				return group.provider.id === groupId;
			});
			console.log(selected);
			if (selected) {
				// TODO: 모임 상세 api 호출 (PR중)
				commit('SET_SELECT_GROUP', selected);
			}
			// if (!selected) {
			// 	// 존재하지 않으면 정보 가져오고 선택 모임 갱신
			// 	await dispatch('pushGroupInfo', groupId);
			// } else {
			// 	// 존재하면 선택 모임 갱신
			// 	commit('SET_SELECT_GROUP', selected);
			// }
		},
		async pushGroupInfo({ commit }, groupId) {
			const url = `/users/providers/${groupId}`;
			await http
				.get(url)
				.then(res => {
					commit('SET_SELECT_GROUP', res.data);
					commit('ADD_GROUP_INFO', res.data);
				})
				.catch(err => {
					alert(err);
				});
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
		async pushWishList({ commit }, { page, size }) {
			const url = `/users/mypage/wishes?page=${page}&size=${size}`;
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
