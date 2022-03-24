<template>
	<div class="home">
		<!-- 검색창~필터링 단락 -->
		<div class="row q-mt-xl q-mb-xl search-filter-frame">
			<q-space class="col-2" />
			<div class="col-8">
				<!-- 검색 -->
				<div class="row q-mb-xl text-left search-frame">
					<q-input
						outlined
						dense
						type="search"
						color="blue"
						class="col-9 search-bar"
						v-model="search">
					</q-input>
					<q-btn unelevated outline color="blue" class="col-2">
						<q-icon name="search" color="blue" />
					</q-btn>
				</div>
				<!--  ott 로고 필터 -->
				<div class="row q-mb-lg ott-icons-frame">
					<q-btn flat padding="none"
                 v-for="(otts, index) in ottFilters"
                 :key="index"
                 :class="{ 'ott-filter-select': otts.isSelect }"
                 @click="ottFilterClick(index)"><!-- console.log() 확인용 매개변수 -->
						<q-avatar rounded color="blue" size="60px" />
					</q-btn>
<!--          <q-avatar rounded color="blue" size="60px"-->
<!--                    v-for="(otts, index) in ottFilters"-->
<!--                    :key="index"-->
<!--                    :class="{ 'ott-filter-select': otts.isSelect }"-->
<!--                    @click="ottFilterClick(index)"/>-->
				</div>
				<!-- 필터링 조건 -->
				<q-list bordered>
					<q-expansion-item
						label="필터링 항목"
						header-class="bg-blue text-white"
						expand-icon-class="text-white">
						<!-- 작품 종류 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">작품 종류</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
                <q-chip
                    outline
                    color="blue"
                    v-for="(category, index) in categoryFilters"
                    :key="index"
                    v-model:selected="category.isSelect">
                  {{ category.label }}
                </q-chip>
							</div>
						</div>
						<!-- 상영 등급 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">상영 등급</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
								<q-chip
									outline
									color="blue"
									v-for="(rate, index) in filmRateFilters"
									:key="index"
                  v-model:selected="rate.isSelect">
									{{ rate.label }}
								</q-chip>
							</div>
						</div>
						<!-- 장르 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">장르</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
								<q-chip
									outline
									color="blue"
									v-for="(genre, index) in genreFilters"
									:key="index"
                  v-model:selected="genre.isSelect">
									{{ genre.label }}
								</q-chip>
							</div>
						</div>
						<!-- 결제 종류 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">결제 종류</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
								<q-chip
									outline
									color="blue"
									v-for="(offer, index) in offerFilters"
									:key="index"
                  v-model:selected="offer.isSelect">
									{{ offer.label }}
								</q-chip>
							</div>
						</div>
						<!-- 국가 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">국가</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
								<q-chip
									outline
									color="blue"
									v-for="country in filters.countries"
									:key="country.id">
									{{ country }}
								</q-chip>
							</div>
							<!-- 관람 여부 -->
						</div>
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">관람 여부</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-ml-sm text-left chips-frame">
								<q-chip
									outline
									color="blue"
									v-for="work in filters.watched"
									:key="work.id">
									{{ work }}
								</q-chip>
							</div>
						</div>
						<!-- 슬라이더 형태 필터링 -->
						<!-- 연도 -->
						<div class="row filter-frame q-mt-md">
							<div class="col-2 q-mt-auto q-mb-auto">연도</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-pa-md q-pb-lg">
								<q-range
									label-always
									switch-label-side
									color="blue"
									v-model="filters.year"
									:min="1970"
									:max="2022"
									:step="1"
									:left-label-value="`${filters.year.min}년`"
									:right-label-value="`${filters.year.max}년`" />
							</div>
						</div>
						<!-- 평점 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">평점</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-pa-md q-pb-lg">
								<q-range
									label-always
									switch-label-side
									color="blue"
									v-model="filters.rate"
									:min="0.5"
									:max="5"
									:step="0.5"
									:left-label-value="`${filters.rate.min}점`"
									:right-label-value="`${filters.rate.max}점`" />
							</div>
						</div>
						<!-- 상영 시간 -->
						<div class="row q-mt-md filter-frame">
							<div class="col-2 q-mt-auto q-mb-auto">상영 시간</div>
							<q-separator vertical inset color="blue" />
							<div class="col-9 q-pa-md q-pb-lg">
								<q-range
									label-always
									switch-label-side
									color="blue"
									v-model="filters.runtime"
									:min="0"
									:max="240"
									:step="10"
									:left-label-value="`${filters.runtime.min}분`"
									:right-label-value="`${filters.runtime.max}분`" />
							</div>
						</div>
						<q-btn unelevated outline color="blue" class="q-ma-lg">
							필터 초기화
						</q-btn>
					</q-expansion-item>
				</q-list>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator inset color="blue" />
		<!-- 정렬 -->
		<div class="row q-ma-md q-mt-xl q-pl-md q-pr-md text-left">
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
		<!-- 작품 포스터 단락 -->
		<q-infinite-scroll :offset="250" @load="videoOnLoad">
			<div class="row q-ma-lg video-list-frame">
				<div class="video-poster" v-for="(video, index) in videos" :key="index">
					{{ video.value }}
				</div>
			</div>
			<template v-slot:loading>
				<div class="row q-mb-lg justify-center">
					<q-spinner-dots color="primary" size="40px" />
				</div>
			</template>
		</q-infinite-scroll>
	</div>
</template>

<script>
export default {
	name: 'Home',
	data() {
		return {
      ottFilters: {
        netflix: { isSelect: false },
        watcha: { isSelect: false },
        disneyPlus: { isSelect: false },
        tving: { isSelect: false },
        wavve: { isSelect: false },
      },
      categoryFilters: {
        all: { label: '전체', isSelect: false },
        movies: { label: '영화', isSelect: false },
        tvSeries: { label: 'TV 시리즈', isSelect: false },
      },
      filmRateFilters: {
        all: { label: '전체', isSelect: false },
        gRated: { label: '전체관람가', isSelect: false },
        pg12: { label: '12세 이상 관람가', isSelect: false },
        pg15: { label: '15세 이상 관람가', isSelect: false },
        pg18: { label: '청소년 관람불가', isSelect: false },
      },
      genreFilters: {
        all: { label: '전체', isSelect: false },
        fantasy: { label: 'SF/판타지', isSelect: false },
        horror: { label: '공포', isSelect: false },
        drama: { label: '드라마', isSelect: false },
        romance: { label: '로맨스', isSelect: false },
        thriller: { label: '스릴러', isSelect: false },
        historicalDrama: { label: '시대극', isSelect: false },
        martialArts: { label: '무협', isSelect: false },
        mystery: { label: '범죄/추리', isSelect: false },
        animation: { label: '애니메이션', isSelect: false },
        action: { label: '액션', isSelect: false },
        comedy: { label: '코미디', isSelect: false },
      },
      offerFilters: {
        all: { label: '전체', isSelect: false },
        purchase: { label: '구매', isSelect: false },
        rental: { label: '대여', isSelect: false },
        flatRate: { label: '정액제', isSelect: false },
      },
			filters: {
				countries: ['전체', '국내', '해외'],
				watched: ['전체', '본 작품', '안 본 작품'],
				year: {
					min: 1970,
					max: 2022,
				},
				rate: {
					min: 0.5,
					max: 5.0,
				},
				runtime: {
					min: 0,
					max: 240,
				},
			},
			search: null,
			videos: [
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
			],

      selected: '',
		};
	},
	methods: {
		videoOnLoad(index, done) {
			setTimeout(() => {
				this.videos.push({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
				done();
			}, 2000);
		},
		ottFilterClick(idx) {
      this.ottFilters[idx].isSelect = !this.ottFilters[idx].isSelect;
    },
	},
};
</script>

<style scoped>
.ott-icons-frame {
	column-gap: 16px;
}
.video-list-frame {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-between;
}
.ott-filter-select {
  border: 3px solid darkblue;
  border-radius: 7px;
}
.video-poster {
	width: 15%;
	height: 0;
	padding-bottom: 20%;
	margin: 0 0 24px 0;
	background: lightgrey;
}
</style>
