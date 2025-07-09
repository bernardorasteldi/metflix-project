<template>
  <div class="form-container">
    <h2>Registrar-se</h2>
    <form @submit.prevent="handleSubmit">
      <label for="username">Usuário</label>
      <input v-model="form.username" id="username" type="text" required />

      <label for="email">Email</label>
      <input v-model="form.email" id="email" type="email" required />

      <label for="password1">Senha</label>
      <input v-model="form.password1" id="password1" type="password" required />

      <label for="password2">Confirmar Senha</label>
      <input v-model="form.password2" id="password2" type="password" required />

      <ul v-if="errors.length">
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>

      <button type="submit">Registrar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "RegisterView",
  data() {
    return {
      form: {
        username: "",
        email: "",
        password1: "",
        password2: "",
      },
      errors: [],
    };
  },
  methods: {
    handleSubmit() {
      this.errors = [];

      // Validação simples de exemplo
      if (this.form.password1 !== this.form.password2) {
        this.errors.push("As senhas não coincidem.");
        return;
      }

      // Aqui você faria uma requisição POST para a API
      console.log("Formulário enviado:", this.form);
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
}

.form-container {
  max-width: 450px;
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

.form-container ul {
  text-align: left;
  color: #ff9999;
  margin-top: 10px;
  padding-left: 20px;
}
</style>
