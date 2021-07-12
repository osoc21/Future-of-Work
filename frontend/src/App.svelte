<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Navigation from './components/Navigation.svelte';
  import Home from './pages/Home.svelte';
  import Supply from './pages/Supply.svelte';
</script>

<Router>
  <div id="app" class="flex">
    <Navigation />
    <main class="pt-7">
      <Route path="/">
        <Home />
      </Route>
      <Route path="/supply">
        <Supply />
      </Route>
    </main>
  </div>
</Router>

<style>
  main {
    margin: auto;
    line-height: 2rem;
    text-align: center;
  }
</style>
