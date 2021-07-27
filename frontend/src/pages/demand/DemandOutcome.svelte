<script>
  import { Link } from 'svelte-navigator';
  import AppLayout from '../../components/layouts/AppLayout.svelte';
  import DemandTable from '../../components/demand/DemandTable.svelte';
  import DefaultButton from '../../components/DefaultButton.svelte';
</script>

<AppLayout>
  <div class="relative flex container-flex mb-36">
    <div class="flex-1 font-bold space-y-7">
      <h1 class="text-2xl">Demand Outcome</h1>
      <p>
        Here you can see the scenario outcome of the previous table with your inserted coefficients!
      </p>
    </div>
  </div>
  <DemandTable />
  <Link to="/demand-graph">
    <DefaultButton>Visualize !</DefaultButton>
  </Link>
</AppLayout>

<style>
</style>
