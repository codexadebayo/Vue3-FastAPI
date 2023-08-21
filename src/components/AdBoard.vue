<template>
    <div class="bg-white rounded-lg p-4 shadow-md">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-semibold text-gray-800">{{ title }}</h2>
        <span class="text-sm text-gray-500">{{ date }}</span>
      </div>
      <div class="flex">
        <div class="w-1/2 pr-4">
          <p class="text-gray-600">{{ description }}</p>
          <router-link to="/sales" class="text-indigo-600 hover:underline">{{ buttonText }}</router-link>
        </div>
        <div class="w-1/2">
          <img alt="Ad" class="w-full h-auto rounded-lg" src="https://dummyimage.com/428x268">
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      date: String,
      image: String,
      description: String,
      link: String,
      buttonText: String,
    },
  };
  </script>
  
  <style scoped>
  /* You can add custom styles here */
  </style>
  