<script>
  import HomeLayout from '../components/HomeLayout.svelte';
  import { Link } from 'svelte-navigator';

  // const currentPage = useLocation();
  // console.log(currentPage);
</script>

<HomeLayout>
  <div id="container" class="space-y-6">
    <div>
      <h1 class="text-center text-6xl font-bold pb-6 ">Future of Work</h1>
      <span class="text-gray-700">Open Source Tool for Strategic Workforce Planning</span>
    </div>
    <div class="pt-12 w-2/3">
      <p class="m-0 text-xl">Welcome to Future of Work!</p>
      <p class="mt-0 text-xl">
        Be ready to upload your CVS files, so they can be turned into comprehensible graphs and
        tables
      </p>
    </div>
    <Link to="/fileupload">
      <button class="hover:bg-green-300 text-white rounded-full text-2xl font-bold py-4 px-20"
        >Let's go</button
      >
    </Link>
  </div>
</HomeLayout>

<style>
  #container {
    min-height: 100vh;
    margin: 0;
  }
  #container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-flow: column;
    position: fixed;
    left: 50%;
    top: 50%;
    width: 50rem;
    margin-top: -40rem;
    margin-left: -25rem;
    text-align: center;
  }
  h1 {
    width: 51.5%;
    line-height: 4rem;
    margin: auto;
    text-align: left;
    color: #41a37e;
  }

  button {
    background-color: #41a37e;
  }
</style>
