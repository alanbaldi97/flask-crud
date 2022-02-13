import Vue from 'vue'
import Vuex from 'vuex'

// import example from './module-example'
import auth from './auth'
import manager from './manager';

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

const Store = new Vuex.Store({
  modules: {
    // example
    auth,
    manager
  },

  // enable strict mode (adds overhead!)
  // for dev mode only
  strict: process.env.DEBUGGING,
  plugins: [ createPersistedState({ storage: window.sessionStorage })]
})

export default function (/* { ssrContext } */) {
  

  return Store
}


export { Store } 
