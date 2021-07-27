<script>
  import { Link } from 'svelte-navigator';
  import CaretDown from './CaretDown.svelte';

  let dropdowns = {};

  const toggleDropdown = (name) => {
    if (!dropdowns[name]) {
      dropdowns[name] = true;
      return;
    }
    dropdowns[name] = !dropdowns[name];
  };
</script>

<div class="navigation w-1/5 text-blue-100 h-full space-y-6 py-7 px-2 mr-8">
  <div class="px-4 pb-12">
    <Link to="/">
      <h1 class="text-white font-bold text-4xl leading-24 w-1/2 mb-4 hover:text-green-300">
        Future of Work
      </h1>
    </Link>
    <span class="text-white">
      <p class="text-base">Open Source Tool for</p>
      <p class="text-base">Strategic Workforce Planning</p>
    </span>
  </div>

  <nav>
    <ul>
      <li>
        <Link to="/fileupload">
          <span
            class="menu-wrp block py-2.5 px-4 rounded hover:bg-green-200 text-white hover:text-white"
          >
            File Upload
          </span>
        </Link>
      </li>

      <li on:click={() => toggleDropdown('supply')}>
        <Link to="">
          <div
            class="flex justify-between items-center py-2.5 px-4 rounded hover:bg-green-200 text-white hover:text-white"
          >
            Supply
            <CaretDown />
          </div>
        </Link>

        <ul class="dropdown-menu" class:active={dropdowns['supply']}>
          <li>
            <Link to="/supply-table">
              <div class="block py-2.5 px-6 text-white">Table</div>
            </Link>
          </li>

          <li>
            <Link to="/supply-graph">
              <div class="block py-2.5 px-6 text-white">Visualization</div>
            </Link>
          </li>
        </ul>
      </li>

      <li on:click={() => toggleDropdown('demand')}>
        <Link to="">
          <div
            class="flex justify-between items-center py-2.5 px-4 rounded hover:bg-green-200 text-white hover:text-white"
          >
            Demand Modeling
            <CaretDown />
          </div>
        </Link>

        <ul class="dropdown-menu" class:active={dropdowns['demand']}>
          <li>
            <Link to="/demand-parameters">
              <a href={'#'} class="block py-2.5 px-6 text-white">Parameters</a>
            </Link>
          </li>
          <li>
            <Link to="/demand-outcome">
              <a href={'#'} class="block py-2.5 px-6 text-white">Outcome</a>
            </Link>
          </li>
          <li>
            <Link to="/demand-graph">
              <a href={'#'} class="block py-2.5 px-6 text-white">Visualization</a>
            </Link>
          </li>
        </ul>
      </li>

      <li>
        <a
          href={'#'}
          class="block py-2.5 px-4 rounded hover:bg-green-200 text-white hover:text-white"
        >
          Gap Analysis
        </a>
      </li>
    </ul>
  </nav>
</div>

<style>
  .dropdown-menu {
    display: none;
  }

  .dropdown-menu.active {
    display: block;
  }

  .navigation {
    background-color: #41a37e;
  }
</style>
