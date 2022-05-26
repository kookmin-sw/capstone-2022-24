import http from '@/api/http';

export const videoInteractions = {
	namespaced: true,
	state: {},
	getters: {},
	mutations: {},
	actions: {
		async addRecord(context, record) {
			const url = `videos/${record.id}/${record.type}/`;
			return new Promise((resolve, reject) => {
				http
					.post(url)
					.then(() => {
						resolve(record.type);
					})
					.catch(() => {
						reject();
					});
			});
		},
		async cancelRecord(context, record) {
			const url = `videos/${record.id}/${record.type}/`;
			return new Promise((resolve, reject) => {
				http
					.delete(url)
					.then(() => {
						resolve(record.type);
					})
					.catch(() => {
						reject();
					});
			});
		},
	},
};
