import { createStore } from 'vuex';
import { auth } from '@/store/modules/auth';
import { user } from '@/store/modules/user';
import { videoList } from '@/store/modules/videoList';

export default createStore({
	state: {},
	getters: {},
	mutations: {},
	actions: {},
	modules: { auth, user, videoList },
});
