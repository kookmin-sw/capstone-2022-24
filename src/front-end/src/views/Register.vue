<template>
	<div class="row q-ma-xl">
		<q-space class="col-2" />
		<!-- 회원가입 영역 -->
		<div class="col-8">
			<!-- 회원가입 타이틀 -->
			<div class="q-mb-lg text-left text-h6 text-weight-bold">회원가입</div>
			<!-- 프로필 사진 입력 -->
			<div class="text-left q-mb-lg">
				<div class="text-weight-bold text-blue-200">프로필 사진</div>
				<div class="q-mb-md">사용할 프로필 사진을 업로드해주세요.</div>
				<q-avatar
					rounded
					size="120px"
					:style="`background-image : url(${imageUrl})`"
					class="q-mb-md profile-img text-blue-200">
					<div @click="clickInputField()">
						<input
							ref="image"
							id="in"
							type="file"
							name="image"
							accept="image/png, image/jpeg, image/jpg"
							class="hidden"
							@change="loadImg()" />
						<q-icon
							size="44px"
							name="add_circle_outline"
							class="text-blue-100" />
					</div>
				</q-avatar>
			</div>
			<!-- 닉네임 입력 -->
			<div class="text-left q-mb-xl">
				<div class="text-weight-bold text-blue-200">닉네임</div>
				<div class="q-mb-md">
					사용할 닉네임을 입력해주세요. 닉네임은 회원가입 후 변경이
					불가능합니다.
				</div>
				<div class="row items-center">
					<q-input
						dense
						label="한글, 알파벳, 숫자를 사용하여 8글자 이하로 입력해주세요."
						:hint="this.canNicknameText"
						color="blue-4"
						class="column col-9 q-pr-lg"
						v-model="nickname"
						@keyup="this.canNickname = false" />
					<q-btn
						outline
						@click="nicknameValidation"
						class="col-3 text-blue-200">
						중복 확인
					</q-btn>
				</div>
			</div>
			<!-- 회원가입 버튼 -->
			<q-btn
				@click="clickSignUp"
				unelevated
				color="blue-4"
				class="full-width q-mb-lg">
				회원가입
			</q-btn>
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
			imageUrl: '',
			imageFile: '',
			albumBucketName: process.env.VUE_APP_S3_BUCKET_NAME,
			bucketRegion: process.env.VUE_APP_S3_BUCKET_REGION,
			IdentityPoolId: process.env.VUE_APP_S3_IDENTITY_POOL_ID,
		};
	},
	computed: {
		canNicknameText() {
			if (!this.canNickname) {
				return '닉네임 입력 후 중복 확인 해주세요.';
			} else {
				return '사용 가능한 닉네임 입니다.';
			}
		},
	},
	methods: {
		...mapActions('auth', ['nicknameDuplication']),
		nicknameValidation() {
			// 닉네임 유효성 검사
			// 특수문자 정규식
			const specialCheck = /[!?@#$%^&*():;+\-=~{}<>\\[\]_|"',.`]/g;
			const blankCheck = /[\s]/;

			// 닉네임 공백, 글자수, 특문 검사
			if (
				!this.nickname ||
				this.nickname.length < 1 ||
				this.nickname.length > 8 ||
				specialCheck.test(this.nickname) ||
				blankCheck.test(this.nickname)
			) {
				alert('형식에 맞지 않는 닉네임입니다.');
				this.canNickname = false;
				return;
			}

			// 닉네임 중복 검사
			this.nicknameDuplication(this.nickname)
				.then(() => {
					alert('사용 가능한 닉네임입니다.');
					this.canNickname = true;
				})
				.catch(() => {
					alert('이미 사용중인 닉네임입니다.');
					this.canNickname = false;
				});
		},
		clickInputField() {
			this.$refs['image'].click();
		},
		loadImg() {
			this.imageFile = this.$refs['image'].files[0];
			// 업로드한 이미지 용량 확인
			if (this.imageFile.size > 4194304) {
				alert('크기가 4MB 이하인 이미지를 선택해주세요.');
				return;
			}
			// '온갖' 회원가입 페이지에서 선택한 이미지 미리보기
			this.imageUrl = URL.createObjectURL(this.imageFile);
		},
		resizeImg() {
			// resizing image
			const reader = new FileReader();
			reader.readAsDataURL(this.imageFile);
			reader.onload = () => {
				const image = new Image();
				image.src = reader.result;
				image.onload = () => {
					const canvas = document.createElement('canvas');
					const maxSize = 240;
					var width = image.width;
					var height = image.height;

					// 가로 세로 중 작은 쪽을 max size에 맞춤
					if (width > height && width > maxSize) {
						width *= maxSize / height;
						height = maxSize;
					} else if (height > width && height > maxSize) {
						height *= maxSize / width;
						width = maxSize;
					}

					canvas.width = width;
					canvas.height = height;

					const ctx = canvas.getContext('2d');
					ctx.drawImage(image, 0, 0, width, height);

					const dataUrl = canvas.toDataURL('image/png');
					this.imageFile = this.dataURItoBlob(dataUrl);
				};
			};
		},
		dataURItoBlob(dataURI) {
			const bytes =
				dataURI.split(',')[0].indexOf('base64') >= 0
					? atob(dataURI.split(',')[1])
					: unescape(dataURI.split(',')[1]);
			const max = bytes.length;
			const ia = new Uint8Array(max);
			for (var i = 0; i < max; i++) ia[i] = bytes.charCodeAt(i);
			return new Blob([ia], { type: 'image/png' });
		},
		clickSignUp() {
			if (!this.canNickname) {
				alert('닉네임 중복 확인 검사를 해주세요.');
				return;
			}
			if (!this.imageFile) {
				alert('이미지를 선택해주세요.');
				return;
			}
			this.resizeImg();
			const albumPhotosKey = 'app/front-end/users/profile/';
			const fileInfo = {
				nickname: this.nickname,
				photoKey: albumPhotosKey + this.nickname + '.png',
				file: this.imageFile,
			};
			this.$store.dispatch('auth/signUp', fileInfo);
		},
	},
};
</script>

<style scoped>
.profile-img {
	border: dotted 2px;
	background-size: cover;
	background-position: 50% 50%;
}
</style>
