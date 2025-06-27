import { createI18n } from 'vue-i18n'
import zhLocale from '../locales/zh.json'
import enLocale from '../locales/en.json'
import frLocale from '../locales/fr.json'
import esLocale from '../locales/es.json'
import ruLocale from '../locales/ru.json'
import jaLocale from '../locales/ja.json'

const i18n = createI18n({
  legacy: false,
  locale: navigator.language.split('-')[0] || 'zh', // 根据浏览器语言自动选择
  fallbackLocale: 'zh',
  messages: {
    zh: zhLocale,
    en: enLocale,
    fr: frLocale,
    es: esLocale,
    ru: ruLocale,
    ja: jaLocale
  }
})

export default i18n
