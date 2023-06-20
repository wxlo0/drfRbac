// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from "path"

export default defineConfig({
  plugins: [
      vue()
  ],
  css: {
    preprocessorOptions: {
      scss: {additionalData: ``},
    }
  },
  resolve: {
    alias: [
      {
        find: '@',
        replacement: resolve(__dirname, './src'),
      }
    ]
  },
  server: {
    port: 8080,
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:8000/api/v1',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      }
    }
  }

})
