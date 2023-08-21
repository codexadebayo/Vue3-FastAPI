<template>
    <div>
        {{ products }}
    </div>
</template>

<script>
import axiosClient from '../axiosClient.js'
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const products = ref([]); // Declare products as a ref
        
        onMounted(async () => {
            try {
                const response = await axiosClient.get("/products/categories");
                console.log(response.data);
                products.value = response.data; // Update products using ref
            } catch (error) {
                console.error(error);
            }
        });

        return {
            products // Expose products to the template
        };
    }
}
</script>

<style scoped>
    /* Your styles here */
</style>
