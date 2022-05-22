<template>
	<div class="discontinue q-ma-xl">
		<div class="row">
			<q-btn
				flat
				size="16px"
				class="q-mb-lg q-mr-md"
				v-for="(d, index) in days"
				:key="index"
				@click="daysButtonClick(index)"
				:class="{
					'text-weight-bold': d.isSelect,
					'text-blue-200': d.isSelect,
				}">
				{{ d.label }}
			</q-btn>
		</div>
		<div>
			<q-infinite-scroll :offset="250" @load="videoOnLoad">
				<div class="row video-list-frame">
					<div
						class="video-poster"
						v-for="(video, index) in videos"
						:key="index"
						style="position: relative">
						<img
							:src="video.posterKey"
							:alt="video.title"
							style="width: 100%; object-fit: cover"
							@click="videoClick(video.videoId, video.category)" />
						<q-badge
							class="row reverse q-ma-none q-pa-sm float-right bg-transparent badge-frame"
							style="position: absolute; top: 0; left: 0">
							<q-avatar
								rounded
								size="md"
								v-for="provider in video.providers"
								:key="provider.id">
								<img
									:src="provider.logoKey"
									:alt="provider.id"
									class="border-grey-100" />
							</q-avatar>
						</q-badge>
					</div>
				</div>
				<!--				<template v-slot:loading>-->
				<!--					<div class="row q-mb-lg justify-center">-->
				<!--						<q-spinner-dots color="primary" size="40px" />-->
				<!--					</div>-->
				<!--				</template>-->
			</q-infinite-scroll>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
	name: 'Discontinue',
	data() {
		return {
			currentTab: 'endSeven',
			days: [
				{
					label: '7일 이내 종료 예정작',
					isSelect: true,
					name: 'endSeven',
					value: 7,
				},
				{
					label: '15일 이내 종료 예정작',
					isSelect: false,
					name: 'endFifteen',
					value: 15,
				},
				{
					label: '30일 이내 종료 예정작',
					isSelect: false,
					name: 'endThirty',
					value: 30,
				},
			],
		};
	},
	computed: {
		...mapState('videoDiscontinued', ['videos', 'totalResult', 'loadFail']),
	},
	async beforeCreate() {
		await this.$store.dispatch('videoDiscontinued/loadVideoList', 7);
	},
	methods: {
		videoOnLoad() {
			// infinite scroll
			return 0;
		},
		daysButtonClick(idx) {
			this.days.forEach(i => {
				if (i !== idx) {
					i.isSelect = false;
				}
			});
			this.days[idx].isSelect = true;
			this.currentTab = this.days[idx].name;
			this.$store.dispatch(
				'videoDiscontinued/loadVideoList',
				this.days[idx].value,
			);
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
	height: 0;
	padding-bottom: 20%;
	margin: 0 0 24px 0;
	align-content: center;
	overflow-y: hidden;
}

.badge-frame {
	display: flex;
	flex-wrap: wrap;
}
</style>
