<style>
.ant-tabs-nav {
  margin: 0 !important;
}
.ant-tabs-tab:not(.ant-tabs-tab-active) .ant-tabs-tab-remove {
  display: none;
  transition: opacity 0.3s ease;
}

.ant-tabs-tab:not(.ant-tabs-tab-active):hover .ant-tabs-tab-remove {
  display: inline-block;
}

.ant-tabs-tab:not(.ant-tabs-tab-active) .ant-tabs-tab-btn {
  transition: margin-right 0.3s ease;
}

.ant-tabs-tab:not(.ant-tabs-tab-active):hover .ant-tabs-tab-btn {
  margin-right: 5px;
}
</style>
<template>
  <a-tabs
      v-model:activeKey="activeKey"
      type="editable-card"
      :hide-add="true"
      @edit="onEdit"
      @tabClick="toPage"
  >
    <a-tab-pane
        v-for="pane in panes"
        :key="pane.key"
        :tab="pane.title"
        :closable="pane.closable"
    />
  </a-tabs>
</template>


<script lang="ts" setup>
import { ref, watch } from 'vue'
import { useStore } from 'vuex'
import {useRoute, useRouter} from "vue-router"
import { message } from 'ant-design-vue'

const store = useStore()
const panes = ref(store.getters.getTabs)
const activeKey = ref(store.getters.getActiveKey)
const router = useRouter()
const remove = (targetKey: string) => {
  let lastIndex = 0;
  panes.value.forEach((pane, i) => {
    if (pane.key === targetKey) {
      lastIndex = i - 1;
    }
  });

  // 判断目标元素是否是列表中的最后一个元素
  if (panes.value.length === 1) {
    // 使用 message 组件显示提示
    message.warn("这已经是最后一页了，无法再关闭了！")
    return;
  }

  panes.value = panes.value.filter(pane => pane.key !== targetKey)
  store.commit('changeTabs', panes.value)
  if (panes.value.length && activeKey.value === targetKey) {
    if (lastIndex >= 0) {
      activeKey.value = panes.value[lastIndex].key
      router.push(panes.value[lastIndex].key)
    } else {
      activeKey.value = panes.value[0].key
      router.push(panes.value[0].key)
    }
  }
}

const toPage = (key) => {
  panes.value.forEach((pane, i) => {
    if (pane.key === key) {
      router.push(pane.key)
    }
  })
}

const onEdit = (targetKey: string | MouseEvent, action: string) => {
  remove(targetKey as string);
}

const route = useRoute();
watch(route, (to, from) => {
  activeKey.value = store.getters.getActiveKey
});

</script>


