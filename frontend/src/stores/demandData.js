import { writable } from 'svelte/store';

export const demandDataStore = writable({
  isLoading: true,
  data: null,
  formatteData: null
});
