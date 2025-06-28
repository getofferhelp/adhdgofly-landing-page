// src/components/DownloadModal.vue
<template>
  <Teleport to="body">
    <div v-if="show" 
         class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
         @click="handleBackdropClick">
      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 max-w-md w-full mx-4"
           @click.stop>
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-xl font-semibold dark:text-white">
            {{ $t('download.selectVersion') }}
          </h3>
          <button @click="close" 
                  class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div class="space-y-4">
          <!-- Apple Silicon 版本 -->
          <div class="download-option">
            <button @click="download('arm64')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700"
                    :class="{ 'ring-2 ring-nva-noun': detectedArch === 'arm64' }">
              <div class="text-left">
                <div class="font-semibold dark:text-white flex items-center">
                  {{ $t('download.macM1') }}
                  <span v-if="detectedArch === 'arm64'" 
                        class="ml-2 text-sm text-nva-noun dark:text-blue-400">
                    ({{ $t('download.recommended') }})
                  </span>
                </div>
                <div class="text-sm text-gray-500 dark:text-gray-400">
                  {{ $t('download.forAppleSilicon') }}
                </div>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </button>
          </div>

          <!-- Intel 版本 -->
          <div class="download-option">
            <button @click="download('x64')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700"
                    :class="{ 'ring-2 ring-nva-noun': detectedArch === 'x64' }">
              <div class="text-left">
                <div class="font-semibold dark:text-white flex items-center">
                  {{ $t('download.macIntel') }}
                  <span v-if="detectedArch === 'x64'" 
                        class="ml-2 text-sm text-nva-noun dark:text-blue-400">
                    ({{ $t('download.recommended') }})
                  </span>
                </div>
                <div class="text-sm text-gray-500 dark:text-gray-400">
                  {{ $t('download.forIntelMac') }}
                </div>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </button>
          </div>
        </div>

        <div class="mt-6 text-center">
          <a href="/download" 
             class="text-nva-noun dark:text-blue-400 hover:underline text-sm">
            {{ $t('download.viewMoreDetails') }}
          </a>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, onMounted } from 'vue'

const props = defineProps<{
  show: boolean
}>()

const emit = defineEmits<{
  (e: 'close'): void
  (e: 'download', arch: 'arm64' | 'x64'): void
}>()

const detectedArch = ref<'arm64' | 'x64' | null>(null)

// 检测系统架构
const detectArchitecture = () => {
  // 检测是否为 Mac 设备
  const isMac = navigator.platform.toLowerCase().includes('mac')
  
  if (!isMac) {
    return null
  }

  // 检测 Apple Silicon
  const isAppleSilicon = /Mac/.test(navigator.userAgent) && 
                        /Apple/.test(navigator.userAgent) &&
                        // macOS 11.0 Big Sur 或更高版本
                        /Mac OS X 10|Mac OS X 11|Mac OS X 12|Mac OS X 13|Mac OS X 14/.test(navigator.userAgent)

  return isAppleSilicon ? 'arm64' : 'x64'
}

onMounted(() => {
  detectedArch.value = detectArchitecture()
})

const close = () => {
  emit('close')
}

const handleBackdropClick = () => {
  close()
}

const download = (arch: 'arm64' | 'x64') => {
  emit('download', arch)
}
</script>

<style scoped>
.btn-download {
  transition: all 0.2s;
}

.btn-download:hover {
  transform: translateY(-2px);
}
</style>