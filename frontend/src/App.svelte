<script>

  /**
   * Routing of the entire app.
   * If you want to add a page to you app, make sure you include it in the <Route></Route> of the Router
   * Then import a page from the  src/ pages folder
  */

  import './app.postcss';
  import { Router, Route } from 'svelte-navigator';

  import Landing from './pages/Landing.svelte';
  import FileUpload from './pages/FileUpload.svelte';

  import SupplyTable from './pages/supply/SupplyTable.svelte';
  import SupplyGraph from './pages/supply/SupplyGraph.svelte';

  import DemandParameters from './pages/demand/DemandParameters.svelte';
  import DemandOutcome from './pages/demand/DemandOutcome.svelte';
  import DemandGraph from './pages/demand/DemandGraph.svelte';

  import GapTable from './pages/gap/GapTable.svelte';
  import GapGraph from './pages/gap/GapGraph.svelte';
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
