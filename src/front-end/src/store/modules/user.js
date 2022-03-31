import http from '@/api/http';

export const user = {
	namespaced: true,
	state: {
		userInfo: {
			nickname: '',
		},
	},
	getters: {},
	mutations: {
		SET_USER_INFO(state, userInfo) {
			state.userInfo = userInfo;
		},
	},
	actions: {
		async getUserProfile({ commit }, videoSize) {
			const url = `/users/mypage?videoSize=${videoSize}`;
			await http
				.get(url)
				.then(res => {
					const user = res.data.profile;
					const userInfo = {
						nickname: user.nickname,
						email: user.email,
						profileImg: user.profileImgUrl,
						socialType: user.socialType.name,
						socialImg: user.socialType.logoUrl,
						isBlocked: user.block.isBlocked,
						endBlocking: user.block.endBlockingDateTime,
					};
					commit('SET_USER_INFO', userInfo);
					console.log('vuex actions: ', userInfo);
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
