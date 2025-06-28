// src/env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_GA_MEASUREMENT_ID: string
    readonly VITE_BAIDU_ANALYTICS_ID: string
    readonly VITE_CLOUDFLARE_ANALYTICS_ID: string
  }
  
  interface ImportMeta {
    readonly env: ImportMetaEnv
  }