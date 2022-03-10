<template>
	<!--  <q-separator color="blue" inset />-->
	<div class="footer">
		<div class="text-menu-frame text-left row">
			<div class="col">회사소개</div>
			<div class="col">이용약관</div>
			<div class="col">개인정보처리방침</div>
			<div class="col">고객센터</div>
			<div class="col">1:1문의</div>
			<div class="col-4"></div>
		</div>
		<div class="business-info col">
			<div class="row text-left">
				(주) 서비스명 | 대표이사: 구다희 | 소재지: 서울 특별시 성북구 정릉로 77
				| 사업자 등록번호: 123-45-6790
			</div>
			<div class="row text-left">copyright 어쩌구</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Footer',
};
</script>

<style scoped>
.footer {
	height: 170px;
	padding: 40px 0 56px 0;
	/*background-color:yellowgreen;*/
}

.business-info {
	margin-top: 16px;
	color: #bdbdbd;
}
</style>
