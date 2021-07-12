<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Home from './pages/Home.svelte';
</script>

<Router>
  <div>
    <Route path="/">
      <Home />
    </Route>
  </div>
</Router>

<style>
</style>
