import http from '@/api/http';

export const user = {
	namespaced: true,
	state: {
		userProfile: {
			nickname: '',
		},
	},
	getters: {},
	mutations: {
		SET_USER_PROFILE(state, userProfile) {
			state.userProfile = userProfile;
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
					console.log('vuex actions: ', userProfile);
				})
				.catch(err => {
					alert(err);
				});
		},
	},
};
