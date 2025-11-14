/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        night: '#0a101f',
        slate: '#111b2e',
        neon: {
          cyan: '#3cf6ff',
          teal: '#14b8a6',
          magenta: '#f472b6'
        }
      }
    }
  },
  plugins: []
};
