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

<div class="relative flex">
  <div id="nav-placeholder" />

  <div class="flex-1">
    <form method="post" enctype="multipart/form-data" on:submit={handleUpload}>
        <input type="file" name="files[]" multiple bind:files />
        <input type="file" name="files[]" multiple bind:files />
        <input type="file" name="files[]" multiple bind:files />
    
        <input type="submit" value="Upload File" />
      </form>   
  </div>

</div>
