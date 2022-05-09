<template>
	<div class="expand q-ma-xl">
		<q-tabs
			dense
			class="text-grey"
			active-color="blue"
			indicator-color="blue"
			align="justify"
			v-model="currentTab">
			<q-tab name="recent" label="최근 조회한 작품" />
			<q-tab name="wish" label="찜한 작품" />
			<q-tab name="star" label="별점 준 작품" />
			<q-tab name="watch" label="본 작품" />
		</q-tabs>
		<q-tab-panels animated v-model="currentTab">
			<q-tab-panel name="recent">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
						<div class="row justify-center">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section>
									<div class="video-poster">{{ video.value }}</div>
									<div class="video-title text-left">영화 제목</div>
									<div class="row no-wrap items-center">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
												color="blue" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row justify-center">
								<q-spinner-dots color="primary" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
			<q-tab-panel name="wish">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
						<div class="row justify-center col-gap-16 q-ma-lg">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster">{{ video.value }}</div>
									<div class="video-title text-left">영화 제목</div>
									<div class="row no-wrap items-center q-mt-sm">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
												color="blue" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots color="primary" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
			<q-tab-panel name="watch">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
						<div class="row justify-center col-gap-16 q-ma-lg">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster">{{ video.value }}</div>
									<div class="video-title text-left">영화 제목</div>
									<div class="row no-wrap items-center q-mt-sm">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
												color="blue" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots color="primary" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
			<q-tab-panel name="star">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
						<div class="row justify-center col-gap-16 q-ma-lg">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster">{{ video.value }}</div>
									<div class="video-title text-left">영화 제목</div>
									<div class="row no-wrap items-center q-mt-sm">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
												color="blue" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots color="primary" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
		</q-tab-panels>
	</div>
</template>

<script>
export default {
	name: 'Discontinue',
	data() {
		return {
			currentTab: 'recent',
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
			stars: 4,
		};
	},
	methods: {
		// videoOnLoad(index, done) {
		// 	setTimeout(() => {
		// 		this.videos.push({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
		// 		done();
		// 	}, 2000);
		// },
	},
};
</script>

<style scoped>
.video-list-frame {
	width: 170px;
	margin-bottom: 16px;
}
.video-poster {
	width: 100%;
	height: 210px;
	background: lightgrey;
}
.video-title {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}
</style>
