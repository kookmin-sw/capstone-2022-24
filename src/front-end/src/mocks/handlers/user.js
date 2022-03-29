import { rest } from 'msw';
export default [
	// 마이페이지 최초 접근
	rest.get('/users/mypage', (req, res, ctx) => {
		return res(
			ctx.status(200),
			ctx.json({
				profile: {
					nickname: 'exampleNickname',
					email: 'exampleEmail',
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
							id: 'ott id',
							name: 'ott name',
							link: 'ott link',
							logoUrl: 'ott logo url',
						},
						status: 'reviewing',
						timeStamps: {
							creationDateTime: '모임시작일',
							startWatchingDateTime: '관람시작일',
							endWatchingDateTime: '관람종료일',
							endReportingDateTime: '검토마감일시',
						},
						reportCount: 0,
						account: {
							id: 'example group ott id',
							password: 'example group ott pw',
							lastModifiedDateTime: '계정 최종 수정일',
						},
						fellows: [
							{
								id: 'member 01 id',
								profileImgUrl: 'member 01 profile url',
								nickname: 'member 01 nickname',
								isLeader: true,
								isMyself: true,
							},
							{
								id: 'member 02 id',
								profileImgUrl: 'member 02 profile url',
								nickname: 'member 02 nickname',
								isLeader: true,
								isMyself: true,
							},
							{
								id: 'member 03 id',
								profileImgUrl: 'member 03 profile url',
								nickname: 'member 03 nickname',
								isLeader: true,
								isMyself: true,
							},
							{
								id: 'member 04 id',
								profileImgUrl: 'member 04 profile url',
								nickname: 'member 04 nickname',
								isLeader: true,
								isMyself: true,
							},
						],
					},
					// 나머지 모임 구독 정보
					others: null,
				},
				videos: {
					recentViews: {
						results: [
							{
								id: 1,
								tmbdId: 1,
								posterUrl: 'poster url',
							},
							{
								id: 2,
								tmbdId: 2,
								posterUrl: 'poster url',
							},
						],
						page: {
							totalPage: 1,
							totalResult: 2,
						},
					},
					watchMarks: {
						results: [],
						page: {},
					},
					dibs: {
						results: null,
						page: null,
					},
					stars: null,
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
