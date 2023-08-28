<template>
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">


            <!-- <router-link
          :to="{ name: 'productsCategory', params: { category: category.strCategory }}"
          v-for="category in categories"
          :key="category.idCategory"
          class="m-5"> -->

            <div class="flex flex-wrap -m-4">
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full" v-for="product in products" :key="product.strName">
                    <router-link :to="{name: 'product', params:{strName: product.strName}}">
                        <a class="block relative h-48 rounded overflow-hidden">
                            <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://dummyimage.com/420x260">
                        </a>
                        <div class="mt-4">
                            <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">{{product.strCategory}}</h3>
                            <h2 class="text-gray-900 title-font text-lg font-medium">{{ product.strName }}</h2>
                            <p class="mt-1">{{ product.strDescription }}</p>
                            <h3 class="text-gray-900 title-font text-lg font-medium">${{product.intPrice}}.00</h3>
                        </div>
                    </router-link>
                
                </div>
        
            </div>
        </div>
    </section>
</template>

<script>
import axiosClient from '../axiosClient.js'
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const products = ref([]); // Declare products as a ref
        
        onMounted(async () => {
            try {
                const response = await axiosClient.get("/products");
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
