<script>
  import { uploadWorkforceData } from '../api/upload';

  let files;
  const handleUpload = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      let file = files[i];
      formData.append('files[]', file);
    }

    try {
      const response = await uploadWorkforceData(formData);
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };
</script>

<svelte:head>
  <title>Home | Strategic Workforce Planning</title>
</svelte:head>

<div id="container" class="space-y-6">
  <h1 class="text-2xl font-bold">Strategic Workflow</h1>
  <p class="max-w-prose">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras magna justo, lacinia in libero ac,
    auctor tincidunt quam. Aenean tempor neque leo, nec accumsan quam ullamcorper quis. Quisque
    gravida aliquet turpis, sed porttitor odio lobortis id. In consectetur non eros at semper.
  </p>
  <button class="bg-green-200 hover:bg-green-100 rounded-full py-5 px-20">START</button>
</div>

<!--
  <form method="post" enctype="multipart/form-data" on:submit={handleUpload}>
  <input type="file" name="files[]" multiple bind:files />
  <input type="submit" value="Upload File" />
</form>
 -->
<style>
</style>
