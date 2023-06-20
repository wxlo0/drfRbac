<style scoped lang="scss">
</style>

<template>
  <div class="home w-full h-full text-4xl">
    home
  </div>
</template>

<script setup>
import {reactive, toRefs} from 'vue'
import { message } from 'ant-design-vue'
const data = reactive({
  input: ""
})


const {input} = {...toRefs(data)}
</script>

