<template>
  <a-drawer
      :visible="modelValue"
      class="custom-class"
      placement="right"
      :closable="false"
      @close="handleClose"
      title="全局设置"
  >
    <p>Some contents...</p>
    <p>Some contents...</p>
    <p>Some contents...</p>
  </a-drawer>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
});

const emits = defineEmits(['update:modelValue']);

const handleClose = () => {
  emits('update:modelValue', false);
}
</script>

