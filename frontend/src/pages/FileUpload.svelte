<script>
  import { uploadWorkforceData } from '../api/upload';
  import AppLayout from '../components/AppLayout.svelte';
  import DefaultButton from '../components/DefaultButton.svelte';
  import { onMount } from 'svelte';

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

  onMount(() => {
    const allRanges = document.querySelectorAll('.range-wrap');

    console.log(allRanges);
    allRanges.forEach((wrap) => {
      const range = wrap.querySelector('.slider');
      const bubble = wrap.querySelector('.bubble');

      range.addEventListener('input', () => {
        setBubble(range, bubble);
      });
      setBubble(range, bubble);
    });
  });
  //Code for the range slider

  function setBubble(range, bubble) {
    
    const val = range.value;
    const min = range.min ? range.min : 1;
    const max = range.max ? range.max : 6;
    const newVal = Number(((val - min) * 100) / (max - min));
    bubble.innerHTML = val;
    
    // Sorta magic numbers based on size of the native UI thumb
    bubble.style.left = `calc(${newVal}% + (${8 - newVal * 0.3}px))`;
  }
</script>

<AppLayout>
  <div class="relative flex container-flex">
    <div class="flex-1 font-bold">
      <div>
        <h1>Upload Page</h1>
        <p>
          Please, upload ONLY csv files with the following names: <mark
            >Population, Attrition, Retirement</mark
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
          <div class="range-wrap">
            <input
              type="range"
              min="1"
              max="6"
              value="1"
              class="slider"
              id="myRange"
              name="foo"
            />
            <output class="bubble bg-green-100"><output /></output>
          </div>

          <div class="w-15">
            <label for="submit-file-button">Done?</label>
            <DefaultButton type="submit" id="submit-file-button" />
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

  .slider {
    -webkit-appearance: none;
    width: 100%;
    height: 15px;
    border-radius: 5px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: 0.2s;
    transition: opacity 0.2s;
  }
  .slider:hover {
    opacity: 1;
  }

  .slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #04aa6d;
    cursor: pointer;
  }

  .slider::-moz-range-thumb {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #04aa6d;
    cursor: pointer;
  }

  .range-wrap {
    position: relative;
    width:50%;
  }
  .bubble {
    position: absolute;
    transform: translateX(-20%);
    border-radius: 5px;
    text-align: center;
    width:30px;
    left: -15%;
    top:18px;
  }

  .bubble::after {
    content: '';
    position: absolute; 
    left: -5%;
  }
</style>
