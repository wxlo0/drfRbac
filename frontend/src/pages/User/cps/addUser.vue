<template>
  <a-modal title="修改角色"
           ref="formRef"
           v-model:visible="props.open"
           @ok="handleOk"
           @cancel="handleCancel"
           cancelText="取消"
           okText="确定">
    <a-checkbox-group v-model:value="checkedRoles" style="width: 100%">
      <a-checkbox v-for="role in roles" :key="role.id" :value="role.id">{{role.role_name}}</a-checkbox>
    </a-checkbox-group>

  </a-modal>
</template>

<script setup lang="ts">
import {onMounted, reactive, ref, watch} from 'vue';
import {roleList, roleChange} from "@/api/user";
import {message} from "ant-design-vue";

const formRef = ref()

const props = defineProps({
  open: {
    default: false,
    type: Boolean
  },
  userId: {
    default: null,
    type: Number
  },
  roles: {
    default: [],
    type: Array
  }
})
const emit = defineEmits(['close', 'list'])

const roles = ref();
const checkedRoles = ref();

const handleOk = () => {
  roleChange(props["userId"], {roles: checkedRoles.value}).then(res => {
    message.success('修改角色成功')
    emit('list')
  }).catch(() => {})
  emit('close')
};

const handleCancel = () => {
  emit('close')
}

watch(() => props["open"], (newValue, oldValue) => {
  if(newValue){
    roleList().then(res => {
      roles.value = res.data
      checkedRoles.value = props["roles"]
      console.log(checkedRoles.value)
    }).catch(() => {
      emit('close')
    })
  }
})
</script>
