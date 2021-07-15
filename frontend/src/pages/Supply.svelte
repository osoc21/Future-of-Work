<script>
  import AppLayout from '../components/AppLayout.svelte';
  import { fetchWorkforceData } from '../api/fetch';
  import { onMount } from 'svelte';

  onMount(async () => {
    const response = await fetchWorkforceData();
    console.log(response);
  })
</script>

<AppLayout>
  <div class="relative flex">
    <div id="nav-placeholder" />

    <div class="flex-1 font-bold">
      <h1 class="text-2xl">Supply</h1>
      <p class="text-1xl">Description</p>
    </div>
  </div>
</AppLayout>
