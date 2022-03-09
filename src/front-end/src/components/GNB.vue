<template>
	<div class="gnb container">
		<div class="row">
			<div class="col-2">
				<span> logo </span>
			</div>
			<div class="text-menu-frame col-6">
				<div class="row">
					<span class="col-4"> 홈 </span>
					<span class="col-4"> 종료 예정작 </span>
					<span class="col-4"> 모임 신청 </span>
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
				<q-btn unelevated color="blue">로그인/회원가입</q-btn>
				<!--				<q-btn unelevated color="blue">로그아웃</q-btn>-->
			</div>
		</div>
		<q-separator color="blue" inset />
	</div>
</template>

<script>
export default {
	name: 'GNB',
};
</script>

<style scoped>
.gnb {
	position: fixed;
	top: 0;
	width: 100%;
	height: 84px;
	line-height: 84px;
	background-color: white;
}
</style>
