<template>
  <div class="expand">
    <div class="row q-ma-lg">
      <q-btn flat class="q-mt-lg q-mb-lg">최근 조회한 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">본 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">찜한 작품</q-btn>
      <q-btn flat class="q-mt-lg q-mb-lg">별점 준 작품</q-btn>
    </div>
    <div class="row q-ma-lg">
      <q-card flat bordered>
        <q-card-section class="q-pa-sm">
          <div class="poster"></div>
          <div class="text-left">영화 제목</div>
          <div class="row no-wrap items-center">
          <div class="row text-right">
            <q-rating size="18px" v-model="stars" :max="5" color="blue" />
            <div>2022.03.14</div>
          </div>
          </div>
        </q-card-section>
      </q-card>
    </div>

    <div>
      <q-infinite-scroll :offset="250" @load="videoOnLoad">
        <div class="row q-ma-lg video-list-frame">
          <div
              class="video-poster"
              v-for="(video, index) in videos"
              :key="index">
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