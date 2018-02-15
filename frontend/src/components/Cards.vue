<template>
  <div>
   <div id="app">
    <div id="main">
      <input type="text" placeholder="Search.." v-model="search"/>
      <div v-bind:key="result" v-for="result in filteredresults">
       <!-- <span>{{result.companyName}}</span> -->

       <SingleCard v-bind:company="result"></SingleCard>
     </div>
   </div>
 </div>
 <button @click="getStocks" type="button" class="btn btn-primmary-outline">Refresh List</button>
</div>
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
      this.search= ''
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
      results: []
    }
  },
  computed:
  {
    filteredresults: function () {
      var self = this
      if (self.search !== '') { return this.results.filter(function (result) { return result.companyName.toLowerCase().indexOf(self.search.toLowerCase()) >= 0 }) } else { return this.results }
    }
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

</style>
