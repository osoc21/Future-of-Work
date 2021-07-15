<script>
  import { uploadWorkforceData } from '../api/upload';
  import AppLayout from '../components/AppLayout.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';

  const fileTypes = [{ name: 'attrition' }, { name: 'population' }, { name: 'retirement' }];

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
        formData.append(fileType.name, fileType.file[0]);
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

      console.log(response.ID);
      localStorage.setItem('globalId', response.ID);
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
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold">
      
        <form method="post" enctype="multipart/form-data" on:submit={handleUpload} >
          
          <div class="form-container  ">
            
            {#each fileTypes as fileType, i}
            <div>
              <h2 class="text-4xl">{i+1}</h2>
              <label for={fileType.name}>Upload {fileType.name} file</label>
              <input type="file" name={fileType.name} bind:files={fileType.file}  id={fileType.name} />
            </div>
              
            {/each}
            <DefaultButton type="submit"></DefaultButton>
            <!-- <input type="submit" value="Upload file" /> -->

          </div>
        </form>
          
    </div>
  </div>
</AppLayout>

<style>
  label,input{
    display: block;
  }
  .container-flex{
    top:20%;
  }
  .form-container {
    display:grid;
    grid-template-rows: repeat(2, 1fr);
    grid-template-columns: repeat(2, 1fr);
    row-gap: 1em;
  }




</style>
