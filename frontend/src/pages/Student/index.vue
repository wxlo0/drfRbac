<template>
 <div class="flex flex-col w-1/12">
   <div class="text-2xl font-bold">权限测试</div>
   <a-button type="primary" class="mt-5" @click="getList">学生列表</a-button>
   <a-button type="primary" ghost class="mt-5" @click="getOne">单个学生</a-button>
   <a-button type="dashed" danger class="mt-5" @click="addOne">添加学生</a-button>
   <a-button danger class="mt-5" @click="updateOne">修改学生</a-button>
   <a-button type="primary" danger class="mt-5" @click="deleteOne">删除学生</a-button>
 </div>
</template>

<script setup>

import {createStudentOne, getStudentList, getStudentOne, updateStudentOne, deleteStudentOne} from "@/api/student";
import {message} from "ant-design-vue";

const getList = () => {
  getStudentList().then(res => {
    message.success('获取学生列表成功')
  })
}

const getOne = () => {
  getStudentOne().then(res => {
    message.success('获取单个学生成功')
  })
}

const addOne = () => {
  createStudentOne().then(res => {
    message.success('添加学生成功')
  })
}

const updateOne = () => {
  updateStudentOne().then(res => {
    message.success('修改学生成功')
  })
}

const deleteOne = () => {
  deleteStudentOne().then(res => {
    message.success('删除学生成功')
  })
}

</script>

<style scoped>

</style>
