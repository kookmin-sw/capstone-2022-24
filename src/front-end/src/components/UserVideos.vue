<template>
	<div class="q-ma-xl">
		<div class="row q-mb-md">
			<div class="text-h6 text-weight-bold">{{ title }}</div>
			<q-btn flat class="text-grey" @click="clickAllBtn">전체보기</q-btn>
		</div>

		<div
			class="text-h6 text-bold bg-blue-70"
			v-if="!totalPage"
			style="height: 230px; line-height: 230px">
			추가된 작품이 없습니다.
		</div>
		<q-carousel
			v-model="currentPage"
			v-else
			transition-prev="slide-right"
			transition-next="slide-left"
			swipeable
			animated
			padding
			arrows
			ref="carousel"
			control-color="blue-4"
			height="230px"
			class="bg-blue-70">
			<q-carousel-slide :name="page" v-for="page in totalPage" :key="page">
				<div
					class="row fit justify-center items-center video-list-frame"
					v-if="videoList[this.currentPage - 1]">
					<div
						class="video-poster bg-grey-4"
						v-for="video in videoList[this.currentPage - 1]"
						:key="video.id">
						<img
							:src="video.posterUrl"
							:alt="video.title"
							@click="videoClick(video.id, video.category)"
							style="width: 100%; object-fit: cover" />
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
		total: {
			require: true,
		},
		totalPage: {
			require: true,
		},
		videoList: {
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
		currentPage: function () {
			this.$store.dispatch('user/pushVideos', this.expandId);
		},
	},
	computed: {
		...mapState('auth', ['profile']),
	},
	methods: {
		clickAllBtn() {
			this.$router.push(`/${this.profile.nickname}/expand/${this.expandId}`);
		},
		videoClick(videoId, category) {
			this.$router.push({ name: 'Details', params: { videoId, category } });
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
	width: 15%;
	height: 0;
	padding-bottom: 20%;
	margin: 0 10px 0 0;
	background: transparent;
	align-content: center;
	overflow-y: hidden;
}
</style>
