import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';

const routes = [
  {
	path: "/",
	name: "Home",
	component: Home,
  },
  ...authRoutes,
];

const router = createRouter({
  base: "/hrms_ai_agents/",
  history: createWebHistory("/hrms_ai_agents"),
  routes,
});

export default router;
