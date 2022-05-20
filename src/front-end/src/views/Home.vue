<template>
	<div class="home-frame">
		<!-- 검색 -->
		<div class="row q-ma-lg" id="search-container ">
			<q-space class="col-2" />
			<div class="col-8 row q-mt-lg q-mb-lg" id="search-bar">
				<q-input
					clearable
					dense
					borderless
					clear-icon="close"
					v-model="search"
					class="border-blue-100 left-radius-2 col-10 q-pl-md q-pr-md"
					id="search-input" />
				<q-btn
					flat
					color="blue"
					class="border-blue-100 right-radius-2 col-2"
					@click="searchButtonClick"
					id="search-btn">
					<q-icon name="search" />
				</q-btn>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- 필터링 -->
		<div class="row q-ma-lg" id="filters-container">
			<q-space class="col-2" />
			<div class="col-8" id="filters-wrapper">
				<!--  ott 필터 -->
				<div class="row q-mb-lg" id="ott-filters-wrapper">
					<q-avatar
						rounded
						color="grey-4"
						size="60px"
						v-for="(ott, index) in ottFilters"
						:key="index"
						:class="{ 'ott-filter-select': ott.isSelect }"
						class="q-mr-sm"
						@click="ottFilterClick(index)">
						<img :src="ott.logoUrl" :alt="ott.name" />
					</q-avatar>
				</div>
				<!-- 세부 필터 -->
				<q-list bordered class="q-mb-lg radius-4">
					<q-expansion-item
						label="필터링 항목"
						header-class="bg-blue-100 text-white text-weight-bold radius-4"
						expand-icon-class="text-white">
						<!-- 작품 종류 -->
						<select-filter
							:filter-label="'작품 종류'"
							:filter-name="'CATEGORIES'"
							:conditions="selectFilters.categories"
							id="categories-filter" />
						<!-- 장르 -->
						<select-filter
							:filter-label="'장르'"
							:filter-name="'GENRES'"
							:conditions="selectFilters.genres"
							id="genres-filter" />
						<!-- 국가 -->
						<select-filter
							:filter-label="'국가'"
							:filter-name="'COUNTRY'"
							:conditions="selectFilters.countries"
							id="countries-filter" />
						<!-- 관람 여부 -->
						<!--						<select-filter-->
						<!--							:filter-label="'관람여부'"-->
						<!--							:filter-name="'WATCHED'"-->
						<!--							:conditions="selectFilters.watched"-->
						<!--							id="watched-filter" />-->
						<!-- 연도 -->
						<div class="row q-mt-md" id="years-filter">
							<div class="col-2 q-mt-auto q-mb-auto">연도</div>
							<q-separator vertical inset dense color="blue-4" />
							<div class="col-9 q-pa-md q-pb-lg">
								<q-range
									label-always
									switch-label-side
									color="blue-4"
									v-model="slideFilters.year"
									@change="yearFilterClick"
									:min="1985"
									:max="2022"
									:step="1"
									:left-label-value="`${slideFilters.year.min}년`"
									:right-label-value="`${slideFilters.year.max}년`" />
							</div>
						</div>
						<!-- 평점 -->
						<!--						<div class="row q-mt-md" id="rating-filter">-->
						<!--							<div class="col-2 q-mt-auto q-mb-auto">평점</div>-->
						<!--							<q-separator vertical inset color="blue-4" />-->
						<!--							<div class="col-9 q-pa-md q-pb-lg">-->
						<!--								<q-range-->
						<!--									label-always-->
						<!--									switch-label-side-->
						<!--									color="blue-4"-->
						<!--									v-model="slideFilters.rate"-->
						<!--									:min="0.5"-->
						<!--									:max="5"-->
						<!--									:step="0.5"-->
						<!--									:left-label-value="`${slideFilters.rate.min}점`"-->
						<!--									:right-label-value="`${slideFilters.rate.max}점`" />-->
						<!--							</div>-->
						<!--						</div>-->
						<!-- 필터 초기화 버튼 -->
						<q-btn
							flat
							color="blue"
							class="q-ma-lg border-blue-100 radius-4"
							text-color="grey-10"
							style="width: 180px"
							id="filters-init-btn"
							@click="initButtonClick">
							필터링 초기화
						</q-btn>
					</q-expansion-item>
				</q-list>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator inset color="blue-1" size="2px" />
		<q-separator inset color="blue-4" />
		<!-- 정렬 -->
		<div class="row q-ma-lg text-left" id="sort-container">
			<div class="q-mt-auto q-mb-auto text-center">정렬</div>
			<q-icon
				color="blue"
				size="24px"
				class="q-mt-auto q-mb-auto"
				name="navigate_next" />
			<q-btn
				flat
				v-for="(s, index) in this.sort"
				:key="index"
				@click="sortButtonClick(index)"
				:class="{ 'text-blue-200 text-bold': s.isSelect }">
				{{ s.label }}
			</q-btn>
		</div>
		<!-- 작품 목록 -->
		<q-infinite-scroll
			:offset="250"
			@load="videoOnLoad"
			id="videos-container"
			:number="1">
			<div class="row" id="videos-wrapper">
				<div class="videos" v-for="video in videos" :key="video.id">
					<img
						:src="video.posterKey"
						:alt="video.title"
						style="width: 100%; object-fit: cover"
						@click="videoClick(video.videoId, video.category)" />
				</div>
			</div>
			<template v-slot:loading>
				<div class="row justify-center" v-if="videos.length < totalResult">
					<q-spinner-dots color="primary" size="40px" class="q-mb-lg" />
				</div>
			</template>
			<div
				class="q-mb-xl text-h6 text-bold"
				v-if="loadFail && videos.length === 0">
				작품이 존재하지 않습니다.
			</div>
		</q-infinite-scroll>
	</div>
</template>

<script>
import { mapState } from 'vuex';
import selectFilter from '@/components/SelectFilter';

export default {
	name: 'Home',
	components: {
		selectFilter,
	},
	data() {
		return {
			ottFilters: {
				netflix: {
					label: '넷플릭스',
					isSelect: false,
					name: 'NF',
					logoUrl:
						'https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg',
				},
				watcha: {
					label: '왓챠',
					isSelect: false,
					name: 'WC',
					logoUrl:
						'https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg',
				},
				disneyPlus: {
					label: '디즈니플러스',
					isSelect: false,
					name: 'DP',
					logoUrl:
						'https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg',
				},
				wavve: {
					label: '웨이브',
					isSelect: false,
					name: 'WV',
					logoUrl:
						'https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg',
				},
			},
			selectFilters: {
				categories: [
					{ label: '전체', isSelect: false, name: 'all' },
					{ label: '영화', isSelect: false, name: 'MV' },
					{ label: 'TV 시리즈', isSelect: false, name: 'TV' },
				],
				genres: [
					{ label: '전체', isSelect: false, name: '전체' },
					{ label: 'SF', isSelect: false, name: 'SF' },
					{ label: '판타지', isSelect: false, name: '판타지' },
					{ label: '공포', isSelect: false, name: '공포' },
					{ label: '드라마', isSelect: false, name: '드라마' },
					{ label: '로맨스', isSelect: false, name: '로맨스' },
					{ label: '스릴러', isSelect: false, name: '스릴러' },
					{ label: '시대극', isSelect: false, name: '역사' },
					{ label: '범죄/추리', isSelect: false, name: '미스터리' },
					{ label: '애니메이션', isSelect: false, name: '애니메이션' },
					{ label: '액션', isSelect: false, name: '액션' },
					{ label: '코미디', isSelect: false, name: '코미디' },
				],
				countries: [
					{ label: '전체', isSelect: false, name: 'all' },
					{ label: '국내', isSelect: false, name: 'KR' },
					{ label: '해외', isSelect: false, name: 'OTHERS' },
				],
				watched: [
					{ label: '전체', isSelect: false, name: 'all' },
					{ label: '본 작품', isSelect: false, name: 'watched' },
					{ label: '안 본 작품', isSelect: false, name: 'unwathced' },
				],
			},
			slideFilters: {
				year: {
					min: 1985,
					max: 2022,
				},
				rate: {
					min: 0.5,
					max: 5.0,
				},
			},
			search: null,
			sort: [
				{ label: '랜덤순', isSelect: true, name: 'random' },
				{ label: '최신순', isSelect: false, name: 'new' },
				{ label: '개봉순', isSelect: false, name: 'release' },
				// { label: '평점순', isSelect: false, name: 'rating' },
				// { label: '인기순', isSelect: false, name: 'wish' },
			],
			selected: {
				ott: [],
			},
			limit: 24,
			videoList: new Set(),
		};
	},
	computed: {
		...mapState('videoList', ['videos', 'totalResult', 'loadFail']),
	},
	async beforeCreate() {
		window.reload;
		await this.$store.dispatch('videoList/initSetting');
		await this.$store.dispatch('videoList/loadVideoList', 0);
	},
	methods: {
		async videoOnLoad(index, done) {
			if (this.videos.length <= this.totalResult) {
				setTimeout(() => {
					this.$store.dispatch('videoList/loadVideoList', this.videos.length);
					done();
				}, 1000);
			}
		},
		videoClick(videoId, category) {
			this.$router.push({ name: 'Details', params: { videoId, category } });
		},
		searchButtonClick() {
			this.$store.dispatch('videoList/searchVideos', this.search);
		},
		sortButtonClick(idx) {
			this.sort.forEach(i => {
				if (i !== idx) {
					i.isSelect = false;
				}
			});
			this.sort[idx].isSelect = true;
			this.$store.dispatch('videoList/sortVideos', this.sort[idx].name);
		},
		ottFilterClick(idx) {
			this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
			if (this.ottFilters[idx].isSelect === true) {
				this.selected.ott.push(this.ottFilters[idx].name);
			} else this.selected.ott.splice(this.ottFilters[idx].name, 1);
			const condition = {
				name: 'PROVIDERS',
				selected: this.selected.ott,
			};
			this.$store.dispatch('videoList/filterVideos', condition);
		},
		yearFilterClick() {
			const condition = {
				name: 'YEAR',
				range: this.slideFilters.year,
			};
			this.$store.dispatch('videoList/slideFilterVideos', condition);
		},
		initButtonClick() {
			// 선택형 필터 초기화
			for (let key in this.selectFilters) {
				this.selectFilters[key].forEach(cond => {
					cond.isSelect = false;
				});
			}
			// 슬라이드형 필터 초기화
			this.slideFilters.year.min = 1985;
			this.slideFilters.year.max = 2022;
			this.slideFilters.rate.min = 0.5;
			this.slideFilters.rate.max = 5;
			this.$store.dispatch('videoList/initSelectCondition');
		},
	},
};
</script>

<style scoped>
#videos-wrapper {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-between;
}
.ott-filter-select {
	border: 3px solid #449bfe;
	border-radius: 6px;
}
.videos {
	width: 15%;
	height: 0;
	padding-bottom: 21%;
	margin: 0 0 24px 0;
	background: transparent;
	align-content: center;
	overflow-y: hidden;
}
</style>
