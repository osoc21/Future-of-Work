<script>
  import { workforceStore } from '../stores/workforce';
  import WorkforceDataProvider from './WorkforceDataProvider.svelte';

  const createWorkforceTable = () => {
    const { formattedData } = $workforceStore;

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
</script>

<WorkforceDataProvider>
  {#if $workforceStore.isLoading}
    <p>Loading...</p>
  {:else}
    <table>
      <tr>
        <th />
        {#each $workforceStore.formattedData as header}
          <th>{header.year}</th>
        {/each}
      </tr>

      {#each createWorkforceTable() as familyRow}
        <tr>
          <td>{familyRow[0].family}</td>
          {#each familyRow as { FTEs }}
            <td>
              {#each FTEs as { role, amount }}
                <p>{role}: {amount}</p>
              {/each}
            </td>
          {/each}
        </tr>
      {/each}
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
    @apply text-base;
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #dddddd;
  }
</style>
