<script>
  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';

  import Landing from './pages/Landing.svelte';
  import FileUpload from './pages/FileUpload.svelte';
  import SupplyTable from './pages/SupplyTable.svelte';
  import SupplyGraph from './pages/SupplyGraph.svelte';
  import DemandParameters from './pages/DemandParameters.svelte';
  import DemandOutcome from './pages/DemandOutcome.svelte';
  import DemandGraph from './pages/DemandGraph.svelte';

  import GapTable from './pages/GapTable.svelte';
  import GapGraph from './pages/GapGraph.svelte';
</script>

<Router>
  <Route path="/">
    <Landing />
  </Route>

  <Route path="/fileupload">
    <FileUpload />
  </Route>
  <Route path="/supply-table">
    <SupplyTable />
  </Route>
  <Route path="/supply-graph">
    <SupplyGraph />
  </Route>

  <Route path="/demand-parameters">
    <DemandParameters />
  </Route>
  <Route path="/demand-outcome">
    <DemandOutcome />
  </Route>
  <Route path="/demand-graph">
    <DemandGraph />
  </Route>
  <Route path="/gaptable">
    <GapTable />
  </Route>
  <Route path="/gapgraph">
    <GapGraph />
  </Route>

</Router>
