import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

const isProduction = process.env.NODE_ENV === 'production';
export default defineConfig({
  plugins: [
    svelte({
      hot: !isProduction,
      emitCss: true,
      extensions: ['.svelte']
    })
  ],
  // https://github.com/mefechoel/svelte-navigator#im-using-vite-why-am-i-getting-errors-with-svelte-navigator
  optimizeDeps: { exclude: ['svelte-navigator'] }
});
