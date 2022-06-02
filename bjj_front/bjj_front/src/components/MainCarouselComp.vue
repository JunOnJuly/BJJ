<template>
  <button id="search-button" @click="SelectCardDatas">get random skills</button>
  <div class="d-flex justify-content-center">
    <div v-for="data in CardDatas" :key="data.title" class="card mx-3" style="width: 18rem;">
      <img :src=data.thumbnail class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">{{ data.title }}</h5>
        <p class="card-text">{{ data.description }}</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    created() {
      this.$store.commit('GetDataList')
    },
    data () {
      return {
        CardDatas: []
      }
    },
    methods: {
      SelectCardDatas () {
        this.$store.commit('SelectCardDatas')
        this.CardDatas = this.$store.state.datas.CardData
      }
    }
  }
</script>

<style scoped>
  img {
    height: 25rem;
  }

  #search-button {
    margin: 1% 0;
    width: 100%;
    border: None;
    background-color: rgba(0, 0, 0, 0.123);
  }
</style>