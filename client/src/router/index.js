import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import SearchBox from '../components/SearchBox.vue'
import Results from '../components/Results.vue'

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
    },
    {
      path: '/results',
      name: 'results',
      component: Results
    }
  ]
})

export default router
