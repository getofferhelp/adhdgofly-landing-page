// src/utils/analytics.ts
interface EventProperties {
    category?: string
    label?: string
    value?: number
    [key: string]: any
  }
  
  // 事件类型定义
  export const EventTypes = {
    DOWNLOAD: {
      MAC_ARM64: 'download_mac_arm64',
      MAC_X64: 'download_mac_x64',
      WINDOWS: 'download_windows',
    },
    NAVIGATION: {
      PAGE_VIEW: 'page_view',
      SCROLL: 'scroll',
    },
    INTERACTION: {
      DARK_MODE: 'toggle_dark_mode',
      LANGUAGE_CHANGE: 'change_language',
    },
  } as const
  
  // 主要追踪函数
  export const trackEvent = (
    eventName: string, 
    properties: EventProperties = {}
  ) => {
    // 开发环境下打印日志
    if (import.meta.env.DEV) {
      console.log('Event tracked:', eventName, properties)
    }
  
    // Google Analytics
    if (window.gtag) {
      window.gtag('event', eventName, {
        ...properties,
        send_to: import.meta.env.VITE_GA_MEASUREMENT_ID
      })
    }
  
    // 百度统计
    if (window._hmt) {
      window._hmt.push(['_trackEvent', 
        properties.category || 'General',
        eventName,
        properties.label || '',
        properties.value || 1
      ])
    }
  }
  
  // 页面访问追踪
  export const trackPageView = (path: string) => {
    trackEvent(EventTypes.NAVIGATION.PAGE_VIEW, {
      page_path: path,
      page_title: document.title
    })
  }
  
  // 下载追踪
  export const trackDownload = (
    type: 'mac_arm64' | 'mac_x64' | 'windows',
    version: string
  ) => {
    const eventName = EventTypes.DOWNLOAD[
      type.toUpperCase() as keyof typeof EventTypes.DOWNLOAD
    ]
    
    trackEvent(eventName, {
      category: 'Download',
      label: `v${version}`,
      value: 1
    })
  }