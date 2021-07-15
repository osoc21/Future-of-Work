<script>
  import AppLayout from '../components/AppLayout.svelte';
  import dataStore from '../dataStore';

  $: console.log($dataStore.workforceData);
</script>

<AppLayout>
  <h1>Gap analysis</h1>
</AppLayout>
