import axios from 'axios';

export const mockTest = {
	namespaced: true,
	state: {
		msg: 'server error',
	},
	getters: {},
	mutations: {
		SET_MSG(state, msg) {
			state.msg = msg;
		},
	},
	actions: {
		setMsg({ commit }) {
			console.log('setMSG!!!');
			axios
				.get('/message')
				.then(res => {
					commit('SET_MSG', res.data.message);
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
