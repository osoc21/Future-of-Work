<script>
  import { demandDataStore } from '../stores/demandData';
  import DemandDataProvider from './DemandDataProvider.svelte';

  console.log($demandDataStore.data);

  const createWorkforceTable = () => {
    const { formattedData } = $demandDataStore;

    // List all the years available
    const years = formattedData.map((y) => y.year);

    // List the names of all the job families available
    const families = formattedData[0].jobFamilies.map((f) => f.family);

    // Create a JS representation of the table to render in HTML
    /* Resulting array has structure of
      family 1 [[ year 1 ], [ year 2 ], [ year 3 ], [...]]
      family 2 [[ year 1 ], [ year 2 ], [ year 3 ], [...]]
      family 3 [[ year 1 ], [ year 2 ], [ year 3 ], [...]]
      family ...
    */
    const table = [];
    families.forEach((_, familyIndex) => {
      table[familyIndex] = [];
      years.forEach((_, yearIndex) => {
        table[familyIndex][yearIndex] = formattedData[yearIndex].jobFamilies[familyIndex];
      });
    });
    return table;
  };

  const format = (num) => {
    // Round to 5 decimal places
    const places = 100000;
    return Math.round(num * places) / places;
  };
</script>

<DemandDataProvider>
  {#if $demandDataStore.isLoading}
    <p>Loading...</p>
  {:else}
    <table>
      <tr>
        <th>Job Family</th>
        <th>Job Title</th>
        {#each $demandDataStore.formattedData as header}
          <th>{header.year}</th>
        {/each}
      </tr>

      {#each createWorkforceTable() as familyRow}
        <tr>
          <td>{familyRow[0].family}</td>
          <td>
            {#each familyRow[0].FTEs as { role }}
              <p class="role">{role}</p>
            {/each}
          </td>
          {#each familyRow as { FTEs }}
            <td class="space-y-3">
              {#each FTEs as { amount }}
                <p>{format(amount.toFixed(5))}</p>
              {/each}
            </td>
          {/each}
        </tr>
      {/each}
    </table>
  {/if}
</DemandDataProvider>

<style>
  table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
  }

  td,
  th {
    @apply text-base;
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }
  .role {
    line-height: 2rem;
  }
</style>
