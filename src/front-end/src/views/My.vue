<!DOCTYPE html>
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
      <div class="q-ml-lg" @click="payment">충전하기</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">계좌</div>
			<div>(은행) 356-xxxx-xxxx-xx</div>
			<div class="q-ml-lg text-grey">등록/수정</div>
		</div>
    <div class="row">
      <q-btn color="blue" outline @click="chargeCredit">충전하기</q-btn>
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
			<q-btn flat dense>모임 탈퇴 하기 &gt;</q-btn>
		</div>
		<!-- 모임 상세 정보 -->
		<div class="q-mb-lg bg-blue-1">
			<!-- 모임 상태 뱃지 -->
			<div class="align-right">
				<q-badge color="blue" text-color="white" align="top" class="q-pa-sm">
					모임 상태 &amp; D-day
				</q-badge>
			</div>
			<!-- 모임 모집 완료 이전 -->
			<div
				class="row q-pa-md q-pb-xl"
				v-if="!getSelectGroup.fellows"
				style="height: 343px">
				<q-space class="col-2" />
				<div class="q-mt-auto q-mb-auto text-h6 text-weight-bold">
					모임 구성원을 기다리는 중입니다.
				</div>
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
		<div v-if="getSelectGroup.account">
			<div class="q-mb-md">
				<q-input readonly label="아이디" v-model="getSelectGroup.account.id" />
				<q-input
					readonly
					label="비밀번호"
					v-model="getSelectGroup.account.password" />
			</div>
			<div class="row">
				<q-space class="col-8" />
				<q-btn outline color="blue" class="q-mr-sm">
					신고<q-icon name="no_accounts" />
				</q-btn>
				<q-btn outline color="blue">
					<a :href="getSelectGroup.provider.link" target="_blank">
						{{ getSelectGroup.provider.name }} 바로가기
					</a>
					<q-icon name="arrow_right_alt" />
				</q-btn>
			</div>
		</div>
	</div>

	<!--  최근 조회 작품  -->
	<q-separator color="blue" inset />
	<user-videos
		:title="recentList.title"
		:video-list="getRecentList"
		:push-video-method="recentList.method"
		:expand-id="recentList.expandId" />

	<!--  찜한 작품  -->
	<q-separator color="blue" inset />
	<user-videos
		:title="dibList.title"
		:video-list="getDibList"
		:push-video-method="dibList.method"
		:expand-id="dibList.expandId" />

	<!-- 별점 준 작품 -->
	<user-videos
		:title="starList.title"
		:video-list="getStarList"
		:push-video-method="starList.method"
		:expand-id="starList.expandId" />

	<!-- 본 작품 -->
	<user-videos
		:title="watchList.title"
		:video-list="getWatchList"
		:push-video-method="watchList.method"
		:expand-id="watchList.expandId" />
</template>

<script>
import { mapGetters, mapState } from 'vuex';
import UserVideos from '@/components/userVideos';
import { loadTossPayments } from "@tosspayments/payment-sdk";
const clientKey = 'test_ck_ADpexMgkW36nWZAzQJE3GbR5ozO0';

export default {
	name: 'My',
	components: { UserVideos },
	data() {
		return {
			selectGroup: {},
			recentList: {
				title: '최근 조회 작품',
				method: 'user/pushRecentList',
				expandId: 'recent',
			},
			dibList: {
				title: '찜한 작품',
				method: 'user/pushDibList',
				expandId: 'dib',
			},
			starList: {
				title: '별점 준 작품',
				method: 'user/pushStarList',
				expandId: 'star',
			},
			watchList: {
				title: '본 작품',
				method: 'user/pushWatchList',
				expandId: 'watched',
			},
		};
	},
	computed: {
		...mapState('user', ['userProfile']),
		...mapGetters('user', [
			'getGroupList',
			'getSelectGroup',
			'getRecentList',
			'getDibList',
			'getStarList',
			'getWatchList',
		]),
	},
	async beforeCreate() {
		await this.$store.dispatch('user/initUserGroups');
		await this.$store.dispatch('user/initUserVideos', 6);
	},
	methods: {
		async clickGroupLogo(groupId) {
			await this.$store.dispatch('user/setSelectGroup', groupId);
		},
    async chargeCredit() {
      const tossPayments = await loadTossPayments(clientKey);
      tossPayments.requestBillingAuth('카드', {
        customerKey: 'zLNZjDKC1uqnMCk_ffMJL',
        successUrl: window.location.origin + '/success',
        failUrl: window.location.origin + '/fail',
      })
      .catch(function (error) {
        if (error.code === 'USER_CANCEL')
          alert("충전 결제가 취소되었습니다!")
      });
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

a {
	color: #0074d9;
}
</style>
