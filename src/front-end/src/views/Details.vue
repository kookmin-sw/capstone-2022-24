<template>
	<!-- 작품 정보 영역 -->
	<div class="q-ma-xl details">
		<!--		<q-btn flat class="row q-mb-sm justify-start">&lt; 뒤로가기</q-btn>-->
		<div class="row col-gap-12" v-if="videoDetails">
			<!-- 포스터 -->
			<div class="col-3 q-ma-sm bg-grey-4" style="width: 242px; height: 342px">
				<img
					:src="videoDetails.posterUrl"
					:alt="videoDetails.title"
					style="width: 100%; object-fit: cover" />
			</div>
			<div class="col text-left">
				<!-- 작품 제목 -->
				<div class="q-ma-sm">
					<div>
						<span class="text-h6 text-weight-bold">
							{{ videoDetails.title }}
						</span>
						<span
							class="text-h6 text-weight-bold"
							v-if="this.$route.params.category === 'TV'">
							{{ season.name }}
						</span>
					</div>
					<div class="q-mb-md text-bold text-grey">
						{{ videoDetails.titleEnglish }}
					</div>
				</div>
				<!-- 작품 상세 정보 -->
				<div class="row q-ma-sm q-mb-lg" v-if="videoDetails">
					<div class="q-mr-sm q-mt-auto q-mb-auto">
						{{ videoDetails.releaseYear }} |
					</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">
						{{ videoDetails.productionCountries.join(', ') }} |
					</div>
					<div class="q-mr-sm q-mt-auto q-mb-auto">
						{{ videoDetails.genres.join(', ') }}
					</div>
					<!--									<div class="q-mr-sm q-mt-auto q-mb-auto">상영시간</div>-->
				</div>
				<!-- 작품 상세 정보: 외부 평점 -->
				<!--				<div class="row q-ma-sm q-mb-md">-->
				<!--					<q-avatar rounded color="grey-4" size="25px" class="q-mr-xs" />-->
				<!--					<div class="q-mr-md q-mt-auto q-mb-auto">IMDB 평점</div>-->
				<!--					<div class="q-mr-sm q-mt-auto q-mb-auto">자체 평점</div>-->
				<!--					<div class="q-mr-sm q-mt-auto q-mb-auto">자체 찜 수</div>-->
				<!--					<div class="q-mt-auto q-mb-auto">자체 본 사람 수</div>-->
				<!--				</div>-->
				<div class="row q-mb-md">
					<q-select
						v-if="this.$route.params.category === 'TV'"
						dense
						outlined
						color="blue-4"
						class="col q-ma-sm"
						v-model="season"
						:options="videoDetails.seasons"
						:option-value="'number'"
						:option-label="'name'">
					</q-select>

					<q-btn
						v-if="this.wished !== null && this.wished"
						flat
						@click="cancleWish"
						class="col q-ma-sm bg-blue-100 text-white text-bold">
						찜 취소
					</q-btn>
					<q-btn
						v-else-if="this.wished !== null && !this.wished"
						outline
						@click="addWish"
						class="col q-ma-sm text-blue-200">
						찜 하기
					</q-btn>
					<!--					<q-btn outline class="col q-ma-sm text-blue-200">안 본 영화</q-btn>-->
					<!--					<q-btn outline class="col q-ma-sm text-blue-200">별점 주기</q-btn>-->
				</div>
				<!-- 작품을 서비스하는 ott 목록-->
				<q-card flat bordered class="q-ma-sm">
					<q-tabs dense class="text-blue-100" align="justify" v-model="tab">
						<q-tab name="all" label="전체" />
					</q-tabs>
					<q-tab-panels v-model="tab">
						<q-tab-panel name="all">
							<div class="ott-icons-frame row">
								<a
									:href="provider.link"
									target="_blank"
									v-for="provider in videoDetails.providers"
									:key="provider">
									<q-avatar rounded color="grey-4" size="40px">
										<img :src="provider.logoUrl" :alt="provider.name" />
									</q-avatar>
								</a>
							</div>
						</q-tab-panel>
					</q-tab-panels>
				</q-card>
			</div>
		</div>
	</div>
	<!-- hr -->
	<q-separator color="blue-1" size="2px" inset />
	<q-separator color="blue-4" inset />
	<!-- 작품 줄거리 영역 -->
	<div class="q-ma-xl text-left">
		<div class="q-mb-md text-h6 text-weight-bold">줄거리</div>
		<div v-if="!videoDetails.overview">등록된 줄거리가 없습니다.</div>
		<div v-else>{{ videoDetails.overview }}</div>
	</div>
	<!-- hr -->
	<!--	<q-separator color="blue-1" size="2px" inset />-->
	<!--	<q-separator color="blue-4" inset />-->
	<!-- 제작진 정보 영역 -->
	<!--	<div class="col q-ma-xl text-left">-->
	<!--		<div class="q-mb-md text-h6 text-weight-bold">제작진</div>-->
	<!--		<div class="row col-gap-12">-->
	<!--			<div v-for="staffMember in staff" :key="staffMember.id">-->
	<!--				{{ staffMember }}-->
	<!--				<q-avatar rounded class="border-blue-100 radius-4" size="73px">-->
	<!--					<div class="text-center">-->
	<!--						<div class="text-body2 text-grey-100">역할</div>-->
	<!--						<div class="text-h6 text-grey-100">김땡땡</div>-->
	<!--					</div>-->
	<!--				</q-avatar>-->
	<!--			</div>-->
	<!--			<q-btn flat>모두 보기</q-btn>-->
	<!--		</div>-->
	<!--	</div>-->
	<!-- hr -->
	<!--	<q-separator color="blue-1" size="2px" inset />-->
	<!--	<q-separator color="blue-4" inset />-->
	<!-- 관련 영상물 영역 -->
	<!--	<div class="q-ma-xl text-left">-->
	<!--		<div class="q-mb-md text-h6 text-weight-bold">관련 영상</div>-->
	<!--		<div>영상 임베드 영역, 링크 -> 임베드</div>-->
	<!--	</div>-->
</template>

<script>
import { mapState } from 'vuex';

export default {
	data() {
		return {
			videoId: null,
			category: null,
			season: '시즌 1',
			tab: 'all',
			staff: ['', '', '', '', ''],
			countryList: {
				KR: '한국',
				US: '미국',
			},
			releaseYear: '',
			productionCountry: '',
			genre: '',
			details: null,
			wished: null,
		};
	},
	watch: {
		season: function () {
			this.$store.dispatch('videoDetails/loadVideoSeason', {
				videoId: this.videoId,
				category: this.category,
				season: this.season.number,
			});
		},
	},
	computed: {
		...mapState('videoDetails', ['videoDetails']),
	},
	async created() {
		await this.loadDetails();
	},
	methods: {
		async loadDetails() {
			const videoId = this.$route.params.videoId;
			let category;
			this.$route.params.category === 'MV'
				? (category = 'movie')
				: (category = 'tv');
			await this.$store.dispatch('videoDetails/loadVideoDetails', {
				videoId,
				category,
			});
			this.videoId = videoId;
			this.category = category;
			this.wished = this.videoDetails.personal.wished;
		},
		addWish() {
			this.$store
				.dispatch('videoInteractions/addWish', this.videoId)
				.then(() => {
					this.wished = true;
				});
		},
		cancleWish() {
			this.$store
				.dispatch('videoInteractions/cancleWish', this.videoId)
				.then(() => {
					this.wished = false;
				});
		},
	},
};
</script>

<style scoped>
.ott-icons-frame {
	column-gap: 16px;
	row-gap: 24px;
}
</style>
