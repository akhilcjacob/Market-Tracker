  <template>
      <div class="card card-block text-center mt-lg-5">
        <h4 class="card-header card-title">{{ company.companyName }}</h4>
        <h5 class="card-text">{{ company.symbol }}</h5>
        <h6 class="card-text">{{ company.changePercent }}</h6>
    </div>
</template>

<script>
export default {
  name: 'SingleCard',
  props: ['company'],
  data () {
    return {
      singleResult: {}
    }
  }
}

</script>
