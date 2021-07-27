<script>
  import AppLayout from '../components/AppLayout.svelte';
  import DemandTable from '../components/DemandTable.svelte';
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
</AppLayout>

<style>
</style>
