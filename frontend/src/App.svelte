<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  // import Home from './pages/Home.svelte';
  import Supply from './pages/Supply.svelte';
  import Demand from './pages/Demand.svelte';
  import Landing from './pages/Landing.svelte';
  import FileUpload from './pages/FileUpload.svelte';
</script>

<Router>
  <Route path="/">
    <Landing />
  </Route>

  <Route path="/fileupload">
    <FileUpload />
  </Route>

  <Route path="/supply">
    <Supply />
  </Route>
  <Route path="/demand">
    <Demand />
  </Route>
</Router>
