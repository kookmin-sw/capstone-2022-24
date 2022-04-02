import http from '@/api/http';

export const user = {
	namespaced: true,
	state: {
		userProfile: {
			nickname: '',
		},
		groupList: [],
		groupsInfo: [],
		selectGroup: {},
		recentViews: {},
	},
	getters: {
		getGroupList(state) {
			return state.groupList;
		},
		getSelectGroup(state) {
			return state.selectGroup;
		},
		getRecentViews(state) {
			return state.recentViews;
		},
	},
	mutations: {
		SET_USER_PROFILE(state, userProfile) {
			state.userProfile = userProfile;
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
		SET_RECENT_VIEWS(state, videoList) {
			state.recentViews = videoList;
		},
		PUSH_RECENT_VIEWS(state, videoList) {
			state.recentViews.results.push(videoList);
		},
	},
	actions: {
		async setUserProfile({ commit }, videoSize) {
			const url = `/users/mypage?videoSize=${videoSize}`;
			await http
				.get(url)
				.then(res => {
					const user = res.data.profile;
					const userProfile = {
						nickname: user.nickname,
						phone: user.cellPhoneNumber,
						email: user.email,
						profileImg: user.profileImgUrl,
						socialType: user.socialType.name,
						socialImg: user.socialType.logoUrl,
						isBlocked: user.block.isBlocked,
						endBlocking: user.block.endBlockingDateTime,
					};
					commit('SET_USER_PROFILE', userProfile);
				})
				.catch(err => {
					alert(err);
				});
		},
		async initUserGroups({ commit }, videoSize) {
			const url = `/users/mypage?videoSize=${videoSize}`;
			await http
				.get(url)
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
		async initUserVideos({ commit }, videoSize) {
			const url = `/users/mypage?videoSize=${videoSize}`;
			await http
				.get(url)
				.then(res => {
					const videos = res.data.videos;
					// const list = dispatch('divisionVideo', {arr: videos.recentViews.results, size: videoSize});
					const recentViews = {
						totalPage: videos.recentViews.page.totalPage,
						totalResult: videos.recentViews.page.totalResult,
						// results: videos.recentViews.results,
						results: [
							{
								videos: videos.recentViews.results,
							},
						],
					};
					commit('SET_RECENT_VIEWS', recentViews);
					// console.log(recentViews);

					// 				const userVideos = {
					// 					recentViews: {
					// 						totalPage: videos.recentViews.page.totalPage,
					// 						hasPage: 1,
					// 						total: videos.recentViews.page.totalResult,
					// 						results: videos.recentViews.results,
					// 					},
					// 					dibs: {
					// 						total: videos.dibs.page.totalResult,
					// 						results: videos.dibs.results,
					// 					},
					// 					stars: {
					// 						total: videos.stars.page.totalResult,
					// 						results: videos.stars.results,
					// 					},
					// 					watchMarks: {
					// 						total: videos.watchMarks.page.totalResult,
					// 						results: videos.watchMarks.results,
					// 					},
					// 				};
					// 				commit('SET_USER_VIDEOS', userVideos);
					// 				// console.log('vuex:', state.userVideos);
				})
				.catch(err => {
					alert(err);
				});
		},
		async pushRecentViews({ commit }, { page, size }) {
			const url = `/users/mypage/recent-views?page=${page}&size=${size}`;
			console.log(`url: ${url}`);
			http
				.get(url)
				.then(res => {
					const videoList = {
						videos: res.data.results,
					};
					commit('PUSH_RECENT_VIEWS', videoList);
				})
				.catch(err => {
					alert(err);
				});
		},
	},
};
