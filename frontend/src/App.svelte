<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Navigation from './components/Navigation.svelte';
  import Home from './pages/Home.svelte';
  import Supply from './pages/Supply.svelte';
  import Demand from './pages/Demand.svelte';
  import Landing from './pages/Landing.svelte';
  import FileUpload from './pages/FileUpload.svelte'
</script>

<Router>
  <div id="app" class="flex">
    <main>
      <Route path="/">
        <Landing />
      </Route>
    </main>
  </div>
</Router>

<Router>
  <div id="app" class="flex">
    <Navigation />
    <main class="flex flex-col justify-center h-screen pt-7 m-auto text-center">
      <Route path="/fileupload">
        <FileUpload />
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
