<template>
	<div class="expand q-ma-xl">
		<div class="row">
			<q-btn
				flat
				size="16px"
				class="q-mb-lg p-mr-md"
				v-for="(i, index) in interactions"
				:key="index"
				@click="interactionButtonClick(index)"
				:class="{
					'text-weight-bold': i.isSelect,
					'text-blue-200': i.isSelect,
				}">
				{{ i.label }}</q-btn
			>
		</div>
		<div v-if="!wishList">찜한 작품이 존재하지 않습니다.</div>
		<div>
			<q-infinite-scroll :offset="250" @load="videoOnLoad">
				<div class="row video-list-frame">
					<div class="video-poster" v-for="video in wishList" :key="video.id">
						<img
							:src="video.posterUrl"
							:alt="video.id"
							style="width: 100%; object-fit: cover"
							@click="videoClick(video.id, video.category)" />
						<div class="row no-wrap items-center">
							<div class="col text-right q-mt-sm">
								<div class="video-title text-left text-weight-bold">
									{{ video.title }}
								</div>
								<!--								<q-rating-->
								<!--									size="18px"-->
								<!--									v-model="stars"-->
								<!--									:max="5"-->
								<!--									class="text-blue-100" />-->
								<div class="q-mb-lg">{{ video.date }}</div>
							</div>
						</div>
					</div>
				</div>
				<template v-slot:loading>
					<div
						class="row q-mb-lg justify-center"
						v-if="wishList.length < totalWish">
						<q-spinner-dots color="primary" size="40px" />
					</div>
				</template>
			</q-infinite-scroll>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex';
export default {
	name: 'Expand',
	data() {
		return {
			currentTab: '',
			interactions: [
				// { label: '최근 조회한 작품', isSelect: false, name: 'recent' },
				{ label: '찜한 작품', isSelect: false, name: 'wish' },
				// { label: '별점 준 작품', isSelect: false, name: 'star' },
				// { label: '본 작품', isSelect: false, name: 'watched' },
			],
			stars: 4,
		};
	},
	async created() {
		this.currentTab = this.$route.params.listType;
		this.interactions.forEach(i => {
			if (this.currentTab === i.name) {
				i.isSelect = true;
			}
		});
		await this.$store.commit('videoExpands/INIT_VIDEOS');
		await this.$store.dispatch('videoExpands/loadWishList', 0);
	},
	computed: {
		...mapState('videoExpands', ['wishList', 'totalWish']),
	},
	methods: {
		videoOnLoad(index, done) {
			if (this.wishList.length <= this.totalWish) {
				setTimeout(() => {
					this.$store.dispatch('videoExpands/loadWishList', this.videos.length);
					done();
				}, 1000);
			}
		},
		interactionButtonClick(idx) {
			this.interactions.forEach(i => {
				if (i !== idx) {
					i.isSelect = false;
				}
			});
			this.interactions[idx].isSelect = true;
			this.currentTab = this.interactions[idx].name;
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
	justify-content: space-between;
}
.video-poster {
	width: 15%;
	margin: 0 0 24px 0;
}
.video-title {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}
</style>
