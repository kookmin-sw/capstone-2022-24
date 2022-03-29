<template>
	<div class="home">
		<!-- 검색창~필터링 단락 -->
		<div class="row q-mt-xl q-mb-xl search-filter-frame">
			<q-space class="col-2" />
			<div class="col-8">
				<!-- 검색 -->
				<div class="row q-mb-xl text-left search-frame">
					<q-input
						clearable
						clear-icon="close"
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
					<!--					<q-btn-->
					<!--						flat-->
					<!--						padding="none"-->
					<!--						v-for="(otts, index) in ottFilters"-->
					<!--						:key="index"-->
					<!--						:class="{ 'ott-filter-select': otts.isSelect }"-->
					<!--						@click="ottFilterClick(index)"-->
					<!--						>&lt;!&ndash; console.log() 확인용 매개변수 &ndash;&gt;-->
					<!--						<q-avatar rounded color="blue" size="60px" />-->
					<!--					</q-btn>-->
					<q-avatar
						rounded
						color="blue"
						size="60px"
						v-for="(otts, index) in ottFilters"
						:key="index"
						:class="{ 'ott-filter-select': otts.isSelect }"
						@click="ottFilterClick(index)" />
          확인: {{ selected.ott }}
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
									v-model:selected="category.isSelect"
									@click="filterClick(category)">
									{{ category.label }}
								</q-chip>
								확인 :{{ selected.category }}
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
									v-model:selected="rate.isSelect"
									@click="filterClick(rate)">
									{{ rate.label }}
								</q-chip>
								확인 :{{ selected.filmRate }}
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
									v-model:selected="genre.isSelect"
									@click="filterClick(genre)">
									{{ genre.label }}
								</q-chip>
								확인 :{{ selected.genre }}
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
									v-model:selected="offer.isSelect"
									@click="filterClick(offer)">
									{{ offer.label }}
								</q-chip>
								확인 :{{ selected.offer }}
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
									v-for="(country, index) in countryFilters"
									:key="index"
									v-model:selected="country.isSelect"
									@click="filterClick(country)">
									{{ country.label }}
								</q-chip>
								확인 :{{ selected.country }}
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
									v-for="(work, index) in watchedFilters"
									:key="index"
									v-model:selected="work.isSelect"
									@click="filterClick(work)">
									{{ work.label }}
								</q-chip>
								확인 :{{ selected.watched }}
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
				netflix: { label: '넷플릭스', isSelect: false },
				watcha: { label: '왓챠', isSelect: false },
				disneyPlus: { label: '디즈니플러스', isSelect: false },
				tving: { label: '티빙', isSelect: false },
				wavve: { label: '웨이브', isSelect: false },
			},
			categoryFilters: {
				all: { label: '전체', isSelect: false, filterName: 'category' },
				movies: { label: '영화', isSelect: false, filterName: 'category' },
				tvSeries: {
					label: 'TV 시리즈',
					isSelect: false,
					filterName: 'category',
				},
			},
			filmRateFilters: {
				all: { label: '전체', isSelect: false, filterName: 'filmRate' },
				gRated: {
					label: '전체관람가',
					isSelect: false,
					filterName: 'filmRate',
				},
				pg12: {
					label: '12세 이상 관람가',
					isSelect: false,
					filterName: 'filmRate',
				},
				pg15: {
					label: '15세 이상 관람가',
					isSelect: false,
					filterName: 'filmRate',
				},
				pg18: {
					label: '청소년 관람불가',
					isSelect: false,
					filterName: 'filmRate',
				},
			},
			genreFilters: {
				all: { label: '전체', isSelect: false, filterName: 'genre' },
				fantasy: { label: 'SF/판타지', isSelect: false, filterName: 'genre' },
				horror: { label: '공포', isSelect: false, filterName: 'genre' },
				drama: { label: '드라마', isSelect: false, filterName: 'genre' },
				romance: { label: '로맨스', isSelect: false, filterName: 'genre' },
				thriller: { label: '스릴러', isSelect: false, filterName: 'genre' },
				historicalDrama: {
					label: '시대극',
					isSelect: false,
					filterName: 'genre',
				},
				martialArts: { label: '무협', isSelect: false, filterName: 'genre' },
				mystery: { label: '범죄/추리', isSelect: false, filterName: 'genre' },
				animation: {
					label: '애니메이션',
					isSelect: false,
					filterName: 'genre',
				},
				action: { label: '액션', isSelect: false, filterName: 'genre' },
				comedy: { label: '코미디', isSelect: false, filterName: 'genre' },
			},
			offerFilters: {
				all: { label: '전체', isSelect: false, filterName: 'offer' },
				purchase: { label: '구매', isSelect: false, filterName: 'offer' },
				rental: { label: '대여', isSelect: false, filterName: 'offer' },
				flatRate: { label: '정액제', isSelect: false, filterName: 'offer' },
			},
			countryFilters: {
				all: { label: '전체', isSelect: false, filterName: 'country' },
				domestic: { label: '국내', isSelect: false, filterName: 'country' },
				international: {
					label: '해외',
					isSelect: false,
					filterName: 'country',
				},
			},
			watchedFilters: {
				all: { label: '전체', isSelect: false, filterName: 'watched' },
				watched: { label: '본 작품', isSelect: false, filterName: 'watched' },
				unwathced: {
					label: '안 본 작품',
					isSelect: false,
					filterName: 'watched',
				},
			},
			filters: {
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
			selected: {
        ott: [],
				category: [],
				filmRate: [],
				genre: [],
				offer: [],
				country: [],
				watched: [],
			},
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
      if (this.ottFilters[idx].isSelect === true) {
        this.selected.ott.push(this.ottFilters[idx].label);
      }else this.selected.ott.splice(this.ottFilters[idx].label, 1);
		},
		filterClick(idx) {
			if (idx.label === '전체' && idx.isSelect === true) {
				switch (idx.filterName) {
					case 'category':
						for (let key in this.categoryFilters) {
              if (!this.selected.category.includes(this.categoryFilters[key].label)) {
                this.selected.category.push(this.categoryFilters[key].label);
              }
							this.selected.category = this.selected.category.filter(
								element => element !== idx.label,
							);
						}
						break;
					case 'filmRate':
						for (let key in this.filmRateFilters) {
              if (!this.selected.filmRate.includes(this.filmRateFilters[key].label)) {
                this.selected.filmRate.push(this.filmRateFilters[key].label);
              }
							this.selected.filmRate = this.selected.filmRate.filter(
								element => element !== idx.label,
							);
						}
						break;
					case 'genre':
						for (let key in this.genreFilters) {
              if (!this.selected.genre.includes(this.genreFilters[key].label)) {
                this.selected.genre.push(this.genreFilters[key].label);
              }
							this.selected.genre = this.selected.genre.filter(
								element => element !== idx.label,
							);
						}
						break;
					case 'offer':
						for (let key in this.offerFilters) {
              if (!this.selected.offer.includes(this.offerFilters[key].label)) {
                this.selected.offer.push(this.offerFilters[key].label);
              }
							this.selected.offer = this.selected.offer.filter(
								element => element !== idx.label,
							);
						}
						break;
					case 'country':
						for (let key in this.countryFilters) {
              if (!this.selected.country.includes(this.countryFilters[key].label)) {
                this.selected.country.push(this.countryFilters[key].label);
              }
							this.selected.country = this.selected.country.filter(
								element => element !== idx.label,
							);
						}
						break;
					case 'watched':
						for (let key in this.watchedFilters) {
              if (!this.selected.watched.includes(this.watchedFilters[key].label)) {
                this.selected.watched.push(this.watchedFilters[key].label);
              }
							this.selected.watched = this.selected.watched.filter(
								element => element !== idx.label,
							);
						}
						break;
				}
			} else if (idx.label === '전체' && idx.isSelect === false) {
				switch (idx.filterName) {
					case 'category':
						this.selected.category = this.selected.category.filter(
							element => element === idx.label,
						);
						break;
					case 'filmRate':
						this.selected.filmRate = this.selected.filmRate.filter(
							element => element === idx.label,
						);
						break;
					case 'genre':
						this.selected.genre = this.selected.genre.filter(
							element => element === idx.label,
						);
						break;
					case 'offer':
						this.selected.offer = this.selected.offer.filter(
							element => element === idx.label,
						);
						break;
					case 'country':
						this.selected.country = this.selected.country.filter(
							element => element === idx.label,
						);
						break;
					case 'watched':
						this.selected.watched = this.selected.watched.filter(
							element => element === idx.label,
						);
						break;
				}
			} else if (idx.label !== '전체' && idx.isSelect === true) {
				switch (idx.filterName) {
					case 'category':
            if (!this.selected.category.includes(idx.label)) {
              this.selected.category.push(idx.label);
            }
						break;
					case 'filmRate':
            if (!this.selected.filmRate.includes(idx.label)) {
              this.selected.filmRate.push(idx.label);
            }
						break;
					case 'genre':
            if (!this.selected.genre.includes(idx.label)) {
              this.selected.genre.push(idx.label);
            }
						break;
					case 'offer':
            if (!this.selected.offer.includes(idx.label)) {
              this.selected.offer.push(idx.label);
            }
						break;
					case 'country':
            if (!this.selected.country.includes(idx.label)) {
              this.selected.country.push(idx.label);
            }
						break;
					case 'watched':
            if (!this.selected.watched.includes(idx.label)) {
              this.selected.watched.push(idx.label);
            }
						break;
				}
			} else if (idx.label !== '전체' && idx.isSelect === false) {
				switch (idx.filterName) {
					case 'category':
            if (this.categoryFilters.all.isSelect === false) {
              this.selected.category.splice(idx.label, 1);
            }
            break;
					case 'filmRate':
            if (this.filmRateFilters.all.isSelect === false) {
              this.selected.filmRate.splice(idx.label, 1)
            }
            break;
					case 'genre':
            if (this.genreFilters.all.isSelect === false) {
              this.selected.genre.splice(idx.label, 1);
            }
            break;
					case 'offer':
            if (this.offerFilters.all.isSelect === false) {
              this.selected.offer.splice(idx.label, 1);
            }
            break;
					case 'country':
            if (this.countryFilters.all.isSelect === false) {
              this.selected.country.splice(idx.label, 1);
            }
            break;
					case 'watched':
            if (this.watchedFilters.all.isSelect === false) {
              this.selected.watched.splice(idx.label, 1);
            }
            break;
				}
			}
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
