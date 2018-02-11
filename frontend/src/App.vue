<template>

  <div>
    <nav class="navbar bg-dark text-light">
      <a class="navbar-brand">Boiler Plate Homepage</a>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
        </li>
      </ul>
    </nav>
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
