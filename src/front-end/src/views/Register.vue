<template>
	<div class="Register q-ma-lg">
		<div class="text-h6 text-weight-bold">회원가입</div>
		<div>사용할 프로필 사진과 닉네임을 입력해주세요.</div>
		<div>
			<q-avatar
				rounded
				size="100px"
				:style="`background-image : url(${selectImg})`" />
		</div>
		<!--		<input @change="uploadExample" accept="image/*" type="file" id="file" />-->
		<div class="row q-mb-lg">
			<q-input dense label="닉네임" class="col-8 q-pr-lg" v-model="nickname" />
			<q-btn
				outline
				color="blue"
				class="col-4"
				@click="duplicationCheckBtnClick">
				중복 확인
			</q-btn>
		</div>
		<div>
			<q-btn unelevated color="blue" class="full-width">회원가입</q-btn>
		</div>
	</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
	name: 'Register',
	data() {
		return {
			nickname: null,
			canNickname: false,
			selectImg: '',
		};
	},
	methods: {
		...mapActions('auth', ['nicknameDuplication']),
		duplicationCheckBtnClick() {
			if (!this.nickname) {
				alert('닉네임 형식을 맞추어 입력해주세요.');
				return;
			}
			this.nicknameDuplication(this.nickname)
				.then(() => {
					alert('사용 가능한 닉네임입니다.');
					this.canNickname = true;
				})
				.catch(() => {
					alert('사용 불가능한 닉네임입니다.');
					this.canNickname = false;
				});
		},
		// uploadExample(e) {
		// 	var file = e.target.files;
		// 	let url = URL.createObjectURL(file[0]); // file[0].type과 같이 js에서 .type 사용하면 image/png 등 확장자 검사가 가능
		// 	this.selectImg = url;
		// },
	},
};
</script>

<style scoped></style>
