/** @type {import('tailwindcss').Config} */
// build using the command below
// npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        'main-green': '#005035',
        'gold1' : '#a49665',
        'darker-green': '#233a30',
        'gold2': '#ad9651',
        'main-gray' : '#222',
      }
    },
  },
  plugins: [],
}
