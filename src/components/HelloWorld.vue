<template>
  <div class="hello-world">
    <h1>Welcome to Your Vue 3 App!</h1>
    <a-button type="primary">Get Started</a-button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HelloWorld',
});
</script>

<style scoped>
.hello-world {
  text-align: center;
  margin-top: 20px;
}
</style>