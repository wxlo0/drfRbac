
<template>
  <div class="h-full flex items-center">
<!--    <div class="mr-3 h-full flex items-center cursor-pointer" @click="changeMenuCollapsed">-->
<!--      <MenuUnfoldOutlined v-if="store.getters.getMenuCollapsed" />-->
<!--      <MenuFoldOutlined v-else />-->
<!--    </div>-->
    <a-breadcrumb class="">
        <a-breadcrumb-item
            :to="item.path"
            v-for="(item, index) in route.matched"
            :key="index">
          <a :href="item.path">{{ item.meta.title }}</a>
        </a-breadcrumb-item>
    </a-breadcrumb>
  </div>
</template>

<script setup>
import {MenuUnfoldOutlined, } from '@ant-design/icons-vue'
import {useStore} from 'vuex'
import { useRoute } from 'vue-router'
const route = useRoute()
const store = useStore()

const changeMenuCollapsed = () => {
  store.commit('changeMenuCollapsed')
}
</script>
