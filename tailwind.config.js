module.exports = {
  content: [
    './templates/**/*.html', // Watch all HTML files in the templates directory and subdirectories
    './static/**/*.css', // Watch all CSS files in the static directory and subdirectories
    './static/js/**/*.js', // Watch all JS files in the static/js directory and subdirectories
  ],
  theme: {
    extend: {
      fontFamily: {
        kanit: ['Kanit', 'sans-serif'],
      },
      fontWeight: {
        thin: 100,
        extralight: 200,
        light: 300,
        normal: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
        extrabold: 800,
        black: 900,
      },
    },
  },
  plugins: [],
}
