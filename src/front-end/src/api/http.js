import axios from 'axios';
// import store from '@/store';

const instance = axios.create({
	baseURL: 'http://localhost:3000',
});

// request interceptor
// instance.interceptors.request.use(config => {
// 	if (store.state.auth.token !== null) {
// 		config['headers'] = {
// 			Authorization: `Bear ${store.state.auth.token}`,
// 			Host: `localhost:8080`,
// 		};
// 	}
// 	return config;
// });

export default instance;
