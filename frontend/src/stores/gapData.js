import { writable } from 'svelte/store';

export const gapDataStore = writable({
  isLoading: true,
  data: null,
  formatteData: null
});
