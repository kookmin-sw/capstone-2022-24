import { rest } from 'msw';
export default [
	// 마이페이지 최초 접근
	rest.get('/users/mypage', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				profile: {
					nickname: '모르는개산책',
					email: 'example@naver.com',
					cellPhoneNumber: '010-xxxx-xxxx',
					profileImgUrl: 'exampleImgUrl',
					block: {
						isBlocked: false,
						endBlockingDateTime: null,
					},
					socialType: {
						name: 'Naver',
						logoUrl: 'NaverlogoUrl',
					},
				},
				groups: {
					default: {
						provider: {
							id: 'ott0001',
							name: 'netflix',
							link: 'https://www.netflix.com/kr/',
							logoUrl: 'netflix logo img',
						},
						status: 'watching',
						timeStamps: {
							creationDateTime: '2022-03-01',
							startWatchingDateTime: '2022-03-19',
							endWatchingDateTime: '2022-04-18',
							endReportingDateTime: '2022-03-22',
						},
						reportCount: 0,
						account: {
							id: 'netflix@email.com',
							password: 'netflx01Pw',
							lastModifiedDateTime: '2022-03-19',
						},
						fellows: [
							{
								id: 'user0001',
								profileImgUrl: 'member 01 profile url',
								nickname: '모르는개산책',
								isLeader: true,
								isMyself: true,
							},
							{
								id: 'user0002',
								profileImgUrl: 'member 02 profile url',
								nickname: '난쟁이가쏘아올린작은공인인증서',
								isLeader: false,
								isMyself: false,
							},
							{
								id: 'user0003',
								profileImgUrl: 'member 03 profile url',
								nickname: 'charlotte',
								isLeader: false,
								isMyself: false,
							},
							{
								id: 'user0004',
								profileImgUrl: 'member 04 profile url',
								nickname: 'zi존국밥',
								isLeader: false,
								isMyself: false,
							},
						],
					},
					// 나머지 모임 구독 정보
					others: [
						{
							provider: {
								id: 'ott0002',
								name: 'watcha',
								link: 'https://watcha.com/',
								logoUrl: 'watcha logo img',
							},
						},
						{
							provider: {
								id: 'ott0003',
								name: 'wavve',
								link: 'https://www.wavve.com/',
								logoUrl: 'wavve logo img',
							},
						},
					],
				},
				// 사용자 작품 정보
				videos: {
					recentViews: {
						results: [
							{
								id: 1,
								tmdbId: 1,
								posterUrl: '01 poster Url',
								dateTime: '2022-03-30',
							},
							{
								id: 2,
								tmdbId: 2,
								posterUrl: '02 poster Url',
								dateTime: '2022-03-30',
							},
							{
								id: 3,
								tmdbId: 3,
								posterUrl: '03 poster Url',
								dateTime: '2022-03-30',
							},
							{
								id: 4,
								tmdbId: 4,
								posterUrl: '04 poster Url',
								dateTime: '2022-03-28',
							},
							{
								id: 5,
								tmdbId: 5,
								posterUrl: '05 poster Url',
								dateTime: '2022-03-27,',
							},
							{
								id: 6,
								tmdbId: 6,
								posterUrl: '06 poster Url',
								dateTime: '2022-03-27',
							},
						],
						page: {
							totalPage: 6,
							totalResult: 31,
						},
					},
					watchMarks: {
						results: [],
						page: {},
					},
					dibs: {
						results: [],
						page: {
							totalPage: 0,
							totalResult: 0,
						},
					},
					stars: {
						results: [],
						page: {
							totalPage: 0,
							totalResult: 0,
						},
					},
				},
			}),
		);
	}),
	// 최근 조회 작품 목록 조회 (2p~)
	rest.get('/users/mypage/recent-views', (req, res, ctx) => {
		return res(
			ctx.json({
				results: [
					{
						id: 1,
						tmdbId: 1,
						dateTime: '2022-03-29',
						posterUrl: 'example poster URl',
					},
				],
				page: {
					current: 1,
					totalPage: 1,
					totalResult: 2,
				},
			}),
		);
	}),
];
