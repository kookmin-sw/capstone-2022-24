import http from '@/api/http';
import router from '@/router';
import AWS from 'aws-sdk';

export const auth = {
	namespaced: true,
	state: {
		token: null,
		naver: {
			clientId: `HDyG0cg2DID7bPsLQ4_u`,
			redirectionUri: `${window.location.origin}/login/naver`,
			code: null,
			resState: null,
		},
		google: {
			clientId: `111000957224-lu56fk9cgkavoika3b1b9872vv0lri8q.apps.googleusercontent.com`,
			redirectionUri: `${window.location.origin}/login/google`,
			token: null,
		},
		profile: {
			nickname: null,
			email: null,
			cellPhone: null,
			imgUrl: null,
		},
	},
	getters: {
		isLogin(state) {
			return state.token !== null;
		},
	},
	mutations: {
		SET_TOKEN(state, token) {
			state.token = token;
		},
		SET_NAVER_AUTH(state, response) {
			state.naver.code = response.code;
			state.naver.resState = response.resState;
		},
		SET_GOOGLE_AUTH(state, token) {
			state.google.token = token;
		},
		SET_PROFILE(state, user) {
			state.profile = user;
		},
		SET_NICKNAME(state, nickname) {
			state.profile.nickname = nickname;
		},
	},
	actions: {
		setToken({ commit }, token) {
			commit('SET_TOKEN', token);
		},
		setNaverAuth({ commit }, response) {
			commit('SET_NAVER_AUTH', response);
		},
		setGoogleAuth({ commit }, response) {
			commit('SET_GOOGLE_AUTH', response);
		},
		async requestNaverAuth({ state }) {
			const reqState = Math.random().toString(36).substr(2, 11);
			const apiUrl = `https://nid.naver.com/oauth2.0/authorize`;
			window.location.href = `${apiUrl}?response_type=code&client_id=${state.naver.clientId}&redirect_uri=${state.naver.redirectionUri}&state=${reqState}`;
		},
		async requestGoogleAuth({ state }) {
			const reqState = Math.random().toString(36).substr(2, 11);
			const apiUrl = `https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly&include_granted_scopes=true&response_type=token`;
			window.location.href = `${apiUrl}&state=${reqState}&redirect_uri=${state.google.redirectionUri}&client_id=${state.google.clientId}`;
		},
		async loginWithSocial({ state, commit }, social) {
			const url = `/users/login/oauth/${social}/`;

			let data = null;
			social === 'naver'
				? (data = { code: state.naver.code })
				: (data = { accessToken: state.google.token });

			return new Promise((resolve, reject) => {
				http.post(url, data).then(res => {
					console.log(res);
					const user = res.data.user.user;
					if (!user.isVerified) {
						// login
						const token = res.data.accessToken;
						localStorage.setItem('ACCESS_TOKEN', token);
						localStorage.setItem('NICKNAME', user.nickname);
						commit('SET_TOKEN', token);
						commit('SET_PROFILE', user);
						resolve();
					} else {
						// sign up
						reject();
					}
				});
			});
		},
		keepLoginToken({ commit }) {
			const token = localStorage.getItem('ACCESS_TOKEN');
			const nickname = localStorage.getItem('NICKNAME');
			commit('SET_TOKEN', token);
			commit('SET_NICKNAME', nickname);
		},
		logout() {
			localStorage.removeItem('ACCESS_TOKEN');
			localStorage.removeItem('NICKNAME');
			router.go(0);
		},
		nicknameDuplication(context, nickname) {
			// 닉네임 중복 검사
			const params = {
				nickname: nickname,
			};
			return new Promise((resolve, reject) => {
				http
					.get('/users/validate-nickname', { params: params })
					.then(() => {
						resolve();
					})
					.catch(() => {
						reject();
					});
			});
		},
		uploadImage(context, fileInfo) {
			const albumBucketName = process.env.VUE_APP_S3_BUCKET_NAME;
			const bucketRegion = process.env.VUE_APP_S3_BUCKET_REGION;
			const IdentityPoolId = process.env.VUE_APP_S3_IDENTITY_POOL_ID;

			// upload to s3 storage
			AWS.config.update({
				region: bucketRegion,
				credentials: new AWS.CognitoIdentityCredentials({
					IdentityPoolId: IdentityPoolId,
				}),
			});

			const upload = new AWS.S3.ManagedUpload({
				params: {
					Bucket: albumBucketName,
					Key: fileInfo.photoKey,
					Body: fileInfo.file,
				},
			});

			const promise = upload.promise();
			promise.then(
				() => {},
				() => {
					return alert('파일 업로드에 실패했습니다. 다시 시도해주세요.');
				},
			);
		},
		signUp({ commit, dispatch }, user) {
			// upload image
			const fileInfo = {
				photoKey: user.photoKey,
				file: user.file,
			};
			dispatch('uploadImage', fileInfo);
			// back-end api
			const url = '/users';
			http
				.post(url)
				.then(res => {
					// 로그인 성공
					const token = res.headers.accesstoken;
					commit('SET_TOKEN', token);
					localStorage.setItem('ACCESS_TOKEN', token);
					alert('회원가입에 성공했습니다.');
					router.replace('/');
				})
				.catch(err => {
					alert('회원가입에 실패했습니다. 다시 시도해주세요.', err);
				});
		},
	},
};
