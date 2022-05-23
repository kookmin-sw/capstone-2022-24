<!DOCTYPE html>
<template>
	<!-- 프로필 영역 -->
	<div class="column q-ma-xl">
		<div class="q-mb-md text-left text-h6 text-weight-bold">
			{{ profile.nickname }}
		</div>
		<!--    TODO: profile img 태그 추가-->
		<q-avatar rounded size="73px" class="q-mb-md bg-blue-100">
			<img
				:src="profile.profileImageUrl"
				:alt="'profile'"
				v-if="profile.profileImageUrl" />
		</q-avatar>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">전화번호</div>
			<div>{{ profile.phone }}</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">이메일</div>
			<div>{{ profile.email }}</div>
		</div>
		<div class="row q-mb-sm text-left">
			<div class="text-weight-bold info-item">정직 비용</div>
			<div>{{ profile.mileages }} 원</div>
			<div
				class="q-ml-md q-pl-md q-pr-md border-blue-100 text-blue-200 radius-4"
				style="cursor: pointer"
				@click="chargeCredit">
				충전하기
			</div>
		</div>
	</div>
	<!-- 모임 영역 -->
	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />
	<div class="column q-ma-xl">
		<div class="q-mb-md text-left text-h6 text-weight-bold">참여 중인 모임</div>
		<!-- 참여, 모집 중인 모임 없음 -->
		<div
			class="row q-mt-lg q-pa-md q-pb-xl bg-blue-70"
			style="height: 343px"
			v-if="getSelectGroup === null">
			<q-space class="col-2" />
			<div class="q-mt-auto q-mb-auto text-h6 text-weight-bold">
				참여 중이거나 모집 중인 모임이 없습니다.
			</div>
			<q-space class="col-2" />
		</div>

		<!-- 참여, 모집 중인 모임 목록-->
		<div class="row" v-if="getSelectGroup !== null">
			<q-avatar
				rounded
				color="grey-4"
				size="40px"
				class="q-mr-sm"
				v-for="group in getGroupList"
				:key="group.provider.id"
				@click="clickGroupLogo(group.provider.id)">
				<img
					:src="group.provider.logoUrl"
					:alt="group.provider.id"
					:class="{
						selected: getSelectGroup.provider.id === group.provider.id,
					}" />
			</q-avatar>
			<q-btn
				outline
				class="text-blue-100 radius-4"
				v-if="getGroupList.length < 2"
				@click="this.$router.push({ name: 'Join' })">
				+
			</q-btn>
		</div>

		<!-- 모임 모집 중 -->
		<div
			class="row q-mt-lg q-pa-md q-pb-xl bg-blue-70"
			v-if="getSelectGroup !== null && getSelectGroup.status === 'Recruiting'"
			style="height: 343px">
			<q-space class="col-2" />
			<div class="q-mt-auto q-mb-auto text-h6 text-weight-bold">
				모임 구성원을 기다리는 중입니다.
			</div>
			<q-space class="col-2" />
		</div>

		<!-- 모집 완료 -->
		<!-- 모임 탈퇴 -->
		<div class="text-left align-right">
			<q-btn
				flat
				dense
				class="text-grey"
				v-if="getSelectGroup !== null && getSelectGroup.status === 'Recruited'">
				모임 탈퇴 하기 &gt;
			</q-btn>
		</div>
		<!-- 모임 상세 정보 -->
		<div
			v-if="getSelectGroup !== null && getSelectGroup.status === 'Recruited'">
			<div class="bg-blue-70">
				<!-- 모임 상태 뱃지 -->
				<div class="align-right">
					<q-badge
						text-color="white"
						align="top"
						class="q-pa-sm bg-blue-200 text-body2">
						모집 완료 및 관람중
					</q-badge>
				</div>
			</div>
			<!-- 구성원 -->
			<div class="row q-pa-md q-pb-xl bg-blue-70">
				<q-space class="col-2" />
				<div
					class="col"
					v-for="fellow in getSelectGroup.fellows"
					:key="fellow.nickname">
					<q-avatar
						rounded
						size="73px"
						:class="{
							selected: fellow.isMyself,
							'bg-blue-100': fellow.profileImageUrl === null,
						}">
						<img
							:src="fellow.profileImageUrl"
							:alt="fellow.id"
							v-if="fellow.profileImageUrl" />
					</q-avatar>
					<div>
						<q-icon
							name="fas fa-crown"
							size="16px"
							color="blue-4"
							v-if="fellow.isLeader" />{{ fellow.nickname }}
					</div>
				</div>
				<q-space class="col-2" />
			</div>
			<!-- ott 계정 정보 -->
			<div v-if="getSelectGroup.account">
				<div class="q-mb-md">
					<q-input
						readonly
						label="아이디"
						v-model="getSelectGroup.account.id" />
					<q-input
						readonly
						label="비밀번호"
						v-model="getSelectGroup.account.password" />
				</div>
			</div>
			<!-- 버튼 -->
			<div class="row">
				<q-space class="col-8" />
				<q-btn outline class="q-mr-sm text-blue-200">
					신고<q-icon name="no_accounts" />
				</q-btn>
				<q-btn outline class="text-blue-200">
					<a
						:href="getSelectGroup.provider.link"
						target="_blank"
						class="text-blue-200">
						{{ getSelectGroup.provider.name }} 바로가기
					</a>
					<q-icon name="arrow_right_alt" />
				</q-btn>
			</div>
		</div>
	</div>

	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />

	<!--  찜한 작품  -->
	<user-videos
		v-if="getWishList"
		:title="wishList.title"
		:total="totalWish"
		:total-page="Math.ceil(totalWish / maxWidth)"
		:video-list="getWishList"
		:push-video-method="wishList.method"
		:expand-id="wishList.expandId" />
</template>

<script>
import { mapGetters, mapState } from 'vuex';
import UserVideos from '@/components/userVideos';
import { loadTossPayments } from '@tosspayments/payment-sdk';

const clientKey = 'test_ck_ADpexMgkW36nWZAzQJE3GbR5ozO0';

export default {
	name: 'My',
	components: { UserVideos },
	data() {
		return {
			maxWidth: 6,
			selectGroup: {},
			recentList: {
				title: '최근 조회 작품',
				method: 'user/pushRecentList',
				expandId: 'recent',
			},
			wishList: {
				title: '찜한 작품',
				method: 'user/pushWishList',
				expandId: 'wish',
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
		...mapState('user', ['profile', 'totalWish']),
		...mapGetters('user', [
			'getGroupList',
			'getSelectGroup',
			'getRecentList',
			'getWishList',
			'getStarList',
			'getWatchList',
		]),
	},
	async beforeCreate() {
		window.reload;
		await this.$store.dispatch('user/initProfile');
	},
	methods: {
		async clickGroupLogo(groupId) {
			await this.$store.dispatch('user/selectGroup', groupId);
		},

		async chargeCredit() {
			const tossPayments = await loadTossPayments(clientKey);
			tossPayments
				.requestBillingAuth('카드', {
					customerKey: 'zLNZjDKC1uqnMCk_ffMJL',
					successUrl: window.location.origin + '/success',
					failUrl: window.location.origin + '/fail',
				})
				.catch(function (error) {
					if (error.code === 'USER_CANCEL') alert('결제가 취소되었습니다!');
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

.selected {
	border: 3px solid #449bfe;
	border-radius: 6px;
}
</style>
