<script>
  import Navigation from './Navigation.svelte';

</script>

<div id="app" class="flex">
  <Navigation />
  <main class="relative w-full">
    <slot />
  </main>
</div>

<style>
  main {
    line-height: 2rem;
  }
</style>
