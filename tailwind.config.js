/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'nva-noun': '#0066cc',
        'nva-noun-bg': 'rgba(0, 102, 204, 0.1)',
        'nva-verb': '#cc0000',
        'nva-verb-bg': 'rgba(204, 0, 0, 0.1)',
        'nva-adj': '#009933',
        'nva-adj-bg': 'rgba(0, 153, 51, 0.1)',
      },
      fontFamily: {
        sans: ['Roboto', 'system-ui', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
      },
      backgroundColor: {
        'page': 'var(--page-background)',
      }
    },
  },
  plugins: [],
}
