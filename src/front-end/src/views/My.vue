<template>
	<!-- 프로필 영역 -->
	<div class="column q-ma-xl">
		<div class="q-mb-md text-left text-h6 text-weight-bold">
			{{ userProfile.nickname }}
		</div>
		<!--    TODO: profile img 태그 추가-->
		<q-avatar rounded color="grey" size="73px" class="q-mb-md" />
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">전화번호</div>
			<div>{{ userProfile.phone }}</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">이메일</div>
			<div>{{ userProfile.email }}</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">정직 비용</div>
			<div>1,000 원</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">계좌</div>
			<div>(은행) 356-xxxx-xxxx-xx</div>
			<div class="q-ml-lg text-grey">등록/수정</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue" inset />
	<!-- 모임 영역 -->
	<div class="column q-ma-xl">
		<div class="q-mb-md text-left text-h6 text-weight-bold">참여 중인 모임</div>
		<div class="row q-mb-md">
			<q-avatar rounded color="grey" size="40px" class="q-mr-sm"></q-avatar>
		</div>
		<div class="text-left">
			<div>모집중 > 모집 완료 > 검토 기간 > 관람중</div>
			<div>모임 상태 설명</div>
			<div class="align-right">
				<q-btn flat dense>모임 탈퇴 하기 ></q-btn>
			</div>
		</div>
		<!-- 구성원 영역 -->
		<div class="q-mb-lg bg-blue-1">
			<!-- 모임 상태 -->
			<div class="align-right">
				<q-badge color="blue" text-color="white" align="top" class="q-pa-sm">
					D-day
				</q-badge>
			</div>
			<!-- 구성원 목록 -->
			<div class="row q-pa-md q-pb-xl">
				<q-space class="col-2" />
				<div class="col">
					<q-avatar rounded color="grey" size="73px" />
					<div>닉네임</div>
				</div>
				<div class="col">
					<q-avatar rounded color="grey" size="73px" />
					<div>닉네임</div>
				</div>
				<div class="col">
					<q-avatar rounded color="grey" size="73px" />
					<div>닉네임</div>
				</div>
				<div class="col">
					<q-avatar rounded color="grey" size="73px" />
					<div>닉네임</div>
				</div>
				<q-space class="col-2" />
			</div>
		</div>
		<!-- 모임장: OTT 계정 입력 가능 -->
		<!--		<div class="col q-mt-md q-mb-md">-->
		<!--			<q-input label="아이디" color="blue" class="ott-id" v-model="ottId">-->
		<!--				<q-btn dense unelevated>-->
		<!--					<q-icon name="edit" color="blue" />-->
		<!--				</q-btn>-->
		<!--			</q-input>-->
		<!--			<q-input label="비밀번호" color="blue" class="ott-pw" v-model="ottPw">-->
		<!--				<q-btn dense unelevated>-->
		<!--					<q-icon name="edit" color="blue" />-->
		<!--				</q-btn>-->
		<!--			</q-input>-->
		<!--		</div>-->
		<!-- 모임원: OTT 계정 read only -->
		<div class="q-mb-lg">
			<q-input readonly label="아이디" v-model="ottId"> </q-input>
			<q-input readonly label="비밀번호" v-model="ottPw"> </q-input>
		</div>
		<div class="row">
			<q-space class="col-8" />
			<q-btn outline color="blue" class="q-mr-sm">
				<q-icon name="report" />
				신고
			</q-btn>
			<q-btn outline color="blue">OTT 바로가기</q-btn>
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
				class="bg-blue-1">
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
				class="bg-blue-1">
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
				class="bg-blue-1">
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
				class="bg-blue-1">
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
import { mapState } from 'vuex';
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
	computed: {
		...mapState('user', ['userProfile']),
	},
};
</script>

<style scoped>
.info-item {
	width: 100px;
}

.align-right {
	display: flex;
	flex-direction: row-reverse;
}

.video-poster {
	width: 15%;
	height: auto;
	background: #83bbfb;
}
</style>
