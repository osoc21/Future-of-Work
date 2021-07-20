<script>
  import AppLayout from '../components/AppLayout.svelte';
  import { fetchWorkforceData } from '../api/fetch';
  import ViewPoint from '../components/ViewPoint.svelte'

  const fetchData = async () => {
    const response = await fetchWorkforceData();
    console.log(response);
}

fetchData();

</script>

<AppLayout>
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold space-y-7">
      <h1 class="text-2xl">Demand modelling: Parameters</h1>
      <p> Select your view and add-in parameters you want to calculate.
        <br>Finally, fill in the coefficients and watch the machine work!
        <br>These profiles will be used to build scenario later on.
      </p>

      <h2>Job Family</h2>
     <ViewPoint />
      <div class="grid-demand">

          <li>Profiles</li>
          <li>Parameters</li>
          <li>Coefficients</li>
          <li>
            <input placeholder="Profile" class="input-class">
            <input placeholder="Profile" class="input-class">
          </li>
          <li>
            <input placeholder="Parameter" class="input-class">
            <input placeholder="Parameter" class="input-class">
          </li>
          <li>
            <input placeholder="Coefficients" class="input-class">
            <input placeholder="Coefficients" class="input-class">
          </li>

      </div>

  </div>
</div>
</AppLayout>

<style>

.grid-demand{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 5px;
  grid-row-gap: 5px;
}

.grid-demand li:nth-child(1) {
  grid-column: 1;
  grid-row: 1;
}

input {
  display: block;
}
</style>