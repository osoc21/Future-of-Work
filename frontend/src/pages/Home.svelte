<svelte:head>
  <title>Home | Strategic Workforce Planning</title>
</svelte:head>

<h1>Basic template</h1>
<div class="chart-container" style="height:50vh; width:50vw">
  <canvas id="myChart" />
</div>

<form method="post" enctype="multipart/form-data">
  <input type="file" name="files[]" multiple />
  <input type="submit" value="Upload File" name="submit" />
</form>
