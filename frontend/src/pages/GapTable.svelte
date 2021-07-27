<script>
  import { fetchWorkforceData } from '../api/fetch';
  import { Link } from 'svelte-navigator';
  import AppLayout from '../components/AppLayout.svelte';
  import Gap from '../components/Gap.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';

  let promise = fetchWorkforceData;
  let sourceJson = 'users';
  // Filtering Table

  function reload(newSource) {
    sourceJson = newSource;
    promise = fetchWorkforceData();
  }
</script>

<AppLayout>
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold space-y-7">
      <div>
        <h2>Gap modelling: Table</h2>
        <p class="text-sm">
          Supply Table allows you to see FTEs per Job Title and Job Family <br />renderded from
          uploaded csv files.
        </p>
      </div>

      <div>
        <Gap />
        <Link to="/supplygraph">
          <DefaultButton>Visualize !</DefaultButton>
        </Link>
      </div>
    </div>
  </div>
</AppLayout>

<style>
</style>
