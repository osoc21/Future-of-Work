<script>
  import AppLayout from '../components/AppLayout.svelte';
  import {Link } from 'svelte-navigator';
  import Demand from '../components/Demand.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';
</script>


<AppLayout>
  <div class="relative flex container-flex mb-36">
    <div class="flex-1 font-bold space-y-7">
      <h1 class="text-2xl">Demand modelling: Parameters</h1>
      <p>
        Select your view and add-in parameters you want to calculate.
        <br />Finally, fill in the coefficients and watch the machine work!
        <br />These profiles will be used to build scenario later on.
      </p>

      <div>
        <Demand />
        <Link to="/demand-outcome">
        <DefaultButton>
          Show outcome
        </DefaultButton>
        </Link>
      </div>
    </div>
  </div>
</AppLayout>

<style>
</style>
