<template lang="">
    <div>
        Our Latest and Best Sellers
    </div>
</template>
<script>
import axiosClient from '../axiosClient.js'
import { onMounted } from 'vue';



onMounted(async() => {
   const response = await axiosClient.get('/bestsellers')
   console.log(response.data)
})
</script>
<style lang="">
    
</style>