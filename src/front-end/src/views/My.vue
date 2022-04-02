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
				v-for="group in getGroupList"
				:key="group.id"
				@click="clickGroupLogo(group.id)">
				<div>{{ group.logoUrl }}</div>
			</q-avatar>
			<q-btn outline color="blue">+</q-btn>
		</div>
		<!-- 모임 탈퇴 -->
		<div class="text-left align-right">
			<q-btn flat dense>모임 탈퇴 하기 ></q-btn>
		</div>
		<!-- 모임 상세 정보 -->
		<div class="q-mb-lg bg-blue-1">
			<!-- 모임 상태 뱃지 -->
			<div class="align-right">
				<q-badge color="blue" text-color="white" align="top" class="q-pa-sm">
					모임 상태 & D-day
				</q-badge>
			</div>
			<!-- 모임 모집 완료 이전 -->
			<!--  TODO: 정상 동작 하는데 null error 어떻게... 잡아야 할까...-->
			<div class="row q-pa-md q-pb-xl" v-if="!getSelectGroup.fellows">
				<q-space class="col-2" />
				<div>모임원 모집 중입니다.</div>
				<q-space class="col-2" />
			</div>
			<!-- 모임 모집 완료 이후 -->
			<div v-else>
				<!-- 구성원 -->
				<div class="row q-pa-md q-pb-xl">
					<q-space class="col-2" />
					<div
						class="col"
						v-for="fellow in getSelectGroup.fellows"
						:key="fellow.nickname">
						<q-avatar rounded color="grey" size="73px" />
						<div>{{ fellow.nickname }}</div>
					</div>
					<q-space class="col-2" />
				</div>
			</div>
		</div>
		<!-- ott 계정 정보 -->
		<div class="q-mb-lg" v-if="getSelectGroup.account">
			<q-input readonly label="아이디" v-model="getSelectGroup.account.id" />
			<q-input
				readonly
				label="비밀번호"
				v-model="getSelectGroup.account.password" />
		</div>
		<!--		<div class="row">-->
		<!--			<q-space class="col-8" />-->
		<!--			<q-btn outline color="blue" class="q-mr-sm">-->
		<!--				<q-icon name="report" />-->
		<!--				신고-->
		<!--			</q-btn>-->
		<!--			<q-btn outline color="blue">OTT 바로가기</q-btn>-->
	</div>
	<!--	 최근 조회 작품 영역-->
	<q-separator color="blue" inset />
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">최근 조회한 작품</div>
			<q-btn flat class="text-grey">전체보기</q-btn>
		</div>
		<div>
			<q-carousel
				v-model="recentPage"
				transition-prev="slide-right"
				transition-next="slide-left"
				swipeable
				animated
				padding
				arrows
				ref="carousel"
				control-color="primary"
				height="230px"
				class="bg-blue-1">
				<q-carousel-slide
					:name="page"
					v-for="page in getRecentViews.totalPage"
					:key="page">
					<div
						class="row fit justify-center items-center video-list-frame"
						v-if="getRecentViews.results[page - 1]">
						<div
							class="video-poster"
							v-for="video in getRecentViews.results[page - 1].videos"
							:key="video.id">
							{{ video.posterUrl }}
						</div>
					</div>
				</q-carousel-slide>
			</q-carousel>
		</div>
	</div>
	<!--	&lt;!&ndash; 본 작품 영역 &ndash;&gt;-->
	<!--	<q-separator color="blue" inset />-->
	<!--	<div class="q-ma-xl">-->
	<!--		<div class="row q-mb-md">-->
	<!--			<div class="text-h6 text-weight-bold">본 작품</div>-->
	<!--			<q-btn flat class="text-grey">전체보기</q-btn>-->
	<!--		</div>-->
	<!--		<div>-->
	<!--			<q-carousel-->
	<!--				v-model="watched"-->
	<!--				transition-prev="slide-right"-->
	<!--				transition-next="slide-left"-->
	<!--				swipeable-->
	<!--				animated-->
	<!--				control-color="primary"-->
	<!--				padding-->
	<!--				arrows-->
	<!--				height="230px"-->
	<!--				class="bg-blue-1">-->
	<!--				<q-carousel-slide :name="1">-->
	<!--					<div class="row fit justify-center items-center video-list-frame">-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--					</div>-->
	<!--				</q-carousel-slide>-->
	<!--			</q-carousel>-->
	<!--		</div>-->
	<!--	</div>-->
	<!--	&lt;!&ndash; 찜한 작품 영역 &ndash;&gt;-->
	<!--	<q-separator color="blue" inset />-->
	<!--	<div class="q-ma-xl">-->
	<!--		<div class="row q-mb-md">-->
	<!--			<div class="text-h6 text-weight-bold">찜한 작품</div>-->
	<!--			<q-btn flat class="text-grey">전체보기</q-btn>-->
	<!--		</div>-->
	<!--		<div>-->
	<!--			<q-carousel-->
	<!--				v-model="dibs"-->
	<!--				transition-prev="slide-right"-->
	<!--				transition-next="slide-left"-->
	<!--				swipeable-->
	<!--				animated-->
	<!--				control-color="primary"-->
	<!--				padding-->
	<!--				arrows-->
	<!--				height="230px"-->
	<!--				class="bg-blue-1">-->
	<!--				<q-carousel-slide :name="1">-->
	<!--					<div class="row fit justify-center items-center video-list-frame">-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--					</div>-->
	<!--				</q-carousel-slide>-->
	<!--			</q-carousel>-->
	<!--		</div>-->
	<!--	</div>-->
	<!--	&lt;!&ndash; 별점 준 작품 &ndash;&gt;-->
	<!--	<q-separator color="blue" inset />-->
	<!--	<div class="q-ma-xl">-->
	<!--		<div class="row q-mb-md">-->
	<!--			<div class="text-h6 text-weight-bold">별점 준 작품</div>-->
	<!--			<q-btn flat class="text-grey">전체보기</q-btn>-->
	<!--		</div>-->
	<!--		<div>-->
	<!--			<q-carousel-->
	<!--				v-model="rated"-->
	<!--				transition-prev="slide-right"-->
	<!--				transition-next="slide-left"-->
	<!--				swipeable-->
	<!--				animated-->
	<!--				control-color="primary"-->
	<!--				padding-->
	<!--				arrows-->
	<!--				height="230px"-->
	<!--				class="bg-blue-1">-->
	<!--				<q-carousel-slide :name="1">-->
	<!--					<div class="row fit justify-center items-center video-list-frame">-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--						<div class="video-poster" />-->
	<!--					</div>-->
	<!--				</q-carousel-slide>-->
	<!--			</q-carousel>-->
	<!--		</div>-->
	<!--	</div>-->
</template>

<script>
import { mapGetters, mapState } from 'vuex';
// import { ref } from 'vue'

export default {
	name: 'My',
	data() {
		return {
			selectGroup: {},
			recentPage: 1,
			recentViews: [],
			dibs: 1,
			rated: 1,
			watched: 1,
		};
	},
	watch: {
		recentPage: function (newVal) {
			if (newVal >= this.getRecentViews.results.length) {
				this.$store.dispatch('user/pushRecentViews', { page: newVal, size: 6 });
			}
		},
	},
	computed: {
		...mapState('user', ['userProfile']),
		...mapGetters('user', ['getGroupList', 'getSelectGroup', 'getRecentViews']),
	},
	async beforeCreate() {
		await this.$store.dispatch('user/initUserGroups');
		await this.$store.dispatch('user/initUserVideos', 6);
		console.log(this.getRecentViews.results);
	},
	methods: {
		async clickGroupLogo(groupId) {
			await this.$store.dispatch('user/setSelectGroup', groupId);
		},
		changeSlide() {
			console.log('change!');
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
