<template>
  <div>
    <Header></Header>
  </div>
  <div class="h-20">

  </div>
  <section class="body">
    <div>
      <router-view />
    </div>
  </section>
  <div>
    <Footer></Footer>
  </div>
</template>

<script setup>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';




</script>

<style scoped>

</style>
