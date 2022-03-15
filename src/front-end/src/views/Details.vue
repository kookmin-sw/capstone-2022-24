<template>
	<!-- 작품 정보 영역 -->
	<div class="col q-ml-md q-mr-md q-mt-xl q-mb-xl">
		<div class="col text-left q-mb-lg">
      <q-btn flat dense>&lt; 뒤로가기</q-btn>
    </div>
		<div class="row video-info-frame">
			<div class="col-3 video-image">포스터</div>
			<div class="col">
				<div class="col text-left q-mb-md">
					<div>작품명</div>
					<div>작품 영어 제목?</div>
				</div>
				<div class="row q-mb-xs video-info">
					<div>연도</div>
					<div>국가</div>
					<div>장르</div>
					<div>상영시간</div>
				</div>
				<div class="row q-mb-sm video-info">
          <!-- 로튼토마토 로고 이미지 -->
					<div class="logo-image" />
					<div>로튼토마토 평점</div>
          <!-- IMDB 로고 이미지 -->
					<div class="logo-image" />
					<div>IMDB 평점</div>
					<div>자체 평점</div>
					<div>자체 찜 수</div>
					<div>자체 본 사람 수</div>
				</div>
				<div class="row q-mb-md video-info">
					<q-select dense outlined
                    v-model="comboBox"
                    :options="seasons"
                    style="width: 24%" />
					<q-btn dense style="width: 23%">찜 하기</q-btn>
					<q-btn dense style="width: 23%">안 본 영화</q-btn>
					<q-btn dense style="width: 23%">별점 주기</q-btn>
				</div>
				<!-- 작품 제공 ott 및 ott별 구매 형태? -->
				<q-card flat bordered>
					<q-tabs
						v-model="tab"
						dense
						class="text-grey"
						active-color="blue"
						indicator-color="blue"
						align="justify">
						<q-tab name="all" label="전체" />
						<q-tab name="fixed-charge" label="정액제" />
						<q-tab name="purchase" label="구매" />
						<q-tab name="rental" label="대여" />
						<q-tab name="free" label="무료" />
					</q-tabs>
					<q-tab-panels v-model="tab" animated>
						<q-tab-panel name="all">
              <div class="ott-icons-frame row">
                <div v-for="icon in ott" :key="icon">
                  {{ icon }}
                  <q-avatar rounded color="blue" size="40px" />
                  <div>금액</div>
                </div>
              </div>
						</q-tab-panel>
						<q-tab-panel name="fixed-charge">
              <div class="ott-icons-frame row">
                <div v-for="icon in ott" :key="icon">
                  {{ icon }}
                  <q-avatar rounded color="blue" size="40px" />
                  <div>금액</div>
                </div>
              </div>
						</q-tab-panel>
						<q-tab-panel name="purchase">
              <div class="ott-icons-frame row">
                <div v-for="icon in ott" :key="icon">
                  {{ icon }}
                  <q-avatar rounded color="blue" size="40px" />
                  <div>금액</div>
                </div>
              </div>
						</q-tab-panel>
            <q-tab-panel name="rental">
              <div class="ott-icons-frame row">
                <div v-for="icon in ott" :key="icon">
                  {{ icon }}
                  <q-avatar rounded color="blue" size="40px" />
                  <div>금액</div>
                </div>
              </div>
            </q-tab-panel>
            <q-tab-panel name="free">
              <div class="ott-icons-frame row">
                <div v-for="icon in ott" :key="icon">
                  {{ icon }}
                  <q-avatar rounded color="blue" size="40px" />
                  <div>금액</div>
                </div>
              </div>
            </q-tab-panel>
					</q-tab-panels>
				</q-card>
			</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 작품 줄거리 영역 -->
	<div class="col text-left q-ml-md q-mr-md q-mt-xl q-mb-xl">
		<div class="q-mb-md">줄거리</div>
    <div class="col">
		  <div>줄거리 내용 텍스트</div>
    </div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 감독/제작/출연 정보 영역 -->
	<div class="col text-left q-ml-md q-mr-md q-mt-xl q-mb-xl">
		<div class="q-mb-md">감독/제작/출연</div>
    <div class="row staff-frame">
      <div v-for="staffMember in staff" :key="staffMember">
        {{ staffMember }}
        <q-avatar rounded color="blue" size="73px">
          <div class="col text-center">
            <div style="font-size: 14px;">역할</div>
            <div style="font-size: 20px;">김땡땡</div>
          </div>
        </q-avatar>
      </div>
      <q-btn flat >모두 보기</q-btn>
    </div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 관련 영상물 영역 -->
	<div class="col text-left q-ml-md q-mr-md q-mt-xl q-mb-xl">
		<div class="q-mb-md">관련 영상물</div>
		<div>영상 썸네일 영역?</div>
	</div>
</template>

<script>


export default {
	data() {
		return {
      comboBox: null,
      seasons: [ '시즌 1', '시즌 2', '시즌 3', ],
			tab: 'all',
      staff : [ '', '', '', '', '', ],
      ott : [ '', '', '', '', '', '', '', '', '', ],
		};
	},
};
</script>

<style scoped>
.video-info-frame {
  column-gap: 12px;
}
.video-image {
  max-width: 200px;
  max-height: 300px;
	background-color: #828282;
}
.video-info {
	column-gap: 12px;
}
.logo-image {
	width: 30px;
	height: 30px;
	background-color: #828282;
}
.ott-icons-frame {
	column-gap: 24px;
  row-gap: 24px;
}
.staff-frame {
  column-gap: 24px;
}
</style>
