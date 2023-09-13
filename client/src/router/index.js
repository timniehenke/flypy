import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import SearchBox from '../components/SearchBox.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/search',
      name: 'search',
      component: SearchBox
    }
  ]
})

export default router
