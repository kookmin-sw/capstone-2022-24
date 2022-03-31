import http from '@/api/http';

export const user = {
	namespaced: true,
	state: {
		userProfile: {
			nickname: '',
		},
		userGroupList: [],
		userGroups: [],
	},
	getters: {},
	mutations: {
		SET_USER_PROFILE(state, userProfile) {
			state.userProfile = userProfile;
		},
		SET_GROUP_LIST(state, groupList) {
			state.userGroupList = groupList;
		},
		ADD_GROUP_INFO(state, groupInfo) {
			state.userGroups.push(groupInfo);
		},
	},
	actions: {
		async getUserProfile({ commit }, videoSize) {
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
		async getGroupList({ commit }, videoSize) {
			const url = `/users/mypage?videoSize=${videoSize}`;
			await http
				.get(url)
				.then(res => {
					const groups = res.data.groups;
					// group list 추가
					const others = groups.others;
					const defaultGroup = groups.default;
					const groupList = [
						{
							id: defaultGroup.provider.id,
							logoUrl: defaultGroup.provider.logoUrl,
						},
					];
					others.forEach(group => {
						groupList.push({
							id: group.provider.id,
							logoUrl: group.provider.logoUrl,
						});
					});
					commit('SET_GROUP_LIST', groupList);
					// default group 추가
					commit('ADD_GROUP_INFO', defaultGroup);
				})
				.catch(err => {
					alert(err);
				});
		},
		async getGroupInfo({ commit }, ottId) {
			const url = `/users/providers/${ottId}`;
			await http
				.get(url)
				.then(res => {
					commit('ADD_GROUP_INFO', res.data);
				})
				.catch(err => {
					alert(err);
				});
		},
	},
};
