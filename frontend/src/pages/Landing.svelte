<script>
    import { Link } from 'svelte-navigator';
    import {  useLocation } from 'svelte-navigator';

    // const currentPage = useLocation();
    // console.log(currentPage);
</script>

<div id="container" class="space-y-6">
  <h1 class="text-2xl font-bold">Strategic Workflow</h1>
  <p class="max-w-prose">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras magna justo, lacinia in libero ac,
    auctor tincidunt quam. Aenean tempor neque leo, nec accumsan quam ullamcorper quis. Quisque
    gravida aliquet turpis, sed porttitor odio lobortis id. In consectetur non eros at semper.
  </p>
  <button class="bg-green-200 hover:bg-green-100 rounded-full py-5 px-20" >
      <Link to="/fileupload">START></Link>
    </button>
</div>

<style>
  html,
  body,
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
    /* margin-top: -40rem; */
    margin-left: -25rem;
    text-align: center;
  }
</style>
