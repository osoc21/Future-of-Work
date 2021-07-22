<script>
  import { fetchWorkforceData } from '../api/fetch';
  import { workforceStore } from '../stores/workforce';
  import { onMount } from 'svelte';

  onMount(async () => {
    if (!$workforceStore.isLoading) {
      return;
    }

    try {
      const data = await fetchWorkforceData();
      workforceStore.set({
        ...$workforceStore,
        data: data,
        displayableData: data.map((row) => {
          delete row.rowID;
          return row;
        })
      });
    } catch (err) {
      console.log(err);
    }
    workforceStore.set({ ...$workforceStore, isLoading: false });
  });
</script>

<slot />
