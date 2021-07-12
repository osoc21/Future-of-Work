<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Navigation from './components/Navigation.svelte';
  import Home from './pages/Home.svelte';
  import About from './pages/About.svelte';
</script>

<Router>
  <Navigation />
  <Route path="/">
    <Home />
  </Route>
  <Route path="/about">
    <About />
  </Route>
</Router>
