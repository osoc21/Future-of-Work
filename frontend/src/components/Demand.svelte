<script>
  import { postParameterData } from '../api/patch';

  import { demandParametersStore } from '../stores/demandParameters';
  import DemandParametersProvider from './DemandParametersProvider.svelte';
  console.log($demandParametersStore.data);

  const yearsArray = [];
  for (let i = 0; i < 5; i++) {
    let year = new Date().getFullYear() + i;
    yearsArray.push(year);
  }

  const attemptValueChange = async (id, year, e) => {
    e.preventDefault();
    let value;
    $demandParametersStore.data.forEach((row) => {
      const result = row.data.find((cell) => cell.id === id && year === year);
      if (result) {
        value = result;
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
          <th />
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
                  type="number"
                  data-year={cell.year}
                  data-id={cell.id}
                  value={cell.parameter}
                />
                <button on:click={(e) => attemptValueChange(cell.id, cell.year, e)}>Update</button>
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

  tr:nth-child(even) {
    background-color: #dddddd;
  }
</style>
