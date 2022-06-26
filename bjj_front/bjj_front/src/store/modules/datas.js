import axios from 'axios'
import _ from 'lodash'

export default ({
  state: {
    DataList: [],
    CardData: [],
  },
  getters: {
  },
  mutations: {
    GetDataList (state) {
      if (state.DataList.length === 0) {
        axios
        .get('http://127.0.0.1:8000/datas/list')
        .then( res => {
          state.DataList = res.data
          console.log(res)
        })
        .catch( err => {
          console.log(err)
        })
      }
    },
    SelectCardDatas (state) {
      state.CardData = _.sampleSize(state.DataList, 6)
    },
  },
  actions: {
  },
  modules: {
  }
})
