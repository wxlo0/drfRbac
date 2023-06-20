<template>
  <div class="aside-menu">
    <a-menu
        v-model:openKeys="openKeys"
        v-model:selectedKeys="selectedKeys"
        mode="inline"
        theme="dark"
        :inline-collapsed="collapsed"
    >
      <template v-for="item in menuData">
        <a-menu-item v-if="!item.children" :key="item.key">
          <template #icon>
            <component :is="iconMap[item.icon]" />
          </template>
          <router-link :to="item.path">
            <span>{{ item.title }}</span>
          </router-link>
        </a-menu-item>
        <a-sub-menu v-else :key="item.key">
          <template #icon>
            <component :is="iconMap[item.icon]" />
          </template>
          <template #title>{{ item.title }}</template>
          <a-menu-item
              v-for="child in item.children"
              :key="child.key">
            <template #icon>
              <component :is="iconMap[child.icon]" />
            </template>
            <router-link :to="child.path">
              <span>{{ child.title }}</span>
            </router-link>
          </a-menu-item>
        </a-sub-menu>
      </template>
    </a-menu>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { computed } from 'vue'
import { useStore } from "vuex"

import {
  BankOutlined,
  TeamOutlined,
  MailOutlined,
  ClusterOutlined,
  RobotOutlined,
  TableOutlined,
  ContactsOutlined
} from '@ant-design/icons-vue';
import sidebarData from './sidebar.json';

const menuData = ref(sidebarData);
const store = useStore()

const collapsed = ref(store.getters.getMenuCollapsed)
const iconMap = {
  TeamOutlined,
  RobotOutlined,
  MailOutlined,
  ClusterOutlined,
  TableOutlined,
  ContactsOutlined,
  BankOutlined
};

const selectedKeys = ref(['1']);
const openKeys = ref([]);
const router = useRouter();

const pathToKeyMap = computed(() => {
  const map = {};
  menuData.value.forEach(item => {
    if (item.path) {
      map[item.path] = item.key;
    }
    if (item.children) {
      item.children.forEach(child => {
        if (child.path) {
          map[child.path] = child.key;
        }
      });
    }
  });
  return map;
});

const updateSelectedKeys = () => {
  const matched = router.currentRoute.value.matched;
  if (matched && matched.length > 0) {
    const path = matched[matched.length - 1].path;
    const key = pathToKeyMap.value[path];
    if (key) {
      selectedKeys.value = [key];
    }
  }
};

const updateOpenKeys = () => {
  const matched = router.currentRoute.value.matched;
  if (matched && matched.length > 0) {
    const path = matched[matched.length - 1].path;
    menuData.value.forEach(item => {
      if (item.children) {
        item.children.forEach(child => {
          if (child.path === path) {
            openKeys.value = [item.key];
          }
        });
      }
    });
  }
};

onMounted(() => {
  updateSelectedKeys();
  updateOpenKeys();
});

watch(
    () => router.currentRoute.value,
    () => {
      updateSelectedKeys();
      updateOpenKeys();
    },
);

</script>
