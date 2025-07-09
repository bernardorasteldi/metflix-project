<template>
  <div class="section">
    <h2 class="section-title">Biblioteca</h2>

    <div class="section">
      <h3 class="section-title">Jogos</h3>
      <div class="card-grid">
        <div v-for="jogo in jogos" :key="jogo.id" class="card">
          <h3>{{ jogo.nome }}</h3>
          <p><span>Lançamento:</span> {{ jogo.data_lancamento }}</p>
          <p><span>Preço:</span> R$ {{ jogo.preco }}</p>
          <button @click="remover('jogo', jogo.id)">
            Remover da Biblioteca
          </button>
        </div>
      </div>
    </div>

    <div class="section">
      <h3 class="section-title">Filmes e Séries</h3>
      <div class="card-grid">
        <div v-for="filme in filmes" :key="filme.id" class="card">
          <h3>{{ filme.nome }}</h3>
          <p><span>Lançamento:</span> {{ filme.data_lancamento }}</p>
          <p><span>Gênero:</span> {{ filme.genero }}</p>
          <button @click="remover('filme', filme.id)">
            Remover da Biblioteca
          </button>
        </div>
      </div>
    </div>

    <div v-if="mensagem" class="mensagens">
      <div class="mensagem success">{{ mensagem }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BibliotecaView",
  data() {
    return {
      jogos: [],
      filmes: [],
      mensagem: "",
    };
  },
  mounted() {
    // Substitua por chamada real à API futuramente
    this.jogos = [
      { id: 1, nome: "The Witcher 3", data_lancamento: "2015", preco: 89.9 },
      { id: 2, nome: "Hollow Knight", data_lancamento: "2017", preco: 39.9 },
    ];
    this.filmes = [
      { id: 1, nome: "Breaking Bad", data_lancamento: "2008", genero: "Drama" },
      { id: 2, nome: "Matrix", data_lancamento: "1999", genero: "Ação" },
    ];
  },
  methods: {
    remover(tipo, id) {
      this.mensagem = `${
        tipo === "jogo" ? "Jogo" : "Filme"
      } removido com sucesso!`;
      setTimeout(() => {
        this.mensagem = "";
      }, 5000);
    },
  },
};
</script>

<style scoped>
/* ... mesmo estilo CSS do Django, copiado e adaptado ... */

body {
  background-color: #141414;
  color: #fff;
  font-family: "Roboto", sans-serif;
  margin: 0;
}

.section-title {
  font-size: 2.5rem;
  margin: 40px 20px 20px;
  color: #e50914;
  border-bottom: 2px solid #e50914;
  display: inline-block;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 0 20px 40px;
}

.card {
  background-color: #1e1e1e;
  border-radius: 10px;
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(229, 9, 20, 0.6);
}

.card h3 {
  margin-top: 0;
  color: #fff;
  font-size: 1.4rem;
}

.card p {
  margin: 5px 0;
  color: #ccc;
}

.card span {
  color: #e50914;
}

button {
  margin-top: 10px;
  padding: 10px;
  background-color: #e50914;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #b20710;
}

.mensagens {
  position: fixed;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
  width: auto;
  max-width: 80%;
  text-align: center;
}

.mensagem {
  background-color: #e50914;
  color: #fff;
  padding: 15px 25px;
  margin: 0 auto;
  border-radius: 5px;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
  animation: fadeOut 5s forwards;
  display: inline-block;
}

@keyframes fadeOut {
  0%,
  80% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    display: none;
  }
}
</style>
