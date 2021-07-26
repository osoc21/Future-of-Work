<script>
  import { fetchDemandParameters } from '../api/fetch';
  import { demandParametersStore } from '../stores/demandParameters';
  import { onMount } from 'svelte';

  onMount(async () => {
    if (!$demandParametersStore.isLoading) {
      return;
    }

    try {
      const data = await fetchDemandParameters();
      demandParametersStore.set({
        ...$demandParametersStore,
        data
      });
    } catch (err) {
      console.log(err);
    }
    demandParametersStore.set({ ...$demandParametersStore, isLoading: false });
  });
</script>

<slot />
