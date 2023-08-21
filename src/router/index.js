import {
   createRouter,
   createWebHistory
} from "vue-router";
import Home from '../views/Home.vue'
import Sale from '../views/Sale.vue'
import Products from '../views/Products.vue'
import About from '../views/About.vue'
import BestSellers from '../views/BestSellers.vue'
import ProductsCategory from '../views/ProductsCategory.vue'
import Categories from '../views/Categories.vue'
import Contacts from '../views/Contacts.vue'



const routes = [
   {
      path: "/",
      name: "home",
      component: Home,
   },
   {
      path: "/sales",
      name: "sales",
      component: Sale,
   },
   {
      path: "/products",
      name: "products",
      component: Products,
   },
   {
      path: "/about",
      name: "about",
      component: About,
   },
   {
      path: "/bestsellers",
      name: "bestsellers",
      component: BestSellers,
   },
   {
      path: "/products/categories",
      name: "categories",
      component: Categories,
   },
   {
      path: "/products/categories/:category",
      name: "productsCategory",
      component: ProductsCategory,
   },
   {
      path: "/contacts",
      name: "contacts",
      component: Contacts,
   }
];

const router = createRouter({
   history: createWebHistory(),
   routes
});

export default router;
