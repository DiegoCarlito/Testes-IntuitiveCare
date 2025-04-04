<template>
  <div id="app" class="container">
    <h1>Busca de Operadoras Ativas</h1>
    <input v-model="query" @keyup.enter="buscarOperadoras" placeholder="Digite o nome da operadora" />
    <button @click="buscarOperadoras">Buscar</button>

    <div v-if="operadoras.length" class="result-box">
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.registro_ans">
          <p><strong>{{ operadora.nome_fantasia }}</strong></p>
          <p>{{ operadora.razao_social }}</p>
        </li>
      </ul>
    </div>

    <p v-else-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: "",
      operadoras: [],
      errorMessage: ""
    };
  },
  methods: {
    async buscarOperadoras() {
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/buscar?q=${this.query}`);
        const data = await res.json();
        if (data && data.length) {
          this.operadoras = data;
          this.errorMessage = "";
        } else {
          this.operadoras = [];
          this.errorMessage = "Nenhuma operadora encontrada.";
        }
      } catch (error) {
        this.operadoras = [];
        this.errorMessage = "Erro ao buscar as operadoras. Tente novamente.";
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 80px auto;
  padding: 2rem;
  text-align: center;
  font-family: 'Segoe UI', sans-serif;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.08);
}

h1 {
  margin-bottom: 2rem;
  font-size: 1.8rem;
  color: #333;
}

input {
  width: 80%;
  padding: 10px;
  font-size: 1rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  outline: none;
}

button {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color: #379f6e;
}

.result-box {
  margin-top: 2rem;
  text-align: left;
}

li {
  list-style: none;
  background: white;
  padding: 1rem;
  margin-bottom: 0.75rem;
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.05);
}

.error {
  color: #cc0000;
  margin-top: 2rem;
}
</style>
