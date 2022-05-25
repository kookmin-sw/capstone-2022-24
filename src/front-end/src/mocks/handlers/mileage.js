import { rest } from 'msw';

export default [
	rest.get('/mileages/', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json([
				[
					{
						amount: 3000,
						renewalDateTime: '2022-05-22 03:38:21',
					},
					{
						amount: -2000,
						renewalDateTime: '2022-05-22 03:38:34',
					},
					{
						amount: 1000,
						renewalDateTime: '2022-05-22 03:38:52',
					},
					{
						amount: -1000,
						renewalDateTime: '2022-05-22 03:41:55',
					},
				],
			]),
		);
	}),
];
