<template>
  <div id="app">
    <h1>Busca de Operadoras Ativas</h1>
    <input v-model="query" placeholder="Digite o nome da operadora" />
    <button @click="buscarOperadoras">Buscar</button>
    <ul v-if="operadoras.length">
      <li v-for="operadora in operadoras" :key="operadora.registro_ans">
        <p>{{ operadora.razao_social }} ({{ operadora.nome_fantasia }})</p>
      </li>
    </ul>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
      operadoras: [],
      errorMessage: ''
    };
  },
  methods: {
    async buscarOperadoras() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/buscar?q=${this.query}`);
        if (!response.ok) {
          throw new Error('Erro na busca');
        }
        const data = await response.json();
        this.operadoras = data;
        this.errorMessage = '';
      } catch (error) {
        this.errorMessage = 'Erro ao buscar as operadoras. Tente novamente.';
        this.operadoras = [];
      }
    }
  }
};
</script>

<style scoped>
input {
  padding: 8px;
  margin-right: 10px;
}

button {
  padding: 8px;
}

ul {
  margin-top: 20px;
}
</style>
