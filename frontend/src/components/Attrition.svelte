<script>
  import WorkforceDataProvider from './WorkforceDataProvider.svelte';
  import { workforceData } from '../store';

  $: console.log($workforceData.data);
</script>

<WorkforceDataProvider>
  {#if $workforceData.isLoading}
    <p>Loading...</p>
  {:else}
    <table>
      <tr>
        {#each Object.keys($workforceData.data.attrition[0]) as header}
          <th>{header}</th>
        {/each}
      </tr>
      {#each $workforceData.displayableData as row}
        <tr>
          {#each Object.values(row) as item}
            <td>{item}</td>
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
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #dddddd;
  }
</style>
