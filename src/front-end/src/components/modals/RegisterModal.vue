<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section>
			<div class="text-h6 text-weight-bold">회원가입</div>
			<div>사용할 프로필 사진과 닉네임을 입력해주세요.</div>
		</q-card-section>
		<q-card-section class="q-pt-none">
			<q-input
				@update:model-value="
					val => {
						file = val[0];
					}
				"
				filled
				type="file"
				class="q-mb-md" />
			<div class="row">
				<q-input
					dense
					label="닉네임"
					class="col-8 q-pr-lg"
					v-model="nickname" />
				<q-btn outline color="blue" class="col-4"> 중복 확인</q-btn>
			</div>
		</q-card-section>
		<q-card-actions align="right" class="text-primary">
			<q-btn flat label="취소" v-close-popup @click="setRegister(false)" />
			<q-btn flat label="회원가입" v-close-popup />
		</q-card-actions>
	</q-card>
</template>

<script>
import { mapActions } from 'vuex';
export default {
	name: 'RegisterModal',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
	},
	data() {
		return {
			nickname: null,
		};
	},
	methods: {
		...mapActions('auth', ['setRegister']),
	},
};
</script>

<style scoped>
/*input[type='file'] {*/
/*	!* 파일 필드 숨기기 *!*/
/*	position: absolute;*/
/*	width: 1px;*/
/*	height: 1px;*/
/*	padding: 0;*/
/*	margin: -1px;*/
/*	overflow: hidden;*/
/*	clip: rect(0, 0, 0, 0);*/
/*	border: 0;*/
/*}*/
</style>
