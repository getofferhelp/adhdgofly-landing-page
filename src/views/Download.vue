// src/views/Download.vue
<template>
  <div class="min-h-screen bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 py-12">
      <h1 class="text-3xl font-bold mb-8 text-center dark:text-white">
        {{ $t('downloadPage.title') }}
      </h1>

      <!-- 版本选择区域 -->
      <div class="max-w-3xl mx-auto">
        <!-- macOS 下载选项 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">macOS</h2>
          <div class="space-y-4">
            <!-- Apple Silicon 版本 -->
            <div class="download-option">
              <!-- 与 Modal 中相似的下载按钮 -->
            </div>
            <!-- Intel 版本 -->
            <div class="download-option">
              <!-- 与 Modal 中相似的下载按钮 -->
            </div>
          </div>
        </div>

        <!-- 系统要求 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.systemRequirements') }}
          </h2>
          <!-- 系统要求内容 -->
        </div>

        <!-- 安装指南 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.installationGuide') }}
          </h2>
          <!-- 安装指南内容 -->
        </div>

        <!-- 版本历史 -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg">
          <h2 class="text-2xl font-semibold mb-4 dark:text-white">
            {{ $t('downloadPage.versionHistory') }}
          </h2>
          <!-- 版本历史内容 -->
        </div>
      </div>
    </div>
  </div>
</template>