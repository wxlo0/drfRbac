<style scoped lang="scss">

</style>

<template>
  <div class="flex flex-col">
    <a-table
        :dataSource="tableData"
        :columns="columns"
        :scroll="{ x: 1200 }"
        :pagination="{
        current: currentPage,
        pageSize: pageSize,
        total: totalData}">
      <template v-slot:bodyCell="{ column, record}">
        <template v-if="column.key === 'roles'">
          <span v-for="(role, index) in record.roles" :key="index">
            <a-tag color="blue">{{ role.role_name }}</a-tag>
          </span>
        </template>
        <template v-else-if="column.key === 'is_active'">
          <a-badge :status="record.is_active ? 'success' : 'error'" />
          <span :class="record.is_active ? 'text-green-600' : 'text-red-600'">
            {{ record.is_active ? '正常' : '已禁用' }}
          </span>
        </template>
        <template v-else-if="column.key === 'action'">
          <a-space>
            <a-button type="primary" @click="updateUserRole(record.id, record.roles)">修改角色</a-button>
          </a-space>
        </template>
      </template>
    </a-table>
    <add-user :open="changeRoleOpen" :userId="changeUserId" :roles="changeUserRoles"
              @close="changeRoleOpen = false" @list="list"/>
  </div>
</template>


<script setup lang="ts">
import {reactive, toRefs, ref, onMounted} from "vue";
import AddUser from "@/pages/User/cps/addUser.vue";
import {userList} from "@/api/user";

const data = reactive({
  changeUserId: null,
  changeUserRoles: [],
  changeRoleOpen: false,
  currentPage: 1,
  pageSize: 10,
  totalData: 10,
  columns: [
    {
      title: '用户姓名',
      dataIndex: 'real_name',
      key: 'real_name',
      width: 150
    },
    {
      title: '登录账号',
      dataIndex: 'username',
      key: 'username',
      width: 150
    },
    {
      title: '用户角色',
      dataIndex: 'roles',
      key: 'roles',
      width: 200
    },
    {
      title: '最后操作时间',
      dataIndex: 'updated_at',
      key: 'updated_at',
      width: 150
    },
    {
      title: '用户状态',
      dataIndex: 'is_active',
      key: 'is_active',
      width: 100
    },
    {
      title: '操作',
      dataIndex: 'action',
      key: 'action',
      fixed: 'right',
      width: 200,
    },
  ],
})

const tableData = ref([])

const list = () => {
  userList().then(res => {
    tableData.value = res.data
  })
}

const updateUserRole = (userId, userRoles) => {
  let roles = []
  changeUserId.value = userId
  userRoles.forEach(role => {
    roles.push(role.id)
  })
  changeUserRoles.value = roles
  changeRoleOpen.value = true
}

onMounted(() => {
  list()
})

const {changeUserRoles, changeUserId, changeRoleOpen, currentPage, pageSize, totalData, columns} = toRefs(data)
</script>

