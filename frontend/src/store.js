import { writable } from 'svelte/store';

export const workforceData = writable({
  isLoading: true,
  data: null,
  displayableData: null
});