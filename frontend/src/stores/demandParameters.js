import { writable } from 'svelte/store';

export const demandParameters = writable({
  isLoading: true,
  data: null
});
