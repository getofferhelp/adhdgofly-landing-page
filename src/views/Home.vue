<template>
  <main class="home min-h-screen bg-page dark:bg-gray-900 transition-colors duration-300">
    <!-- Loading State -->
    <div v-if="isLoading" class="fixed inset-0 bg-white dark:bg-gray-900 z-50 flex items-center justify-center">
      <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-nva-noun"></div>
    </div>

    <!-- Top Bar -->
    <div class="w-full bg-white/95 dark:bg-gray-900/95 backdrop-blur-sm sticky top-0 z-40">
      <div class="container mx-auto px-4 py-2 md:py-3">
        <div class="flex justify-between items-center">
          <div class="flex items-center">
            <img src="/images/logo.svg" alt="ADHD GO FLY - 多语言阅读编辑工具" class="w-8 md:w-12 h-auto"/>
          </div>
          <div class="flex items-center space-x-3">
            <button @click="toggleDark"
                    class="p-1.5 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors focus:outline-none focus:ring-2 focus:ring-nva-noun"
                    :aria-label="isDark ? '切换到浅色模式' : '切换到深色模式'">
              <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
              </svg>
            </button>
            <select v-model="$i18n.locale"
                    class="bg-transparent hover:bg-gray-100 dark:hover:bg-gray-800 dark:text-white rounded-lg px-2 py-1 text-xs border border-gray-200 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-nva-noun"
                    @change="updateMetaTags">
              <option value="zh">中文</option>
              <option value="en">English</option>
              <option value="fr">Français</option>
              <option value="es">Español</option>
              <option value="ru">Русский</option>
              <option value="ja">日本語</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <!-- Hero Section -->
    <section class="hero relative" id="hero">
      <div class="absolute inset-0">
        <img :src="heroBackgroundSrc"
             :alt="isDark ? 'ADHD GO FLY 工具界面展示 - 深色模式' : 'ADHD GO FLY 工具界面展示 - 浅色模式'"
             class="w-full h-full object-cover"
             fetchpriority="high" />
        <div class="absolute inset-0 bg-white/20 dark:bg-black/40"></div>
      </div>

      <!-- Content -->
      <div class="relative min-h-[80vh] flex items-center">
        <div class="container mx-auto px-4 py-16 md:py-24">
          <div class="max-w-4xl mx-auto">
            <h1 class="text-center mb-4 md:mb-6">
              <div class="text-3xl md:text-5xl font-bold mb-2">
                <span class="text-nva-noun dark:text-blue-400">{{ $t('hero.titleADHD') }}</span>
                <span class="text-nva-verb dark:text-red-400">{{ $t('hero.titleGoFly') }}</span>
              </div>
              <div class="text-2xl md:text-4xl font-bold text-nva-adj dark:text-green-400">{{ $t('hero.titleLine2') }}</div>
            </h1>
            <p class="text-lg md:text-xl text-center text-gray-600 dark:text-gray-300 mb-8 md:mb-12">{{ $t('hero.subtitle') }}</p>

            <div class="flex flex-col md:flex-row justify-center items-center gap-4 md:gap-6">
              <a href="https://adhdgofly.online"
                 target="_blank"
                 rel="noopener noreferrer"
                 class="btn-primary inline-block w-auto focus:outline-none focus:ring-4 focus:ring-nva-noun/50"
                 @click="trackEvent('hero_web_try')">
                {{ $t('hero.tryWeb') }}
              </a>
              <a href="#download"
                 class="btn-secondary inline-block w-auto focus:outline-none focus:ring-4 focus:ring-nva-noun/50"
                 @click="scrollToSection('download')">
                {{ $t('hero.download') }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Screenshots Showcase -->
    <div class="relative z-10 container mx-auto px-4 py-4 md:py-12 bg-white/80 dark:bg-gray-800/80">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8">
        <!-- Screenshot 1: Editor Mode -->
        <div class="screenshot-card" tabindex="0">
          <div class="aspect-w-16 aspect-h-9 bg-gray-100 rounded-lg overflow-hidden">
            <img src="/images/screenshots/editor.png"
                 alt="ADHD GO FLY 智能编辑器界面 - 支持实时分词和多语言编辑"
                 class="w-full h-full object-cover"
                 loading="lazy" />
          </div>
          <h3 class="mt-4 text-xl font-semibold text-nva-noun">{{ $t('features.editor.title') }}</h3>
          <p class="mt-2 text-gray-600 dark:text-gray-200">{{ $t('features.editor.desc') }}</p>
        </div>

        <!-- Screenshot 2: AI Text Processing -->
        <div class="screenshot-card" tabindex="0">
          <div class="aspect-w-16 aspect-h-9 bg-gray-100 rounded-lg overflow-hidden">
            <img src="/images/screenshots/ai.png"
                 alt="ADHD GO FLY AI文本处理功能展示 - 智能分析和翻译功能"
                 class="w-full h-full object-cover"
                 loading="lazy" />
          </div>
          <h3 class="mt-4 text-xl font-semibold text-nva-verb">{{ $t('features.ai.title') }}</h3>
          <p class="mt-2 text-gray-600 dark:text-gray-200">{{ $t('features.ai.desc') }}</p>
        </div>

        <!-- Screenshot 3: Focus Features -->
        <div class="screenshot-card" tabindex="0">
          <div class="aspect-w-16 aspect-h-9 bg-gray-100 rounded-lg overflow-hidden">
            <img src="/images/screenshots/focus.png"
                 alt="ADHD GO FLY 专注模式界面 - 减少干扰的阅读环境"
                 class="w-full h-full object-cover"
                 loading="lazy" />
          </div>
          <h3 class="mt-4 text-xl font-semibold text-nva-adj">{{ $t('features.focus.title') }}</h3>
          <p class="mt-2 text-gray-600 dark:text-gray-200">{{ $t('features.focus.desc') }}</p>
        </div>
      </div>
    </div>

    <!-- Features Section -->
    <section class="features py-4 md:py-12 bg-white/80 dark:bg-gray-800/80" id="features">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl md:text-3xl font-bold text-center mb-4 md:mb-12 text-nva-verb">{{ $t('features.title') }}</h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-8">
          <div v-for="(feature, index) in features" :key="index"
               class="feature-card transform hover:scale-105 transition-transform focus-within:ring-4 focus-within:ring-nva-noun/50"
               tabindex="0">
            <div class="icon-wrapper mb-4 flex justify-center">
              <component :is="feature.icon" class="w-12 h-12"
                        :class="getIconColor(index)" />
            </div>
            <h3 class="text-xl font-semibold mb-3 text-center" :class="getTextColor(index)">
              {{ $t(feature.titleKey) }}
            </h3>
            <p class="text-gray-600 dark:text-gray-200 text-center">{{ $t(feature.descKey) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials py-4 md:py-12 bg-white/80 dark:bg-gray-800/80" id="testimonials">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl md:text-3xl font-bold text-center mb-4 md:mb-12 text-nva-noun">{{ $t('testimonials.title') }}</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8">
          <div v-for="(testimonial, index) in testimonials" :key="index"
               class="testimonial-card focus-within:ring-4 focus-within:ring-nva-noun/50"
               tabindex="0">
            <div class="mb-4">
              <div class="flex items-center mb-3">
                <div class="w-10 h-10 rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
                  <span class="text-lg font-semibold">{{ testimonial.initial }}</span>
                </div>
                <div class="ml-3">
                  <h4 class="font-semibold text-gray-900 dark:text-white">
                    <template v-if="testimonial.isXiaohongshu">
                      <a :href="testimonial.link" target="_blank" rel="noopener noreferrer"
                         class="hover:text-nva-noun transition-colors flex items-center focus:outline-none focus:ring-2 focus:ring-nva-noun/50 rounded">
                        {{ testimonial.name }}
                        <svg class="w-4 h-4 ml-1" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M10 6H5V19H18V14M14 5H19M19 5V10M19 5L9 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </a>
                    </template>
                    <template v-else>
                      {{ testimonial.name }}
                    </template>
                  </h4>
                  <p class="text-sm text-gray-600 dark:text-gray-300">{{ testimonial.title }}</p>
                </div>
              </div>
              <p class="text-gray-700 dark:text-gray-300 mb-3 testimonial-content" v-html="$t(testimonial.contentKey)"></p>
              <div v-if="testimonial.hasImage" class="mt-4">
                <img :src="testimonial.imagePath" :alt="testimonial.name + '的评价截图'"
                     class="rounded-lg shadow-md w-full h-auto" loading="lazy" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Download Section -->
    <section id="download" class="download py-4 md:py-12 bg-gray-50 dark:bg-gray-800/80">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl md:text-3xl font-bold text-center mb-4 md:mb-12 text-nva-adj">{{ $t('download.title') }}</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-8 max-w-4xl mx-auto">
          <div class="download-card">
            <h3 class="text-xl font-semibold mb-4 dark:text-white">macOS</h3>
            <button @click="showDownloadModal = true" 
                    class="btn-download focus:outline-none focus:ring-4 focus:ring-nva-adj/50">
              {{ $t('download.mac') }}
            </button>
          </div>

          <div class="download-card transform hover:scale-105 transition-transform focus-within:ring-4 focus-within:ring-nva-adj/50" tabindex="0">
            <h3 class="text-xl font-semibold mb-4 dark:text-white">Windows</h3>
            <a href="#" target="_blank" rel="noopener noreferrer"
               class="btn-download focus:outline-none focus:ring-4 focus:ring-nva-adj/50"
               @click="trackEvent('download_windows')">
              {{ $t('download.windows') }}
            </a>
            <div class="install-tips mt-4 text-sm text-gray-600 dark:text-gray-300">
              <p class="font-medium mb-2">{{ $t('download.winTipsTitle') }}</p>
              <ol class="list-decimal list-inside space-y-1 text-left">
                <li>{{ $t('download.winTip1') }}</li>
                <li>{{ $t('download.winTip2') }}</li>
              </ol>
            </div>
          </div>
        </div>
      </div>

      <!-- 引入下载 Modal -->
      <DownloadModal 
        :show="showDownloadModal"
        @close="showDownloadModal = false"
        @download="handleDownload"
      />
    </section>

    <!-- Back to Top Button -->
    <button v-show="showBackToTop"
            @click="scrollToTop"
            class="fixed bottom-8 right-8 bg-nva-noun dark:bg-blue-600 text-white p-3 rounded-full shadow-lg hover:bg-opacity-90 transition-all duration-300 focus:outline-none focus:ring-4 focus:ring-nva-noun/50 z-30"
            :aria-label="$t('backToTop')">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
      </svg>
    </button>
  </main>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import { ref, onMounted, computed, onUnmounted } from 'vue'
import DownloadModal from '@/components/DownloadModal.vue'

const { t, locale } = useI18n()
const isDark = ref(false)
const windowWidth = ref(1920)
const isLoading = ref(true)
const showBackToTop = ref(false)
const showDownloadModal = ref(false)

// 响应式背景图片选择
const heroBackgroundSrc = computed(() => {
  const mode = isDark.value ? 'dark' : 'light'
  const width = windowWidth.value

  // 根据窗口宽度选择合适的图片
  let imageWidth = 1920
  if (width <= 375) imageWidth = 375
  else if (width <= 414) imageWidth = 414
  else if (width <= 768) imageWidth = 768
  else if (width <= 1024) imageWidth = 1024
  else if (width <= 1280) imageWidth = 1280
  else if (width <= 1366) imageWidth = 1366
  else if (width <= 1440) imageWidth = 1440
  else imageWidth = 1920

  const imageHeight = getImageHeight(imageWidth)
  const suffix = mode === 'dark' ? '-dark' : ''

  return `/images/hero-bg-${imageWidth}x${imageHeight}${suffix}.png`
})

// 根据宽度获取对应的高度
const getImageHeight = (width: number): number => {
  const heightMap: { [key: number]: number } = {
    375: 812,
    414: 896,
    768: 1024,
    1024: 768,
    1280: 720,
    1366: 768,
    1440: 900,
    1920: 1080
  }
  return heightMap[width] || 1080
}

// 监听窗口大小变化
const updateWindowWidth = () => {
  windowWidth.value = window.innerWidth
}

// 监听滚动事件
const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

// 平滑滚动到指定区域
const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

// 滚动到顶部
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// 事件追踪
const trackEvent = (eventName: string) => {
  // 这里可以集成 Google Analytics 或其他分析工具
  console.log('Event tracked:', eventName)
}

// 更新 meta 标签
const updateMetaTags = () => {
  const currentLocale = locale.value
  const title = t('meta.title')
  const description = t('meta.description')

  // 更新页面标题
  document.title = title

  // 更新 meta description
  let metaDesc = document.querySelector('meta[name="description"]')
  if (!metaDesc) {
    metaDesc = document.createElement('meta')
    metaDesc.setAttribute('name', 'description')
    document.head.appendChild(metaDesc)
  }
  metaDesc.setAttribute('content', description)

  // 更新 Open Graph 标签
  let ogTitle = document.querySelector('meta[property="og:title"]')
  if (!ogTitle) {
    ogTitle = document.createElement('meta')
    ogTitle.setAttribute('property', 'og:title')
    document.head.appendChild(ogTitle)
  }
  ogTitle.setAttribute('content', title)

  let ogDesc = document.querySelector('meta[property="og:description"]')
  if (!ogDesc) {
    ogDesc = document.createElement('meta')
    ogDesc.setAttribute('property', 'og:description')
    document.head.appendChild(ogDesc)
  }
  ogDesc.setAttribute('content', description)

  // 更新语言属性
  document.documentElement.lang = currentLocale
}

const toggleDark = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    document.body.style.setProperty('--page-background', '#111827') // gray-900
  } else {
    document.documentElement.classList.remove('dark')
    document.body.style.setProperty('--page-background', '#ffffff')
  }
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

const handleDownload = (arch: 'arm64' | 'x64') => {
  // 实现下载逻辑
  const url = arch === 'arm64' 
    ? '/downloads/adhdgofly-arm64.dmg'
    : '/downloads/adhdgofly-x64.dmg'
  
  // 追踪下载事件
  trackEvent(`download_mac_${arch}`)
  
  // 开始下载
  window.location.href = url
  
  // 关闭 Modal
  showDownloadModal.value = false
}

onMounted(() => {
  const theme = localStorage.getItem('theme')
  isDark.value = theme === 'dark'
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    document.body.style.setProperty('--page-background', '#111827')
  } else {
    document.body.style.setProperty('--page-background', '#ffffff')
  }

  // 初始化窗口宽度
  updateWindowWidth()

  // 监听窗口大小变化
  window.addEventListener('resize', updateWindowWidth)

  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)

  // 模拟加载完成
  setTimeout(() => {
    isLoading.value = false
  }, 1000)

  // 更新 meta 标签
  updateMetaTags()

  // 添加结构化数据
  const script = document.createElement('script')
  script.type = 'application/ld+json'

  // 根据当前语言获取 FAQ 数据
  const getFAQData = () => {
    const faqData: { [key: string]: Array<{ question: string; answer: string }> } = {
      zh: [
        {
          question: 'ADHD GO FLY 支持哪些语言？',
          answer: 'ADHD GO FLY 支持中文、英文、法文、西班牙文、俄文和日文六种语言，满足不同语言用户的需求。'
        },
        {
          question: 'ADHD GO FLY 是免费的吗？',
          answer: '是的，ADHD GO FLY 完全免费使用，包括所有核心功能如智能分词、AI辅助、专注模式等。'
        },
        {
          question: 'ADHD GO FLY 支持哪些操作系统？',
          answer: 'ADHD GO FLY 支持 Windows、macOS 系统，同时提供网页版，可以随时在线使用。'
        },
        {
          question: '什么是智能分词功能？',
          answer: '智能分词功能可以实时分析文本，将长句子分解成易于理解的片段，帮助ADHD用户更好地理解和处理文本内容。'
        },
        {
          question: '专注模式有什么特点？',
          answer: '专注模式通过减少界面干扰元素、提供简洁的阅读环境，帮助ADHD用户保持注意力集中，提高阅读和写作效率。'
        },
        {
          question: '如何开始使用 ADHD GO FLY？',
          answer: '您可以直接访问网页版 https://adhdgofly.online 立即体验，或者下载桌面应用获得更好的使用体验。'
        },
        {
          question: 'AI 辅助功能包括哪些？',
          answer: 'AI 辅助功能包括智能文本分析、自动生成摘要、多语言翻译、写作建议等，帮助用户更好地处理文本内容。'
        },
        {
          question: '数据会自动保存吗？',
          answer: '是的，ADHD GO FLY 具有自动保存功能，确保您的工作内容不会丢失，可以随时恢复之前的编辑状态。'
        }
      ],
      en: [
        {
          question: 'What languages does ADHD GO FLY support?',
          answer: 'ADHD GO FLY supports Chinese, English, French, Spanish, Russian, and Japanese, meeting the needs of users in different languages.'
        },
        {
          question: 'Is ADHD GO FLY free?',
          answer: 'Yes, ADHD GO FLY is completely free to use, including all core features such as smart word segmentation, AI assistance, and focus mode.'
        },
        {
          question: 'What operating systems does ADHD GO FLY support?',
          answer: 'ADHD GO FLY supports Windows and macOS systems, and also provides a web version that can be used online anytime.'
        },
        {
          question: 'What is the smart word segmentation feature?',
          answer: 'The smart word segmentation feature can analyze text in real-time, breaking down long sentences into easily understandable segments, helping ADHD users better understand and process text content.'
        },
        {
          question: 'What are the features of focus mode?',
          answer: 'Focus mode helps ADHD users maintain concentration and improve reading and writing efficiency by reducing interface distractions and providing a clean reading environment.'
        },
        {
          question: 'How do I start using ADHD GO FLY?',
          answer: 'You can directly visit the web version at https://adhdgofly.online to experience it immediately, or download the desktop application for a better experience.'
        },
        {
          question: 'What AI assistance features are included?',
          answer: 'AI assistance features include intelligent text analysis, automatic summary generation, multilingual translation, writing suggestions, and more to help users better process text content.'
        },
        {
          question: 'Is data automatically saved?',
          answer: 'Yes, ADHD GO FLY has an auto-save feature that ensures your work content won\'t be lost and you can restore previous editing states at any time.'
        }
      ]
    }

    return faqData[locale.value] || faqData.zh
  }

  const faqData = getFAQData()

  script.textContent = JSON.stringify({
    '@context': 'https://schema.org',
    '@graph': [
      // 软件应用信息
      {
        '@type': 'SoftwareApplication',
        'name': 'ADHD GO FLY',
        'applicationCategory': 'Productivity',
        'operatingSystem': ['Windows', 'macOS', 'Web'],
        'offers': {
          '@type': 'Offer',
          'price': '0',
          'priceCurrency': 'USD'
        },
        'description': t('meta.description'),
        'screenshot': [
          {
            '@type': 'ImageObject',
            'url': 'https://adhdgofly.com/images/screenshots/editor.png',
            'caption': locale.value === 'zh' ? '智能编辑器界面' : 'Smart Editor Interface'
          },
          {
            '@type': 'ImageObject',
            'url': 'https://adhdgofly.com/images/screenshots/ai.png',
            'caption': locale.value === 'zh' ? 'AI文本处理功能' : 'AI Text Processing'
          },
          {
            '@type': 'ImageObject',
            'url': 'https://adhdgofly.com/images/screenshots/focus.png',
            'caption': locale.value === 'zh' ? '专注模式界面' : 'Focus Mode Interface'
          }
        ],
        'featureList': [
          locale.value === 'zh' ? '多语言支持（中、英、法、西、俄、日）' : 'Multilingual Support (Chinese, English, French, Spanish, Russian, Japanese)',
          locale.value === 'zh' ? '智能分词系统' : 'Smart Word Segmentation',
          locale.value === 'zh' ? 'AI辅助功能' : 'AI Assistance',
          locale.value === 'zh' ? '专注模式' : 'Focus Mode',
          locale.value === 'zh' ? '自动保存' : 'Auto Save'
        ],
        'url': 'https://adhdgofly.com',
        'softwareVersion': '1.0.0'
      },
      // 组织信息
      {
        '@type': 'Organization',
        'name': 'ADHD GO FLY',
        'url': 'https://adhdgofly.com',
        'logo': {
          '@type': 'ImageObject',
          'url': 'https://adhdgofly.com/images/logo.svg',
          'width': 200,
          'height': 60
        },
        'description': locale.value === 'zh' ? '为ADHD群体提供专业的多语言阅读编辑工具' : 'Providing professional multilingual reading and editing tools for ADHD individuals',
        'sameAs': [
          'https://adhdgofly.online'
        ]
      },
      // 面包屑导航
      {
        '@type': 'BreadcrumbList',
        'itemListElement': [
          {
            '@type': 'ListItem',
            'position': 1,
            'name': locale.value === 'zh' ? '首页' : 'Home',
            'item': 'https://adhdgofly.com'
          },
          {
            '@type': 'ListItem',
            'position': 2,
            'name': locale.value === 'zh' ? '产品介绍' : 'Features',
            'item': 'https://adhdgofly.com/#features'
          },
          {
            '@type': 'ListItem',
            'position': 3,
            'name': locale.value === 'zh' ? '用户评价' : 'Testimonials',
            'item': 'https://adhdgofly.com/#testimonials'
          },
          {
            '@type': 'ListItem',
            'position': 4,
            'name': locale.value === 'zh' ? '下载' : 'Download',
            'item': 'https://adhdgofly.com/#download'
          }
        ]
      },
      // FAQ 结构化数据
      {
        '@type': 'FAQPage',
        'mainEntity': faqData.map((faq: { question: string; answer: string }) => ({
          '@type': 'Question',
          'name': faq.question,
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': faq.answer
          }
        }))
      },
      // 网站信息
      {
        '@type': 'WebSite',
        'name': 'ADHD GO FLY',
        'url': 'https://adhdgofly.com',
        'description': t('meta.description'),
        'publisher': {
          '@type': 'Organization',
          'name': 'ADHD GO FLY'
        }
      }
    ]
  })
  document.head.appendChild(script)
})

onUnmounted(() => {
  // 清理事件监听器
  window.removeEventListener('resize', updateWindowWidth)
  window.removeEventListener('scroll', handleScroll)
})

const features = [
  {
    icon: 'BrainIcon',
    titleKey: 'features.adhd.title',
    descKey: 'features.adhd.desc'
  },
  {
    icon: 'LanguageIcon',
    titleKey: 'features.language.title',
    descKey: 'features.language.desc'
  },
  {
    icon: 'DevicesIcon',
    titleKey: 'features.platform.title',
    descKey: 'features.platform.desc'
  }
]

const testimonials = [
  {
    initial: 'L',
    name: 'Liu Wei',
    title: 'ADHD 创作者',
    contentKey: 'testimonials.review1'
  },
  {
    initial: 'S',
    name: 'Sarah Chen',
    title: 'Technical Writer',
    contentKey: 'testimonials.review2'
  },
  {
    initial: 'M',
    name: 'Mike Zhang',
    title: '自由撰稿人',
    contentKey: 'testimonials.review3'
  },
  {
    initial: 'X',
    name: '小红书@专注力研究',
    title: 'ADHD 生活博主',
    contentKey: 'testimonials.review4',
    link: 'https://www.xiaohongshu.com/user/profile/12345678',
    isXiaohongshu: true
  },
  {
    initial: 'Y',
    name: 'Yang Min',
    title: '内容创作者',
    contentKey: 'testimonials.review5',
    hasImage: true,
    imagePath: '/images/userimages/yangmin.png'
  }
]

const getIconColor = (index: number) => {
  const colors = ['text-nva-noun', 'text-nva-verb', 'text-nva-adj']
  return colors[index]
}

const getTextColor = (index: number) => {
  const colors = ['text-nva-noun', 'text-nva-verb', 'text-nva-adj']
  return colors[index]
}
</script>

<style lang="postcss" scoped>
.hero {
  position: relative;
  overflow: hidden;
}

.btn-primary {
  @apply px-6 md:px-8 py-3 bg-nva-noun dark:bg-blue-600 text-white rounded-lg font-semibold shadow-lg;
  @apply hover:bg-opacity-90 transition-all duration-300;
  @apply hover:shadow-xl hover:-translate-y-0.5 transform;
}

.btn-secondary {
  @apply px-6 md:px-8 py-3 bg-white dark:bg-gray-800 text-nva-noun dark:text-blue-400 rounded-lg font-semibold border border-nva-noun dark:border-blue-400 shadow-lg;
  @apply hover:bg-nva-noun-bg dark:hover:bg-blue-900 transition-all duration-300;
  @apply hover:shadow-xl hover:-translate-y-0.5 transform;
}

.feature-card {
  @apply p-6 rounded-xl bg-white dark:bg-gray-800 shadow-md;
}

.download-card {
  @apply p-6 md:p-8 rounded-xl bg-white dark:bg-gray-800 shadow-md text-center;

  .btn-download {
    @apply inline-block px-6 py-3 bg-nva-adj dark:bg-green-600 text-white rounded-lg font-semibold;
    @apply hover:bg-opacity-90 transition-colors;
  }
}

.screenshot-card {
  @apply bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg transform transition-transform duration-300;
  &:hover {
    @apply -translate-y-2 shadow-xl;
  }
}

.aspect-w-16 {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
}

.aspect-w-16 > * {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.testimonial-card {
  @apply bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg;
  @apply transform transition-all duration-300;

  &:hover {
    @apply -translate-y-1 shadow-xl;
  }
}

.testimonial-content :deep(a) {
  @apply text-nva-noun hover:opacity-80 transition-colors;
  @apply underline underline-offset-2;
}
</style>
