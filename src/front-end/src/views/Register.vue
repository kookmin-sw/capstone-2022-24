<template>
	<div class="Register q-ma-lg">
		<div class="text-h6 text-weight-bold">회원가입</div>
		<div>사용할 프로필 사진과 닉네임을 입력해주세요.</div>
		<q-input
			@update:model-value="
				val => {
					file = val[0];
				}
			"
			filled
			type="file"
			class="q-mb-md" />
		<div class="row q-mb-lg">
			<q-input dense label="닉네임" class="col-8 q-pr-lg" v-model="nickname" />
			<q-btn
				outline
				color="blue"
				class="col-4"
				@click="this.nicknameDuplication(this.nickname)">
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
		};
	},
	methods: {
		...mapActions('auth', ['nicknameDuplication']),
	},
};
</script>

<style scoped></style>
