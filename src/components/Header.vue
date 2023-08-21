<template lang="">
    <header class="fixed w-full bg-white mb-5 shadow-lg top-0 text-gray-600 body-font">
        <div class="container mx-auto flex flex-wrap pt-3 pb-3 flex-col w-full md:flex-row items-center justify-start">
            <nav class="flex lg:w-2/5 flex-wrap items-center justify-start text-base md:ml-auto">
                <router-link :to="{name: 'about', params:{about}}" :key="about"><a class="mr-5 hover:text-gray-900">About</a></router-link>

                <router-link :to="{name: 'categories', params:{categories}}" :key="categories"><a class="mr-5 hover:text-gray-900">Product Categories </a></router-link>
                
                <router-link :to="{name: 'sales', params:{sales}}" :key="sales"><a class="mr-5 hover:text-gray-900">Sale</a></router-link>

                <router-link :to="{name: 'bestsellers', params:{bestsellers}}" :key="bestseller"><a class="mr-5 hover:text-gray-900">New + Bestseller</a></router-link>
                
                <router-link :to="{name: 'products', params:{products}}" :key="products"><a class="hover:text-gray-900">Explore</a></router-link>
            </nav>
            <router-link to="/" class="flex order-first lg:order-none lg:w-1/5 title-font font-medium items-center text-gray-900 lg:items-center lg:justify-center mb-4 md:mb-0"><svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
                </svg>
                <span class="ml-3 text-xl">Diadem</span></router-link>
            <input type="text" class="flex
             order-last
             lg:w-1/5
             justify-end
             md:ml-auto
             rounded 
             border-2 border-gray-200
             w-30
             h-25"
             placeholder="Search" 
            />
        </div>
    </header>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
:v-deep .body {
  margin-top: 7px;
}

</style>