import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace CSS variables
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

# Replace HTML header
html_header_old = r"""    <header>
        <div class="glow-circle"></div>
        <div class="container">
            <nav class="navbar">
                <a href="#" class="brand">
                    <img src="logo.png" alt="Turbo Social Logo">
                    <span class="brand-name">Turbo Social</span>
                </a>
            </nav>
            <div class="hero-content floating">
                <h1>Engajamento de<br>Alta Qualidade</h1>
                <p>Escale seus resultados, aumente sua autoridade e viralize seus conteúdos de forma segura e imediata nas principais redes sociais.</p>
            </div>
        </div>
    </header>"""

html_header_new = """    <header class="cyber-header">
        <div class="cyber-glow-bg"></div>
        <div class="cyber-particles">
            <div class="particle p1"></div>
            <div class="particle p2"></div>
            <div class="particle p3"></div>
            <div class="particle p4"></div>
            <div class="particle p5"></div>
            <div class="particle p6"></div>
            <div class="particle p7"></div>
            <div class="particle p8"></div>
        </div>
        <div class="energy-rays"></div>

        <div class="container relative-z">
            <nav class="navbar">
                <a href="#" class="brand">
                    <img src="logo.png" alt="Turbo Social Logo">
                    <span class="brand-name">Turbo Social</span>
                </a>
            </nav>
            <div class="hero-content cyberpunk-hero">
                <div class="hero-glow-pulse"></div>
                <div class="hero-inner">
                    <h1>Engajamento de<br>Alta Qualidade</h1>
                    <p>Escale seus resultados, aumente sua autoridade e viralize seus conteúdos de forma segura e imediata nas principais redes sociais.</p>
                </div>
            </div>
        </div>
    </header>"""
content = content.replace(html_header_old, html_header_new)

# Add new CSS before </style>
new_css = """
        /* CYBERPUNK HERO STYLES */
        .cyber-header {
            position: relative;
            overflow: hidden;
            padding: 40px 20px 100px;
            text-align: center;
        }

        .relative-z {
            position: relative;
            z-index: 10;
        }

        .cyber-glow-bg {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 800px;
            height: 800px;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, rgba(0,245,255,0.15) 0%, rgba(138,43,226,0.1) 40%, transparent 70%);
            filter: blur(80px);
            z-index: 1;
            animation: pulse-bg 8s ease-in-out infinite alternate;
        }

        @keyframes pulse-bg {
            0% { transform: translate(-50%, -50%) scale(1); opacity: 0.6; }
            100% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
        }

        .energy-rays {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: 
                linear-gradient(90deg, transparent 45%, rgba(0, 245, 255, 0.03) 50%, transparent 55%),
                linear-gradient(90deg, transparent 25%, rgba(217, 70, 239, 0.02) 30%, transparent 35%);
            z-index: 1;
            transform-origin: center top;
            animation: rays-rotate 20s linear infinite;
        }

        @keyframes rays-rotate {
            0% { transform: scale(2) rotate(0deg); }
            100% { transform: scale(2) rotate(360deg); }
        }

        /* Hero Element Cyberpunk Float */
        .cyberpunk-hero {
            position: relative;
            display: inline-block;
            margin: 0 auto;
            z-index: 20;
            animation: cyber-float 8s ease-in-out infinite;
            will-change: transform;
        }

        .hero-inner {
            position: relative;
            z-index: 2;
        }

        .hero-glow-pulse {
            position: absolute;
            top: 50%; left: 50%;
            width: 120%; height: 140%;
            transform: translate(-50%, -50%);
            background: radial-gradient(ellipse at center, rgba(0, 191, 255, 0.25) 0%, rgba(217, 70, 239, 0.15) 40%, transparent 70%);
            filter: blur(40px);
            z-index: 1;
            animation: hero-glow 8s ease-in-out infinite;
        }

        @keyframes hero-glow {
            0%, 100% { opacity: 0.6; transform: translate(-50%, -50%) scale(0.95); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
        }

        @keyframes cyber-float {
            0%, 100% {
                transform: translateY(0) scale(1) rotate(-3deg);
            }
            50% {
                transform: translateY(-20px) scale(1.05) rotate(3deg);
            }
        }

        .cyberpunk-hero h1 {
            font-size: 4.8rem;
            font-weight: 800;
            margin-bottom: 24px;
            background: linear-gradient(135deg, #fff 10%, var(--neon-cyan) 50%, var(--magenta) 90%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
            line-height: 1.1;
            text-shadow: 0 0 40px rgba(0, 245, 255, 0.3);
        }

        .cyberpunk-hero p {
            color: var(--text-muted);
            font-size: 1.35rem;
            max-width: 750px;
            margin: 0 auto;
            line-height: 1.6;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        /* Partículas Orbitantes */
        .cyber-particles {
            position: absolute;
            top: 50%; left: 50%;
            width: 100%; height: 100%;
            transform: translate(-50%, -50%);
            z-index: 2;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            border-radius: 50%;
            background: #fff;
            box-shadow: 0 0 10px 2px #fff;
            opacity: 0;
            animation: orbit-particle linear infinite;
        }

        .p1 { width: 4px; height: 4px; top: 20%; left: 20%; background: var(--neon-cyan); box-shadow: 0 0 15px 3px var(--neon-cyan); animation-duration: 12s; animation-delay: 0s; }
        .p2 { width: 6px; height: 6px; top: 70%; left: 80%; background: var(--magenta); box-shadow: 0 0 20px 4px var(--magenta); animation-duration: 18s; animation-delay: -3s; }
        .p3 { width: 3px; height: 3px; top: 80%; left: 30%; background: var(--electric-blue); box-shadow: 0 0 12px 2px var(--electric-blue); animation-duration: 15s; animation-delay: -7s; }
        .p4 { width: 5px; height: 5px; top: 30%; left: 70%; background: var(--primary-purple); box-shadow: 0 0 18px 4px var(--primary-purple); animation-duration: 20s; animation-delay: -10s; }
        .p5 { width: 4px; height: 4px; top: 50%; left: 10%; background: var(--neon-cyan); box-shadow: 0 0 15px 3px var(--neon-cyan); animation-duration: 14s; animation-delay: -5s; }
        .p6 { width: 5px; height: 5px; top: 60%; left: 90%; background: var(--magenta); box-shadow: 0 0 18px 4px var(--magenta); animation-duration: 16s; animation-delay: -1s; }
        .p7 { width: 7px; height: 7px; top: 10%; left: 60%; background: var(--electric-blue); box-shadow: 0 0 25px 5px var(--electric-blue); animation-duration: 22s; animation-delay: -12s; }
        .p8 { width: 3px; height: 3px; top: 90%; left: 50%; background: #fff; box-shadow: 0 0 10px 2px #fff; animation-duration: 11s; animation-delay: -8s; }

        @keyframes orbit-particle {
            0% { transform: translate(0, 0) scale(0.5); opacity: 0; }
            20% { opacity: 0.8; transform: translate(30px, -30px) scale(1.2); }
            50% { opacity: 1; transform: translate(60px, -10px) scale(1); }
            80% { opacity: 0.8; transform: translate(20px, 40px) scale(1.2); }
            100% { transform: translate(-20px, 10px) scale(0.5); opacity: 0; }
        }

        /* Responsivo Cyberpunk */
        @media (max-width: 768px) {
            .cyberpunk-hero h1 { font-size: 3rem; }
            .cyberpunk-hero p { font-size: 1.1rem; }
            .cyber-header { padding: 30px 20px 60px; }
            @keyframes cyber-float {
                0%, 100% { transform: translateY(0) scale(1) rotate(-2deg); }
                50% { transform: translateY(-10px) scale(1.02) rotate(2deg); }
            }
        }
        @media (max-width: 480px) {
            .cyberpunk-hero h1 { font-size: 2.3rem; }
            .cyberpunk-hero p { font-size: 1rem; }
        }
    </style>"""

content = content.replace("    </style>", new_css)

# Remove old CSS animations that are not needed
content = re.sub(r'\.floating\s*\{[^}]+\}', '', content)
content = re.sub(r'@keyframes floating\s*\{[^}]+\}', '', content)
content = re.sub(r'\.glow-circle\s*\{[^}]+\}', '', content)
# Also remove `header h1` and `header p` as we use `.cyberpunk-hero h1`
content = re.sub(r'header\s+h1\s*\{[^\}]+\}', '', content)
content = re.sub(r'header\s+p\s*\{[^\}]+\}', '', content)
content = re.sub(r'header\s*\{[^\}]+\}', '', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
