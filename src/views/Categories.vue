<template>
    <div>
      <div class="p-2 w-full">
        <router-link
          :to="{ name: 'productsCategory', params: { category: category.strCategory }}"
          v-for="category in categories"
          :key="category.idCategory"
          class="m-5"
        >
          <button class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">
            {{ category.strCategory }}
          </button>
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axiosClient from '../axiosClient.js'
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const categories = ref([]);
  
      onMounted(async () => {
        try {
          const response = await axiosClient.get("/products/categories");
          console.log(response.data);
          categories.value = response.data;
        } catch (error) {
          console.error(error);
        }
      });
  
      return {
        categories
      };
    }
  }
  </script>
  
  <style>
      
  </style>
  