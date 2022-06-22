import { createStore } from 'vuex'
import axios from 'axios'
import _ from 'lodash'

export default createStore({
  state: {
    DataList: []
  },
  getters: {
  },
  mutations: {
    GetDataList (state) {
      axios
      .get('http://127.0.0.1:8000/datas/list')
      .then( res => {
        state.DataList = res.data
      })
      .catch( err => {
        console.log(err)
      })
    }
  },
  actions: {
    SelectCarouselDatas (context) {
      context.commit('GetDataList')
      return _.sample(context.DataList, 6)
    },
    SelectAllDatas (context) {
      context.commit('GetDataList')
      return context.DataList
    }
  },
  modules: {
  }
})
