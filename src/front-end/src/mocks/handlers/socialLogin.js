import { rest } from 'msw';

export default [
	rest.post('/login/oauth/naver', (req, res, ctx) => {
		return res(
			ctx.status(301),
			ctx.json({
				accessToken: 'ongaj.access.token',
			}),
		);
	}),
];
