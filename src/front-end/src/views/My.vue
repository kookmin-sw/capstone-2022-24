<template>
  <!-- 프로필 영역 -->
  <div class="col q-mt-xl q-mb-xl q-ml-lg q-mr-lg profile-frame">
    <div class="row profile-info">
      <div class="profile-img">프로필 사진</div>
      <div class="col text-left profile-text ">
        <div class="q-mb-sm">사용자 닉네임</div>
        <div>010-1234-5678</div>
        <div class="row">
          <!-- 로고는 가입시 이용한 카카오/네이버 API 아이콘 -->
          <div class="api-logo q-mr-xs">로고</div>
          <div>naver_email@naver.com</div>
        </div>
      </div>
    </div>
  </div>
  <!-- hr -->
  <q-separator color="blue" inset />
</template>

<style scoped>
.profile-img {
  width: 73px;
  height: 73px;
  background-color: #83BBFB;
}
.profile-info {
  column-gap: 24px;
}
.profile-text {
  row-gap: 12px;
}
</style>