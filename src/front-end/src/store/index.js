import { createStore } from 'vuex';
import { auth } from '@/store/modules/auth';
import { user } from '@/store/modules/user';
import { videoList } from '@/store/modules/videoList';
import { videoDetails } from '@/store/modules/videoDetails';
import { videoDiscontinued } from '@/store/modules/videoDiscontinued';
import { videoInteractions } from '@/store/modules/videoInteractions';
import { join } from '@/store/modules/join';

export default createStore({
	state: {},
	getters: {},
	mutations: {},
	actions: {},
	modules: {
		auth,
		user,
		videoList,
		videoDetails,
		videoDiscontinued,
		videoInteractions,
		join,
	},
});
