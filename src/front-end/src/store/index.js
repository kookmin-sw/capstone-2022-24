import { createStore } from 'vuex';
import { auth } from '@/store/modules/auth';
import { mockTest } from '@/store/modules/mockTest';

export default createStore({
	state: {},
	getters: {},
	mutations: {},
	actions: {},
	modules: { auth, mockTest },
});
