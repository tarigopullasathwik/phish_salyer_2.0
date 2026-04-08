import React, { useEffect, useRef } from 'react';

const MatrixRainingCode = ({ className = "fixed inset-0 pointer-events-none -z-10 opacity-30" }) => {
    const canvasRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');

        // Set size based on parent element or window
        const handleResize = () => {
            if (canvas.parentElement && className.includes('absolute')) {
                canvas.width = canvas.parentElement.clientWidth;
                canvas.height = canvas.parentElement.clientHeight;
            } else {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
        };

        window.addEventListener('resize', handleResize);
        handleResize();

        // Characters to display
        const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?/αβγδεζηθικλμνξοπρστυφχψω';
        const charArray = chars.split('');

        const fontSize = 16;
        const columns = Math.ceil(canvas.width / fontSize);

        // An array to store the current position of each drop
        const drops = [];
        for (let x = 0; x < columns; x++) {
            drops[x] = Math.random() * -100; // Random start positions above screen
        }

        const draw = () => {
            // Semi-transparent black to create trailing effect
            ctx.fillStyle = 'rgba(2, 6, 23, 0.05)'; // Matches flow background
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#0f172a'; // Reset character base color
            ctx.font = fontSize + 'px monospace';

            for (let i = 0; i < drops.length; i++) {
                // Randomly pick a character
                const text = charArray[Math.floor(Math.random() * charArray.length)];
                
                // Color gradient for the drop
                const opacity = Math.random();
                if (Math.random() > 0.98) {
                   ctx.fillStyle = '#10b981'; // Bright green head
                } else {
                   ctx.fillStyle = 'rgba(16, 185, 129, 0.2)'; // Subtle matrix green
                }

                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                // Move drop down
                drops[i]++;

                // Reset drop if it reaches bottom or randomly after it's off-screen
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
            }
        };

        const interval = setInterval(draw, 50);

        return () => {
            clearInterval(interval);
            window.removeEventListener('resize', handleResize);
        };
    }, [className]);

    return (
        <canvas
            ref={canvasRef}
            className={className}
            style={{ filter: 'blur(0.5px)' }}
        />
    );
};

export default MatrixRainingCode;
