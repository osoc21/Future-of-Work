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

<h1>Basic template</h1>
<div class="chart-container" style="height:50vh; width:50vw">
  <canvas id="myChart" />
</div>

<form method="post" enctype="multipart/form-data" on:submit={handleUpload}>
  <input type="file" name="files[]" multiple bind:files />
  <input type="submit" value="Upload File" />
</form>
