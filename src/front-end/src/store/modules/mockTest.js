// import axios from 'axios';

import http from '@/api/http';

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
			http
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
