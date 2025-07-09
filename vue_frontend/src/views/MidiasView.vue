<template>
  <div class="container">
    <h2 class="section-title">Filmes</h2>
    <div class="card-container">
      <div v-for="filme in filmes" :key="'filme-' + filme.id" class="card">
        <strong>{{ filme.titulo }}</strong>
      </div>
      <p v-if="filmes.length === 0">Nenhum filme encontrado.</p>
    </div>

    <h2 class="section-title">Séries</h2>
    <div class="card-container">
      <div v-for="serie in series" :key="'serie-' + serie.id" class="card">
        <strong>{{ serie.titulo }}</strong>
      </div>
      <p v-if="series.length === 0">Nenhuma série encontrada.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MidiasView",
  data() {
    return {
      filmes: [],
      series: [],
    };
  },
  mounted() {
    fetch("/api/midias")
      .then((res) => res.json())
      .then((data) => {
        this.filmes = data.filmes || [];
        this.series = data.series || [];
      });
  },
};
</script>

<style scoped>
.section-title {
  font-size: 2.5rem;
  margin: 40px 20px 20px;
  color: #e50914;
  border-bottom: 2px solid #e50914;
  display: inline-block;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 0 20px 40px;
}

.card {
  background-color: #1e1e1e;
  border-radius: 10px;
  padding: 20px;
  color: #fff;
  font-size: 1.2rem;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(229, 9, 20, 0.6);
}
</style>
