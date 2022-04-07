<template>
	<div class="Register q-ma-lg">
		<!-- 회원가입 타이틀 -->
		<div class="q-mb-lg">
			<div class="text-h6 text-weight-bold">회원가입</div>
			<div>사용할 프로필 사진과 닉네임을 입력해주세요.</div>
		</div>

		<!-- 프로필 사진 입력 -->
		<q-avatar
			rounded
			size="120px"
			style="border: dotted 2px cornflowerblue"
			:style="`background-image : url(${selectImg})`">
			<div @click="clickInputField()">
				<input
					ref="image"
					id="in"
					type="file"
					name="image"
					accept="image/png, image/jpeg, image/jpg"
					class="hidden"
					@change="uploadImg()" />
				<q-icon name="add_circle_outline" />
			</div>
		</q-avatar>

		<!-- 닉네임 입력 -->
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

		<!-- 회원가입 버튼 -->
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
		uploadImg() {
			const file = this.$refs['image'].files[0];
			if (file.size > 4194304) {
				alert('크기가 4MB 이하인 이미지를 선택해주세요.');
				return;
			}
			this.selectImg = URL.createObjectURL(file);
		},
		clickInputField() {
			this.$refs['image'].click();
		},
	},
};
</script>

<style scoped></style>
