<template>
  <div>
    <header>
      <nav class="navbar">
        <a href="#/">
          <img
            :src="'/static/midia/img/logo.png'"
            alt="Metflix Logo"
            class="logo"
          />
        </a>
        <ul class="nav-links">
          <li><router-link to="/">Início</router-link></li>
          <li>
            <router-link to="/filmes_series">Filmes e Séries</router-link>
          </li>
          <li><router-link to="/jogos">Jogos</router-link></li>
          <li><router-link to="/biblioteca">Biblioteca</router-link></li>
          <li><router-link to="/login">Entrar</router-link></li>
        </ul>
      </nav>
    </header>

    <main>
      <div class="content-wrapper">
        <router-view />
      </div>
    </main>

    <div class="corner-line diag-left"></div>
    <div class="corner-line diag-right"></div>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
body {
  margin: 0;
  font-family: "Roboto", sans-serif;
  background-color: #141414;
  color: #fff;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background-color: #000;
  padding: 10px 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  width: 120px;
  height: auto;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav-links li {
  margin: 0;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-size: 1.2rem;
  font-weight: bold;
  text-transform: uppercase;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-links a:hover {
  background-color: #e50914;
  color: #fff;
}

.nav-links a:active {
  background-color: #b4070e;
}

@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .nav-links {
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
  }
}

.corner-line {
  position: fixed;
  width: 160px;
  height: 6px;
  background-color: #e50914;
  z-index: 10;
}

.corner-line.diag-left {
  bottom: 30px;
  left: -25px;
  transform: rotate(45deg);
}

.corner-line.diag-right {
  bottom: 30px;
  right: -25px;
  transform: rotate(-45deg);
}
</style>
