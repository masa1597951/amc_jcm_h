/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mytheme: {
          primary: "#38bdf8",

          secondary: "#818cf8",

          accent: "#1FB2A5",

          neutral: "#f3f4f6",

          "base-100": "#2A303C",

          info: "#1d4ed8",

          success: "#22c55e",

          warning: "#FBBD23",

          error: "#F87272",
        },
      },
    ],
  },
  plugins: [require("daisyui")],
};
