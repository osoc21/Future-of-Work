<!-- <script>
  import { fetchWorkforceData } from '../api/fetch';

  let things = [];
  let colNames = [];

  const getData = async () => {
    const response = await fetchWorkforceData();
    console.log(response);

  }

  getData();


</script>

<table>
  <thead>
    <tr>
      {#each colNames as col}
    <th>{col} &varr;</th>
  {/each}
    </tr>
  </thead>
  <tbody>
    {#each things as thing, index (thing.id)}
      <tr>
        {#each colNames as col, index}
          <td>{thing[col]}</td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table> -->


<script>
  import { fetchWorkforceData } from '../api/fetch';

  // let things = [];
  // Colomn names for testing 
  let colNames = ["Birth date",'Cont. End'];

  let workForceDataPromise = fetchWorkforceData();

  
</script>

{#await workForceDataPromise}
  <p>Loading...</p>
  {console.log("test")}
{:then data}
  <!-- {console.log(data['result']['attrition'])} -->
  {console.log(Object.entries(Object.entries(data["result"]["attrition"])))}

  {console.log(Object.entries(Object.entries(data["result"]["attrition"])[0][1]))}
  {console.log(data["result"]["attrition"][0])}
  <table>
    <thead>
      <tr>
        <th />
      </tr>
    </thead>
    <tbody>
      {#each Object.entries(Object.entries(data["result"]["attrition"])[0][1]) as item}
        <tr>
          
          {#each item as col, index}
            <td>{col}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
{:catch error}
  Oops: {error}
{/await}