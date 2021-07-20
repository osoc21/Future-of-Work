<div class="relative inline-block  text-gray-700">
    <select on:change={() => document.getElementById('jsonSelector').value} id="jsonSelector"  class="w-full h-10 pl-3 pr-6 text-base placeholder-gray-600 border rounded-lg appearance-none focus:shadow-outline " placeholder="Select">
      <!-- {console.log(document.getElementById('test'))} -->
      <option value="" hidden>View</option>
      <option value="FTE" id="test">Profile </option>
      <option value="job-family">Job Family</option>
    </select>
    
    <div class="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none">
        <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" fill-rule="evenodd">
            </path>
        </svg>
    </div>
  </div>  