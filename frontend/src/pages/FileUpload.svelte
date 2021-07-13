<script>
  import { uploadWorkforceData } from '../api/upload';

  let file2;
  let file1;

  

//   let file2;
  const handleUpload = async (e) => {
      //TODO check if every field contains a file
    e.preventDefault();

    const formData = new FormData();
    // for (let i = 0; i < files.length; i++) {
    //   let file = files[i];
    //   formData.append('files[]', file);
    // }

    formData.append('files[]',file1[0]);
    formData.append('files[]',file2[0]);    

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
        <input type="file" multiplename="file1" bind:files={file1} />
        <input type="file" name="file2" bind:files={file2} />
        <!-- <input type="file" name="file2" bind:file2 /> -->

    
        <input type="submit" value="Upload File" />
      </form>   
  </div>

</div>
