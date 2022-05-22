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
			<q-infinite-scroll
				:offset="250"
				@load="videoOnLoad"
				id="videos-container"
				:number="1">
				<div class="row" id="videos-wrapper">
					<div
						class="videos"
						v-for="video in videos"
						:key="video.id"
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
								class="q-mr-xs"
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
				<template v-slot:loading>
					<div class="row justify-center" v-if="videos.length < totalResult">
						<q-spinner-dots color="primary" size="40px" class="q-mb-lg" />
					</div>
				</template>
				<div
					class="q-mb-xl text-h6 text-bold"
					v-if="loadFail && videos.length === 0">
					작품이 존재하지 않습니다.
				</div>
			</q-infinite-scroll>
			<!--			<q-infinite-scroll :offset="250" @load="videoOnLoad">-->
			<!--				<div class="row video-list-frame">-->
			<!--					<div-->
			<!--						class="video-poster"-->
			<!--						v-for="(video, index) in videos"-->
			<!--						:key="index"-->
			<!--						style="position: relative">-->
			<!--						<img-->
			<!--							:src="video.posterKey"-->
			<!--							:alt="video.title"-->
			<!--							style="width: 100%; object-fit: cover"-->
			<!--							@click="videoClick(video.videoId, video.category)" />-->
			<!--						<q-badge-->
			<!--							class="row reverse q-ma-none q-pa-sm float-right bg-transparent badge-frame"-->
			<!--							style="position: absolute; top: 0; left: 0">-->
			<!--							<q-avatar-->
			<!--								rounded-->
			<!--								size="md"-->
			<!--								class="q-mr-xs"-->
			<!--								v-for="provider in video.providers"-->
			<!--								:key="provider.id">-->
			<!--								<img-->
			<!--									:src="provider.logoKey"-->
			<!--									:alt="provider.id"-->
			<!--									class="border-grey-100" />-->
			<!--							</q-avatar>-->
			<!--						</q-badge>-->
			<!--					</div>-->
			<!--				</div>-->
			<!--				<template v-slot:loading>-->
			<!--					<div-->
			<!--						class="row q-mb-lg justify-center"-->
			<!--						v-if="videos.length < totalResult">-->
			<!--						<q-spinner-dots color="primary" size="40px" />-->
			<!--					</div>-->
			<!--				</template>-->
			<!--				<div-->
			<!--					class="q-mb-xl text-h6 text-bold"-->
			<!--					v-if="loadFail && videos.length === 0">-->
			<!--					{{ currentTab }}일 이내 종료 예정인 작품이 존재하지 않습니다.-->
			<!--				</div>-->
			<!--			</q-infinite-scroll>-->
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
	name: 'Discontinue',
	data() {
		return {
			currentTab: 7,
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
		window.reload;
		await this.$store.commit('videoDiscontinued/INIT_VIDEOS');
		await this.$store.dispatch('videoDiscontinued/loadVideoList', {
			day: 7,
			offset: 0,
		});
	},
	methods: {
		async videoOnLoad(index, done) {
			if (this.videos.length <= this.totalResult) {
				setTimeout(() => {
					this.$store.dispatch('videoDiscontinued/loadVideoList', {
						day: this.currentTab,
						offset: this.videos.length,
					});
					done();
				}, 1000);
			}
		},
		async daysButtonClick(idx) {
			this.days.forEach(i => {
				if (i !== idx) {
					i.isSelect = false;
				}
			});
			this.days[idx].isSelect = true;
			this.currentTab = this.days[idx].value;
			await this.$store.commit('videoDiscontinued/INIT_VIDEOS');
			await this.$store.dispatch('videoDiscontinued/loadVideoList', {
				day: this.currentTab,
				offset: 0,
			});
		},
		videoClick(videoId, category) {
			this.$router.push({ name: 'Details', params: { videoId, category } });
		},
	},
};
</script>

<style scoped>
#videos-wrapper {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-between;
}

.videos {
	width: 15%;
	height: 0;
	padding-bottom: 21%;
	margin: 0 0 24px 0;
	background: transparent;
	align-content: center;
	overflow-y: hidden;
}

.badge-frame {
	display: flex;
	flex-wrap: wrap;
}
</style>
