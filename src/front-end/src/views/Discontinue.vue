<template>
	<div class="discontinue">
		<div class="row q-ma-lg">
			<q-btn flat class="q-mt-lg q-mb-lg"> 7일 이내 종료 예정작</q-btn>
			<q-btn flat class="q-mt-lg q-mb-lg"> 15일 이내 종료 예정작</q-btn>
			<q-btn flat class="q-mt-lg q-mb-lg"> 30일 이내 종료 예정작</q-btn>
		</div>
		<div>
			<q-infinite-scroll :offset="250" @load="videoOnLoad">
				<div class="row q-ma-lg video-list-frame">
					<div
						class="video-poster"
						v-for="(video, index) in videos"
						:key="index">
						<q-badge
							class="row reverse q-ma-none q-pa-sm float-right bg-transparent badge-frame">
							<q-avatar rounded color="grey" size="28px" class="q-ma-xs" />
							<q-avatar rounded color="grey" size="28px" class="q-ma-xs" />
						</q-badge>
						{{ video.value }}
					</div>
				</div>
				<template v-slot:loading>
					<div class="row q-mb-lg justify-center">
						<q-spinner-dots color="primary" size="40px" />
					</div>
				</template>
			</q-infinite-scroll>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Discontinue',
	data() {
		return {
			videos: [
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
				{},
			],
		};
	},
	methods: {
		videoOnLoad(index, done) {
			setTimeout(() => {
				this.videos.push({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
				done();
			}, 2000);
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
	background: lightgrey;
}

.badge-frame {
	display: flex;
	flex-wrap: wrap;
}
</style>
