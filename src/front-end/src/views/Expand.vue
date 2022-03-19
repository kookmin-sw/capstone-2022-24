<template>
  <div class="expand">
    <div class="row q-ma-lg">
      <q-btn flat class="q-mt-lg q-mb-lg">최근 조회한 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">본 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">찜한 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">별점 준 작품</q-btn>
    </div>
    <div>
      <q-infinite-scroll :offset="250" @load="videoOnLoad">
        <div class="row justify-center col-gap-16 q-ma-lg">
          <q-card flat bordered
                  class="video-list-frame"
                  v-for="(video, index) in videos"
                  :key="index">
            <q-card-section class="q-pa-sm">
              <div class="video-poster">{{ video.value }}</div>
              <div class="text-left">영화 제목</div>
              <div class="row no-wrap items-center q-mt-sm">
                <div class="col text-right">
                  <q-rating size="18px" v-model="stars" :max="5" color="blue" />
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
      stars: 4,
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
  width: 170px;
  margin-bottom: 16px;
}
.video-poster {
  width: 100%;
  height: 210px;
  background: lightgrey;
}
</style>