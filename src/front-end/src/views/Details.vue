<template>
	<!-- 작품 정보 영역 -->
	<div class="q-ma-xl details">
		<q-btn flat class="row q-mb-sm justify-start">&lt; 뒤로가기</q-btn>
		<div class="row col-gap-12">
			<!-- 포스터 -->
			<div
				class="col-3 q-ma-sm bg-grey-4"
				style="width: 242px; height: 342px" />
			<div class="col text-left">
				<!-- 작품 제목 -->
				<div class="q-ma-sm">
					<div class="text-h6 text-weight-bold">작품명</div>
					<div class="q-mb-md text-bold text-grey">작품 영어 제목</div>
				</div>
				<!-- 작품 상세 정보 -->
				<div class="row q-ma-sm">
					<div class="q-mr-sm q-mt-auto q-mb-auto">연도</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">국가</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">장르</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">상영시간</div>
				</div>
				<!-- 작품 상세 정보: 외부 평점 -->
				<div class="row q-ma-sm q-mb-md">
					<!-- IMDB -->
					<q-avatar rounded color="grey-4" size="25px" class="q-mr-xs" />
					<div class="q-mr-md q-mt-auto q-mb-auto">IMDB 평점</div>
					<!-- 자체 기준 -->
					<div class="q-mr-sm q-mt-auto q-mb-auto">자체 평점</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">자체 찜 수</div>
					<div class="q-mt-auto q-mb-auto">자체 본 사람 수</div>
				</div>
				<div class="row q-mb-md">
					<q-select
						dense
						outlined
						color="blue-4"
						class="col q-ma-sm"
						v-model="seasonComboBox"
						:options="seasons" />
					<q-btn outline class="col q-ma-sm text-blue-100">찜 하기</q-btn>
					<q-btn outline class="col q-ma-sm text-blue-100">안 본 영화</q-btn>
					<q-btn outline class="col q-ma-sm text-blue-100">별점 주기</q-btn>
				</div>
				<!-- 작품을 서비스하는 ott 목록-->
				<q-card flat bordered class="q-ma-sm">
					<q-tabs
						dense
						class="text-grey"
						active-color="blue-4"
						indicator-color="blue-4"
						align="justify"
						v-model="tab">
						<q-tab name="all" label="전체" />
					</q-tabs>
					<q-tab-panels v-model="tab">
						<q-tab-panel name="all">
							<div class="ott-icons-frame row">
								<div v-for="ott in serviceOtts" :key="ott.id">
									<q-avatar rounded color="grey-4" size="40px" />
									<div class="text-center">금액</div>
								</div>
							</div>
						</q-tab-panel>
					</q-tab-panels>
				</q-card>
			</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />
	<!-- 작품 줄거리 영역 -->
	<div class="q-ma-xl text-left">
		<div class="q-mb-md text-h6 text-weight-bold">줄거리</div>
		<div>줄거리 내용 텍스트</div>
	</div>
	<!-- hr -->
	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />
	<!-- 제작진 정보 영역 -->
	<div class="col q-ma-xl text-left">
		<div class="q-mb-md text-h6 text-weight-bold">제작진</div>
		<div class="row col-gap-12">
			<div v-for="staffMember in staff" :key="staffMember.id">
				{{ staffMember }}
				<q-avatar rounded class="bg-blue-100" size="73px">
					<div class="text-center">
						<div class="text-body2 text-grey-100">역할</div>
						<div class="text-h6 text-grey-100">김땡땡</div>
					</div>
				</q-avatar>
			</div>
			<q-btn flat>모두 보기</q-btn>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />
	<!-- 관련 영상물 영역 -->
	<div class="q-ma-xl text-left">
		<div class="q-mb-md text-h6 text-weight-bold">관련 영상</div>
		<div>영상 임베드 영역, 링크 -> 임베드</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			seasonComboBox: '시즌 1',
			seasons: ['시즌 1', '시즌 2', '시즌 3'],
			tab: 'all',
			staff: ['', '', '', '', ''],
			serviceOtts: ['', '', '', '', '', '', '', '', ''],
		};
	},
};
</script>

<style scoped>
.ott-icons-frame {
	column-gap: 16px;
	row-gap: 24px;
}
</style>
