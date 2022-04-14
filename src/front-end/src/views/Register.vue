<template>
	<div class="row q-ma-lg">
		<q-space class="col-2" />
		<!-- 회원가입 영역 -->
		<div class="col-8">
			<!-- 회원가입 타이틀 -->
			<div class="q-mb-md text-left text-h5 text-weight-bold">회원가입</div>

			<q-btn @click="vueEnvTest">click vue env test</q-btn>

			<!-- 프로필 사진 입력 -->
			<div class="text-left q-mb-lg">
				<div class="text-h6 text-weight-bold">프로필 사진</div>
				<div class="q-mb-md">사용할 프로필 사진을 업로드해주세요.</div>
				<q-avatar
					rounded
					size="120px"
					:style="`background-image : url(${selectImg})`"
					class="q-mb-lg profile-img">
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
						hint="닉네임은 공백없이 한글, 알파벳, 숫자만 8글자 이하로 입력해주세요."
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
import AWS from 'aws-sdk';
// import fs from 'fs';

export default {
	name: 'Register',
	data() {
		return {
			nickname: null,
			canNickname: false,
			selectImg: '',

			albumBucketName: 'bucket name',
			bucketRegion: 'ap-northeast-2',
			IdentityPoolId: 'poolId',
		};
	},
	methods: {
		...mapActions('auth', ['nicknameDuplication']),
		vueEnvTest() {
			console.log(process.env.VUE_APP_TEST);
		},

		duplicationCheckBtnClick() {
			// 특수문자 정규식
			const specialCheck = /[!?@#$%^&*():;+\-=~{}<>\\[\]_|"',.`]/g;
			const blankCheck = /[\s]/;

			// 닉네임 공백, 글자수, 특문 체크
			if (
				!this.nickname ||
				this.nickname.length < 1 ||
				this.nickname.length > 8 ||
				specialCheck.test(this.nickname) ||
				blankCheck.test(this.nickname)
			) {
				alert('형식에 맞지 않는 닉네임입니다.');
				return;
			}

			// 닉네임 중복 체크
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
		uploadImg() {
			const file = this.$refs['image'].files[0];
			if (file.size > 4194304) {
				alert('크기가 4MB 이하인 이미지를 선택해주세요.');
				return;
			}

			// '온갖' 회원가입 페이지에서 선택한 이미지 미리보기
			this.selectImg = URL.createObjectURL(file);

			// upload to s3 storage
			AWS.config.update({
				region: this.bucketRegion,
				credentials: new AWS.CognitoIdentityCredentials({
					IdentityPoolId: this.IdentityPoolId,
				}),
			});

			const photoKey = file.name;

			const upload = new AWS.S3.ManagedUpload({
				params: {
					Bucket: this.albumBucketName,
					Key: photoKey,
					Body: file,
				},
			});

			// console.log(upload)
			const promise = upload.promise();
			promise.then(
				() => {
					alert('Successfully uploaded photo.');
				},
				err => {
					return alert(
						'There was an error uploading your photo: ',
						err.message,
					);
				},
			);

			// const s3 = new AWS.S3({
			// 	apiVersion: '2006-03-01',
			// 	params: { Bucket: 'ongaj-s3' },
			// });

			// image resizing
			// const reader = new FileReader();
			// reader.readAsDataURL(file);
			// reader.onload = () => {
			// 	const image = new Image();
			// 	image.src = reader.result;
			// 	image.onload = () => {
			// 		// console.log(image.width, image.height);
			// 		const canvas = document.createElement('canvas');
			// 		const maxSize = 240;
			// 		var width = image.width;
			// 		var height = image.height;
			//
			// 		if (width > height && width > maxSize) {
			// 			height *= maxSize / width;
			// 			width = maxSize;
			// 		} else if (height > width && height > maxSize) {
			// 			width *= maxSize / height;
			// 			height = maxSize;
			// 		}
			//
			// 		canvas.width = width;
			// 		canvas.height = height;
			//
			// 		const ctx = canvas.getContext('2d');
			// 		ctx.drawImage(image, 0, 0, width, height);
			//
			// 		const dataUrl = canvas.toDataURL('image/png');
			// 		const ex = this.dataURItoBlob(dataUrl);
			// 		console.log(ex);
			// 	};
			// };
		},
		// dataURItoBlob(dataURI) {
		// 	var bytes =
		// 		dataURI.split(',')[0].indexOf('base64') >= 0
		// 			? atob(dataURI.split(',')[1])
		// 			: unescape(dataURI.split(',')[1]);
		// 	var mime = dataURI.split(',')[0].split(':')[1].split(';')[0];
		// 	console.log(mime);
		// 	var max = bytes.length;
		// 	var ia = new Uint8Array(max);
		// 	for (var i = 0; i < max; i++) ia[i] = bytes.charCodeAt(i);
		// 	return new Blob([ia], { type: 'image/png' });
		// },
		clickInputField() {
			this.$refs['image'].click();
		},
	},
};
</script>

<style scoped>
.profile-img {
	border: dotted 2px cornflowerblue;
	background-size: cover;
	background-position: 50% 50%;
}
</style>
