<template>
  <div class="center-container">
    <h2 class="section-title">Bem-vindo ao Metflix</h2>

    <form @submit.prevent="buscar">
      <input
        type="text"
        v-model="termoBusca"
        placeholder="Buscar por título..."
      />
      <button type="submit">Buscar</button>
    </form>

    <div class="card-container">
      <div v-if="resultados.length > 0">
        <div class="card" v-for="(item, index) in resultados" :key="index">
          <strong>{{ item.nome }}</strong>
          <span>
            <template v-if="item.preco !== null">
              Jogo - R$ {{ item.preco }}
            </template>
            <template v-else>
              {{ item.categoria }}
            </template>
          </span>
        </div>
      </div>
      <p v-else>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "DashboardView",
  data() {
    return {
      termoBusca: "",
      resultados: [], // mock inicialmente
    };
  },
  methods: {
    buscar() {
      // Simula uma busca fictícia (substitua depois por chamada à API)
      this.resultados = [
        { nome: "The Witcher 3", preco: 99.9 },
        { nome: "Breaking Bad", categoria: "Série" },
      ].filter((item) =>
        item.nome.toLowerCase().includes(this.termoBusca.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
body {
  background-color: #141414;
  color: #fff;
  font-family: "Roboto", sans-serif;
  margin: 0;
  position: relative;
  overflow-x: hidden;
}

.center-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 80vh;
  text-align: center;
  padding: 20px;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 30px;
  color: #e50914;
  border-bottom: 2px solid #e50914;
  display: inline-block;
}

form {
  margin-bottom: 30px;
  display: flex;
  gap: 10px;
}

input[type="text"] {
  padding: 10px;
  font-size: 1rem;
  width: 300px;
  border: none;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  background-color: #e50914;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #ff1e2d;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  width: 100%;
  max-width: 1000px;
}

.card {
  background-color: #1e1e1e;
  border-radius: 10px;
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  text-align: left;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(229, 9, 20, 0.6);
}

.card strong {
  font-size: 1.2rem;
  color: #fff;
}

.card span {
  color: #e50914;
  display: block;
  margin-top: 5px;
}
</style>
