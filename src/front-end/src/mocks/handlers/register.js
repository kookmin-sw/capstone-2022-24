import { rest } from 'msw';

export default [
	// 닉네임 중복 확인
	rest.get('/users/validate-nickname', (req, res, ctx) => {
		const nickname = req.url.searchParams.get('nickname');
		if (nickname === 'conflict') {
			// 중복 닉네임
			return res(ctx.status(409));
		} else {
			// 사용 가능한 닉네임
			return res(ctx.status(200));
		}
	}),
];
