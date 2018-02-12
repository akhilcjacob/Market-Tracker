<template>
  <div>
    <div class="row">
     <div class="col-md-4  pb-2 pt-2" v-for="result in results">
      <div class="card card-block text-center">
        <h4 class="card-header card-title">{{ result.companyName }}</h4>
        <p class="card-text">{{ result.symbol }}</p>
      </div>
    </div>
  </div>
  <button @click="getStocks" type="button" class="btn btn-primmary-outline">Refresh List</button>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      results: []
    }
  },
  methods: {
    getStocks () {
      this.results = this.getStockFromBackend()
    },
    getStockFromBackend () {
      const path = `http://localhost:5000/api/stocks`
      axios.get(path)
        .then(response => {
          this.results = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}

</script>
