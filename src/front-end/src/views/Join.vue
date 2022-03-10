<template>
      <!-- 1단계 영역 -->
      <div class="step-one-frame row q-mt-xl q-mb-xl">
          <q-space class="col-2" />
          <div class="col-10">
              <div class="guide-text row text-left q-mb-md">
                  <div>1단계</div>
                  <div>신청할 OTT 서비스 선택</div>
              </div>
              <div class="ott-icons-frame row">
                  <div class="ott-icon">OTT</div>
                  <div class="ott-icon">OTT</div>
                  <div class="ott-icon">OTT</div>
                  <div class="ott-icon">OTT</div>
                  <div class="ott-icon">OTT</div>
              </div>
          </div>
          <q-space class="col-2" />
      </div>
      <!-- hr -->
      <q-separator color="blue" inset />
      <!-- 2단계 영역 -->
      <div class="step-two-frame row q-mt-xl q-mb-xl">
          <q-space class="col-2" />
          <div class="col-10">
              <div class="guide-text row text-left q-mb-md">
                  <div>2단계</div>
                  <div>모임장/모임원 선택</div>
              </div>
              <div class="explanation col text-left q-mb-lg">
                  <div class="leader-expl col q-mb-md">
                      <div>모임장이란?</div>
                      <div>모임장 설명</div>
                  </div>
                  <div class="member-expl col">
                      <div>모임원이란?</div>
                      <div>모임원 설명</div>
                  </div>
              </div>
              <div class="btn-frame row">
                  <q-btn>모임장</q-btn>
                  <q-btn>모임원</q-btn>
              </div>
          </div>
          <q-space class="col-2" />
      </div>
      <!-- hr -->
      <q-separator color="blue" inset />
      <!-- 3단계 영역 -->
      <div class="step-three-frame row q-mt-xl q-mb-xl">
          <q-space class="col-2" />
          <div class="col-10">
              <div class="guide-text row text-left q-mb-md">
                  <div>3단계</div>
                  <div>모임 신청 및 결제</div>
              </div>
              <div class="explanationn col text-left q-mb-lg">
                  <div>OTT 및 결제 비용 안내 ~</div>
              </div>
              <div class="btn-frame row">
                  <q-btn>신청하기</q-btn>
              </div>
          </div>
          <q-space class="col-2" />
      </div>
</template>

<style scoped>
.guide-text {
    column-gap: 4px;
}
.ott-icons-frame {
    column-gap: 16px;
}
.ott-icon {
    width: 60px;
    height: 60px;
}
</style>