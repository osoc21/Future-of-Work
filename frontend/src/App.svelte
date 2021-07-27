<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';
  import Supply from './pages/Supply.svelte';
  import Landing from './pages/Landing.svelte';
  import FileUpload from './pages/FileUpload.svelte';
  import SupplyTable from './pages/SupplyTable.svelte';
  import SupplyGraph from './pages/SupplyGraph.svelte';
  import DemandParameters from './pages/DemandParameters.svelte';
  import DemandOutcome from './pages/DemandOutcome.svelte';
  import GapTable from './pages/GapTable.svelte';
  import GapGraph from './pages/GapTable.svelte';
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
  <Route path="/supplytable">
    <SupplyTable />
  </Route>
  <Route path="/supplygraph">
    <SupplyGraph />
  </Route>

  <Route path="/demand-parameters">
    <DemandParameters />
  </Route>
  <Route path="/demand-outcome">
    <DemandOutcome />
  </Route>

  <Route path="/gaptable">
    <GapTable />
  </Route>
  <Route path="/gapgraph">
    <GapGraph />
  </Route>
</Router>
