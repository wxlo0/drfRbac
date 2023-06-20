<script setup lang="ts">
import {useStore} from "vuex";

const store = useStore()
</script>

<template>
  <a-spin :spinning="store.getters.getIsSpinning">
    <router-view/>
  </a-spin>
</template>

<style>
#app, .ant-spin-container{
  width: 100%;
  height: 100vh;
  min-width: 1000px;
  min-height: 600px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.ant-message .anticon {
  top: -3px !important;
}

.ant-tabs-tab-remove {
  display: flex;
  align-items: center;
}
</style>
