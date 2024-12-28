/** @type {import("tailwindcss").Config} */
export default {
    content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "light": "#e9e9eb",
                "dark": "#141f38",
                "primary": "#ef4b4c",
                "secondary": "#ebc2c4",
                "tertiary": "#20325a",
            },
        },
    },
    plugins: [
        require("@tailwindcss/typography"),
    ],
}
