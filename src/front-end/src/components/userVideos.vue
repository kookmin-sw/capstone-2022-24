<template>
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">{{ title }}</div>
			<q-btn flat class="text-grey" @click="clickAllBtn">전체보기</q-btn>
		</div>
		<q-carousel
			v-model="currentPage"
			transition-prev="slide-right"
			transition-next="slide-left"
			swipeable
			animated
			padding
			arrows
			ref="carousel"
			control-color="primary"
			height="230px"
			class="bg-blue-1">
			<q-carousel-slide
				:name="page"
				v-for="page in videoList.totalPage"
				:key="page">
				<div
					class="row fit justify-center items-center video-list-frame"
					v-if="videoList.results[page - 1]">
					<div v-if="videoList.totalResult === 0">추가된 작품이 없습니다.</div>
					<div
						class="video-poster"
						v-for="video in videoList.results[page - 1].videos"
						:key="video.id">
						{{ video.posterUrl }}
					</div>
				</div>
			</q-carousel-slide>
		</q-carousel>
	</div>
</template>

<script>
import { mapState } from 'vuex';
export default {
	name: 'userVideos',
	props: {
		title: {
			type: String,
			require: true,
		},
		videoList: {
			require: true,
		},
		pushVideoMethod: {
			type: String,
			require: true,
		},
		expandId: {
			type: String,
			require: true,
		},
	},
	data() {
		return {
			currentPage: 1,
		};
	},
	watch: {
		currentPage: function (newVal) {
			if (newVal >= this.videoList.results.length) {
				this.$store.dispatch('user/pushRecentList', { page: newVal, size: 6 });
			}
		},
	},
	computed: {
		...mapState('user', ['userProfile']),
	},
	methods: {
		clickAllBtn() {
			this.$router.push(
				`/${this.userProfile.nickname}/expand/${this.expandId}`,
			);
		},
	},
};
</script>

<style scoped>
.video-list-frame {
	display: flex;
	flex-wrap: wrap;
}

.video-poster {
	width: 14%;
	height: 0;
	padding-bottom: 20%;
	margin: 0 12px 0 0;
	background: lightgrey;
}
</style>
