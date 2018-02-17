  <template>
    <!-- <div class="card card-block text-center greenify col-centered"> -->
      <!-- <h4 class="card-title">{{ company.symbol }}</h4> -->

      <!-- <a href="#" class="card credentialing"> -->
        <!-- <h5 class="card-text">{{ company.symbol }}</h5> -->
        <!-- <h6 class="card-text">{{ company.price }}</h6> -->
        <!-- <div class="overlay"></div> -->
        <!-- <div class="circle"></div> -->
        <!-- </a> -->
          <a href="#" class="card col-centered" >
           <div class="overlay greenify" v-if="!isNeg"></div>
           <div class="overlay redify" v-else></div>
           <!-- <p class="pt-5">asdf</p> -->
           <div class="container mt-lg-5 mb-5">
           <p class="text-center col font-weight-bold mb-4">{{ company.symbol }}</p>
           <p class="text-center col align-text-top mt-4">{{ quote.changePercent }}%</p>
           </div>
           <div class="container" >
              <h5 class="text-center">{{ quote.companyName  | truncate '5'}}</h5></div>
              <h6 class="text-center text-info">${{ company.price }}</h6>
         </p>
           </div>
         </a>
       </div>
   </template>

   <script>
   import axios from 'axios'
   
   export default {
    name: 'SingleCard',
    props: ['company','quote'],
    data () {
      return {
        isNeg: false,
        singleResult: {},
        quote: []
      }
    },
    methods: {
      getStatus () {
        if (this.company.symbol === undefined) return

          const path = `http://localhost:5000/api/` + this.company.symbol
        axios.get(path)
        .then(response => {
          this.quote = response.data
          var factor = Math.pow(10, 3)
          this.quote.changePercent = Math.round(this.quote.changePercent * factor) / factor
          if (this.quote.changePercent > 0) {
            this.isNeg = false
            this.quote.changePercent = '+' + this.quote.changePercent
          } else { this.isNeg = true }
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    filters: {
  
    truncate: function(string, value) {
      return string.substring(0, value) + '...';
    }},
    beforeMount () {
      this.getStatus()
    }

  }

  </script>
  <style type="text/css">

  .redify {
    --bg-color:  rgba(255, 100, 90, 0.48);
    --bg-color-light: #B8F9D3;
    --text-color-hover: #4C5656;
    --box-shadow-color: rgba(255, 100, 97, 0.48);
  }

  .greenify {
    --bg-color: #B8F9D3;
    --bg-color-light: #e2fced;
    --text-color-hover: #4C5656;
    --box-shadow-color: rgba(184, 249, 211, 0.48);
  }

  .card {
    width: 220px;
    height: 322px;
    background: #fff;
    border-top-right-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    box-shadow: 0 14px 26px rgba(0,0,0,0.04);
    transition: all 0.3s ease-out;
    text-decoration: none;
  }

  .card:hover {
    transform: translateY(-5px) scale(1.005) translateZ(0);
    box-shadow: 0 24px 36px rgba(0,0,0,0.11),
    0 24px 46px var(--box-shadow-color);
  }

  .card:hover .overlay {
    transform: scale(4) translateZ(0);
  }

  .card:hover .circle {
    border-color: var(--bg-color-light);
    background: var(--bg-color);
  }

  .card:hover .circle:after {
    background: var(--bg-color-light);
  }

  .card:hover p {
    color: var(--text-color-hover);
  }

  .card:active {
    transform: scale(1) translateZ(0);
    box-shadow: 0 15px 24px rgba(0,0,0,0.11),
    0 15px 24px var(--box-shadow-color);
  }

  .card p {
    font-size: 17px;
    color: #4C5656;
    z-index: 1000;
    transition: color 0.3s ease-out;
  }

  .circle {
    width: 131px;
    height: 131px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid var(--bg-color);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    z-index: 1;
    transition: all 0.3s ease-out;
  }

  .circle:after {
    content: "";
    width: 118px;
    height: 118px;
    display: block;
    position: absolute;
    background: var(--bg-color);
    border-radius: 50%;
    top: 7px;
    left: 7px;
    transition: opacity 0.3s ease-out;
  }


  .overlay {
    width: 118px;
    position: absolute;
    height: 118px;
    border-radius: 50%;
    background: var(--bg-color);
    top: 70px;
    left: 50px;
    z-index: 0;
    transition: transform 0.3s ease-out;
  }
  .col-centered{
    float: none;
    margin: 0 auto;
  }
  </style>
