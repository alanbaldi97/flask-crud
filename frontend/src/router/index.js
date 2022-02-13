import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'
import EventBus from 'app/src/common/event-bus';

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

import { AuthService } from '../services/auth/AuthService';

const authService = new AuthService();

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })


  Router.beforeEach(async (to, from, next) => {
    EventBus.$emit('visible-bar');
    const isAutenticate = await authService.isAutenticate();

    if( !to.meta.auth ){
      if(to.name == 'login' && !isAutenticate) return next()
      if(to.name == 'login' && isAutenticate) return next({name:'managers'})

      return next();
    }

    if(!isAutenticate) return next({ name: 'login'})


    return next()

  });

  Router.afterEach( (to, from) => {
    EventBus.$emit('hide-bar');
  })

  return Router
}
