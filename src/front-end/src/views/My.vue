<!DOCTYPE html>
<template>
	<!-- mileage modal -->
	<q-dialog v-model="isMileageModal">
		<mileage-modal :isActive="isMileageModal" />
	</q-dialog>
	<!-- ott 계정 수정 모달 -->
	<q-dialog v-model="isInputModal">
		<input-account
			persistent
			:isActive="isInputModal"
			:group-id="getSelectGroup.account.id"
			:id="getSelectGroup.account.identifier"
			:pw="getSelectGroup.account.password" />
	</q-dialog>
	<!-- 모임 탈퇴 모달 -->
	<q-dialog v-model="isLeaveModal">
		<leave-group-modal
			persistent
			:isActive="isLeaveModal"
			@clickLeave="leaveGroup" />
	</q-dialog>
	<!-- 모임 탈퇴 성공 모달 -->
	<q-dialog v-model="isLeaveSuccess">
		<leave-group-success persistent :isActive="isLeaveSuccess" />
	</q-dialog>
	<!-- 프로필 영역 -->
	<div class="column q-ma-xl">
		<div class="q-mb-md text-left text-h6 text-weight-bold">
			{{ profile.nickname }}
		</div>
		<q-avatar rounded size="73px" class="q-mb-md" v-if="profile.profileImg">
			<img :src="profile.profileImg" :alt="'profile'" />
		</q-avatar>
		<q-avatar v-else rounded size="73px" class="q-mb-md bg-blue-100" />
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
			<div
				class="q-ml-md q-pl-md q-pr-md border-blue-100 text-blue-200 radius-4"
				style="cursor: pointer"
				@click="mileageHistoryBtnClick">
				내역조회
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

		<!-- 모임 탈퇴 -->
		<div class="text-left align-right">
			<q-btn
				flat
				dense
				class="text-grey"
				v-if="
					getSelectGroup !== null &&
					(getSelectGroup.status === 'Recruited' ||
						getSelectGroup.status === 'Reviewing')
				"
				@click="clickLeaveGroup">
				모임 탈퇴 하기 &gt;
			</q-btn>
		</div>
		<!-- 모임 모집 중 -->
		<div
			class="row q-pa-md q-mt-md q-pb-xl bg-blue-70"
			v-if="getSelectGroup !== null && getSelectGroup.status === 'Recruiting'"
			style="height: 343px">
			<q-space class="col-2" />
			<div class="q-mt-auto q-mb-auto text-h6 text-weight-bold">
				모임 구성원을 기다리는 중입니다.
			</div>
			<q-space class="col-2" />
		</div>

		<!-- 모집 완료 -->
		<!-- 모임 상세 정보 -->
		<div
			v-if="
				getSelectGroup !== null &&
				(getSelectGroup.status === 'Recruited' ||
					getSelectGroup.status === 'Reviewing')
			">
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
						v-model="getSelectGroup.account.identifier" />
					<q-input
						readonly
						label="비밀번호"
						v-model="getSelectGroup.account.password" />
				</div>
			</div>
			<!-- 버튼 -->
			<div class="row">
				<q-space class="col-6" />
				<!-- TODO: 모임장에게만 보이게 -->
				<q-btn
					outline
					class="q-mr-sm text-blue-200"
					@click="clickChangeAccount">
					{{ getSelectGroup.provider.name }} 계정 입력<q-icon
						name="fas fa-pen"
						size="18px" />
				</q-btn>
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
		:title="myVideos.wishes.title"
		:total="total.wishes"
		:total-page="Math.ceil(total.wishes / maxWidth)"
		:video-list="videos.wishes"
		:expand-id="myVideos.wishes.expandId" />
	<!-- 본 작품 -->
	<user-videos
		:title="myVideos['watch-marks'].title"
		:total="total['watch-marks']"
		:total-page="Math.ceil(total['watch-marks'] / maxWidth)"
		:video-list="videos['watch-marks']"
		:expand-id="myVideos['watch-marks'].expandId" />
</template>

<script>
import { loadTossPayments } from '@tosspayments/payment-sdk';
import { mapGetters, mapState } from 'vuex';
import UserVideos from '@/components/UserVideos';
import MileageModal from '@/components/modals/MileageModal';
import InputAccount from '@/components/modals/InputAccount';
import LeaveGroupModal from '@/components/modals/LeaveGroupModal';
import LeaveGroupSuccess from '@/components/modals/LeaveGroupSuccess';

const clientKey = 'test_ck_ADpexMgkW36nWZAzQJE3GbR5ozO0';

export default {
	name: 'My',
	components: {
		LeaveGroupSuccess,
		LeaveGroupModal,
		InputAccount,
		UserVideos,
		MileageModal,
	},
	data() {
		return {
			isMileageModal: false,
			isInputModal: false,
			isLeaveModal: false,
			isLeaveSuccess: false,
			maxWidth: 6,
			selectGroup: {},
			myVideos: {
				wishes: {
					title: '찜한 작품',
					expandId: 'wishes',
				},
				'watch-marks': {
					title: '본 작품',
					expandId: 'watch-marks',
				},
			},
		};
	},
	computed: {
		...mapState('user', ['profile', 'total', 'videos']),
		...mapGetters('user', ['getGroupList', 'getSelectGroup']),
	},
	async beforeCreate() {
		window.reload;
		await this.$store.dispatch('user/initProfile');
	},
	methods: {
		async clickGroupLogo(groupId) {
			await this.$store.dispatch('user/selectGroup', groupId);
		},
		clickLeaveGroup() {
			this.isLeaveModal = !this.isLeaveModal;
		},
		leaveGroup() {
			// TODO: api 호출
			// TODO: 성공, 실패 판단
			this.isLeaveSuccess = true;
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
		mileageHistoryBtnClick() {
			this.isMileageModal = !this.isMileageModal;
		},
		clickChangeAccount() {
			this.isInputModal = !this.isInputModal;
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
