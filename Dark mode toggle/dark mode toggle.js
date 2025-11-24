import { useState, useEffect } from "react";

export default function ThemeToggle() {
    const themes = ["light", "dark", "high-contrast"];

    const [theme, setTheme] = useState(
        localStorage.getItem("theme") || "light"
    );

    useEffect(() => {
        document.body.className = theme;
        localStorage.setItem("theme", theme);
    }, [theme]);

    const toggleTheme = () => {
        const next = themes[(themes.indexOf(theme) + 1) % themes.length];
        setTheme(next);
    };

    return (
        <button onClick={toggleTheme}>
            Switch Theme (Current: {theme})
        </button>
    );
}
