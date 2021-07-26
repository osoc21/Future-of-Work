<script>
  import { demandParameters } from '../stores/demandParameters';
  import DemandParametersProvider from './DemandParametersProvider.svelte';
</script>

<DemandParametersProvider>
  {console.log(demandParameters)}
</DemandParametersProvider>
