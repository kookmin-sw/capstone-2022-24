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
			state.groupList = groupList;
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
		async setProfile({ commit }) {
			const url = `/users/mypage/`;

			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
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
				})
				.catch(err => {
					alert(err);
				});
		},
		async initUserGroups({ commit }) {
			const url = `/users/mypage/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
					const groups = res.data.groups;
					// set: select group = default group
					const defaultGroup = groups.default;
					commit('ADD_GROUP_INFO', defaultGroup);
					commit('SET_SELECT_GROUP', defaultGroup);

					// list에 default group 추가
					const groupList = [
						{
							id: defaultGroup.provider.id,
							logoUrl: defaultGroup.provider.logoUrl,
						},
					];
					// list에 others 추가
					const others = groups.others;
					others.forEach(group => {
						groupList.push({
							id: group.provider.id,
							logoUrl: group.provider.logoUrl,
						});
					});
					commit('SET_GROUP_LIST', groupList);
				})
				.catch(err => {
					alert(err);
				});
		},
		async setSelectGroup({ state, commit, dispatch }, groupId) {
			// 사용자가 선택한 모임 정보가 존재하는지 확인
			const selected = state.groupsInfo.find(group => {
				return group.provider.id === groupId;
			});
			if (!selected) {
				// 존재하지 않으면 정보 가져오고 선택 모임 갱신
				await dispatch('pushGroupInfo', groupId);
			} else {
				// 존재하면 선택 모임 갱신
				commit('SET_SELECT_GROUP', selected);
			}
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
		async initUserVideos({ commit }) {
			const url = `/users/mypage/`;
			const token = String(localStorage.getItem('ACCESS_TOKEN'));
			const headers = {
				authorization: `Bearer ${token}`,
			};
			await http
				.get(url, { headers })
				.then(res => {
					// 최근 조회 작
					const videos = res.data.videos;
					const recentList = {
						totalPage: videos.recentViews.page.totalPage,
						totalResult: videos.recentViews.page.totalResult,
						results: [
							{
								videos: videos.recentViews.results,
							},
						],
					};
					commit('SET_RECENT_LIST', recentList);

					// 찜 작
					const wishList = {
						totalPage: videos.wishes.page.totalPage,
						totalResult: videos.wishes.page.totalResult,
						results: [
							{
								videos: videos.wishes.results,
							},
						],
					};
					commit('SET_WISH_LIST', wishList);

					// 별점 작
					const starList = {
						totalPage: videos.stars.page.totalPage,
						totalResult: videos.stars.page.totalResult,
						results: [
							{
								videos: videos.stars.results,
							},
						],
					};
					commit('SET_STAR_LIST', starList);

					// 본 작
					const watchList = {
						totalPage: videos.watchMarks.page.totalPage,
						totalResult: videos.watchMarks.page.totalResult,
						results: [
							{
								videos: videos.watchMarks.results,
							},
						],
					};
					commit('SET_WATCH_LIST', watchList);
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
