// src/views/Download.vue
<template>
  <div class="min-h-screen bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 py-12">
      <h1 class="text-3xl font-bold mb-8 text-center dark:text-white">
        {{ $t('downloadPage.title') }}
      </h1>

      <div class="max-w-3xl mx-auto">
        <!-- macOS 下载选项 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">macOS</h2>
          <div class="space-y-4">
            <DownloadModal :show="showDownloadModal" @close="showDownloadModal = false" @download="handleDownload" />
            <button @click="showDownloadModal = true" 
                    class="w-full btn-primary p-4 text-center">
              {{ $t('downloadPage.downloadNow') }}
            </button>
          </div>
        </div>

        <!-- Windows 下载选项 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">Windows</h2>
          <div class="space-y-4">
            <a href="javascript:void(0)" 
               @click="downloadWindows"
               class="block w-full btn-primary p-4 text-center">
              {{ $t('downloadPage.downloadNow') }}
            </a>
          </div>
        </div>

        <!-- 系统要求 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.systemRequirements') }}
          </h2>
          
          <!-- macOS 系统要求 -->
          <h3 class="text-xl font-semibold mb-3 dark:text-white">macOS:</h3>
          <ul class="space-y-3 text-gray-600 dark:text-gray-300 mb-6">
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>macOS 11.0 (Big Sur) 或更高版本</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>4GB RAM 以上内存</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>500MB 可用磁盘空间</span>
            </li>
          </ul>

          <!-- Windows 系统要求 -->
          <h3 class="text-xl font-semibold mb-3 dark:text-white">Windows:</h3>
          <ul class="space-y-3 text-gray-600 dark:text-gray-300">
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>Windows 10 64位 或 Windows 11</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>4GB RAM 以上内存</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>500MB 可用磁盘空间</span>
            </li>
          </ul>
        </div>

        <!-- 安装指南 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.installationGuide') }}
          </h2>
          
          <!-- macOS 安装指南 -->
          <h3 class="text-xl font-semibold mb-3 dark:text-white">macOS:</h3>
          <ol class="space-y-4 text-gray-600 dark:text-gray-300 mb-6">
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">1</span>
              <p>下载对应您 Mac 芯片类型的安装包（.dmg 文件）</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">2</span>
              <p>双击下载的 .dmg 文件打开安装镜像</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">3</span>
              <p>将 ADHD GO FLY 应用程序拖拽到应用程序文件夹</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">4</span>
              <p>首次运行时，按住 Control 键点击应用图标并选择"打开"</p>
            </li>
          </ol>

          <!-- Windows 安装指南 -->
          <h3 class="text-xl font-semibold mb-3 dark:text-white">Windows:</h3>
          <ol class="space-y-4 text-gray-600 dark:text-gray-300">
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">1</span>
              <p>下载 Windows 安装包（.exe 文件）</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">2</span>
              <p>双击运行下载的安装程序</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">3</span>
              <p>按照安装向导的提示完成安装</p>
            </li>
            <li class="flex items-start">
              <span class="flex-shrink-0 w-6 h-6 rounded-full bg-nva-noun text-white flex items-center justify-center mr-3">4</span>
              <p>安装完成后，从开始菜单或桌面快捷方式启动应用</p>
            </li>
          </ol>
        </div>

        <!-- 版本历史 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.versionHistory') }}
          </h2>
          <div class="space-y-6">
            <div class="version-item">
              <h3 class="text-lg font-semibold text-nva-noun dark:text-blue-400">v1.0.0 (2024-03)</h3>
              <ul class="mt-2 space-y-2 text-gray-600 dark:text-gray-300">
                <li class="flex items-start">
                  <span class="text-nva-noun dark:text-blue-400 mr-2">•</span>
                  <span>首次发布</span>
                </li>
                <li class="flex items-start">
                  <span class="text-nva-noun dark:text-blue-400 mr-2">•</span>
                  <span>支持多语言实时分词</span>
                </li>
                <li class="flex items-start">
                  <span class="text-nva-noun dark:text-blue-400 mr-2">•</span>
                  <span>AI 辅助功能</span>
                </li>
                <li class="flex items-start">
                  <span class="text-nva-noun dark:text-blue-400 mr-2">•</span>
                  <span>专注模式</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import DownloadModal from '@/components/DownloadModal.vue'

const showDownloadModal = ref(false)

const handleDownload = (arch: 'arm64' | 'x64') => {
  const url = arch === 'arm64' 
    ? '/downloads/adhdgofly-arm64.dmg'
    : '/downloads/adhdgofly-x64.dmg'
  
  window.location.href = url
  showDownloadModal.value = false
}

const downloadWindows = () => {
  window.location.href = '/downloads/adhdgofly-win-x64.exe'
}
</script>

<style scoped>
.btn-primary {
  @apply bg-nva-noun text-white rounded-lg font-semibold hover:bg-opacity-90 transition-all duration-300;
}
</style>