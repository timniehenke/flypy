<template>
    <div class="text-5xl text-center text-red-500">
      <p>{{ msg }}</p>
    </div> 
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Ping',
    data() {
      return {
        msg: 'Hello',
      };
    },
    methods: {
      getMessage() {
        const path = 'http://localhost:5000/ping';
        axios.get(path)
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
  
            console.error(error);
          });
      },
    },
    created() {
      this.getMessage();
    },
  };
  </script>