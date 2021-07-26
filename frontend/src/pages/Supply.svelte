<script>
  import AppLayout from '../components/AppLayout.svelte';
  import Attrition from '../components/Attrition.svelte';
  import { onMount } from 'svelte';

  // onMount(async () => {
  //   const response = await fetchWorkforceData();
  //   console.log(response);
  // })
</script>

<AppLayout>
  <Attrition/>
  <div class="relative flex">
 

    <div class="flex-1 font-bold">
      <h1 class="text-2xl">Supply</h1>
      <p class="text-1xl">Description</p>
    </div>
  </div>
</AppLayout>
