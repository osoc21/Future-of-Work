<script>
  import WorkforceDataProvider from './WorkforceDataProvider.svelte';
  import { workforceData } from '../store';

  $: console.log($workforceData.data);

  // $: $workforceData.data.forEach((element) => {
  //   // console.log(element);
  //   // console.log(element.year);
  //   // console.log(Object.values(element.data));
  //   // console.log(Object.entries(element.data));

  //   // Object.values(element.data).forEach(job => {
  //   //   console.log(job[0]);
  //   // });
  // });
</script>

<WorkforceDataProvider>
  {#if $workforceData.isLoading}
    <p>Loading...</p>
  {:else}
    <table>
      <tr>
        <th />
        {#each $workforceData.data as header}
          <th>{header.year}</th>
        {/each}
      </tr>
      
      {#each $workforceData.data as yearOfData}
        {#each Object.values(yearOfData.data) as jobFamily}
          {#each jobFamily as job}
            {#each Object.entries(job) as [jobTitle,FTE]}
              <tr>
                <td>{jobTitle}</td>
                <td>{FTE}</td>
              </tr>
            {/each} 
          {/each}
        {/each}
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
