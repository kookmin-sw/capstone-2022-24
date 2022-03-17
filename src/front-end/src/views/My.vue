<template>
	<!-- 프로필 영역 -->
	<div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg profile-area">
		<div class="row">
			<q-avatar rounded color="blue" size="73px" class="q-mr-lg" />
			<div class="col text-left row-gap-12">
				<div class="q-mb-sm">사용자 닉네임</div>
				<div>010-1234-5678</div>
				<div class="row col-gap-12">
					<!-- 가입시 이용한 카카오/네이버 API 아이콘 -->
					<div class="api-icon" />
					<div>naver_email@naver.com</div>
				</div>
			</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 모임 관련 영역 -->
	<div class="row q-mt-xl q-mb-xl q-ml-lg q-mr-lg">
		<div class="col">
			<div class="guide-text text-left q-mb-lg">참여 중인 모임</div>
			<div class="row q-mb-md ott-icons-frame">
				<q-avatar rounded color="blue" size="40px"></q-avatar>
				<q-avatar rounded color="blue" size="40px"></q-avatar>
				<q-avatar rounded color="blue" size="40px"></q-avatar>
				<q-avatar rounded color="blue" size="40px"></q-avatar>
				<q-avatar rounded color="blue" size="40px"></q-avatar>
			</div>
			<div class="col text-left row-gap-12">
				<div>모집중 > 모집 완료 > 검토 기간 > 관람중</div>
				<div>모집 상태 설명</div>
				<div>추가 설명들</div>
				<div class="align-right">
					<q-btn dense unelevated>모임 탈퇴 하기 ></q-btn>
				</div>
			</div>
			<!-- 모임 구성원 관련 영역 -->
			<div class="col group-members">
				<div class="align-right">
					<q-badge
						color="blue"
						text-color="white"
						align="top"
						class="state-badge"
						>모임 상태 설명</q-badge
					>
				</div>
				<div class="row q-pt-lg q-pb-xl group-profile-frame">
					<q-space class="col-2" />
					<div class="col group-nicknames">
						<q-avatar rounded color="blue" size="73px" />
						<div>사용자닉네임</div>
					</div>
					<div class="col group-nicknames">
						<q-avatar rounded color="blue" size="73px" />
						<div>
							<q-icon name="military_tech" size="16px" />
							닉네임
						</div>
					</div>
					<div class="col group-nicknames">
						<q-avatar rounded color="blue" size="73px" />
						<div>닉네임</div>
					</div>
					<div class="col group-nicknames">
						<q-avatar rounded color="blue" size="73px" />
						<div>닉네임</div>
					</div>
					<q-space class="col-2" />
				</div>
			</div>
			<!-- 모임장: OTT 계정 ID/PW 입력 및 수정 가능 -->
			<div class="col q-mt-md q-mb-md">
				<q-input label="아이디" color="blue" class="ott-id" v-model="ottId">
					<q-btn dense unelevated>
						<q-icon name="edit" color="blue" />
					</q-btn>
				</q-input>
				<q-input label="비밀번호" color="blue" class="ott-pw" v-model="ottPw">
					<q-btn dense unelevated>
						<q-icon name="edit" color="blue" />
					</q-btn>
				</q-input>
			</div>
			<!-- 모임원: 모임장이 공유해 준 OTT 계정 ID/PW read only(드래그 & 복사 가능) -->
			<div class="col q-mt-md q-mb-md">
				<q-input
					readonly
					label="아이디"
					color="blue"
					class="ott-id"
					v-model="ottId">
				</q-input>
				<q-input
					readonly
					label="비밀번호"
					color="blue"
					class="ott-pw"
					v-model="ottPw">
				</q-input>
			</div>
			<div class="row col-gap-12">
				<q-space class="col-8" />
				<q-btn dense outline color="blue">
					<q-icon name="report" />
					신고
				</q-btn>
				<q-btn dense outline color="blue">OTT 바로가기</q-btn>
			</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 최근 조회 작품 영역 -->
	<div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg">
		<div class="row">
			<div class="q-mr-md">최근 조회한 작품</div>
			<q-btn>전체보기</q-btn>
		</div>
    <div class="q-mt-lg">
      <q-carousel
          v-model="recent"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          control-color="primary"
          padding
          arrows
          height="230px"
          class="bg-blue-1"
      >
        <q-carousel-slide :name="1" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 본 작품 영역 -->
	<div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg">
		<div class="row">
			<div class="q-mr-md">본 작품</div>
			<q-btn>전체보기</q-btn>
		</div>
    <div class="q-mt-lg">
      <q-carousel
          v-model="watched"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          control-color="primary"
          padding
          arrows
          height="230px"
          class="bg-blue-1"
      >
        <q-carousel-slide :name="1" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 찜한 작품 영역 -->
	<div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg">
		<div class="row">
			<div class="q-mr-md">찜한 작품</div>
			<q-btn>전체보기</q-btn>
		</div>
    <div class="q-mt-lg">
      <q-carousel
          v-model="scrap"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          control-color="primary"
          padding
          arrows
          height="230px"
          class="bg-blue-1"
      >
        <q-carousel-slide :name="1" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 별점 준 작품 -->
	<div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg">
		<div class="row">
			<div class="q-mr-md">별점 준 작품</div>
			<q-btn>전체보기</q-btn>
		</div>
    <div class="q-mt-lg">
      <q-carousel
          v-model="rated"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          control-color="primary"
          padding
          arrows
          height="230px"
          class="bg-blue-1"
      >
        <q-carousel-slide :name="1" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap">
          <div class="row fit justify-center items-center col-gap-16 no-wrap">
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
            <div class="col-2 full-height video-poster" />
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
	</div>
</template>

<script>
export default {
	name: 'My',
	data() {
		return {
			ottId: 'netfilxID@gmail.com',
			ottPw: 'netflix*Password',
      recent: 1,
      watched: 1,
      scrap: 1,
      rated: 1,
		};
	},
};
</script>

<style scoped>
.api-icon {
	width: 20px;
	height: 20px;
	background-color: #828282;
}
.ott-icons-frame {
	column-gap: 16px;
}
.align-right {
	display: flex;
	flex-direction: row-reverse;
}
.state-badge {
	width: auto;
	height: 30px;
}
.group-members {
	background-color: #e3f0ff;
}
.group-profile-frame {
	column-gap: 24px;
}
.group-nicknames {
	text-align: center;
}
.video-poster {
	width: 15%;
	height: auto;
	background: #83BBFB;
}
</style>
