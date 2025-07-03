/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../tasks/templates/**/*.html",     // ✅ RUTA CORRECTA a tus plantillas
    "../tasks/templates/*.html",        // ✅ Incluye también raíz si hay plantillas sueltas
    "../static/**/*.js",          // ✅ RUTA CORRECTA a tus archivos JS
    "../static/**/**/*.js",         // ✅ RUTA CORRECTA a tus archivos js
  ],
  theme: {
    extend: {
      colors: {
        'farm-green': '#22c55e',
        'farm-brown': '#92400e',
        'farm-cream': '#fef3c7',
        'farm-dark': '#1f2937',
      },
      screens: {
        'xs': '475px',
      },
    },
  },
  plugins: [],
}
