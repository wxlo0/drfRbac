<style scoped>
.avatar {
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background-color: #535bf2;
  color: white;
  font-size: 16px;
  cursor: pointer;
}
</style>

<template>
  <div class="flex mr-5 items-center justify-between w-16">
    <a-dropdown placement="bottom">
      <div class="avatar">{{ store.getters.getRealName[0].toUpperCase() || 'M' }}</div>
      <template #overlay>
        <a-menu>
          <a-menu-item>
            <span>账号设置</span>
          </a-menu-item>
          <a-menu-item @click="logout">
            <span>退出登陆</span>
          </a-menu-item>
        </a-menu>
      </template>
    </a-dropdown>
    <SettingOutlined @click="showDrawer" />
  </div>
  <SettingDrawer v-model="visible" />
</template>

<script setup>
import { ref } from 'vue';
import { SettingOutlined } from '@ant-design/icons-vue';
import SettingDrawer from './SettingDrawer/index.vue';
import {useRouter} from "vue-router";
import {useStore} from "vuex";

const router = useRouter()
const store = useStore()

const visible = ref(false)

const showDrawer = () => {
  visible.value = true
}

function logout(){
  localStorage.clear()
  router.push('/login')
}

</script>
