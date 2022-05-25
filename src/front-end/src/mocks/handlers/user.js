import { rest } from 'msw';
export default [
	// 마이페이지 최초 접근
	rest.get('/mypage/', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				profile: {
					nickname: 'ongot',
					name: 'ongot',
					email: 'ongot@123.com',
					cellPhoneNumber: '010-1234-5678',
					profileImageUrl: null,
					birthday: '1990-01-01',
					isActive: true,
					isVerified: true,
				},
				groups: {
					default: {
						provider: {
							id: 1,
							tmdbId: 8,
							name: 'NF',
							link: '',
							logoUrl:
								'https://some.storage.com/providers/logo_images/app/back-end/static/https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg',
						},
						status: 'Recruited',
						timeStamps: {
							creationDateTime: '2022-05-14T03:11:47',
							startWatchingDateTime: '2022-05-14T03:11:58',
							endWatchingDateTime: null,
							endReportingDateTime: '2022-05-17T03:11:58',
						},
						fellows: [
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
								isLeader: true,
								isMyself: true,
							},
						],
						account: {
							id: 1,
							identifier: null,
							password: 'password123456',
							creationDateTime: null,
							lastModificationDateTime: null,
						},
						report: {
							reported: true,
							reportCount: 1,
							leaderReportCount: 0,
						},
					},
					others: [
						{
							fellows: [],
							provider: {
								id: 4,
								tmdbId: 337,
								name: 'DP',
								link: 'https://default_ott_link.com',
								logoUrl:
									'https://some.storage.com/providers/logo_images/app/back-end/static/https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg',
							},
							applyDateTime: '2022-05-17T01:23:47',
							status: 'Recruiting',
						},
					],
				},
				videos: {
					recentViews: {
						page: { limit: 3, offset: 0, totalCount: 4 },
						results: [
							{
								id: 9,
								tmdbId: 454626,
								posterUrl:
									'https://image.tmdb.org/t/p/original/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg',
							},
							{
								id: 14,
								tmdbId: 783461,
								posterUrl:
									'https://image.tmdb.org/t/p/original/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg',
							},
							{
								id: 19,
								tmdbId: 800407,
								posterUrl:
									'https://image.tmdb.org/t/p/original/hmqocSNKCgMY5yrVOOmfCUHdXkl.jpg',
							},
						],
					},
					watchMarks: {
						page: { limit: 3, offset: 0, totalCount: 0 },
						results: [],
					},
					wishes: {
						page: { limit: 3, offset: 0, totalCount: 1 },
						results: [
							{
								id: 167,
								tmdbId: 76479,
								posterUrl:
									'https://image.tmdb.org/t/p/original/dzOxNbbz1liFzHU1IPvdgUR647b.jpg',
							},
						],
					},
					stars: { page: { limit: 3, offset: 0, totalCount: 0 }, results: [] },
				},
			}),
		);
	}),
];
