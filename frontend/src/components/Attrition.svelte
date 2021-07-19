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
  <!-- {console.log(data['result']['attrition'])} -->
  <!-- {console.log(Object.entries(Object.entries(data["result"]["attrition"])))}

  {console.log(Object.entries(Object.entries(data["result"]["attrition"])[0][1]))}
  {console.log(data["result"]["attrition"][0])} -->
  <table>
    <thead>
      <tr>
        <th />
      </tr>
    </thead>
    <tbody>
      {#each Object.entries(data.result.attrition) as row, index}
          <li>{index + 1}</li>
          {console.log(row[1])}
          {#each row as item}
            <p>{item}</p>
          {/each}
      {/each}
      <!-- {#each Object.entries(Object.entries(data["result"]["attrition"])[0][1]) as item}
        <tr>
          {#each item as col, index}
            <td>{col}</td>
          {/each}
        </tr>
      {/each} -->
    </tbody>
  </table>
{:catch error}
  Oops: {error}
{/await}