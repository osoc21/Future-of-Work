<script>
  import AppLayout from '../components/AppLayout.svelte';
  import { fetchDemandParameters } from '../api/fetch';
  import ViewPoint from '../components/ViewPoint.svelte';

  const fetchData = async () => {
    const response = await fetchDemandParameters();
    console.log(response);
  };

  fetchData();
</script>


<AppLayout>
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold space-y-7">
      <h1 class="text-2xl">Demand modelling: Parameters</h1>
      <p>
        Select your view and add-in parameters you want to calculate.
        <br />Finally, fill in the coefficients and watch the machine work!
        <br />These profiles will be used to build scenario later on.
      </p>

      <h2>Select your view</h2>
      <ViewPoint />
    </div>
  </div>
</AppLayout>

<style>
</style>
