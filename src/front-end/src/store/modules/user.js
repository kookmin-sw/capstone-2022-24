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
		total: {
			wishes: 0,
			'watch-marks': 0,
		},
		videos: {
			wishes: [],
			'watch-marks': [],
		},
	},
	getters: {
		getGroupList(state) {
			return state.groupList;
		},
		getSelectGroup(state) {
			return state.selectGroup;
		},
		isLeader(state) {
			return state.selectGroup.fellows.find(fellow => {
				return fellow.isMyself && fellow.isLeader;
			});
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
		INIT_VIDEOS(state, videos) {
			state.total.wishes = videos.wishes.page.totalCount;
			state.videos.wishes = [];
			state.videos.wishes.push(videos.wishes.results);

			state.total['watch-marks'] = videos.watchMarks.page.totalCount;
			state.videos['watch-marks'] = [];
			state.videos['watch-marks'].push(videos.watchMarks.results);
		},
		PUSH_VIDEO_LIST(state, videos) {
			state.videos[videos.type].push(videos.results);
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
					commit('INIT_VIDEOS', videos);

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
		async pushVideos({ state, commit }, type) {
			const url = `/mypage/${type}`;
			const params = {
				videoLimit: 6,
				videoOffset: state.videos[type].length * 6,
			};
			http.get(url, { params }).then(res => {
				const videos = {
					type: type,
					results: res.data.results,
				};
				commit('PUSH_VIDEO_LIST', videos);
			});
		},
	},
};
