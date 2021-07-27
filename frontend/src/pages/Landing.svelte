<script>
  import HomeLayout from '../components/layouts/HomeLayout.svelte';
  import { Link } from 'svelte-navigator';
</script>

<HomeLayout>
  <div id="container" class="m-auto w-full">
    <div class="mb-16">
      <div class="header-container m-auto mb-6">
        <h1 class="text-6xl font-bold text-left">Future</h1>
        <h1 class="text-6xl font-bold text-left">of Work</h1>
      </div>
      <span class="text-gray-700 text-xl">Open Source Tool for Strategic Workforce Planning</span>
    </div>
    <div class="mb-12 w-1/3 m-auto">
      <p class="text-xl">Welcome to Future of Work!</p>
      <p class="text-xl">
        Be ready to upload your CVS files, so they can be turned into comprehensible graphs and
        tables
      </p>
    </div>
    <Link to="/fileupload">
      <button class="start-btn rounded-full px-12 py-4 text-white text-xl">Let's go</button>
    </Link>
  </div>
</HomeLayout>

<style>
  #container {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }
  .header-container {
    width: 12%;
    line-height: 4rem;
  }
  .header-container > h1 {
    color: #3f9c79;
  }
  .start-btn {
    background-color: #3f9c79;
  }
  .start-btn:hover {
    background-color: #75c8a8;
  }
</style>
