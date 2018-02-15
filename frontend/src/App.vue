<template>

  <div>
<!--     <nav class="navbar navbar-light text-">
      <a class="navbar-brand">Market Monitor</a>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
        </li>
      </ul>
    </nav> -->
    <div id="app" class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style type="text/css">
  .navbar{
    background-color: white !important;
  }
</style>
