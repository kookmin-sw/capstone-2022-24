import axios from 'axios';

const instance = axios.create({
	baseURL: 'http://localhost:80',
});

instance.interceptors.request.use(config => {
	const token = localStorage.getItem('ACCESS_TOKEN');
	if (token) {
		if (config.headers && token)
			config.headers.Authorization = `Bearer ${token}`;
	}
	return config;
});
export default instance;
