<template>
  <div>
    <h2 class="section-title">Filmes e Séries</h2>

    <div class="card-grid">
      <div v-for="filme in filmesSeries" :key="filme.id" class="card">
        <h3>{{ filme.nome }}</h3>
        <p><span>Gênero:</span> {{ filme.genero }}</p>
        <p><span>Lançamento:</span> {{ filme.data_lancamento }}</p>
        <form @submit.prevent="adicionarFilme(filme.id)">
          <button type="submit">Adicionar à Biblioteca</button>
        </form>
      </div>
    </div>

    <div v-if="mensagem" class="mensagens">
      <div class="mensagem success">{{ mensagem }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilmesSeriesView",
  data() {
    return {
      filmesSeries: [],
      mensagem: "",
    };
  },
  mounted() {
    fetch("/api/filmes_series")
      .then((res) => res.json())
      .then((data) => {
        this.filmesSeries = data;
      });
  },
  methods: {
    async adicionarFilme(id) {
      const response = await fetch(`/api/adicionar-filme/${id}`, {
        method: "POST",
        headers: {
          "X-CSRFToken": this.getCookie("csrftoken"),
        },
      });
      if (response.ok) {
        this.mensagem = "Adicionado à Biblioteca!";
        setTimeout(() => (this.mensagem = ""), 5000);
      }
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
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

.mensagens {
  position: fixed;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
  max-width: 80%;
  text-align: center;
}

.mensagem {
  background-color: #e50914;
  color: #fff;
  padding: 15px 25px;
  border-radius: 5px;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
  animation: fadeOut 5s forwards;
  display: inline-block;
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  80% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    display: none;
  }
}
</style>
