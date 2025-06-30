// src/types/analytics.d.ts
interface Window {
    gtag?: (
      command: 'event',
      eventName: string,
      eventParameters: object
    ) => void
    _hmt?: any[]
  }