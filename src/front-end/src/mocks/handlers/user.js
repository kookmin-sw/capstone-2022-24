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
							name: '넷플릭스',
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
								nickname: '난쟁이가쏘아올린',
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
								name: '왓챠',
								link: 'https://watcha.com/',
								logoUrl: 'watcha logo img',
							},
						},
						{
							provider: {
								id: 'ott0003',
								name: '웨이브',
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
							totalPage: 5,
							totalResult: 31,
						},
					},
					watchMarks: {
						results: [],
						page: {
							totalPage: 1,
							totalResult: 0,
						},
					},
					dibs: {
						results: [
							{
								id: 13,
								tmdbId: 13,
								posterUrl: '13 poster Url',
								dateTime: '2022-03-30',
							},
							{
								id: 14,
								tmdbId: 14,
								posterUrl: '14 poster Url',
								dateTime: '2022-03-30',
							},
						],
						page: {
							totalPage: 1,
							totalResult: 2,
						},
					},
					stars: {
						results: [],
						page: {
							totalPage: 1,
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
						id: 7,
						tmdbId: 7,
						posterUrl: '07 poster Url',
						dateTime: '2022-03-30',
					},
					{
						id: 8,
						tmdbId: 8,
						posterUrl: '08 poster Url',
						dateTime: '2022-03-30',
					},
					{
						id: 9,
						tmdbId: 9,
						posterUrl: '09 poster Url',
						dateTime: '2022-03-30',
					},
					{
						id: 10,
						tmdbId: 10,
						posterUrl: '10 poster Url',
						dateTime: '2022-03-28',
					},
					{
						id: 11,
						tmdbId: 11,
						posterUrl: '11 poster Url',
						dateTime: '2022-03-27,',
					},
					{
						id: 12,
						tmdbId: 12,
						posterUrl: '12 poster Url',
						dateTime: '2022-03-27',
					},
				],
				page: {
					current: 2,
					totalPage: 6,
					totalResult: 31,
				},
			}),
		);
	}),
	rest.get('/users/mypage/dibs', (req, res, ctx) => {
		return res(
			ctx.json({
				results: [],
				page: {
					current: 1,
					totalPage: 1,
					totalResult: 2,
				},
			}),
		);
	}),
	rest.get('/users/mypage/stars', (req, res, ctx) => {
		return res(
			ctx.json({
				results: [],
				page: {
					current: 1,
					totalPage: 1,
					totalResult: 2,
				},
			}),
		);
	}),
	rest.get('/users/mypage/watch-marks', (req, res, ctx) => {
		return res(
			ctx.json({
				results: [],
				page: {
					current: 1,
					totalPage: 1,
					totalResult: 2,
				},
			}),
		);
	}),
];
