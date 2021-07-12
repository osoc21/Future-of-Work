<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Navigation from './components/Navigation.svelte';
  import Home from './pages/Home.svelte';
  import Supply from './pages/Supply.svelte';
  import Demand from './pages/Demand.svelte';
</script>

<Router>
  <div id="app" class="flex">
    <Navigation />
    <main class="flex flex-col justify-center h-screen pt-7 m-auto text-center">
      <Route path="/">
        <Home />
      </Route>
      <Route path="/supply">
        <Supply />
      </Route>
      <Route path="/demand">
        <Demand />
      </Route>
    </main>
  </div>
</Router>

<style>
  main {
    line-height: 2rem;
  }
</style>
