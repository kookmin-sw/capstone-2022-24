import { rest } from 'msw';

export default [
	// 모집 중
	rest.get('/providers/1', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				id: 1,
				provider: {
					id: 5,
					tmdbId: 119,
					name: '아마존 프라임',
					link: 'https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_ko_KR',
					logoUrl:
						'https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg',
				},
				status: 'Recruiting',
				account: {
					id: 1,
					identifier: null,
					password: null,
					creationDateTime: null,
					lastModificationDateTime: null,
				},
				timeStamps: {
					creationDateTime: '2022-05-20 02:33:15',
					startWatchingDateTime: null,
					endWatchingDateTime: null,
					endReportingDateTime: null,
				},
				fellows: [],
				report: {
					reported: false,
					reportCount: 0,
					leaderReportCount: 0,
				},
				role: null,
			}),
		);
	}),
	// 모집 완료
	rest.get('/providers/4', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				id: 2,
				provider: {
					id: 4,
					tmdbId: 0,
					name: '라프텔',
					link: 'https://laftel.net/',
					logoUrl:
						'https://blog.kakaocdn.net/dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png',
				},
				status: 'Recruited',
				account: {
					id: 2,
					identifier: null,
					password: null,
					creationDateTime: null,
					lastModificationDateTime: null,
				},
				timeStamps: {
					creationDateTime: '2022-05-20 02:33:25',
					startWatchingDateTime: null,
					endWatchingDateTime: null,
					endReportingDateTime: null,
				},
				fellows: [
					{
						id: 4,
						nickname: 'string',
						profileImageUrl: null,
						isLeader: false,
						isMyself: false,
					},
					{
						id: 3,
						nickname: '본인',
						profileImageUrl: null,
						isLeader: true,
						isMyself: true,
					},
					{
						id: 2,
						nickname: '캡스톤',
						profileImageUrl:
							'https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FS16182251276.jpg%3Fut%3D20220129023802',
						isLeader: false,
						isMyself: false,
					},
					{
						id: 1,
						nickname: 'ongot',
						profileImageUrl: null,
						isLeader: false,
						isMyself: false,
					},
				],
				report: {
					reported: false,
					reportCount: 0,
					leaderReportCount: 0,
				},
			}),
		);
	}),

	rest.put('/applies/leader', (req, res, ctx) => {
		return res(ctx.status(204), ctx.json({}));
	}),
];
