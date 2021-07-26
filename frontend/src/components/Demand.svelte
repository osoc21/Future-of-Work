<script>
  import { demandParametersStore } from '../stores/demandParameters';
  import DemandParametersProvider from './DemandParametersProvider.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';

  const yearsArray = [];
  for (let i = 0; i < 5; i++) {
    let year = new Date().getFullYear() + i;
    yearsArray.push(year);
  }
</script>

<DemandParametersProvider>
  {#if !$demandParametersStore.isLoading}
    <form>
      <table>
        <tr>
          <td />
          {#each yearsArray as year}
            <th>{year}</th>
          {/each}
        </tr>
        {#each $demandParametersStore.data as param}
          <tr>
            <td>{param}</td>
            <td><input type="number" /></td>
            <td><input type="number" /></td>
            <td><input type="number" /></td>
            <td><input type="number" /></td>
            <td><input type="number" /></td>
          </tr>
        {/each}
      </table>
      <DefaultButton type="submit" />
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
