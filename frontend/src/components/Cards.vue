<template>
 <div id="app" class="container-fluid">
  <input type="text" class="" placeholder="Search..." v-model="search"/>
      <paginate v-if="isReady"
      name="filteredresults"
      :list="filteredresults"
      tag="div"
      class="row align-content-stretch"
      :per="52">
      <div class="col-md-3 col-md-offset-5 col-centered" v-bind:key="item" v-for="item in paginated('filteredresults')">
        <SingleCard  class="mt-3" v-bind:company="item"></SingleCard>
      </div>
    </paginate>
<div class="container text-right">
  
    <paginate-links
    for="filteredresults"
    :simple="{
    prev: '<< Back  |',
    next: '|  Next >>'
  }"
  ></paginate-links>
</div>
</div>
</div>
<!-- <button @click="getStocks" type="button" class="btn btn-primmary-outline">Refresh List</button> -->
</template>

<script>
import axios from 'axios'
import SingleCard from './SingleCard'

export default {
  name: 'Cards',
  components: {
    SingleCard
  },
  methods: {
    getStocks () {
      this.results = this.getStockFromBackend()
      this.search = ''
      this.isReady = true
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
  },
  data () {
    return {
      search: '',
      isReady: false,
      results: [],
      paginate: ['filteredresults']
    }
  },
  computed:
  {
    filteredresults: function () {
      var self = this
      if (self.search !== '') { return this.results.filter(function (result) { return result.symbol.toLowerCase().indexOf(self.search.toLowerCase()) >= 0 }) } else { return this.results }
    }
  },
  beforeMount () {
    this.getStocks()
  }
}

</script>
<style type="text/css">
input{
  background-color: transparent;
  border-color: transparent;
  border-bottom-color: black;
  width: 100%;
  height: 100px;
  color :#111;
  font-size :4em;
  outline :none;
  text-align :center;
}
body{
  background: #f2f4f8;
  width: 100%;
}
ul.paginate-links{
  color: green;
  text-align: center;
}
li.prev, li.next {
  display: inline-block;
}
</style>
