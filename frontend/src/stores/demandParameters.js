import { writable } from 'svelte/store';

export const demandParametersStore = writable({
  isLoading: true,
  data: null
});
