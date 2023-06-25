<style scoped>

</style>

<template>
  <a-table
      :dataSource="tableData"
      :columns="columns"
      :scroll="{ x: 1200 }">
    <template v-slot:bodyCell="{ column, record}">
      <template v-if="column.key === 'permissions_status'">
        <a-badge :status="record.permissions_status ? 'success' : 'error'" />
        <span :class="record.permissions_status ? 'text-green-600' : 'text-red-600'">
            {{ record.permissions_status ? '正常' : '已禁用' }}
          </span>
      </template>
    </template>
  </a-table>
</template>

<script setup>

import {onMounted, ref} from "vue";
import {permissionsList} from "@/api/permissions";

const columns = [
  {
    title: '权限名称',
    dataIndex: 'permissions_name',
    key: 'role_name',
    width: 150
  },
  {
    title: '权限描述',
    dataIndex: 'permissions_desc',
    key: 'permissions_desc',
    width: 150
  },
  {
    title: '权限状态',
    dataIndex: 'permissions_status',
    key: 'permissions_status',
    width: 150
  }
]

function list() {
  permissionsList().then(res => {
    tableData.value = res.data
  }).catch(() => {})
}

onMounted(() => {
  list()
})
const tableData = ref([])
</script>

