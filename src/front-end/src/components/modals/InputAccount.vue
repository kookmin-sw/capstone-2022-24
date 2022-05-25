<template>
	<q-card style="width: 600px; max-width: 80vw" v-if="isActive">
		<q-card-section class="row items-center q-ma-sm">
			<div class="text-h6 text-weight-bold q-ml-sm">OTT 계정 입력</div>
			<div class="q-ma-sm text-blue-200 text-weight-bold">
				아이디, 비밀번호를 입력하세요.
			</div>
			<q-space />
		</q-card-section>

		<q-card-section class="q-pt-none">
			<q-input
				dense
				label="아이디"
				color="blue-4"
				class="column col-9 q-pr-lg q-mb-md"
				v-model="identifier"
				@keyup="prompt = false" />
			<q-input
				dense
				label="비밀번호"
				color="blue-4"
				class="column col-9 q-pr-lg"
				v-model="password"
				@keyup="prompt = false" />
		</q-card-section>

		<q-card-actions align="right">
			<q-btn flat label="취소" color="red" v-close-popup />
			<q-btn flat label="변경" class="text-blue-200" @click="clickEdit" />
		</q-card-actions>
	</q-card>
</template>

<script>
import { ref } from 'vue';

export default {
	name: 'InputAccount',
	props: {
		isActive: {
			type: Boolean,
			require: true,
		},
		id: {
			require: true,
		},
		pw: {
			require: true,
		},
	},
	data() {
		return {
			identifier: ref(''),
			password: ref(''),
		};
	},
	created() {
		this.identifier = this.id;
		this.password = this.pw;
	},
	methods: {
		clickEdit() {
			console.log(this.identifier);
			console.log(this.password);
		},
	},
};
</script>

<style scoped></style>
