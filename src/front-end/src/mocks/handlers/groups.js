import { rest } from 'msw';

export default [
	rest.get('/users/providers/ott0002', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				provider: {
					id: 'ott0002',
					name: '왓챠',
					link: 'https://watcha.com/',
					logoUrl: 'watcha logo img',
				},
				status: 'watching',
				timeStamps: {
					creationDateTime: '2022-03-12',
					startWatchingDateTime: '2022-03-24',
					endWatchingDateTime: '2022-04-23',
					endReportingDateTime: '2022-03-27',
				},
				report: {
					reported: false,
					reportCount: 0,
				},
				account: {
					id: 'watcha@email.com',
					password: 'watcha02pW',
					lastModifiedDateTime: '2022-03-24',
				},
				fellows: [
					{
						id: 'user0001',
						profileImgUrl: '01ImgUrl',
						nickname: '모르는개산책',
						isLeader: false,
						isMyself: true,
					},
					{
						id: 'user0005',
						profileImgUrl: '05ImgUrl',
						nickname: '왜전부있는닉이래',
						isLeader: true,
						isMyself: false,
					},
					{
						id: 'user0006',
						profileImgUrl: '06ImgUrl',
						nickname: 'bb',
						isLeader: false,
						isMyself: false,
					},
					{
						id: 'user0007',
						profileImgUrl: '07ImgUrl',
						nickname: 'SIM',
						isLeader: false,
						isMyself: false,
					},
				],
			}),
		);
	}),
	rest.get('/users/providers/ott0003', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				provider: {
					id: 'ott0003',
					name: 'wavve',
					link: 'https://www.wavve.com/',
					logoUrl: 'wavve logo img',
				},
				status: 'recruiting',
			}),
		);
	}),
];
