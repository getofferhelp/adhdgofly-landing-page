import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import { trackPageView } from '@/utils/analytics'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/download',
      name: 'Download',
      component: () => import('@/views/Download.vue'),
      meta: {
        title: 'Download ADHD GO FLY'
      }
    }
    
  ]
})

router.afterEach((to) => {
  trackPageView(to.fullPath)
})

export default router
