<template>
	<div class="row q-ma-lg">
		<q-space class="col-2" />
		<!-- 회원가입 영역 -->
		<div class="col-8">
			<!-- 회원가입 타이틀 -->
			<div class="q-mb-md text-left text-h5 text-weight-bold">회원가입</div>

			<!-- 프로필 사진 입력 -->
			<div class="text-left q-mb-lg">
				<div class="text-h6 text-weight-bold">프로필 사진</div>
				<div class="q-mb-md">사용할 프로필 사진을 업로드해주세요.</div>
				<q-avatar
					rounded
					size="120px"
					style="border: dotted 2px cornflowerblue"
					:style="`background-image : url(${selectImg})`"
					class="q-mb-lg">
					<div @click="clickInputField()">
						<input
							ref="image"
							id="in"
							type="file"
							name="image"
							accept="image/png, image/jpeg, image/jpg"
							class="hidden"
							@change="uploadImg()" />
						<q-icon size="44px" name="add_circle_outline" />
					</div>
				</q-avatar>
			</div>
			<!-- 닉네임 입력 -->
			<div class="text-left q-mb-lg">
				<div class="q-mb-xs text-h6 text-weight-bold">닉네임</div>
				<div>
					사용할 닉네임을 입력해주세요. 닉네임은 회원가입 후 변경이
					불가능합니다.
				</div>
				<div class="row items-center">
					<q-input
						dense
						hint="닉네임은 8글자 이하로 입력해주세요."
						class="column col-9 q-pr-lg q-mb-lg"
						v-model="nickname" />
					<q-btn
						outline
						color="blue"
						@click="duplicationCheckBtnClick"
						class="col-3">
						중복 확인
					</q-btn>
				</div>
			</div>
			<!-- 회원가입 버튼 -->
			<q-btn unelevated color="blue" class="full-width q-mb-lg">회원가입</q-btn>
		</div>
		<!-- 회원가입 영역 종료 -->
		<q-space class="col-2" />
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
