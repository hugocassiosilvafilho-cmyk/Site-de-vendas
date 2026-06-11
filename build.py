import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove .tabs-container and its CSS
content = re.sub(r'/\*\s*Tabs / Filtros\s*\*/.*?(?=\/\*\s*Grid de Preços\s*\*\/)', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="container">\s*<div class="tabs-container">.*?</div>\s*</div>', '<div class="container" style="text-align: center; margin-bottom: 20px;"><p style="color: var(--neon-cyan); font-weight: 600; font-size: 1.1rem; letter-spacing: 1px; text-transform: uppercase;">⚡ Válido para Instagram, TikTok e Facebook</p></div>', content, flags=re.DOTALL)

# 2. Remove .micro-benefits from HTML and CSS
content = re.sub(r'<div class="micro-benefits">.*?</div>', '', content, flags=re.DOTALL)
content = re.sub(r'\.micro-benefits\s*\{.*?(?=\.faq-section\s*\{)', '', content, flags=re.DOTALL)

# 3. Fix JS logic (Remove tabs logic, currentPlatform, updateAll)
js_new = """    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var wppNumber = '5511977418328';
            var cards = document.querySelectorAll('.pricing-card');

            function getCardBaseName(cardId) {
                if (cardId === 'card1') return 'Visualizações';
                if (cardId === 'card2') return 'Curtidas';
                if (cardId === 'card3') return 'Seguidores';
                return '';
            }

            function formatPrice(value) {
                var num = parseFloat(value);
                var parts = num.toFixed(2).split('.');
                var intPart = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.');
                return 'R$ ' + intPart + ',' + parts[1];
            }

            function updateCard(card) {
                var cardId = card.getAttribute('data-card-id');
                var select = card.querySelector('.price-select');
                var option = select.options[select.selectedIndex];
                var inputWrapper = card.querySelector('.custom-input-wrapper');
                var numInput = card.querySelector('.custom-number-input');
                var btn = card.querySelector('.btn-buy');
                var priceDisplay = card.querySelector('.price-value');
                var qtyText, price;

                if (option.value === 'custom') {
                    inputWrapper.classList.add('show');
                    var customVal = parseInt(numInput.value) || 1000;
                    if (customVal < 1000) customVal = 1000;
                    
                    var multiplier = 0;
                    if (cardId === 'card1') multiplier = 0.00236;
                    if (cardId === 'card2') multiplier = 0.00796;
                    if (cardId === 'card3') multiplier = 0.028;
                    
                    price = (customVal * multiplier).toFixed(2);
                    qtyText = customVal.toLocaleString('pt-BR') + ' (Personalizado)';
                } else {
                    inputWrapper.classList.remove('show');
                    qtyText = option.getAttribute('data-qty-text');
                    price = option.getAttribute('data-price');
                }

                priceDisplay.textContent = formatPrice(price);

                var cardName = getCardBaseName(cardId);
                var message = 'Olá! Gostaria de comprar o pacote de ' + qtyText + ' ' + cardName + '.';

                btn.href = 'https://wa.me/' + wppNumber + '?text=' + encodeURIComponent(message);
            }

            cards.forEach(function (card) {
                updateCard(card);
            });

            document.querySelectorAll('.price-select').forEach(function (select) {
                select.addEventListener('change', function () {
                    var card = this.closest('.pricing-card');
                    if (card) {
                        updateCard(card);
                    }
                });
            });

            document.querySelectorAll('.custom-number-input').forEach(function (input) {
                input.addEventListener('input', function () {
                    var card = this.closest('.pricing-card');
                    if (card) {
                        updateCard(card);
                    }
                });
            });

            document.querySelectorAll('.faq-question').forEach(function (btn) {
                btn.addEventListener('click', function () {
                    var item = this.parentElement;
                    var isOpen = item.classList.contains('active');
                    document.querySelectorAll('.faq-item').forEach(function (i) {
                        i.classList.remove('active');
                    });
                    if (!isOpen) {
                        item.classList.add('active');
                    }
                });
            });

            function openModal(id) {
                document.getElementById(id).classList.add('open');
                document.body.style.overflow = 'hidden';
            }

            function closeModals() {
                document.querySelectorAll('.modal-overlay').forEach(function (m) {
                    m.classList.remove('open');
                });
                document.body.style.overflow = '';
            }

            document.querySelectorAll('.modal-trigger').forEach(function (link) {
                link.addEventListener('click', function (e) {
                    e.preventDefault();
                    var modalId = this.getAttribute('data-modal') + '-modal';
                    openModal(modalId);
                });
            });

            document.querySelectorAll('.modal-close').forEach(function (el) {
                el.addEventListener('click', function (e) {
                    e.stopPropagation();
                    closeModals();
                });
            });

            document.querySelectorAll('.modal-overlay').forEach(function (overlay) {
                overlay.addEventListener('click', function (e) {
                    if (e.target === this) {
                        closeModals();
                    }
                });
            });

            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') {
                    closeModals();
                }
            });
        });
    </script>"""
content = re.sub(r'<script>.*?</script>', js_new, content, flags=re.DOTALL)

# Add Global Benefits under cards
global_benefits = """
        <div class="global-benefits">
            <div class="global-benefit-item"><i class="fa-solid fa-bolt"></i> Entrega Automática e Rápida</div>
            <div class="global-benefit-item"><i class="fa-solid fa-shield-halved"></i> Sem Precisar de Senha</div>
            <div class="global-benefit-item"><i class="fa-solid fa-star"></i> Alta Retenção e Qualidade</div>
        </div>
    </main>
"""
content = content.replace("    </main>", global_benefits)

# Add Como Funciona and Prova Social before FAQ
new_sections = """
    <!-- Como Funciona -->
    <section class="how-it-works">
        <div class="container">
            <h2>Como Funciona?</h2>
            <div class="steps-container">
                <div class="step-card">
                    <i class="fa-solid fa-hand-pointer step-icon"></i>
                    <h4>1. Escolha o Pacote</h4>
                    <p>Selecione a quantidade de seguidores, curtidas ou visualizações que deseja.</p>
                </div>
                <div class="step-card">
                    <i class="fa-brands fa-whatsapp step-icon"></i>
                    <h4>2. Fale Conosco</h4>
                    <p>Clique em comprar para nos chamar no WhatsApp. Envie apenas o link do seu perfil ou postagem (não pedimos senha).</p>
                </div>
                <div class="step-card">
                    <i class="fa-solid fa-rocket step-icon"></i>
                    <h4>3. Receba na Hora</h4>
                    <p>Faça o pagamento seguro e veja os números subirem na sua conta em questão de minutos!</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Prova Social -->
    <section class="social-proof">
        <div class="container">
            <h2>O que nossos clientes dizem</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="testimonial-avatar"><i class="fa-solid fa-user"></i></div>
                        <div>
                            <div class="testimonial-name">João Marcos</div>
                            <div class="testimonial-stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                        </div>
                    </div>
                    <div class="testimonial-text">"Muito rápido! Comprei 10k de seguidores e em menos de uma hora já tinha chegado tudo. Recomendo muito!"</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="testimonial-avatar"><i class="fa-solid fa-user"></i></div>
                        <div>
                            <div class="testimonial-name">Ana Beatriz</div>
                            <div class="testimonial-stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                        </div>
                    </div>
                    <div class="testimonial-text">"Uso pra dar uma alavancada nos Reels dos meus clientes. A entrega é sempre automática, nunca tive problemas com queda."</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="testimonial-avatar"><i class="fa-solid fa-user"></i></div>
                        <div>
                            <div class="testimonial-name">Carlos Eduardo</div>
                            <div class="testimonial-stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                        </div>
                    </div>
                    <div class="testimonial-text">"O melhor é que não precisa de senha. Faço o pix, mando o link e o engajamento bomba. Excelente serviço."</div>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
"""
content = content.replace("    <!-- FAQ Section -->\n", new_sections)

# Add payments to footer
payments = """
            <div class="payment-methods">
                <i class="fa-brands fa-pix" style="color: #32BCAD;" title="Pix"></i>
                <i class="fa-brands fa-cc-mastercard" style="color: #ff5f00;" title="Mastercard"></i>
                <i class="fa-brands fa-cc-visa" style="color: #1a1f71;" title="Visa"></i>
                <i class="fa-solid fa-shield-check" style="color: #25D366;" title="Compra Segura"></i>
            </div>
            <p>&copy; 2026 Turbo Social. Todos os direitos reservados. Site 100% Seguro.</p>
"""
content = re.sub(r'<p>&copy; 2026 Turbo Social. Todos os direitos reservados.</p>', payments, content)


# Add new CSS
new_css = """
        /* Benefícios Globais */
        .global-benefits {
            background: rgba(0, 243, 255, 0.05);
            border: 1px solid rgba(0, 243, 255, 0.1);
            border-radius: 16px;
            padding: 20px;
            margin-top: 40px;
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        .global-benefit-item {
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--text-main);
            font-size: 0.95rem;
            font-weight: 600;
        }
        .global-benefit-item i {
            color: var(--neon-cyan);
            font-size: 1.2rem;
        }

        /* Como Funciona e Prova Social */
        .how-it-works, .social-proof {
            padding: 80px 20px;
        }
        .social-proof {
            background: linear-gradient(180deg, transparent, rgba(162, 0, 255, 0.05), transparent);
        }
        .how-it-works h2, .social-proof h2 {
            text-align: center;
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 50px;
            background: linear-gradient(135deg, #fff, var(--neon-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .steps-container, .testimonials-grid {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            max-width: 1000px;
            margin: 0 auto;
        }
        .step-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 30px;
            flex: 1;
            min-width: 250px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .step-card:hover {
            transform: translateY(-5px);
            border-color: rgba(162, 0, 255, 0.3);
        }
        .step-icon {
            font-size: 3rem;
            color: var(--neon-cyan);
            margin-bottom: 20px;
        }
        .step-card h4 {
            font-size: 1.3rem;
            margin-bottom: 12px;
            color: #fff;
        }
        .step-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .testimonial-card {
            background: rgba(25, 18, 43, 0.6);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 30px;
            flex: 1;
            min-width: 300px;
            text-align: left;
            position: relative;
        }
        .testimonial-card::before {
            content: '\\201C';
            font-family: serif;
            font-size: 6rem;
            color: rgba(162, 0, 255, 0.1);
            position: absolute;
            top: 10px;
            right: 20px;
            line-height: 1;
        }
        .testimonial-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        .testimonial-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-cyan), var(--electric-purple));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: #fff;
        }
        .testimonial-name {
            font-weight: 800;
            color: #fff;
            font-size: 1.1rem;
        }
        .testimonial-stars {
            color: #FFD700;
            font-size: 0.85rem;
            margin-top: 4px;
        }
        .testimonial-text {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.6;
            font-style: italic;
        }
        .payment-methods {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 16px;
            font-size: 2rem;
        }

    </style>
"""
content = content.replace("    </style>", new_css)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
