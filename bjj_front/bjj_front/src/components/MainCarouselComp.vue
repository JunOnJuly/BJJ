<template>
  <div>
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
      <div v-for="data in CarouselDatas" :key=data.title class="carousel-inner">
        <div class="carousel-item active">
          <img :src=data.thumbnail class="d-block w-100">
          <div class="carousel-caption d-none d-md-block">
            <h5>{{ data.guard_name}}</h5>
            <p> {{ data.description}} </p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    mounted () {
      this.CarouselDatas = this.$store.datas.dispatch("SelectCarouselDatas")
      console.log(this.CarouselDatas)
    },
    data () {
      return {
        CarouselDatas: []
      }
    },
  }
</script>

<style scoped>
  img {
    height: 50rem;
  }
</style>