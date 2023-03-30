/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    
    extend: {
      fontFamily: {
        'oswald': ['Oswald', 'sans-serif']
      },
      colors: {
        "main-green": "#005035",
        "gold1":" #a49665",
        "darker-green": "#233a30",
        "gold2": "#ad9651",
        "main-gray": "#222",
        "main-gold": "#a49665"
      }
    },
  },
  plugins: [],
}
