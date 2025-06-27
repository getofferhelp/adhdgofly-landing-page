<template>
  <div class="app min-h-screen bg-page dark:bg-gray-900 transition-colors duration-300">
    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()
</script>

<style lang="scss">
.app {
  min-height: 100vh;
}
</style>
