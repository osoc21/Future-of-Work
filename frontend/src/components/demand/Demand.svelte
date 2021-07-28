<script>
  import { postParameterData } from '../../api/patch';
  import { demandParametersStore } from '../../stores/demandParameters';
  import DemandParametersProvider from '../dataProviders/DemandParametersProvider.svelte';

  // Get the next 5 years for table headers
  const yearsArray = [];
  for (let i = 0; i < 5; i++) {
    let year = new Date().getFullYear() + i;
    yearsArray.push(year);
  }

  // Get changed data from cell and send it to server with patch request
  const attemptValueChange = async (id, year, e) => {
    e.preventDefault();
    let value;
    // Find the changed cell
    $demandParametersStore.data.forEach((row) => {
      const result = row.data.find((cell) => cell.id === id && cell.year === year);
      if (result) {
        value = result.parameter;
        return;
      }
    });
    await postParameterData(id, year, value);
  };
</script>

<DemandParametersProvider>
  {#if !$demandParametersStore.isLoading}
    <form>
      <table>
        <tr>
          <th>Parameters</th>
          {#each yearsArray as year}
            <th>{year}</th>
          {/each}
        </tr>

        {#each $demandParametersStore.data as row}
          <tr>
            <td>{row.name}</td>
            {#each row.data as cell}
              <td>
                <input
                  class="h-12 w-12 text-center mr-4"
                  type="number"
                  data-year={cell.year}
                  data-id={cell.id}
                  bind:value={cell.parameter}
                  on:blur={(e) => attemptValueChange(cell.id, cell.year, e)}
                />
              </td>
            {/each}
          </tr>
        {/each}
      </table>
    </form>
  {/if}
</DemandParametersProvider>

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
  button {
    background-color: #3f9c79;
  }
  button:hover {
    background-color: #75c8a8;
  }
</style>
