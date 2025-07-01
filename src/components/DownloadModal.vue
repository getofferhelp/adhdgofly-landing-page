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

        <!-- 检测提示 -->
        <div v-if="detectedArch" class="mb-4 p-3 bg-blue-50 dark:bg-blue-900/30 rounded-lg text-sm">
          <p class="text-blue-700 dark:text-blue-300">
            {{ $t('download.detectedInfo', { 
              chip: detectedArch === 'arm64' ? 'Apple Silicon' : 'Intel' 
            }) }}
          </p>
        </div>

        <!-- 区域检测提示 -->
        <div v-if="isInChina !== null" class="mb-4 p-3 bg-green-50 dark:bg-green-900/30 rounded-lg text-sm">
          <p class="text-green-700 dark:text-green-300">
            {{ isInChina ? $t('download.downloadSources.china.recommended') : $t('download.downloadSources.github.recommended') }}
          </p>
        </div>
        <div v-else class="mb-4 p-3 bg-yellow-50 dark:bg-yellow-900/30 rounded-lg text-sm">
          <p class="text-yellow-700 dark:text-yellow-300">
            {{ $t('download.downloadSources.detection.error') }}
          </p>
        </div>

        <div class="space-y-4">
          <!-- Apple Silicon 版本 -->
          <div class="download-option space-y-3">
            <h4 class="font-semibold dark:text-white flex items-center">
              {{ $t('download.macM1') }}
              <span v-if="detectedArch === 'arm64'" 
                    class="ml-2 text-sm text-nva-noun dark:text-blue-400 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                {{ $t('download.recommended') }}
              </span>
            </h4>
            
            <!-- 国内下载源 -->
            <button @click="download('arm64', 'china')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg"
                    :class="[
                      isInChina && detectedArch === 'arm64'
                        ? 'border-nva-noun bg-nva-noun-bg dark:bg-blue-900/30 border-2' 
                        : 'border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                    ]">
              <div class="text-left">
                <div class="font-semibold dark:text-white">{{ $t('download.downloadSources.china.name') }}</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">{{ $t('download.downloadSources.china.description') }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </button>

            <!-- GitHub 下载源 -->
            <button @click="download('arm64', 'github')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg"
                    :class="[
                      !isInChina && detectedArch === 'arm64'
                        ? 'border-nva-noun bg-nva-noun-bg dark:bg-blue-900/30 border-2' 
                        : 'border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                    ]">
              <div class="text-left">
                <div class="font-semibold dark:text-white">{{ $t('download.downloadSources.github.name') }}</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">{{ $t('download.downloadSources.github.description') }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </button>
          </div>

          <!-- Intel 版本 -->
          <div class="download-option space-y-3">
            <h4 class="font-semibold dark:text-white flex items-center">
              {{ $t('download.macIntel') }}
              <span v-if="detectedArch === 'x64'" 
                    class="ml-2 text-sm text-nva-noun dark:text-blue-400 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                {{ $t('download.recommended') }}
              </span>
            </h4>
            
            <!-- 国内下载源 -->
            <button @click="download('x64', 'china')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg"
                    :class="[
                      isInChina && detectedArch === 'x64'
                        ? 'border-nva-noun bg-nva-noun-bg dark:bg-blue-900/30 border-2' 
                        : 'border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                    ]">
              <div class="text-left">
                <div class="font-semibold dark:text-white">{{ $t('download.downloadSources.china.name') }}</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">{{ $t('download.downloadSources.china.description') }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </button>

            <!-- GitHub 下载源 -->
            <button @click="download('x64', 'github')" 
                    class="w-full btn-download flex items-center justify-between p-4 border rounded-lg"
                    :class="[
                      !isInChina && detectedArch === 'x64'
                        ? 'border-nva-noun bg-nva-noun-bg dark:bg-blue-900/30 border-2' 
                        : 'border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                    ]">
              <div class="text-left">
                <div class="font-semibold dark:text-white">{{ $t('download.downloadSources.github.name') }}</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">{{ $t('download.downloadSources.github.description') }}</div>
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
  (e: 'download', arch: 'arm64' | 'x64', source: 'china' | 'github'): void
}>()

const detectedArch = ref<'arm64' | 'x64' | null>(null)
const isInChina = ref<boolean | null>(null)

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

// 检测用户地区
const detectRegion = async () => {
  try {
    const response = await fetch('https://ipapi.co/json/')
    const data = await response.json()
    isInChina.value = data.country === 'CN'
  } catch (error) {
    console.error('Failed to detect region:', error)
    isInChina.value = null
  }
}

onMounted(() => {
  detectedArch.value = detectArchitecture()
  detectRegion()
})

const close = () => {
  emit('close')
}

const handleBackdropClick = () => {
  close()
}

const download = (arch: 'arm64' | 'x64', source: 'china' | 'github') => {
  emit('download', arch, source)
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