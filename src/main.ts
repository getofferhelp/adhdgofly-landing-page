import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'
import App from './App.vue'
import router from './router'

import zhLocale from '@/locales/zh.json'
import enLocale from '@/locales/en.json'
import esLocale from '@/locales/es.json'
import frLocale from '@/locales/fr.json'
import ruLocale from '@/locales/ru.json'
import jaLocale from '@/locales/ja.json'

import './assets/main.css'

// 创建 i18n 实例
const i18n = createI18n({
  legacy: false,
  locale: navigator.language.split('-')[0] || 'zh', // 根据浏览器语言自动选择
  fallbackLocale: 'en',
  messages: {
    zh: zhLocale,
    en: enLocale,
    es: esLocale,
    fr: frLocale,
    ru: ruLocale,
    ja: jaLocale
  }
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')
