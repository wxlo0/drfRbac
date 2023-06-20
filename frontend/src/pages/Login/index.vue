<style lang="scss">

</style>
<template>
  <div class="login w-full h-full flex flex-col justify-center items-center bg-[url('/src/assets/bg.svg')]">
    <div class="w-1/4 min-w-[300px] max-w-[400px]">
      <div class="text-2xl font-bold mb-7">Django Rbac Admin</div>
      <a-tabs v-model:activeKey="data.activeKey" centered>
        <a-tab-pane key="1" tab="账号密码登录" class="mt-5">
          <a-form
              :model="data.loginData">
            <a-form-item
                name="username"
                :rules="[{ required: true, message: '手机号不能为空' ,trigger: 'change' }]">
              <a-input v-model:value="data.loginData.username"
                       placeholder="请输入手机号"
                       size="large">
                <template #prefix>
                  <TabletOutlined class="site-form-item-icon" />
                </template>
              </a-input>
            </a-form-item>
            <a-form-item
                :rules="[{ required: true, message: '密码不能为空' }]"
                name="password">
              <a-input-password v-model:value="data.loginData.password"
                                placeholder="请输入密码"
                                size="large">
                <template #prefix>
                  <LockOutlined class="site-form-item-icon" />
                </template>
              </a-input-password>
            </a-form-item>
          </a-form>
        </a-tab-pane>
      </a-tabs>
      <div class="flex flex-col">
        <a-checkbox v-model:checked="data.loginData.remember">记住密码</a-checkbox>
        <a-button type="primary" class="mt-3" html-type="submit" @click="submit">
          登录
        </a-button>
      </div>
    </div>
    <div class="mt-10">
      <span>@2023 Clyde出品  </span>
      <a class="cursor-pointer" href="https://github.com/Tengxu666" target="_blank">Github For This Project</a>
    </div>
  </div>
</template>

<script setup>
import { LockOutlined, TabletOutlined } from '@ant-design/icons-vue';
import {reactive, computed, onMounted} from 'vue';
import { useRouter } from "vue-router"
import { message } from "ant-design-vue";
import { useStore } from "vuex";
import {userLogin} from "@/api/user";

const router = useRouter()
const store = useStore()

const data = reactive({
  loginData: {
    username: '',
    password: '',
    remember: true,
  },
  activeKey: "1",
  codeButton: "发送",
  codeTotalTime: 60,
  codeButtonDisabled: false
})


function setRemember() {
  if (data.loginData.remember) {
    localStorage.setItem('username', data.loginData.username)
    localStorage.setItem('password', data.loginData.password)
  } else {
    localStorage.setItem('username', '')
    localStorage.setItem('password', '')
  }
}

function submit(){
  let loginData = {
    username: data.loginData.username,
    password: data.loginData.password
  }
  userLogin(loginData).then(res => {
    store.commit("setUserInfo", res.data)
    router.push("/home")
    message.success("登录成功")
  })
}



onMounted(() => {
  data.loginData.password = localStorage.password
  data.loginData.username = localStorage.username
})

</script>
