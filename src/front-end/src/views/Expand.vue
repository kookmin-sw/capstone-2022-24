<template>
	<div class="expand q-ma-xl">
		<q-tabs
			dense
			class="text-grey"
			active-color="blue-4"
			indicator-color="blue-4"
			align="justify"
			v-model="currentTab">
			<q-tab name="recent" label="최근 조회한 작품" />
			<q-tab name="wish" label="찜한 작품" />
			<q-tab name="star" label="별점 준 작품" />
			<q-tab name="watch" label="본 작품" />
		</q-tabs>
		<q-tab-panels animated v-model="currentTab">
      <!-- 최근 조회한 작품 탭 -->
			<q-tab-panel name="recent">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
            <div class="row justify-center q-mt-lg q-mb-lg" style="column-gap: 10px">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster bg-grey-4">{{ video.value }}</div>
									<div class="video-title text-left text-weight-bold q-mt-sm">영화 제목</div>
									<div class="row no-wrap items-center">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
                        class="text-blue-100" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row justify-center">
								<q-spinner-dots class="text-blue-200" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
      <!-- 찜한 작품 탭 -->
			<q-tab-panel name="wish">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
						<div class="row justify-center q-mt-lg q-mb-lg" style="column-gap: 10px">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster bg-grey-4">{{ video.value }}</div>
									<div class="video-title text-left text-weight-bold q-mt-sm">영화 제목</div>
									<div class="row no-wrap items-center">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
												class="text-blue-100" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots class="text-blue-200" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
      <!-- 별점 준 작품 탭 -->
			<q-tab-panel name="star">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
            <div class="row justify-center q-mt-lg q-mb-lg" style="column-gap: 10px">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster bg-grey-4">{{ video.value }}</div>
									<div class="video-title text-left text-weight-bold q-mt-sm">영화 제목</div>
									<div class="row no-wrap items-center">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
                        class="text-blue-100" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots class="text-blue-200" size="40px" />
							</div>
						</template>
					</q-infinite-scroll>
				</div>
			</q-tab-panel>
      <!-- 본 작품 탭 -->
			<q-tab-panel name="watch">
				<div>
					<q-infinite-scroll :offset="250" @load="videoOnLoad">
            <div class="row justify-center q-mt-lg q-mb-lg" style="column-gap: 10px">
							<q-card
								flat
								bordered
								class="video-list-frame"
								v-for="(video, index) in videos"
								:key="index">
								<q-card-section class="q-pa-sm">
									<div class="video-poster bg-grey-4">{{ video.value }}</div>
									<div class="video-title text-left text-weight-bold q-mt-sm">영화 제목</div>
									<div class="row no-wrap items-center">
										<div class="col text-right">
											<q-rating
												size="18px"
												v-model="stars"
												:max="5"
                        class="text-blue-100" />
											<div>2022.03.14</div>
										</div>
									</div>
								</q-card-section>
							</q-card>
						</div>
						<template v-slot:loading>
							<div class="row q-mb-lg justify-center">
								<q-spinner-dots class="text-blue-200" size="40px" />
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
	height: 200px;
}
.video-title {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}
</style>
