<template>
	<div class="home">
		<!-- 검색창~필터링 단락 -->
		<div class="search-filter-frame row q-mt-xl q-mb-xl">
			<q-space class="col-2" />
			<div class="col-8">
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
				<div class="ott-icons-frame row q-mb-lg">
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
					<q-avatar rounded color="blue" size="60px"></q-avatar>
				</div>
				<!-- 필터링 조건 -->
				<q-expansion-item label="필터링 조건들">
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">작품 종류</div>
						<q-separator color="blue" vertical inset />
						<q-chip>전체</q-chip>
						<q-chip>영화</q-chip>
						<q-chip>TV 시리즈</q-chip>
					</div>
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">상영 등급</div>
						<q-separator color="blue" vertical inset />
						<q-chip>전체</q-chip>
						<q-chip>전체관람가</q-chip>
						<q-chip>12세 이상 관람가</q-chip>
						<q-chip>15세 이상 관람가</q-chip>
						<q-chip>청소년 관람불가</q-chip>
					</div>
					<!-- 장르 조건이 가장 많아서 정렬 밖으로 벗어나는데 해결 방법을 모르겠습니다. 확인 후 조언 부탁드려요 -->
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">장르</div>
						<q-separator color="blue" vertical inset />
						<div class="row-2">
							<q-chip>전체</q-chip>
							<q-chip>SF/판타지</q-chip>
							<q-chip>공포</q-chip>
							<q-chip>드라마</q-chip>
							<q-chip>로맨스</q-chip>
							<q-chip>스릴러</q-chip>
							<q-chip>시대극</q-chip>
							<q-chip>무협</q-chip>
							<q-chip>범죄/추리</q-chip>
							<q-chip>애니메이션</q-chip>
							<q-chip>액션</q-chip>
							<q-chip>코미디</q-chip>
						</div>
					</div>
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">결제 종류</div>
						<q-separator color="blue" vertical inset />
						<q-chip>전체</q-chip>
						<q-chip>구매</q-chip>
						<q-chip>대여</q-chip>
						<q-chip>정액제</q-chip>
					</div>
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">국가</div>
						<q-separator color="blue" vertical inset />
						<q-chip>전체</q-chip>
						<q-chip>국내</q-chip>
						<q-chip>해외</q-chip>
					</div>
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">관람 여부</div>
						<q-separator color="blue" vertical inset />
						<q-chip>전체</q-chip>
						<q-chip>본 작품</q-chip>
						<q-chip>안 본 작품</q-chip>
					</div>
					<!-- 슬라이더 형태 필터링 -->
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">연도</div>
						<q-separator color="blue" vertical inset />
						<div class="q-pa-md q-pb-lg">
							<q-range
								class="range-slider"
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
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">평점</div>
						<q-separator color="blue" vertical inset />
						<div class="q-pa-md q-pb-lg">
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
					<div class="filter-frame row">
						<div class="filter-text q-ma-md">상영 시간</div>
						<q-separator color="blue" vertical inset />
						<div class="q-pa-md q-pb-lg">
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
	setup() {
		return {
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

.filter-text {
}

.filter-frame {
}

.range-slider {
	width: 500px;
	/* 칸에 맞춘 너비 설정방법 모르겠어서 임시로 값 지정해뒀습니다 */
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
