<template>
	<!--  Login Modal -->
	<q-dialog v-model="isLoginModal">
		<login-modal :isActive="isLoginModal"></login-modal>
	</q-dialog>
	<!--  GNB -->
	<div class="gnb container">
		<div class="row items-center">
			<div class="col-2 q-pl-lg">
				<div class="q-pt-sm q-pl-md q-pb-md">
					<img
						src="@/assets/logo.png"
						alt=""
						style="display: block; width: 100%; height: 76px"
						@click="$router.push({ name: 'Home' })" />
				</div>
			</div>
			<div class="text-menu-frame col-6 row">
				<router-link to="/" class="col-4">
					{{ $t('gnb.home') }}
				</router-link>
				<router-link to="/discontinue" class="col-4">
					{{ $t('gnb.discontinued') }}
				</router-link>
				<router-link :to="`/join/${userId}`" class="col-4">
					{{ $t('gnb.groupJoin') }}
				</router-link>
			</div>
			<div class="icon-menu-frame col-2">
				<div class="row" v-if="isLogin === true">
					<q-space class="col-3" />
					<q-btn flat class="col-4">
						<router-link :to="`/my/${userId}`">
							<q-icon name="person" size="md" color="blue" />
						</router-link>
					</q-btn>
					<q-btn flat class="col-4">
						<q-icon name="notifications_none" size="md" color="blue" />
					</q-btn>
					<q-space class="col-1" />
				</div>
			</div>
			<div class="col-2">
				<q-btn
					unelevated
					color="blue"
					v-if="isLogin === false"
					@click="loginBtnClick">
					{{ $t('gnb.login') }}
				</q-btn>
				<q-btn unelevated color="blue" v-else @click="logoutBtnClick">
					{{ $t('gnb.logout') }}
				</q-btn>
			</div>
		</div>
		<q-separator color="blue" inset />
	</div>
</template>

<script>
import { mapGetters, mapState } from 'vuex';
import LoginModal from '@/components/modals/LoginModal';
export default {
	name: 'GNB',
	components: {
		LoginModal,
	},
	data() {
		return {
			isLoginModal: false,
		};
	},
	computed: {
		...mapState('auth', ['userId']),
		...mapGetters('auth', ['isLogin']),
	},
	methods: {
		loginBtnClick() {
			this.isLoginModal = !this.isLoginModal;
		},
		logoutBtnClick() {
			this.$store.dispatch('auth/setToken', null);
			this.$router.push({ name: 'Home' });
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
