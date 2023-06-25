<template>
  <a-drawer
      :visible="modelValue"
      class="custom-class"
      placement="right"
      :closable="false"
      @close="handleClose"
      title="修改角色"
  >
    <a-form layout="vertical" :model="formData">
      <a-form-item label="角色名称">
        <a-input v-model:value="formData.role_name" placeholder="input placeholder" />
      </a-form-item>
      <a-form-item label="角色简介">
        <a-textarea v-model:value="formData.role_desc" placeholder="input placeholder" />
      </a-form-item>
      <a-form-item label="权限列表">
        <a-checkbox-group v-model:value="formData.permissions">
          <a-row>
            <a-col :span="12" v-for="item in permissionList">
            <a-checkbox :key="item.id" :value="item.id">{{item.permissions_desc}}</a-checkbox>
            </a-col>
          </a-row>
        </a-checkbox-group>
      </a-form-item>
      <a-form-item>
        <a-button type="primary" @click="submit">提交</a-button>
      </a-form-item>
    </a-form>
  </a-drawer>
</template>

<script setup>
import {ref, watch} from "vue";
import {rolePermissionsList, roleUpdate} from "@/api/role";
import {message} from "ant-design-vue";
import {permissionsList} from "@/api/permissions";

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
  roleInfo: {
    type: Object,
    default: {
      id: null,
      role_name: '',
      role_desc: ''
    },
    required: true
  }
})

const emits = defineEmits(['update:modelValue', 'list']);
const formData = ref()

const permissionList = ref([])

const handleClose = () => {
  emits('update:modelValue', false);
}

function submit(){
  roleUpdate(formData.value.id, formData.value).then(res => {
    message.success('修改角色成功')
    emits('list')
  }).catch(() => {})
  emits('update:modelValue', false);
}

watch(() => props["roleInfo"], (newValue, oldValue) => {
  if(newValue){
    formData.value = props["roleInfo"]
    rolePermissionsList(formData.value.id).then(res => {
      formData.value.permissions = res.data
    }).catch(() => {
      emits('update:modelValue', false);
    })
    permissionsList().then(res => {
      permissionList.value = res.data
    }).catch(() => {})
  }
})
</script>

