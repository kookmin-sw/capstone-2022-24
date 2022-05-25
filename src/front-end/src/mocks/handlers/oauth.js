import { rest } from 'msw';

export default [
	// 네이버 로그인 mock data : status 200 (로그인 성공)
	rest.post('/users/login/oauth/naver/', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.set({
				Location: 'https://localhost:80/register',
			}),
			ctx.json({
				accessToken: 'ongot.access.token',
				refreshToken: 'ongot.refresh.token',
				user: {
					nickname: 'ongot',
					name: 'ongot',
					email: 'ongot@123.com',
					cellPhoneNumber: '010-1111-1111',
					profileImageUrl:
						'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Swagger-logo.png/150px-Swagger-logo.png',
					birthday: '1998-01-01',
					isActive: true,
					isVerified: true,
				},
			}),
		);
	}),
	rest.post('/users', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.set({
				Location: 'https://localhost:80/join',
			}),
			ctx.json({
				accessToken: 'ongaj.access.token',
			}),
		);
	}),
];
