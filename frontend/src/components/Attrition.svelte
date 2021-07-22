<script>
  import { workforceStore } from '../stores/workforce';
  import WorkforceDataProvider from './WorkforceDataProvider.svelte';

  $: console.log($workforceStore.data);

  // $: $workforceStore.data.forEach((element) => {
  //   // console.log(element);
  //   // console.log(element.year);
  //   // console.log(Object.values(element.data));
  //   // console.log(Object.entries(element.data));

  //   // Object.values(element.data).forEach(job => {
  //   //   console.log(job[0]);
  //   // });
  // });

  $: if (!$workforceStore.isLoading) console.log($workforceStore.formattedData);
  $: console.log($workforceStore);
</script>

<WorkforceDataProvider>
  {#if $workforceStore.isLoading}
    <p>Loading...</p>
  {:else}
    <table>
      <!--
<tr>
        <th />
        {#each $workforceStore.data as header}
          <th>{header.year}</th>
        {/each}
      </tr>
      {#each $workforceStore.data as dataByYear, i}
        {#each jobFamilies as family, j}
          <tr>
            {#if i === 0}
              <td>
                {family}
              </td>
            {/if}
          </tr>
        {/each}
      {/each}
      -->
    </table>
  {/if}
</WorkforceDataProvider>

<style>
  table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
  }

  td,
  th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #dddddd;
  }
</style>
