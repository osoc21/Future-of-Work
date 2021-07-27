<script>
  import { uploadWorkforceData } from '../api/upload';
  import AppLayout from '../components/AppLayout.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';

  const fileTypes = [
    { name: 'attrition' },
    { name: 'population' },
    { name: 'retirement' },
    { name: 'demand' }
  ];

  // Loading the error is Upload files are missing
  function missingUploadFiles() {
    alert('File is missing');
  }

  function successUpload() {
    alert('All files are uploaded!');
  }

  const handleUpload = async (e) => {
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
      missingUploadFiles();
      console.log('file missing');
    } else {
      successUpload();
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
</script>

<AppLayout>
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold">
      <div>
        <h1>Upload Page</h1>
        <p>
          Please, upload ONLY csv files with the following names: <mark
            >Population, Attrition, Retirement, Demand.</mark
          >
        </p>
      </div>

      <form method="post" enctype="multipart/form-data" on:submit={handleUpload}>
        <div class="form-container  space-y-5">
          {#each fileTypes as fileType, i}
            <div>
              <h2 class="text-4xl">{i + 1}</h2>
              <label for={fileType.name}>Upload {fileType.name} file</label>

              <input
                type="file"
                name={fileType.name}
                bind:files={fileType.file}
                id={fileType.name}
              />
            </div>
          {/each}

          <div class="w-15">
            <label for="submit-file-button">Done?</label>
            <DefaultButton type="submit" id="submit-file-button" on:click={missingUploadFiles} />
          </div>
        </div>
      </form>
    </div>
  </div>
</AppLayout>

<style>
  label,
  input {
    display: block;
  }
  .container-flex {
    top: 10%;
  }
  .form-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }
</style>
