<template>
	<!--  Login Modal -->
	<q-dialog v-model="isLoginModal">
		<login-modal :isActive="isLoginModal"></login-modal>
	</q-dialog>
	<!-- Alarm Modal -->
	<q-dialog v-model="isAlarmModal">
		<alarm-modal :isActive="isAlarmModal"></alarm-modal>
	</q-dialog>
	<!-- gnb -->
	<div class="gnb container">
		<div class="row items-center">
			<!-- logo wrapper -->
			<div class="logo-wrapper col-2 q-pl-lg">
				<div class="q-pt-sm q-pb-md">
					<img
						src="@/assets/service_logo.svg"
						alt=""
						style="display: block; width: 100%; height: 76px"
						class="logo-img"
						@click="$router.push({ name: 'Home' })" />
				</div>
			</div>
			<!-- text menu wrapper -->
			<div class="text-menu-wrapper col-6 row">
				<router-link to="/" class="col-4"> 홈 </router-link>
				<router-link to="/discontinue" class="col-4"> 종료예정작 </router-link>
				<router-link :to="`/join/${profile.nickname}`" class="col-4">
					모임 신청
				</router-link>
			</div>
			<!-- icon menu wrapper -->
			<div class="icon-menu-wrapper col-2">
				<div class="row" v-if="isLogin === true">
					<q-space class="col-3" />
					<q-btn flat class="my-menu col-4">
						<router-link :to="`/my/${profile.nickname}`">
							<q-icon name="person" size="md" color="blue-4" />
						</router-link>
					</q-btn>
					<q-btn flat class="alarm-menu col-4" @click="alarmBtnClick">
						<q-icon
							name="notifications_none"
							size="md"
							color="blue-4"
							class="alarm-icon" />
					</q-btn>
					<q-space class="col-1" />
				</div>
			</div>
			<!-- login/register/logout button -->
			<div class="btn-wrapper col-2">
				<q-btn
					unelevated
					class="bg-blue-100 text-white text-bold"
					id="login-btn"
					v-if="isLogin === false"
					@click="loginBtnClick">
					로그인/회원가입
				</q-btn>
				<q-btn
					unelevated
					class="text-blue-100 border-blue-100-none text-bold"
					id="logout-btn"
					v-else
					@click="logoutBtnClick">
					로그아웃
				</q-btn>
			</div>
		</div>
		<q-separator color="blue-1" size="2px" inset />
		<q-separator color="blue-4" inset />
	</div>
</template>

<script>
import { mapGetters, mapState } from 'vuex';
import LoginModal from '@/components/modals/LoginModal';
import AlarmModal from '@/components/modals/AlarmModal';
export default {
	name: 'GNB',
	components: {
		LoginModal,
		AlarmModal,
	},
	data() {
		return {
			isLoginModal: false,
			isRegisterModal: false,
			isAlarmModal: false,
		};
	},
	computed: {
		...mapState('auth', ['profile']),
		...mapGetters('auth', ['isLogin']),
	},
	methods: {
		loginBtnClick() {
			this.isLoginModal = !this.isLoginModal;
		},
		logoutBtnClick() {
			this.$store.dispatch('auth/logout');
		},
		alarmBtnClick() {
			this.isAlarmModal = !this.isAlarmModal;
		},
	},
};
</script>

<style scoped>
.gnb {
	height: 100px;
	line-height: 100px;
	background-color: white;
}
</style>
