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
    <tbody>
      <table>
        <thead>{Object.keys(data.result.attrition[0]).join('')}</thead>
        {#each data.result.attrition as row, index}
          <tr>{Object.values(data.result.attrition[index]).join('')}</tr>
        {/each}
    </table>
    </tbody>
  </table>
{:catch error}
  Oops: {error}
{/await}