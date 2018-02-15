import Vue from 'vue'
import Router from 'vue-router'
import Cards from '@/components/Cards'
import fileNotFound from '@/components/fileNotFound'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Cards
    },
    {
      path: '*',
      component: fileNotFound
    }
  ]
})
