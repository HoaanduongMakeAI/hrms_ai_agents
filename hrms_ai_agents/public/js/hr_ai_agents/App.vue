<script setup>
import { ref } from "vue";

const dynamicMessage = ref("Hello from App.vue");
</script>
<template>
  <div>
	<h3>{{ dynamicMessage }}</h3>
    <h4>Start editing at hrms_ai_agents/public/js/hr_ai_agents/App.vue</h4>
  </div>
</template>