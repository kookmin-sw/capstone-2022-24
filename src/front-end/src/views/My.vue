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
	<!-- 모임 영역 -->
	<q-separator color="blue" inset />
	<div class="column q-ma-xl">
		<!-- 참여 중인 모임 목록 (로고) -->
		<div class="q-mb-md text-left text-h6 text-weight-bold">참여 중인 모임</div>
		<div class="row q-mb-md">
			<q-avatar
				rounded
				color="grey"
				size="40px"
				class="q-mr-sm"
				v-for="group in this.userGroupList"
				:key="group.id"
				@click="setSelectedGroup(group.id)">
				<div>{{ group.logoUrl }}</div>
			</q-avatar>
			<q-btn outline color="blue">+</q-btn>
		</div>
		<!-- 모임 상태 -->
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
				<div
					class="col"
					v-for="fellow in selectGroup.fellows"
					:key="fellow.nickname">
					<q-avatar rounded color="grey" size="73px" />
					<div>{{ fellow.nickname }}</div>
				</div>
				<q-space class="col-2" />
			</div>
		</div>
		<!-- ott 계정 정보 -->
		<div class="q-mb-lg" v-if="selectGroup.account">
			<q-input readonly label="아이디" v-model="selectGroup.account.id" />
			<q-input
				readonly
				label="비밀번호"
				v-model="selectGroup.account.password" />
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
	<!-- 최근 조회 작품 영역 -->
	<q-separator color="blue" inset />
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">최근 조회한 작품</div>
			<q-btn flat class="text-grey">전체보기</q-btn>
		</div>
		<div>
			<q-carousel
				v-model="recents"
				transition-prev="slide-right"
				transition-next="slide-left"
				swipeable
				animated
				control-color="primary"
				padding
				arrows
				height="230px"
				class="bg-blue-1">
				<q-carousel-slide :name="1">
					<div class="row fit justify-center items-center video-list-frame">
						<!--						            <div class="video-poster" v-for="video in this.recentViews" :key="video.id">{{video}}</div>-->
						<!--						            <div class="video-poster" v-for="video in this.userVideos.recentViews.results" :key="video.id">{{video}}</div>-->
					</div>
				</q-carousel-slide>
			</q-carousel>
		</div>
	</div>
	<!-- 본 작품 영역 -->
	<q-separator color="blue" inset />
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">본 작품</div>
			<q-btn flat class="text-grey">전체보기</q-btn>
		</div>
		<div>
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
				<q-carousel-slide :name="1">
					<div class="row fit justify-center items-center video-list-frame">
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
					</div>
				</q-carousel-slide>
			</q-carousel>
		</div>
	</div>
	<!-- 찜한 작품 영역 -->
	<q-separator color="blue" inset />
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">찜한 작품</div>
			<q-btn flat class="text-grey">전체보기</q-btn>
		</div>
		<div>
			<q-carousel
				v-model="dibs"
				transition-prev="slide-right"
				transition-next="slide-left"
				swipeable
				animated
				control-color="primary"
				padding
				arrows
				height="230px"
				class="bg-blue-1">
				<q-carousel-slide :name="1">
					<div class="row fit justify-center items-center video-list-frame">
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
					</div>
				</q-carousel-slide>
			</q-carousel>
		</div>
	</div>
	<!-- 별점 준 작품 -->
	<q-separator color="blue" inset />
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">별점 준 작품</div>
			<q-btn flat class="text-grey">전체보기</q-btn>
		</div>
		<div>
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
				<q-carousel-slide :name="1">
					<div class="row fit justify-center items-center video-list-frame">
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
						<div class="video-poster" />
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
			watched: 1,
			recents: 1,
			dibs: 1,
			rated: 1,
			selectGroup: {},
		};
	},
	computed: {
		...mapState('user', [
			'userProfile',
			'userGroups',
			'userGroupList',
			'userVideos',
		]),
	},
	async beforeCreate() {
		await this.$store.dispatch('user/getGroupList');
		await this.$store.dispatch('user/getUserVideos');
	},
	methods: {
		findGroup(ottId) {
			const selected = this.userGroups.find(ott => {
				return ott.provider.id === ottId;
			});
			return selected;
		},
		setSelectedGroup(ottId) {
			// TODO: bug fix - default 모임 외 나머지 첫 클릭 시 에러, 2번째 클릭 부터 제대로 동작
			let selected = this.findGroup(ottId);
			if (!selected) {
				this.$store.dispatch('user/getGroupInfo', ottId);
				selected = this.findGroup(ottId);
			}
			this.selectGroup = selected;
		},
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

.video-list-frame {
	display: flex;
	flex-wrap: wrap;
	/*justify-content: space-between;*/
}

.video-poster {
	width: 14%;
	height: 0;
	padding-bottom: 20%;
	margin: 0 12px 0 0;
	background: lightgrey;
}
</style>
