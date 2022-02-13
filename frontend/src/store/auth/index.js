const state = {
    user:null,
}

const mutations = {
    setUser(state, value){
        state.user = value;
    }
}

const actions = {
    setUser({commit}, value){
        commit('setUser', value);
    }
}

const getters = {
    
}

export default {
    namespaced:true,
    state,
    mutations,
    actions,
    getters
}