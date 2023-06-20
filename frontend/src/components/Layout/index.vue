<style scoped lang="scss">
.layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

</style>

<template>
  <a-layout class="layout">
    <a-layout-sider>
      <Logo/>
      <AsideMenu/>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background-color: white; padding: 12px; border-bottom: 1px solid #e5e7eb">
        <Header/>
      </a-layout-header>
      <div class="w-full bg-white px-2 pt-2">
        <Tabs/>
      </div>
      <a-layout-content class="px-2 pt-2">
        <router-view v-slot="{ Component }">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup>
import Logo from "@/components/Layout/Logo/index.vue"
import AsideMenu from "@/components/Layout/AsideMenu/index.vue"
import Header from "@/components/Layout/Header/index.vue"
import Tabs from "@/components/Layout/Tabs/index.vue"

</script>
