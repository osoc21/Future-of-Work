<script>
  import { fetchDemandData } from '../api/fetch';
  import { demandDataStore } from '../stores/demandData';
  import { onMount } from 'svelte';

  onMount(async () => {
    if (!$demandDataStore.isLoading) {
      return;
    }

    try {
      const data = await fetchDemandData();
      demandDataStore.set({
        ...$demandDataStore,
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
    demandDataStore.set({ ...$demandDataStore, isLoading: false });
  });
</script>

<slot />
