<template>
	<!--  Login Modal -->
	<q-dialog v-model="isLoginModal">
		<login-modal :isActive="isLoginModal"></login-modal>
	</q-dialog>
	<!--  GNB -->
	<div class="gnb container">
		<div class="row">
			<div class="col-2">
				<span class="text-h6 text-weight-bolder">
					{{ $t('serviceName') }}
				</span>
			</div>
			<div class="text-menu-frame col-6">
				<div class="row">
					<span class="col-4"> {{ $t('gnb.home') }} </span>
					<span class="col-4"> {{ $t('gnb.discontinued') }} </span>
					<span class="col-4"> {{ $t('gnb.groupJoin') }} </span>
				</div>
			</div>
			<div class="icon-menu-frame col-2">
				<!--				<div class="row">-->
				<!--					<q-space class="col-3" />-->
				<!--					<div class="col-4">-->
				<!--						<q-icon name="person" size="md" color="blue" />-->
				<!--					</div>-->
				<!--					<div class="col-4">-->
				<!--						<q-icon name="notifications_none" size="md" color="blue" />-->
				<!--					</div>-->
				<!--					<q-space class="col-1" />-->
				<!--				</div>-->
			</div>
			<div class="col-2">
				<q-btn unelevated color="blue" @click="loginBtnClick">
					{{ $t('gnb.login') }}
				</q-btn>
				<!--				<q-btn unelevated color="blue">{{ $t('gnb.logout') }}</q-btn>-->
			</div>
		</div>
		<q-separator color="blue" inset />
	</div>
</template>

<script>
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
	methods: {
		loginBtnClick() {
			this.isLoginModal = !this.isLoginModal;
		},
	},
};
</script>

<style scoped>
.gnb {
	height: 84px;
	line-height: 84px;
	background-color: white;
	z-index: 10;
}
</style>
