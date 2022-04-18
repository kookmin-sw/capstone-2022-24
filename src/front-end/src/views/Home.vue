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
					class="border-blue-100 left-radius-2 col-9 q-pl-md q-pr-md"
					id="search-input" />
				<q-btn
					flat
					color="blue"
					class="border-blue-100 right-radius-2 col-2"
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
						@click="ottFilterClick(index)" />
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
						<select-filter
							:filter-label="'관람여부'"
							:filter-name="'WATCHED'"
							:conditions="selectFilters.watched"
							id="watched-filter" />
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
									:min="1800"
									:max="2022"
									:step="1"
									:left-label-value="`${slideFilters.year.min}년`"
									:right-label-value="`${slideFilters.year.max}년`" />
							</div>
						</div>
						<!-- 평점 -->
						<div class="row q-mt-md" id="rating-filter">
							<div class="col-2 q-mt-auto q-mb-auto">평점</div>
							<q-separator vertical inset color="blue-4" />
							<div class="col-9 q-pa-md q-pb-lg">
								<q-range
									label-always
									switch-label-side
									color="blue-4"
									v-model="slideFilters.rate"
									:min="0.5"
									:max="5"
									:step="0.5"
									:left-label-value="`${slideFilters.rate.min}점`"
									:right-label-value="`${slideFilters.rate.max}점`" />
							</div>
						</div>
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
			<q-btn flat>랜덤순</q-btn>
			<q-btn flat>평점순</q-btn>
			<q-btn flat>최신순</q-btn>
			<q-btn flat>인기순</q-btn>
		</div>
		<!-- 작품 목록 -->
		<q-infinite-scroll :offset="250" @load="videoOnLoad" id="videos-container">
			<div class="row" id="videos-wrapper">
				<!--								<div class="videos" v-for="(video, index) in videos" :key="index">-->
				<!--									{{ video }}-->
				<!--								</div>-->
			</div>
			<template v-slot:loading>
				<div class="row justify-center">
					<q-spinner-dots color="primary" size="40px" />
				</div>
			</template>
		</q-infinite-scroll>
	</div>
</template>

<script>
// import mapState from 'vuex';
import selectFilter from '@/components/SelectFilter';

export default {
	name: 'Home',
	components: {
		selectFilter,
	},
	data() {
		return {
			ottFilters: {
				netflix: { label: '넷플릭스', isSelect: false },
				watcha: { label: '왓챠', isSelect: false },
				disneyPlus: { label: '디즈니플러스', isSelect: false },
				tving: { label: '티빙', isSelect: false },
				wavve: { label: '웨이브', isSelect: false },
			},
			selectFilters: {
				categories: [
					{ label: '전체', isSelect: false, name: 'all' },
					{ label: '영화', isSelect: false, name: 'movie' },
					{ label: 'TV 시리즈', isSelect: false, name: 'tv' },
				],
				genres: [
					{ label: '전체', isSelect: false, name: 'all' },
					{ label: 'SF/판타지', isSelect: false, name: 'sf' },
					{ label: '공포', isSelect: false, name: 'horror' },
					{ label: '드라마', isSelect: false, name: 'drama' },
					{ label: '로맨스', isSelect: false, name: 'romance' },
					{ label: '스릴러', isSelect: false, name: 'thriller' },
					{ label: '시대극', isSelect: false, name: 'historicalDrama' },
					{ label: '무협', isSelect: false, name: 'martialArts' },
					{ label: '범죄/추리', isSelect: false, name: 'mystery' },
					{ label: '애니메이션', isSelect: false, name: 'animation' },
					{ label: '액션', isSelect: false, name: 'action' },
					{ label: '코미디', isSelect: false, name: 'comedy' },
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
					min: 1800,
					max: 2022,
				},
				rate: {
					min: 0.5,
					max: 5.0,
				},
			},
			search: null,
			selected: {
				ott: [],
			},
		};
	},
	computed: {
		// ...mapState('videoList', ['videos']),
	},
	async beforeCreate() {
		await this.$store.dispatch('videoList/initVideoList');
	},
	methods: {
		videoOnLoad() {
			// setTimeout(() => {
			// 	this.videos.push({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
			// 	done();
			// }, 2000);
		},
		ottFilterClick(idx) {
			this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
			if (this.ottFilters[idx].isSelect === true) {
				this.selected.ott.push(this.ottFilters[idx].label);
			} else this.selected.ott.splice(this.ottFilters[idx].label, 1);
		},
		initButtonClick() {
			// 선택형 필터 초기화
			for (let key in this.selectFilters) {
				this.selectFilters[key].forEach(cond => {
					cond.isSelect = false;
				});
			}
			// 슬라이드형 필터 초기화
			this.slideFilters.year.min = 1800;
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
	padding-bottom: 20%;
	margin: 0 0 24px 0;
	background: lightgrey;
}
</style>
