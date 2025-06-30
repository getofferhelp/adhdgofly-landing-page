<!-- ImageModal.vue -->
<template>
  <transition name="modal">
    <div v-if="show" 
         class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80"
         @click="$emit('close')">
      <img :src="imageSrc" 
           :alt="imageAlt"
           class="max-h-[90vh] max-w-[90vw] object-contain rounded-lg cursor-zoom-out"
           loading="lazy" />
    </div>
  </transition>
</template>

<script setup>
defineProps({
  show: {
    type: Boolean,
    required: true
  },
  imageSrc: {
    type: String,
    required: true
  },
  imageAlt: {
    type: String,
    default: ''
  }
})

defineEmits(['close'])
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style> 