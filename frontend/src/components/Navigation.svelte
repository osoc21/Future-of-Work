<script>
  import { Link } from 'svelte-navigator';

  var dropdownMenusWrp = document.querySelectorAll('.dropdown-menu-wrp');

  dropdownMenusWrp.forEach((dropDownMenuWrp) => {
    dropDownMenuWrp.addEventListener('click', function () {
      let dropDownMenu = dropDownMenuWrp.querySelector('.dropdown-menu');
      dropDownMenu.classList.toggle('active');
    });
  });
</script>

<div class="bg-green-300 w-1/6 text-blue-100 h-screen space-y-6 py-7 px-2 mr-8">
  <Link to="/">
    <span class="text-white flex items-center space-x-2 px-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-8 w-8"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
        />
      </svg>
      <span class="text-2xl font-extrabold">Future of Work</span>
    </span>
  </Link>

  <nav>
    <ul class="space-y-3">
      <li>
        <Link to="/">
          <span
            class="menu-wrp block py-2.5 px-4 rounded hover:bg-green-200 text-green-900 hover:text-white"
          >
            Home
          </span>
        </Link>
      </li>

      <li class="dropdown-menu-wrp menu-wrp">
        <Link to="/supply">
          <span class="flex py-2.5 px-4 rounded hover:bg-green-200 text-green-900 hover:text-white">
            Supply
          </span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </Link>

        <ul class="dropdown-menu space-y-1">
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Input</a></li>
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Attrition Table</a></li>
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Graphs</a></li>
        </ul>
      </li>

      <li class="dropdown-menu-wrp">
        <a
          href="#"
          class="flex py-2.5 px-4 rounded hover:bg-green-200 text-green-900 hover:text-white"
          >Demand Modeling
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </a>

        <ul class="dropdown-menu space-y-1">
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Input</a></li>
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Table</a></li>
          <li><a href="#" class="block py-2.5 px-6 text-green-900">Graphs</a></li>
        </ul>
      </li>

      <li>
        <a
          href="#"
          class="block py-2.5 px-4 rounded hover:bg-green-200 text-green-900 hover:text-white"
          >Gap Analysis</a
        >
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
</style>
