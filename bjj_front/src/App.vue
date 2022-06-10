<template>
  <div>
    <p>hi</p>
    <button @click="getData">
      click
    </button>

    <div v-for="(video, index) in videos " :key="index">
    {{ video.title }} <br>
    <img :src="video.thumbnail"> <br>
    <a :href="video.url">{{ video.url }}</a> <br>
    {{ video.description }} <br>
    channel : {{ video.channel }} <br><hr>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      videos: [],
    }
  },
  methods: {
    getData() {
      axios
      .get('http://127.0.0.1:8000/datas/list')
      .then(res => {
        this.videos = res.data
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })

    }
  }

}
</script>
<style>

</style>