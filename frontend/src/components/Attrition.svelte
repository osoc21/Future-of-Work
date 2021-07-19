<script>
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
      <th></th>
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
</table>