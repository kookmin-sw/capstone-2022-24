<template>
	<div class="home">
		<!-- 검색창~필터링 단락 -->
		<div class="search-filter-frame row q-mt-xl q-mb-xl">
			<q-space class="col-2" />
			<div class="col-8">
				<!-- 검색 -->
				<div class="search-frame row text-left q-mb-md">
					<q-input
						class="search-bar q-mb-lg"
						v-model="search"
						type="search"
						outlined
						dense>
						<q-separator color="blue" vertical inset />
						<template v-slot:append>
							<q-icon name="search" color="blue" />
						</template>
					</q-input>
				</div>
				<!--  ott 로고 필터 -->
				<div class="ott-icons-frame row q-mb-lg">
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
				</div>
				<!-- 필터링 조건 -->
				<q-list bordered>
					<q-expansion-item
						style="border-radius: 50%"
						header-class="bg-blue text-white"
						expand-icon-class="text-white"
						label="필터링 항목">
						<!-- 작품 종류 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">작품 종류</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
								<q-chip
									outline
									color="blue"
									v-for="category in filters.categories"
									:key="category.id">
									{{ category }}
								</q-chip>
							</div>
						</div>
						<!-- 상영 등급 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">상영 등급</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
								<q-chip
									outline
									color="blue"
									v-for="rate in filters.filmRatings"
									:key="rate.id">
									{{ rate }}
								</q-chip>
							</div>
						</div>
						<!-- 장르 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">장르</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
								<q-chip
									outline
									color="blue"
									v-for="genre in filters.genres"
									:key="genre.id">
									{{ genre }}
								</q-chip>
							</div>
						</div>
						<!-- 결제 종류 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">결제 종류</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
								<q-chip
									outline
									color="blue"
									v-for="offer in filters.offers"
									:key="offer.id">
									{{ offer }}
								</q-chip>
							</div>
						</div>
						<!-- 국가 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">국가</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
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
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">관람 여부</div>
							<q-separator color="blue" vertical inset />
							<div class="chips-frame q-ml-sm text-left col-9">
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
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">연도</div>
							<q-separator color="blue" vertical inset />
							<div class="q-pa-md q-pb-lg col-9">
								<q-range
									v-model="filters.year"
									:min="1970"
									:max="2022"
									:step="1"
									:left-label-value="filters.year.min + '년'"
									:right-label-value="filters.year.max + '년'"
									label-always
									switch-label-side
									color="blue" />
							</div>
						</div>
						<!-- 평점 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">평점</div>
							<q-separator color="blue" vertical inset />
							<div class="q-pa-md q-pb-lg col-9">
								<q-range
									class="range-slider"
									v-model="filters.rate"
									:min="0.5"
									:max="5.0"
									:step="0.5"
									:left-label-value="filters.rate.min + '점'"
									:right-label-value="filters.rate.max + '점'"
									label-always
									switch-label-side
									color="blue" />
							</div>
						</div>
						<!-- 상영 시간 -->
						<div class="filter-frame row q-mt-md">
							<div class="q-mt-auto q-mb-auto col-2">상영 시간</div>
							<q-separator color="blue" vertical inset />
							<div class="q-pa-md q-pb-lg col-9">
								<q-range
									class="range-slider"
									v-model="filters.runtime"
									:min="0"
									:max="240"
									:step="10"
									:left-label-value="filters.runtime.min + '분'"
									:right-label-value="filters.runtime.max + '분'"
									label-always
									switch-label-side
									color="blue" />
							</div>
						</div>
						<q-btn unelevated outline class="q-ma-lg" color="blue">
							필터 초기화
						</q-btn>
					</q-expansion-item>
				</q-list>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator color="blue" inset />
		<!-- 작품 포스터 단락 -->
		<q-infinite-scroll @load="onLoad" :offset="250" class="video-frame">
			<div class="row">
				<div
					v-for="(poster, index) in posters"
					:key="index"
					class="video col-2 q-ma-md"
					style="background: grey">
					{{ poster }}
				</div>
			</div>
			<template v-slot:loading>
				<div class="row justify-center q-my-md">
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
			filters: {
				categories: ['전체', '영화', 'TV 시리즈'],
				filmRatings: [
					'전체',
					'전체관람가',
					'12세 이상 관람가',
					'15세 이상 관람가',
					'청소년 관람불가',
				],
				genres: [
					'전체',
					'SF/판타지',
					'공포',
					'드라마',
					'로맨스',
					'스릴러',
					'시대극',
					'무협',
					'범죄/추리',
					'애니메이션',
					'액션',
					'코미디',
				],
				offers: ['전체', '구매', '대여', '정액제'],
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
			posters: [
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
				{},
				{},
			],
		};
	},
	methods: {
		onLoad(index, done) {
			setTimeout(() => {
				this.posters.push(
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
					{},
					{},
				);
				done();
			}, 2000);
		},
	},
};
</script>

<style scoped>
.search-bar {
	width: 750px;
}

.btn-frame * {
	margin-right: 12px;
}

.ott-icons-frame {
	column-gap: 16px;
}
</style>
