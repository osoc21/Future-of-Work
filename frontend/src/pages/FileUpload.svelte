<script>
  import { uploadWorkforceData } from '../api/upload';
  import AppLayout from '../components/AppLayout.svelte';

  const fileTypes = [{ name: 'Attrition' }, { name: 'Population' }, { name: 'Retirement' }];

  //   let file2;
  const handleUpload = async (e) => {
    //TODO check if every field contains a file
    e.preventDefault();

    const formData = new FormData();
    const missingFiles = [];
    fileTypes.forEach((fileType) => {
      if (!fileType.file) {
        missingFiles.push(fileType.name);
      } else {
        console.log(fileType.file[0]);
        formData.append('files[]', fileType.file[0]);
      }
    });

    for (var value of formData.values()) {
      // console.log(value);
    }

    if (missingFiles.length > 0) {
      // show error
    } else {
      // upload
    }

    try {
      const response = await uploadWorkforceData(formData);
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };

  // for (let i = 0; i < files.length; i++) {
  //   let file = files[i];
  //   formData.append('files[]', file);
  // }
</script>

<AppLayout>
  <form method="post" enctype="multipart/form-data" on:submit={handleUpload}>
    {#each fileTypes as fileType}
      <input type="file" name={fileType.name} bind:files={fileType.file} />
    {/each}
    <input type="submit" value="Upload file" />
  </form>
</AppLayout>
