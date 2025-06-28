// src/types/analytics.d.ts
interface CfAnalytics {
  trackEvent: (eventName: string, properties: object) => void
}

interface Window {
  cfAnalytics?: CfAnalytics
  gtag?: (
    command: 'event',
    eventName: string,
    eventParameters: object
  ) => void
  _hmt?: any[]
}