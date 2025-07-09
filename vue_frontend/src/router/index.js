import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import BibliotecaView from "../views/BibliotecaView.vue";
import DashboardView from "../views/DashboardView.vue";
import FilmesSeriesView from "../views/FilmesSeriesView.vue";
import JogosView from "../views/JogosView.vue";
import MidiasView from "../views/MidiasView.vue";

const routes = [
  { path: "/", component: DashboardView },
  { path: "/login", component: LoginView },
  { path: "/register", component: RegisterView },
  { path: "/biblioteca", component: BibliotecaView },
  { path: "/dashboard", component: DashboardView },
  { path: "/filmes_series", component: FilmesSeriesView },
  { path: "/jogos", component: JogosView },
  { path: "/midias", component: MidiasView },
];

const router = createRouter({
  history: createWebHistory("/app/"),
  routes,
});

export default router;
