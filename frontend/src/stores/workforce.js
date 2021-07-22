import { writable } from 'svelte/store';

export const workforceStore = writable({
  isLoading: true,
  data: null,
  displayableData: null
});
