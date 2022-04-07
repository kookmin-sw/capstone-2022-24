import { rest } from 'msw';

export default [
	// 네이버 로그인 mock data : status 301 (회원가입)
	rest.post('/login/oauth/naver', (req, res, ctx) => {
		return res(
			ctx.status(301),
		);
	}),
	// 구글 로그인 mock data : status 200 (로그인 성공)
	rest.post('/login/oauth/google', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.set({
				Location: 'https://localhost:8080/join',
			}),
			ctx.json({
				accessToken: 'ongaj.access.token',
			}),
		);
	}),
];
