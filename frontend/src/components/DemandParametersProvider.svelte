<script>
  import { fetchDemandParameters } from '../api/fetch';
  import { demandParameters } from '../stores/demandParameters';
  import { onMount } from 'svelte';

  onMount(async () => {
    if (!demandParameters.isLoading) {
      return;
    }

    try {
      const data = await fetchDemandParameters();
      demandParameters.set({
        ...$demandParameters,
        data
      });
    } catch (err) {
      console.log(err);
    }
    demandParameters.set({ ...$demandParameters, isLoading: false });
  });
</script>

<slot />
