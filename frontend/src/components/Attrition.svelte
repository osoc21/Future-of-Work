<script>
  import { fetchWorkforceData } from '../api/fetch';

  // let things = [];
  // Colomn names for testing 
  let colNames = ["Birth date",'Cont. End'];

  let workForceDataPromise = fetchWorkforceData();

  let index = 0;
  
</script>

{#await workForceDataPromise}
  <p>Loading...</p>
{:then data}
  <table>
    <tr>
      {#each Object.keys(data.result.attrition[0]) as header}
        <th>{header}</th>
      {/each}
    </tr>
    {#each data.result.attrition as row}
      <tr>
        {#each Object.values(row) as item}
          <td>{item}</td>
        {/each}
      </tr>
    {/each}
  </table>
{:catch error}
  Oops: {error}
{/await}

<style>
  table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>