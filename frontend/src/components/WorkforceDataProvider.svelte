<script>
  import { fetchWorkforceData } from '../api/fetch';
  import { workforceData } from '../store';
  import { onMount } from 'svelte';

  onMount(async () => {
    if (!$workforceData.isLoading) {
      return;
    }

    try {
      const data = await fetchWorkforceData();
      console.log('testset', data);
      workforceData.set({
        ...$workforceData,
        data: data,
        displayableData: data.map((row) => {
          delete row.rowID;
          return row;
        })
      });
    } catch (err) {
      console.log(err);
    }
    workforceData.set({ ...$workforceData, isLoading: false });
  });
</script>

<slot />
