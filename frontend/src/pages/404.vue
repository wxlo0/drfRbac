<template>
  <div class="flex flex-col items-center">
    <img src="/src/assets/404.png" class="w-1/4">
    <div class="w-1/2 flex flex-col items-center">
      <router-link to="/home" class="w-24 py-2 text-white bg-blue-500 rounded">返回首页</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
}
</script>
