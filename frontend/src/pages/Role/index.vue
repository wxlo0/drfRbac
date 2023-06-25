<style scoped>

</style>

<template>
  <div class="w-full flex flex-col">
    <a-button class="my-3 w-1/12" @click="addRole">添加角色</a-button>
    <a-table
        :dataSource="tableData"
        :columns="columns"
        :scroll="{ x: 1200 }">
      <template v-slot:bodyCell="{ column, record}">
        <template v-if="column.key === 'action'">
          <a-space>
            <a-button type="primary" @click="showDrawer(record)">修改角色</a-button>
          </a-space>
        </template>
      </template>
    </a-table>
  </div>
  <change-role v-model="visible" :roleInfo="roleInfo" @list="list"></change-role>
</template>

<script setup>

import {onMounted, reactive, ref, toRefs} from "vue";
import {roleList} from "@/api/user";
import {message} from "ant-design-vue";
import ChangeRole from "@/pages/Role/cps/changeRole.vue"

const visible = ref(false)
const roleInfo = ref({})
const showDrawer = (info) => {
  if(info.role_name === "超级管理员"){
    message.error("超级管理员不允许修改")
    return
  }
  roleInfo.value = info
  visible.value = true
}


const data = reactive({
  tableData: [],
  columns: [
    {
      title: '角色名称',
      dataIndex: 'role_name',
      key: 'role_name',
      width: 150
    },
    {
      title: '角色描述',
      dataIndex: 'role_desc',
      key: 'role_desc',
      width: 150
    },
    {
      title: '操作',
      dataIndex: 'action',
      key: 'action',
      width: 150
    }
  ]
})

function list(){
  roleList().then(res => {
    data.tableData = res.data
  })
}

function addRole(){
  message.warn('功能开发中')
}

onMounted(() => {
  list()
})


const {tableData, columns} = toRefs(data)
</script>

