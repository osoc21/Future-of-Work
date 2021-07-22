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
        data,
        /*
          Run a transformation to make the API response easier to work with,
          Ideally this is temporary fix
        */
        formattedData: data.reduce((acc, { year }, i) => {
          const yearData = data[i].data;
          const jobFamily = Object.keys(yearData).map((d) => ({
            family: d,
            FTEs: yearData[d].map((f) => ({
              role: Object.keys(f)[0],
              amount: f[Object.keys(f)[0]]
            }))
          }));
          acc.push({
            year,
            jobFamilies: jobFamily
          });
          return acc;
        }, [])
      });
    } catch (err) {
      console.log(err);
    }
    workforceStore.set({ ...$workforceStore, isLoading: false });
  });
</script>

<slot />
