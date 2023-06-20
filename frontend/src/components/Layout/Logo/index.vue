<style scoped lang="scss">
.logo {
  @apply flex overflow-hidden whitespace-nowrap items-center;
  height: 64px;
  line-height: 64px;
  display: flex;
  justify-content: center;
  img {
    height: 32px;
    margin-right: 8px;
  }
  .title {
    @apply mb-0 text-xl;
    color: white;
  }
}
</style>

<template>
  <div class="logo">
<!--    <img src="" alt="" />-->
    <h2 v-show="true" class="title">Rbac Admin</h2>
  </div>
</template>

<script setup>

</script>
