const state = {
    isEdit:false,
    isVisibility: false,
}

const mutations = {
    setIsEdit(state, value){
        state.isEdit = value;
    },
    setIsVisibilty(state, value){
        state.isVisibility = value;
    }
}

const actions = {
    setIsEdit({commit}, value){
        commit('setIsEdit', value);
    },
    setIsVisibilty({commit}, value){
        commit('setIsVisibilty', value);
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