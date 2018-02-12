import Vue from 'vue'
import Router from 'vue-router'
import Cards from '@/components/Cards'
import Home from '@/components/Home'
import fileNotFound from '@/components/fileNotFound'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/hi',
      component: Cards
    },
    {
      path: '*',
      component: fileNotFound
    }
  ]
})
