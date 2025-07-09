<template>
  <div class="form-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">Usuário</label>
      <input v-model="form.username" id="username" type="text" required />

      <label for="password">Senha</label>
      <input v-model="form.password" id="password" type="password" required />

      <button type="submit">Entrar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    handleLogin() {
      console.log("Login:", this.form);
      // Aqui você pode integrar com sua API Django futuramente
      alert("Login simulado! (sem backend ainda)");
    },
  },
};
</script>

<style>
.form-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 30px;
  background-color: #1e1e1e;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(229, 9, 20, 0.3);
  text-align: center;
}

.form-container h2 {
  color: #e50914;
  margin-bottom: 20px;
  font-size: 2rem;
}

.form-container form {
  display: flex;
  flex-direction: column;
}

.form-container label {
  text-align: left;
  margin-top: 10px;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-container input {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #2a2a2a;
  color: white;
}

.form-container button {
  margin-top: 20px;
  padding: 10px;
  background-color: #e50914;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-container button:hover {
  background-color: #b20710;
}
</style>
