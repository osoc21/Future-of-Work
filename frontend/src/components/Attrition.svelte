<script>
  import { onMount } from 'svelte';
  import { fetchWorkforceData } from '../api/fetch';

  let isLoading = true;
  let data;

  onMount(async () => {
    try {
      data = await fetchWorkforceData();
      console.log(data)
    } catch (err) {
      console.log(err);
    }
    isLoading = false;
  });

  $: attritionData = isLoading ? null : data.result.attrition.map((row) => {
    delete row.rowID;
    return row;
  })
</script>

{#if isLoading}
  <p>Loading...</p>
{:else}
  <table>
    <tr>
      {#each Object.keys(data.result.attrition[0]) as header}
        <th>{header}</th>
      {/each}
    </tr>
    {#each attritionData as row}
      <tr>
        {#each Object.values(row) as item}
          <td>{item}</td>
        {/each}
      </tr>
    {/each}
  </table>
{/if}

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