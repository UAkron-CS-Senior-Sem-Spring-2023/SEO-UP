import {defineConfig} from 'astro/config';

// https://astro.build/config
// https://vitejs.dev/config/
export default defineConfig({
    server: {
        host: '0.0.0.0',
        port: 3000,
        proxy: {
            '/api/scraper': 'http://scraper:3001'
        },
        strictPort: true,
        hmr: {
            port: 3000,
            clientPort: 80
        }
    }
});

