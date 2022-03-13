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
						<!-- 슬롯을 왜 씀?(찾아보기) -->
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
				<q-expansion-item label="필터링 조건들">
					<!-- 작품 종류 -->
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">작품 종류</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="category in filters.categories" :key="category.id">
								{{ category }}
							</q-chip>
						</div>
					</div>
					<!-- 상영 등급 -->
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">상영 등급</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="rate in filters.ratings" :key="rate.id">
								{{ rate }}
							</q-chip>
						</div>
					</div>
					<!-- 장르 -->
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">장르</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="genre in filters.genres" :key="genre.id">
								{{ genre }}
							</q-chip>
						</div>
					</div>
					<!-- 결제 종류 -->
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">결제 종류</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="offer in filters.offers" :key="offer.id">
								{{ offer }}
							</q-chip>
						</div>
					</div>
					<!-- 국가 -->
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">국가</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="country in filters.countries" :key="country.id">
								{{ country }}
							</q-chip>
						</div>
						<!-- 관람 여부 -->
					</div>
					<div class="filter-frame row q-mt-md">
						<div class="q-mt-auto q-mb-auto col-2">관람 여부</div>
						<q-separator color="blue" vertical inset />
						<div class="chips-frame q-ml-sm text-left col-9">
							<q-chip v-for="work in filters.watched" :key="work.id">
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
								v-model="year"
								:min="1970"
								:max="2022"
								:step="1"
								:left-label-value="year.min + '년'"
								:right-label-value="year.max + '년'"
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
								v-model="rate"
								:min="0"
								:max="5.0"
								:step="0.5"
								:left-label-value="rate.min + '점'"
								:right-label-value="rate.max + '점'"
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
								v-model="runtime"
								:min="0"
								:max="240"
								:step="10"
								:left-label-value="runtime.min + '분'"
								:right-label-value="runtime.max + '분'"
								label-always
								switch-label-side
								color="blue" />
						</div>
					</div>
					<q-btn>초기화</q-btn>
				</q-expansion-item>
			</div>
			<q-space class="col-2" />
		</div>
		<!-- hr -->
		<q-separator color="blue" inset />
		<!-- 작품 포스터 단락 -->
		<div>
			<div class="video-frame q-mt-xl q-mb-xl">
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
				<div class="video">poster</div>
			</div>
			<q-btn>더보기</q-btn>
		</div>
	</div>
</template>

<script>
import { ref } from 'vue';

export default {
	name: 'Home',
	data() {
		return {
			filters: {
				categories: ['전체', '영화', 'TV 시리즈'],
				ratings: [
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
			},
			search: ref(''),
			year: ref({
				min: 1990,
				max: 2010,
			}),
			rate: ref({
				min: 0.5,
				max: 4.5,
			}),
			runtime: ref({
				min: 5,
				max: 180,
			}),
		};
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

.video-frame {
	display: grid;
	grid-template-columns: repeat(6, 170px);
	grid-template-rows: repeat(6, 238px);
	column-gap: 24px;
	row-gap: 40px;
}

.video {
	width: 170px;
	height: 238px;
	background-color: #828282;
}
</style>
