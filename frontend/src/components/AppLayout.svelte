<script>
  import Navigation from './Navigation.svelte';
</script>

<div id="app" class="flex">
  <Navigation />
  <main class="flex flex-col justify-center h-screen pt-7 m-auto text-center">
    <slot />
  </main>
</div>

<style>
  main {
    line-height: 2rem;
  }
</style>
