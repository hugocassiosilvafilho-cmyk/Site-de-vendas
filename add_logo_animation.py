import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add CSS for the cyberpunk logo
new_css = """
        /* Cyberpunk Logo Animation */
        .cyber-logo-container {
            position: relative;
            display: inline-block;
            margin: 0 auto 30px;
            width: 150px;
            height: 150px;
            z-index: 10;
        }

        .cyber-logo {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 20px;
            position: relative;
            z-index: 5;
            animation: cyber-float 8s ease-in-out infinite;
            box-shadow: 0 0 30px rgba(0, 245, 255, 0.4);
            background: rgba(5, 8, 22, 0.5);
            border: 2px solid rgba(0, 245, 255, 0.3);
        }

        .cyber-glow-bg {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, rgba(0,245,255,0.4) 0%, rgba(138,43,226,0.2) 40%, transparent 70%);
            filter: blur(40px);
            z-index: 1;
            animation: pulse-glow 8s ease-in-out infinite;
        }

        @keyframes pulse-glow {
            0%, 100% { opacity: 0.6; transform: translate(-50%, -50%) scale(0.9); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
        }

        @keyframes cyber-float {
            0%, 100% {
                transform: translateY(0) scale(1) rotate(-3deg);
                box-shadow: 0 0 30px rgba(0, 245, 255, 0.4), 0 0 60px rgba(217, 70, 239, 0.2);
            }
            50% {
                transform: translateY(-15px) scale(1.05) rotate(3deg);
                box-shadow: 0 0 50px rgba(0, 245, 255, 0.6), 0 0 80px rgba(138, 43, 226, 0.4);
            }
        }

        /* Partículas Orbitantes ao redor do logo */
        .cyber-particles {
            position: absolute;
            top: 50%; left: 50%;
            width: 100%; height: 100%;
            transform: translate(-50%, -50%);
            z-index: 2;
            pointer-events: none;
        }

        .particle {
            position: absolute;
            border-radius: 50%;
            background: #fff;
            box-shadow: 0 0 10px 2px #fff;
            opacity: 0;
            animation: orbit-particle linear infinite;
        }

        .p1 { width: 4px; height: 4px; top: 10%; left: 10%; background: #00F5FF; box-shadow: 0 0 15px 3px #00F5FF; animation-duration: 8s; animation-delay: 0s; }
        .p2 { width: 6px; height: 6px; top: 80%; left: 80%; background: #D946EF; box-shadow: 0 0 20px 4px #D946EF; animation-duration: 10s; animation-delay: -3s; }
        .p3 { width: 3px; height: 3px; top: 90%; left: 20%; background: #00BFFF; box-shadow: 0 0 12px 2px #00BFFF; animation-duration: 9s; animation-delay: -5s; }
        .p4 { width: 5px; height: 5px; top: 20%; left: 80%; background: #8A2BE2; box-shadow: 0 0 18px 4px #8A2BE2; animation-duration: 11s; animation-delay: -2s; }

        @keyframes orbit-particle {
            0% { transform: translate(0, 0) scale(0.5); opacity: 0; }
            20% { opacity: 0.8; transform: translate(40px, -40px) scale(1.2); }
            50% { opacity: 1; transform: translate(80px, 0px) scale(1); }
            80% { opacity: 0.8; transform: translate(40px, 40px) scale(1.2); }
            100% { transform: translate(-20px, 10px) scale(0.5); opacity: 0; }
        }
    </style>"""

content = content.replace("    </style>", new_css)

# Inject the logo HTML inside .hero-content
logo_html = """
            <div class="hero-content floating">
                <div class="cyber-logo-container">
                    <div class="cyber-glow-bg"></div>
                    <div class="cyber-particles">
                        <div class="particle p1"></div>
                        <div class="particle p2"></div>
                        <div class="particle p3"></div>
                        <div class="particle p4"></div>
                    </div>
                    <img src="logo.png" alt="Tubarão Logo" class="cyber-logo">
                </div>
"""

content = content.replace('            <div class="hero-content floating">', logo_html)

# Also let's change the root variables for the whole site to slightly match the dark theme the user requested, since they explicitly asked for it ("fundo preto escuro #050816, cores neon..."). Or should I keep the rest of the site exact? "Crie uma animação hero section futurista para um site dark mode... Estilo visual: - Tema cyberpunk premium. - Fundo preto escuro (#050816)."
# I will just update the body background color as they requested, but leave tabs alone.
css_vars_old = r""":root\s*\{[^\}]+\}"""
css_vars_new = """:root {
            --bg-color: #050816;
            --card-bg: rgba(25, 18, 43, 0.6);
            --primary-purple: #8A2BE2;
            --electric-purple: #a200ff;
            --magenta: #D946EF;
            --neon-cyan: #00F5FF;
            --electric-blue: #00BFFF;
            --text-main: #ffffff;
            --text-muted: #a0a0b5;
            --glass-border: rgba(255, 255, 255, 0.08);
            --wpp-green: #25D366;
            --wpp-green-hover: #1ebe57;
        }"""
content = re.sub(css_vars_old, css_vars_new, content, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
