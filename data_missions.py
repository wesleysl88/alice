# -*- coding: utf-8 -*-
"""
All mission data for Alice's 3rd Grade Math - Sistema Monetário
Chapters 9 (pages 54 to 80)
"""

MISSIONS = [
    # =========================================================================
    # ILHA 1: PÁGINAS 54 A 58
    # =========================================================================
    {
        "id": "missao-1",
        "number": 1,
        "title": "Ilha 1: O Surgimento do Dinheiro e Nosso Sistema",
        "pages_label": "Páginas 54 a 58 do Livro",
        "desc": "A vitrine de brinquedos da Sara, o presente da amiga, do escambo ao Pix, a regra da vírgula e o cofrinho!",
        "badge": "Explorador da Moeda",
        "color": "#10b981",
        "icon": "🪙",
        "questions": [
            {
                "id": "p54_q1",
                "page": "Página 54",
                "title": "A Vitrine da Loja de Brinquedos da Sara",
                "story": "Sara e o pai foram à loja de brinquedos para escolher um presente para a melhor amiga dela. Na prateleira, eles observaram quatro brinquedos com seus preços:<br><br>"
                         "<div class='toy-grid'>"
                         "  <div class='toy-card'><span class='toy-icon'>🧸</span><div class='toy-name'>Ursinho de Pelúcia</div><div class='toy-price'>R$ 65,00</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>⚽</span><div class='toy-name'>Bola Colorida</div><div class='toy-price'>R$ 20,00</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>🐰</span><div class='toy-name'>Bicho de Pelúcia</div><div class='toy-price'>R$ 85,25</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>👧</span><div class='toy-name'>Boneca Grande</div><div class='toy-price'>R$ 120,50</div></div>"
                         "</div>",
                "prompt": "Observe os preços na prateleira e responda:",
                "subquestions": [
                    {
                        "id": "p54_s1",
                        "text": "1. Qual é o brinquedo MAIS CARO da prateleira?",
                        "type": "radio",
                        "options": [
                            {"val": "boneca", "text": "Boneca Grande — R$ 120,50", "correct": True},
                            {"val": "coelho", "text": "Bicho de Pelúcia — R$ 85,25", "correct": False},
                            {"val": "urso", "text": "Ursinho de Pelúcia — R$ 65,00", "correct": False},
                            {"val": "bola", "text": "Bola Colorida — R$ 20,00", "correct": False}
                        ],
                        "explain": "Comparando os números: R$ 120,50 é o maior valor (possui 1 centena, 2 dezenas e 50 centavos). Ordem decrescente: R$ 120,50 > R$ 85,25 > R$ 65,00 > R$ 20,00."
                    },
                    {
                        "id": "p54_s2",
                        "text": "2. Qual é o brinquedo MAIS BARATO da prateleira?",
                        "type": "radio",
                        "options": [
                            {"val": "bola", "text": "Bola Colorida — R$ 20,00", "correct": True},
                            {"val": "urso", "text": "Ursinho de Pelúcia — R$ 65,00", "correct": False},
                            {"val": "coelho", "text": "Bicho de Pelúcia — R$ 85,25", "correct": False},
                            {"val": "boneca", "text": "Boneca Grande — R$ 120,50", "correct": False}
                        ],
                        "explain": "O menor valor entre todos os brinquedos da vitrine é R$ 20,00 (Bola Colorida)."
                    },
                    {
                        "id": "p54_s3",
                        "text": "3. O pai de Sara combinou que o presente deve custar ATÉ R$ 100,00. Quais brinquedos eles podem escolher sem ultrapassar esse limite?",
                        "type": "checkbox",
                        "options": [
                            {"val": "bola", "text": "Bola Colorida (R$ 20,00)", "correct": True},
                            {"val": "urso", "text": "Ursinho de Pelúcia (R$ 65,00)", "correct": True},
                            {"val": "coelho", "text": "Bicho de Pelúcia (R$ 85,25)", "correct": True},
                            {"val": "boneca", "text": "Boneca Grande (R$ 120,50)", "correct": False}
                        ],
                        "explain": "Podem escolher qualquer brinquedo com preço menor ou igual a R$ 100,00: a Bola (20 < 100), o Urso (65 < 100) e o Bicho de Pelúcia (85,25 < 100). A Boneca custa R$ 120,50, ultrapassando o limite em R$ 20,50!"
                    }
                ]
            },
            {
                "id": "p55_q1",
                "page": "Página 55",
                "title": "O Presente de R$ 85,25 para a Amiga",
                "story": "Sara escolheu comprar o bicho de pelúcia de <strong>R$ 85,25</strong> para a melhor amiga.<br>"
                         "Qual grupo de cédulas e moedas abaixo representa o <strong>valor exato</strong> para pagar no caixa sem troco?",
                "subquestions": [
                    {
                        "id": "p55_s1",
                        "text": "Assinale a opção com o valor exato de R$ 85,25:",
                        "type": "radio",
                        "options": [
                            {"val": "op1", "text": "1 nota de R$ 50 + 1 nota de R$ 20 + 1 nota de R$ 10 + 1 nota de R$ 5 + 1 moeda de 25 centavos", "correct": True},
                            {"val": "op2", "text": "1 nota de R$ 50 + 2 notas de R$ 20 + 1 nota de R$ 5 + 1 moeda de 25 centavos", "correct": False},
                            {"val": "op3", "text": "1 nota de R$ 50 + 1 nota de R$ 20 + 1 nota de R$ 10 + 1 moeda de 50 centavos", "correct": False}
                        ],
                        "explain": "Vamos somar a Opção 1:<br>"
                                   "• 50 + 20 = 70 reais<br>"
                                   "• 70 + 10 = 80 reais<br>"
                                   "• 80 + 5 = 85 reais<br>"
                                   "• Mais a moeda de 25 centavos = <strong>R$ 85,25</strong>!<br>"
                                   "Na Opção 2 daria R$ 95,25 (10 reais a mais). Na Opção 3 daria R$ 80,50."
                    }
                ],
                "caderno": "✏️ Atividade do Caderno/Livro: No livro há um espaço de etiqueta para desenhar um brinquedo de até R$ 100,00 e desenhar as notas para pagar sem troco."
            },
            {
                "id": "p56_q1",
                "page": "Página 56",
                "title": "A História do Dinheiro: Do Escambo ao Papel-Moeda",
                "story": "Sara e o pai usaram cédulas e moedas na loja. Mas nem sempre existiu dinheiro de papel e moeda no mundo!",
                "subquestions": [
                    {
                        "id": "p56_s1",
                        "text": "1. Antes da invenção das moedas, as pessoas trocavam diretamente mercadorias (exemplo: trocar sacos de milho por peixe). Qual é o nome dessa prática de troca direta?",
                        "type": "radio",
                        "options": [
                            {"val": "escambo", "text": "Escambo", "correct": True},
                            {"val": "comercio_online", "text": "Comércio Online", "correct": False},
                            {"val": "leilao", "text": "Leilão", "correct": False}
                        ],
                        "explain": "<strong>Escambo</strong> é a troca direta de mercadorias sem a intermediação de moeda ou cédulas."
                    },
                    {
                        "id": "p56_s2",
                        "text": "2. Por que o escambo começou a ficar difícil para as pessoas?",
                        "type": "radio",
                        "options": [
                            {"val": "dificuldade", "text": "Porque nem sempre uma pessoa desejava o produto da outra e era difícil definir o valor justo de cada troca", "correct": True},
                            {"val": "proibido", "text": "Porque os agricultores não queriam mais plantar alimentos", "correct": False}
                        ],
                        "explain": "Imagine um tecelão querendo peixe: se o pescador já tivesse tecido, a troca não acontecia! Por isso inventaram o dinheiro como medida universal aceita por todos."
                    },
                    {
                        "id": "p56_s3",
                        "text": "3. Hoje em dia, além de moedas de metal e notas de papel, quais outras formas modernas usamos para pagar?",
                        "type": "checkbox",
                        "options": [
                            {"val": "pix", "text": "Pix (transferência instantânea pelo celular)", "correct": True},
                            {"val": "cartao", "text": "Cartão de débito ou de crédito", "correct": True},
                            {"val": "escambo_sal", "text": "Troca de peixes por trigo no supermercado", "correct": False}
                        ],
                        "explain": "Hoje usamos dinheiro físico, cartões magnéticos e sistemas digitais instantâneos como o Pix."
                    }
                ]
            },
            {
                "id": "p57_q1",
                "page": "Página 57",
                "title": "O Sistema Monetário Brasileiro e a Regra da Vírgula",
                "story": "A moeda oficial do Brasil é o <strong>Real</strong>, com símbolo <strong>R$</strong>.<br>"
                         "Veja como escrevemos o preço da boneca da vitrine: <strong>R$ 85,25</strong>.",
                "subquestions": [
                    {
                        "id": "p57_s1",
                        "text": "1. O que a VÍRGULA faz na escrita do nosso dinheiro?",
                        "type": "radio",
                        "options": [
                            {"val": "separa", "text": "Separa a parte inteira em REAIS (à esquerda) da parte dos CENTAVOS (à direita)", "correct": True},
                            {"val": "centena", "text": "Serve apenas para separar centenas de dezenas", "correct": False}
                        ],
                        "explain": "<strong>Regra de Ouro da Vírgula:</strong><br>À esquerda da vírgula: REAIS inteiros.<br>À direita da vírgula: CENTAVOS (frações de 1 real de 00 a 99)."
                    },
                    {
                        "id": "p57_s2",
                        "text": "2. Como se lê corretamente por extenso a quantia R$ 85,25?",
                        "type": "radio",
                        "options": [
                            {"val": "oitenta_e_cinco", "text": "Oitenta e cinco reais e vinte e cinco centavos", "correct": True},
                            {"val": "oitenta_vinte", "text": "Oitenta e cinco reais e vinte centavos", "correct": False},
                            {"val": "oitocentos", "text": "Oitocentos e cinquenta e dois reais", "correct": False}
                        ],
                        "explain": "85 = oitenta e cinco reais. 25 = vinte e cinco centavos. Lê-se: <em>Oitenta e cinco reais e vinte e cinco centavos</em>."
                    },
                    {
                        "id": "p57_s3",
                        "text": "3. O brinquedo mais caro custava R$ 120,50. É possível pagar R$ 120,50 usando APENAS CÉDULAS, sem moedas e sem troco?",
                        "type": "radio",
                        "options": [
                            {"val": "nao", "text": "Não, porque a menor cédula é de R$ 2,00. Os 50 centavos exigem moeda!", "correct": True},
                            {"val": "sim", "text": "Sim, existe nota de 50 centavos", "correct": False}
                        ],
                        "explain": "Não existem notas de centavos no Brasil! Para pagar os 50 centavos exatos, é necessário usar moeda (uma de 50¢ ou duas de 25¢)."
                    }
                ]
            },
            {
                "id": "p58_q1",
                "page": "Página 58",
                "title": "O Cofrinho da Sara: Economia e Compras",
                "story": "Sara levou todo o dinheiro que havia economizado no seu cofrinho: exatamente <strong>R$ 80,00</strong>.<br>"
                         "Ela viu três opções de brinquedos na loja:<br>"
                         "• <strong>Opção 1:</strong> Boneca Grande por <strong>R$ 85,25</strong><br>"
                         "• <strong>Opção 2:</strong> Ursinho de Pelúcia por <strong>R$ 65,00</strong><br>"
                         "• <strong>Opção 3:</strong> Jogo 4 em 1 por <strong>R$ 35,00</strong>",
                "subquestions": [
                    {
                        "id": "p58_s1",
                        "text": "1. Sara tem dinheiro suficiente para comprar a Boneca de R$ 85,25?",
                        "type": "radio",
                        "options": [
                            {"val": "nao", "text": "Não, porque R$ 85,25 é maior que R$ 80,00 (faltam R$ 5,25)", "correct": True},
                            {"val": "sim", "text": "Sim, o dinheiro dela é suficiente", "correct": False}
                        ],
                        "explain": "85,25 > 80,00. Faltam R$ 5,25 para ela conseguir comprar a boneca."
                    },
                    {
                        "id": "p58_s2",
                        "text": "2. Sara decidiu comprar o Ursinho de R$ 65,00. Quanto dinheiro vai SOBRAR do cofrinho dela?",
                        "type": "input_number",
                        "correct": 15,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "<strong>Conta Armada (Subtração CDU):</strong><br>"
                                   "<pre class='math-box'>"
                                   "   D  U
"
                                   "   7 10   (o 8 das dezenas emprestou 1 para a unidade)
"
                                   "   8  0
"
                                   " - 6  5
"
                                   " -------
"
                                   "   1  5
"
                                   "</pre>"
                                   "10 - 5 = 5 unidades.<br>7 - 6 = 1 dezena.<br>Resultado: Vão sobrar <strong>R$ 15,00</strong>!"
                    },
                    {
                        "id": "p58_s3",
                        "text": "3. Para pagar os R$ 65,00 do urso sem precisar de troco, qual grupo de cédulas ela pode entregar?",
                        "type": "radio",
                        "options": [
                            {"val": "3x20_1x5", "text": "3 notas de R$ 20,00 e 1 nota de R$ 5,00 (20 + 20 + 20 + 5 = 65)", "correct": True},
                            {"val": "2x20_2x10", "text": "2 notas de R$ 20,00 e 2 notas de R$ 10,00 (dá 60 reais)", "correct": False},
                            {"val": "1x50_2x10", "text": "1 nota de R$ 50,00 e 2 notas de R$ 10,00 (dá 70 reais)", "correct": False}
                        ],
                        "explain": "3 notas de 20 reais = 60 reais. Mais uma nota de 5 reais = 65 reais exatos!"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # ILHA 2: PÁGINAS 59 A 64
    # =========================================================================
    {
        "id": "missao-2",
        "number": 2,
        "title": "Ilha 2: Cédulas, Moedas e o Troco",
        "pages_label": "Páginas 59 a 64 do Livro",
        "desc": "Conhecendo todo o dinheiro brasileiro, equivalências de moedas, escrita por extenso e o troco de Isaque, Luísa e Felipe!",
        "badge": "Mestre do Troco",
        "color": "#3b82f6",
        "icon": "💵",
        "questions": [
            {
                "id": "p59_q1",
                "page": "Página 59",
                "title": "O Dinheiro Brasileiro: Moedas e Equivalências de R$ 1,00",
                "story": "No Brasil circulam cédulas de <strong>2, 5, 10, 20, 50, 100 e 200 reais</strong>, e moedas de <strong>1, 5, 10, 25, 50 centavos e 1 real</strong>.<br>"
                         "Lembre-se que <strong>100 centavos valem exatamente R$ 1,00</strong>!",
                "subquestions": [
                    {
                        "id": "p59_s1",
                        "text": "1. Quantas moedas de 50 centavos são necessárias para formar R$ 1,00?",
                        "type": "input_number",
                        "correct": 2,
                        "unit": "moedas",
                        "explain": "50 + 50 = 100 centavos = R$ 1,00. São necessárias <strong>2 moedas</strong> de 50 centavos."
                    },
                    {
                        "id": "p59_s2",
                        "text": "2. Quantas moedas de 25 centavos são necessárias para formar R$ 1,00?",
                        "type": "input_number",
                        "correct": 4,
                        "unit": "moedas",
                        "explain": "25 + 25 + 25 + 25 = 100 centavos = R$ 1,00. São necessárias <strong>4 moedas</strong> de 25 centavos."
                    },
                    {
                        "id": "p59_s3",
                        "text": "3. Quantas moedas de 10 centavos são necessárias para formar R$ 1,00?",
                        "type": "input_number",
                        "correct": 10,
                        "unit": "moedas",
                        "explain": "10 x 10 centavos = 100 centavos = R$ 1,00. São necessárias <strong>10 moedas</strong> de 10 centavos."
                    }
                ]
            },
            {
                "id": "p60_q1",
                "page": "Página 60",
                "title": "Leitura, Escrita por Extenso e Armadilhas do Caderno",
                "story": "Atenção especial! Vamos treinar a escrita dos valores por extenso com muita atenção aos centavos e à ortografia correta das palavras!",
                "subquestions": [
                    {
                        "id": "p60_s1",
                        "text": "1. Alice somou: 1 nota de R$ 50 + 1 nota de R$ 5 + 1 moeda de R$ 1 + 1 moeda de 25 centavos. Qual é o valor e como se escreve por extenso?",
                        "type": "radio",
                        "options": [
                            {"val": "56_25", "text": "R$ 56,25 — Cinquenta e seis reais e vinte e cinco centavos", "correct": True},
                            {"val": "56_20", "text": "R$ 56,20 — Cinquenta e seis reais e vinte centavos (Cuidado!)", "correct": False},
                            {"val": "66_25", "text": "R$ 66,25 — Sessenta e seis reais e vinte e cinco centavos", "correct": False}
                        ],
                        "explain": "50 + 5 + 1 = 56 reais. A moeda é de 25 centavos.<br>"
                                   "<span class='trap-alert'>⚠️ Cuidado com a pegadinha do caderno:</span> não se esqueça do 'cinco' nos centavos! É <strong>cinquenta e seis reais e vinte e cinco centavos</strong>."
                    },
                    {
                        "id": "p60_s2",
                        "text": "2. Somando 1 moeda de 50 centavos, 1 de 25 centavos, 1 de 10 centavos e 1 de 5 centavos: qual é o total e a escrita correta?",
                        "type": "radio",
                        "options": [
                            {"val": "noventa", "text": "90 centavos — escrito corretamente como: 'Noventa centavos'", "correct": True},
                            {"val": "no_venta", "text": "90 centavos — escrito como: 'No venta centavos' (Erro de separação!)", "correct": False},
                            {"val": "oitenta", "text": "80 centavos — Oitenta centavos", "correct": False}
                        ],
                        "explain": "50 + 25 = 75; 75 + 10 = 85; 85 + 5 = 90 centavos.<br>"
                                   "<span class='trap-alert'>⚠️ Grafia correta:</span> a palavra <strong>noventa</strong> é escrita junta, com N e V (nunca separada como 'no venta')."
                    },
                    {
                        "id": "p60_s3",
                        "text": "3. Somando 2 moedas de 25 centavos, 1 de 10 centavos e 1 de 5 centavos: quanto temos e qual a escrita correta?",
                        "type": "radio",
                        "options": [
                            {"val": "sessenta_e_cinco", "text": "65 centavos — escrito: 'Sessenta e cinco centavos'", "correct": True},
                            {"val": "assenta", "text": "65 centavos — escrito: 'Assenta e cinco centavos' (Erro de ortografia!)", "correct": False}
                        ],
                        "explain": "25 + 25 = 50; 50 + 10 = 60; 60 + 5 = 65 centavos.<br>"
                                   "<span class='trap-alert'>⚠️ Ortografia correta:</span> escreve-se <strong>sessenta</strong> (com dois S e terminação -enta), nunca 'assenta'."
                    }
                ]
            },
            {
                "id": "p61_q1",
                "page": "Página 61",
                "title": "Isaque e o Livro de R$ 48,00",
                "story": "Isaque foi à livraria e escolheu um livro infantil de <strong>R$ 48,00</strong>.<br>"
                         "No bolso, Isaque tinha:<br>"
                         "• 2 cédulas de <strong>R$ 20,00</strong><br>"
                         "• 1 cédula de <strong>R$ 10,00</strong>",
                "subquestions": [
                    {
                        "id": "p61_s1",
                        "text": "1. Quanto dinheiro Isaque tem ao todo?",
                        "type": "input_number",
                        "correct": 50,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "20 + 20 = 40. 40 + 10 = <strong>R$ 50,00</strong>."
                    },
                    {
                        "id": "p61_s2",
                        "text": "2. O dinheiro de Isaque é suficiente para comprar o livro de R$ 48,00?",
                        "type": "radio",
                        "options": [
                            {"val": "sim", "text": "Sim, porque R$ 50,00 é maior que R$ 48,00 (sobrará troco)", "correct": True},
                            {"val": "nao", "text": "Não, faltam 2 reais", "correct": False}
                        ],
                        "explain": "50 > 48. O dinheiro é suficiente e Isaque ainda receberá troco."
                    },
                    {
                        "id": "p61_s3",
                        "text": "3. Quanto Isaque vai receber de TROCO?",
                        "type": "input_number",
                        "correct": 2,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Fórmula do Troco:<br><strong>Troco = Dinheiro Pago - Preço da Compra</strong><br>Troco = 50 - 48 = <strong>R$ 2,00</strong> (ele pode receber 1 moeda de R$ 2 ou 1 cédula de R$ 2,00)."
                    }
                ]
            },
            {
                "id": "p62_q1",
                "page": "Página 62",
                "title": "Luísa e Felipe na Lanchonete da Escola",
                "story": "Veja o cardápio da lanchonete da escola:<br><br>"
                         "<div class='menu-card-grid'>"
                         "  <div class='menu-item'><span class='menu-icon'>🥪</span> <div>Sanduíche Natural</div> <strong>R$ 12,00</strong></div>"
                         "  <div class='menu-item'><span class='menu-icon'>🧃</span> <div>Suco de Fruta</div> <strong>R$ 6,00</strong></div>"
                         "  <div class='menu-item'><span class='menu-icon'>🥣</span> <div>Salada de Frutas</div> <strong>R$ 8,00</strong></div>"
                         "  <div class='menu-item'><span class='menu-icon'>🧀</span> <div>Pão de Queijo</div> <strong>R$ 4,00</strong></div>"
                         "</div>",
                "subquestions": [
                    {
                        "id": "p62_s1",
                        "text": "1. Luísa comprou 1 Sanduíche Natural (R$ 12,00) e 1 Suco (R$ 6,00). Pagou com uma cédula de R$ 20,00. Qual foi o seu troco?",
                        "type": "input_number",
                        "correct": 2,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Passo 1: Gasto da Luísa = 12 + 6 = R$ 18,00.<br>Passo 2: Troco = 20 - 18 = <strong>R$ 2,00</strong>."
                    },
                    {
                        "id": "p62_s2",
                        "text": "2. Felipe comprou 1 Salada de Frutas (R$ 8,00), 1 Suco (R$ 6,00) e 1 Pão de Queijo (R$ 4,00). Pagou com uma cédula de R$ 50,00. Qual foi o seu troco?",
                        "type": "input_number",
                        "correct": 32,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Passo 1: Gasto do Felipe = 8 + 6 + 4 = R$ 18,00.<br>Passo 2: Troco = 50 - 18 = <strong>R$ 32,00</strong>.<br>(50 - 10 = 40; 40 - 8 = 32)."
                    },
                    {
                        "id": "p62_s3",
                        "text": "3. Comparando o que Luísa e Felipe gastaram no lanche, quem gastou mais?",
                        "type": "radio",
                        "options": [
                            {"val": "iguais", "text": "Os dois gastaram a mesma quantia (R$ 18,00 cada um)", "correct": True},
                            {"val": "luisa", "text": "Luísa gastou mais", "correct": False},
                            {"val": "felipe", "text": "Felipe gastou mais", "correct": False}
                        ],
                        "explain": "Luísa gastou 12 + 6 = R$ 18,00. Felipe gastou 8 + 6 + 4 = R$ 18,00. Gastaram exatamente o mesmo valor!"
                    }
                ]
            },
            {
                "id": "p63_q1",
                "page": "Página 63",
                "title": "Daniele e a Compra de 3 Estojos Escolares",
                "story": "Daniele foi comprar estojos escolares para ela e seus dois irmãos. Ela comprou <strong>3 estojos iguais</strong>, custando <strong>R$ 14,00 cada um</strong>.<br>"
                         "Daniele entregou uma nota de <strong>R$ 50,00</strong> no caixa.",
                "subquestions": [
                    {
                        "id": "p63_s1",
                        "text": "1. Qual foi o valor total da compra dos 3 estojos?",
                        "type": "input_number",
                        "correct": 42,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Multiplicação: 3 x 14 = <strong>R$ 42,00</strong>.<br>(Ou por adição: 14 + 14 + 14 = 28 + 14 = 42 reais)."
                    },
                    {
                        "id": "p63_s2",
                        "text": "2. Quanto Daniele recebeu de troco ao pagar com os R$ 50,00?",
                        "type": "input_number",
                        "correct": 8,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Troco = 50 - 42 = <strong>R$ 8,00</strong>.<br>(Subtração: 50 vira 4 dezenas e 10 unidades. 10 - 2 = 8 unidades. 4 - 4 = 0 dezenas)."
                    },
                    {
                        "id": "p63_s3",
                        "text": "3. Se Daniele quisesse comprar uma mochila de R$ 78,00 e pagasse com uma nota de R$ 100,00, qual seria o troco?",
                        "type": "input_number",
                        "correct": 22,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "100 - 78 = <strong>R$ 22,00</strong>.<br>Cálculo mental: 100 - 70 = 30. 30 - 8 = 22 reais!"
                    }
                ]
            },
            {
                "id": "p64_q1",
                "page": "Página 64",
                "title": "Os Desafios do Troco de Mariana e Juliano",
                "story": "Vamos praticar mais duas situações de troco com Mariana e Juliano!",
                "subquestions": [
                    {
                        "id": "p64_s1",
                        "text": "1. Mariana comprou 1 caderno de R$ 23,00 e 1 caneta de R$ 7,00. Pagou com uma cédula de R$ 50,00. Qual foi o troco dela?",
                        "type": "input_number",
                        "correct": 20,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Passo 1: Total da compra = 23 + 7 = R$ 30,00.<br>Passo 2: Troco = 50 - 30 = <strong>R$ 20,00</strong>."
                    },
                    {
                        "id": "p64_s2",
                        "text": "2. Juliano comprou um jogo de tabuleiro por R$ 64,00 e pagou com DUAS notas de R$ 50,00 (total de R$ 100,00). Qual foi o troco dele?",
                        "type": "input_number",
                        "correct": 36,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Total pago = 50 + 50 = R$ 100,00.<br>Troco = 100 - 64 = <strong>R$ 36,00</strong>.<br>"
                                   "<pre class='math-box'>"
                                   "  C  D  U
"
                                   "  0  9 10   (1 centena vira 9 dezenas e 10 unidades)
"
                                   "  1  0  0
"
                                   "-    6  4
"
                                   "----------
"
                                   "     3  6
"
                                   "</pre>"
                                   "10 - 4 = 6 unidades. 9 - 6 = 3 dezenas. Troco = R$ 36,00."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # ILHA 3: PÁGINAS 65 A 68
    # =========================================================================
    {
        "id": "missao-3",
        "number": 3,
        "title": "Ilha 3: Estratégias de Cálculo Mental e Algoritmo CDU",
        "pages_label": "Páginas 65 a 68 do Livro",
        "desc": "O método de decomposição da Sara, a armadilha crítica das 3 bolas de R$ 56 e a feira do Paulo!",
        "badge": "Estrategista Mental",
        "color": "#f59e0b",
        "icon": "🧠",
        "questions": [
            {
                "id": "p65_q1",
                "page": "Página 65",
                "title": "O Cálculo Mental da Sara por Decomposição",
                "story": "Sara tem uma estratégia genial para calcular subtrações mentalmente sem precisar de papel e lápis!<br>"
                         "Veja como ela pensa para calcular <strong>85 - 28</strong>:<br>"
                         "1º) Ela decompõe o 28 em <strong>20 + 8</strong>.<br>"
                         "2º) Tira primeiro as dezenas: <strong>85 - 20 = 65</strong>.<br>"
                         "3º) Depois tira as unidades restantes: <strong>65 - 8 = 57</strong>!<br>"
                         "Ou então arredonda: 85 - 30 = 55, e compensa somando 2: 55 + 2 = 57!",
                "subquestions": [
                    {
                        "id": "p65_s1",
                        "text": "1. Use a estratégia da Sara para calcular de cabeça: 74 - 26 =",
                        "type": "input_number",
                        "correct": 48,
                        "unit": "",
                        "explain": "Pensando como a Sara:<br>74 - 20 = 54.<br>54 - 6 = <strong>48</strong>!"
                    },
                    {
                        "id": "p65_s2",
                        "text": "2. Calcule mentalmente: 92 - 35 =",
                        "type": "input_number",
                        "correct": 57,
                        "unit": "",
                        "explain": "Decompondo 35 em 30 + 5:<br>92 - 30 = 62.<br>62 - 5 = <strong>57</strong>!"
                    },
                    {
                        "id": "p65_s3",
                        "text": "3. Calcule mentalmente: 150 - 68 =",
                        "type": "input_number",
                        "correct": 82,
                        "unit": "",
                        "explain": "150 - 60 = 90.<br>90 - 8 = <strong>82</strong>! (Ou 150 - 70 = 80, 80 + 2 = 82)."
                    }
                ]
            },
            {
                "id": "p66_q1",
                "page": "Página 66",
                "title": "A Grande Armadilha do Caderno: 3 Bolas de R$ 56 e o Troco de R$ 200",
                "story": "⚠️ <strong>ATENÇÃO MÁXIMA NESTA QUESTÃO!</strong><br>"
                         "Esta foi a questão onde o caderno teve uma dúvida importante entre <strong>R$ 32,00</strong> e <strong>R$ 38,00</strong>.<br><br>"
                         "O problema diz: Uma escola comprou <strong>3 bolas de futebol por R$ 56,00 cada uma</strong>.<br>"
                         "O pagamento foi feito com uma nota de <strong>R$ 200,00</strong>.",
                "subquestions": [
                    {
                        "id": "p66_s1",
                        "text": "1. Qual é o valor total das 3 bolas (3 x 56)?",
                        "type": "input_number",
                        "correct": 168,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Multiplicação armada:<br>3 x 6 unidades = 18 (fica 8 e vai 1 dezena).<br>3 x 5 dezenas = 15 + 1 = 16 dezenas.<br>Total: <strong>R$ 168,00</strong>.<br>(Ou por decomposição: 3 x 50 = 150; 3 x 6 = 18; 150 + 18 = 168)."
                    },
                    {
                        "id": "p66_s2",
                        "text": "2. Pagando os R$ 168,00 com R$ 200,00, qual é o TROCO EXATO?",
                        "type": "radio",
                        "options": [
                            {"val": "32", "text": "R$ 32,00 (Resposta Correta)", "correct": True},
                            {"val": "38", "text": "R$ 38,00 (⚠️ Atenção! Erro comum do empréstimo!)", "correct": False},
                            {"val": "42", "text": "R$ 42,00", "correct": False}
                        ],
                        "explain": "<div class='trap-box'>"
                                   "<h4>🔍 Por que a resposta é R$ 32,00 e NUNCA R$ 38,00?</h4>"
                                   "Veja a conta armada com os empréstimos passo a passo:<br>"
                                   "<pre class='math-box'>"
                                   "  C  D  U
"
                                   "  1  9 10   <-- Atenção aqui!
"
                                   "  2  0  0
"
                                   "- 1  6  8
"
                                   "----------
"
                                   "  0  3  2
"
                                   "</pre>"
                                   "<strong>Passo 1:</strong> Na unidade temos 0 - 8 (não dá).<br>"
                                   "<strong>Passo 2:</strong> A centena (2) empresta 1 e vira <strong>1</strong>. A dezena recebe 10.<br>"
                                   "<strong>Passo 3:</strong> A dezena tem 10, mas PRECISA emprestar 1 para a unidade! Então a dezena fica valendo <strong>9</strong> (e não 10!).<br>"
                                   "<strong>Passo 4:</strong> A unidade fica com 10: 10 - 8 = <strong>2</strong>.<br>"
                                   "<strong>Passo 5:</strong> A dezena ficou com 9: 9 - 6 = <strong>3</strong> (Se você esquecer que ela emprestou e fizer 10 - 6 achará 4, gerando o erro!).<br>"
                                   "<strong>Passo 6:</strong> A centena ficou com 1: 1 - 1 = 0.<br>"
                                   "<strong>Portanto, o troco correto é exatamente R$ 32,00!</strong>"
                                   "</div>"
                    }
                ]
            },
            {
                "id": "p67_q1",
                "page": "Página 67",
                "title": "Paulo e as Compras na Feira",
                "story": "Paulo foi à feira e comprou:<br>"
                         "• 1 kg de tomates por <strong>R$ 8,50</strong><br>"
                         "• 1 dúzia de bananas por <strong>R$ 6,50</strong><br>"
                         "• 1 pacote de maçãs por <strong>R$ 12,00</strong><br>"
                         "Ele levou uma cédula de <strong>R$ 50,00</strong>.",
                "subquestions": [
                    {
                        "id": "p67_s1",
                        "text": "1. Quanto Paulo gastou ao todo na feira?",
                        "type": "input_number",
                        "correct": 27,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Somando com atenção aos centavos:<br>8,50 + 6,50 = 15,00 (50¢ + 50¢ = R$ 1,00; 8 + 6 = 14 + 1 = 15).<br>15,00 + 12,00 = <strong>R$ 27,00</strong>."
                    },
                    {
                        "id": "p67_s2",
                        "text": "2. Quanto sobrou de troco para Paulo?",
                        "type": "input_number",
                        "correct": 23,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Troco = 50 - 27 = <strong>R$ 23,00</strong>.<br>(50 - 20 = 30; 30 - 7 = 23 reais)."
                    },
                    {
                        "id": "p67_s3",
                        "text": "3. Com os R$ 23,00 de troco, Paulo quer comprar um melão de R$ 15,00. Ele consegue? Quanto ainda vai sobrar?",
                        "type": "input_number",
                        "correct": 8,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Sim, ele consegue pois 23 > 15.<br>Sobra final: 23 - 15 = <strong>R$ 8,00</strong>."
                    }
                ]
            },
            {
                "id": "p68_q1",
                "page": "Página 68",
                "title": "O Planejamento e a Meta de Poupança da Clara",
                "story": "Clara tem um sonho: comprar um lindo patins que custa <strong>R$ 160,00</strong>.<br>"
                         "Para isso, ela guardou no cofre durante 3 meses:<br>"
                         "• Janeiro: <strong>R$ 25,00</strong><br>"
                         "• Fevereiro: <strong>R$ 35,00</strong><br>"
                         "• Março: <strong>R$ 40,00</strong>",
                "subquestions": [
                    {
                        "id": "p68_s1",
                        "text": "1. Quanto Clara já conseguiu economizar nesses 3 meses?",
                        "type": "input_number",
                        "correct": 100,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "25 + 35 = 60 reais. 60 + 40 = <strong>R$ 100,00</strong>."
                    },
                    {
                        "id": "p68_s2",
                        "text": "2. Quanto dinheiro ainda falta para Clara atingir a meta de R$ 160,00?",
                        "type": "input_number",
                        "correct": 60,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Falta = Valor do Patins - Valor Guardado = 160 - 100 = <strong>R$ 60,00</strong>."
                    },
                    {
                        "id": "p68_s3",
                        "text": "3. Se Clara conseguir guardar R$ 20,00 todo mês a partir de agora, em quantos meses ela conseguirá juntar os R$ 60,00 que faltam?",
                        "type": "input_number",
                        "correct": 3,
                        "unit": "meses",
                        "explain": "Divisão por parcelas iguais:<br>1º mês: 20<br>2º mês: 20 + 20 = 40<br>3º mês: 40 + 20 = 60.<br>São necessários <strong>3 meses</strong> (60 ÷ 20 = 3)."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # ILHA 4: PÁGINAS 69 A 73 (MATERIAL DE APOIO - PARTE 1)
    # =========================================================================
    {
        "id": "missao-4",
        "number": 4,
        "title": "Ilha 4: Orçamento Familiar e Problemas em Etapas",
        "pages_label": "Páginas 69 a 73 do Livro",
        "desc": "Débito vs Crédito, o orçamento familiar do Lucas, comparando preços no mercado e a papelaria da Fátima!",
        "badge": "Planejador Financeiro",
        "color": "#8b5cf6",
        "icon": "📊",
        "questions": [
            {
                "id": "p69_q1",
                "page": "Página 69",
                "title": "Contas no Banco: Cartão de Débito vs Cartão de Crédito",
                "story": "No banco, as pessoas guardam seu dinheiro com segurança. Elas podem usar cartões eletrônicos para fazer pagamentos.",
                "subquestions": [
                    {
                        "id": "p69_s1",
                        "text": "1. Quando uma pessoa paga usando o CARTÃO DE DÉBITO, o que acontece com o dinheiro dela?",
                        "type": "radio",
                        "options": [
                            {"val": "debito", "text": "O valor é descontado imediatamente do saldo que ela tem na conta do banco", "correct": True},
                            {"val": "emprestimo", "text": "O banco dá o produto de graça", "correct": False},
                            {"val": "futuro", "text": "O valor só é cobrado depois de 5 anos", "correct": False}
                        ],
                        "explain": "No <strong>Débito</strong>, o dinheiro sai da sua conta na mesma hora. Você só pode gastar o que tiver de saldo!"
                    },
                    {
                        "id": "p69_s2",
                        "text": "2. E quando a pessoa paga com CARTÃO DE CRÉDITO?",
                        "type": "radio",
                        "options": [
                            {"val": "credito", "text": "O banco paga a loja na hora e envia uma fatura para a pessoa pagar no mês seguinte", "correct": True},
                            {"val": "sorteio", "text": "A pessoa ganha pontos mas nunca precisa pagar nada", "correct": False}
                        ],
                        "explain": "No <strong>Crédito</strong>, o banco faz um empréstimo temporário: junta todos os gastos numa fatura mensal para ser paga até o dia do vencimento."
                    }
                ]
            },
            {
                "id": "p70_q1",
                "page": "Página 70",
                "title": "O Orçamento Familiar da Casa do Lucas",
                "story": "A família do Lucas organizou todas as contas do mês numa tabela de orçamento:<br><br>"
                         "• <strong>Entradas (Renda total da família):</strong> R$ 3.200,00<br>"
                         "• <strong>Despesas do mês:</strong><br>"
                         "  - Aluguel da casa: R$ 1.100,00<br>"
                         "  - Compras de alimentação: R$ 950,00<br>"
                         "  - Contas de água e luz: R$ 350,00<br>"
                         "  - Transporte e combustível: R$ 400,00",
                "subquestions": [
                    {
                        "id": "p70_s1",
                        "text": "1. Qual é o valor TOTAL das despesas da família do Lucas neste mês?",
                        "type": "input_number",
                        "correct": 2800,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Somando as quatro despesas:<br>1.100 + 950 = 2.050<br>2.050 + 350 = 2.400<br>2.400 + 400 = <strong>R$ 2.800,00</strong>."
                    },
                    {
                        "id": "p70_s2",
                        "text": "2. Sobrou dinheiro do salário no final do mês? Qual é o SALDO positivo?",
                        "type": "input_number",
                        "correct": 400,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Fórmula do Saldo:<br><strong>Saldo = Entradas - Despesas</strong><br>Saldo = 3.200 - 2.800 = <strong>R$ 400,00</strong>.<br>Como o resultado é maior que zero, é um saldo positivo (a família conseguiu economizar!)."
                    }
                ]
            },
            {
                "id": "p71_q1",
                "page": "Página 71",
                "title": "Comparando Preços no Supermercado: Comprar Avulso ou Pacote?",
                "story": "Aprender a comparar preços nos ajuda a economizar bastante no supermercado!<br>"
                         "Veja a oferta de sabonetes:<br>"
                         "• <strong>Sabonete avulso (1 unidade):</strong> R$ 4,00<br>"
                         "• <strong>Pacote promocional com 3 unidades:</strong> R$ 9,00",
                "subquestions": [
                    {
                        "id": "p71_s1",
                        "text": "1. Quanto custariam 3 sabonetes se fossem comprados avulsos?",
                        "type": "input_number",
                        "correct": 12,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "3 unidades x R$ 4,00 = <strong>R$ 12,00</strong>."
                    },
                    {
                        "id": "p71_s2",
                        "text": "2. Quantos reais a pessoa ECONOMIZA comprando o pacote promocional de 3 por R$ 9,00?",
                        "type": "input_number",
                        "correct": 3,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Economia = Preço Avulso Total - Preço da Promoção = 12 - 9 = <strong>R$ 3,00 de economia</strong>!"
                    }
                ]
            },
            {
                "id": "p72_q1",
                "page": "Página 72",
                "title": "As Compras da Fátima na Papelaria (Problema em 3 Etapas)",
                "story": "Fátima foi comprar materiais escolares para o novo semestre:<br>"
                         "• <strong>2 cadernos universitários</strong> por R$ 18,00 cada um<br>"
                         "• <strong>1 estojo completo</strong> por R$ 24,00<br>"
                         "• <strong>1 caixa de lápis de cor</strong> por R$ 15,00<br>"
                         "Fátima pagou no caixa com uma cédula de <strong>R$ 100,00</strong>.",
                "subquestions": [
                    {
                        "id": "p72_s1",
                        "text": "1. Etapa 1: Quanto ela gastou apenas com os 2 cadernos?",
                        "type": "input_number",
                        "correct": 36,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "2 x 18 = <strong>R$ 36,00</strong>."
                    },
                    {
                        "id": "p72_s2",
                        "text": "2. Etapa 2: Qual foi o valor TOTAL da compra da Fátima?",
                        "type": "input_number",
                        "correct": 75,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Somando todos os itens:<br>Cadernos: R$ 36,00<br>Estojo: R$ 24,00<br>Lápis de cor: R$ 15,00<br>36 + 24 = 60 reais.<br>60 + 15 = <strong>R$ 75,00</strong>."
                    },
                    {
                        "id": "p72_s3",
                        "text": "3. Etapa 3: Quanto Fátima recebeu de troco ao pagar com R$ 100,00?",
                        "type": "input_number",
                        "correct": 25,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Troco = 100 - 75 = <strong>R$ 25,00</strong>.<br>(100 - 70 = 30; 30 - 5 = 25 reais)."
                    }
                ]
            },
            {
                "id": "p73_q1",
                "page": "Página 73",
                "title": "A Loja de Calçados do Mário e o Empréstimo das Centenas",
                "story": "Na loja de calçados do senhor Mário, um cliente comprou um <strong>tênis esportivo por R$ 145,00</strong> e um <strong>par de meias por R$ 18,00</strong>.<br>"
                         "Para pagar, o cliente entregou <strong>DUAS cédulas de R$ 100,00</strong> (total de R$ 200,00).",
                "subquestions": [
                    {
                        "id": "p73_s1",
                        "text": "1. Qual foi o total da compra do cliente?",
                        "type": "input_number",
                        "correct": 163,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "145 + 18 = <strong>R$ 163,00</strong>.<br>(145 + 10 = 155; 155 + 8 = 163)."
                    },
                    {
                        "id": "p73_s2",
                        "text": "2. Quanto o senhor Mário deve devolver de troco?",
                        "type": "input_number",
                        "correct": 37,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Troco = 200 - 163 = <strong>R$ 37,00</strong>.<br>"
                                   "<pre class='math-box'>"
                                   "  C  D  U
"
                                   "  1  9 10
"
                                   "  2  0  0
"
                                   "- 1  6  3
"
                                   "----------
"
                                   "  0  3  7
"
                                   "</pre>"
                                   "10 - 3 = 7 unidades.<br>9 - 6 = 3 dezenas.<br>1 - 1 = 0 centenas.<br>Troco exato: <strong>R$ 37,00</strong>!"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # ILHA 5: PÁGINAS 74 A 80 (MATERIAL DE APOIO - PARTE 2)
    # =========================================================================
    {
        "id": "missao-5",
        "number": 5,
        "title": "Ilha 5: Empreendedorismo, Gráficos e Grande Desafio Final",
        "pages_label": "Páginas 74 a 80 do Livro",
        "desc": "A contagem dos cofres, a barraca de limonada, compras à vista vs a prazo, gráfico de economia e a Grande Prova dos Campeões!",
        "badge": "Grande Mestre da Matemática Financeira",
        "color": "#ec4899",
        "icon": "🏆",
        "questions": [
            {
                "id": "p74_q1",
                "page": "Página 74",
                "title": "O Desafio da Contagem Rápida dos Dois Cofres",
                "story": "Dois amigos abriram seus cofres para contar as economias.<br>"
                         "• <strong>Cofre de Moedas:</strong> 5 moedas de R$ 1,00 + 8 moedas de 50 centavos + 12 moedas de 25 centavos.<br>"
                         "• <strong>Cofre Misto:</strong> 2 notas de R$ 20 + 3 notas de R$ 10 + 7 notas de R$ 2 + 6 moedas de 50 centavos.",
                "subquestions": [
                    {
                        "id": "p74_s1",
                        "text": "1. Quanto há no Cofre de Moedas?",
                        "type": "input_number",
                        "correct": 12,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Contando por partes:<br>"
                                   "• 5 moedas de R$ 1 = R$ 5,00<br>"
                                   "• 8 moedas de 50¢ = 400 centavos = R$ 4,00<br>"
                                   "• 12 moedas de 25¢ = 300 centavos = R$ 3,00<br>"
                                   "Total: 5 + 4 + 3 = <strong>R$ 12,00</strong>."
                    },
                    {
                        "id": "p74_s2",
                        "text": "2. Quanto há no Cofre Misto?",
                        "type": "input_number",
                        "correct": 87,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Contando cada cédula e moeda:<br>"
                                   "• 2 x 20 = 40 reais<br>"
                                   "• 3 x 10 = 30 reais<br>"
                                   "• 7 x 2 = 14 reais<br>"
                                   "• 6 moedas de 50¢ = R$ 3,00<br>"
                                   "Total: 40 + 30 + 14 + 3 = 70 + 17 = <strong>R$ 87,00</strong>."
                    }
                ]
            },
            {
                "id": "p75_q1",
                "page": "Página 75",
                "title": "A Barraca de Limonada do João e da Alice: Receita, Custo e Lucro",
                "story": "João e Alice montaram uma barraca de limonada fresca na feira da escola:<br>"
                         "• Eles gastaram <strong>R$ 22,00</strong> comprando limões, açúcar e copos descartáveis (<strong>Custo</strong>).<br>"
                         "• Eles venderam <strong>20 copos de suco por R$ 2,50 cada um</strong> (<strong>Faturamento</strong>).",
                "subquestions": [
                    {
                        "id": "p75_s1",
                        "text": "1. Quanto dinheiro João e Alice arrecadaram com as vendas (Faturamento)?",
                        "type": "input_number",
                        "correct": 50,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Multiplicação: 20 x 2,50 = <strong>R$ 50,00</strong>.<br>(10 copos x 2,50 = 25 reais; 20 copos = 25 + 25 = 50 reais)."
                    },
                    {
                        "id": "p75_s2",
                        "text": "2. Qual foi o LUCRO real de João e Alice?",
                        "type": "input_number",
                        "correct": 28,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Fórmula do Lucro:<br><strong>Lucro = Faturamento (Vendas) - Custos</strong><br>Lucro = 50 - 22 = <strong>R$ 28,00 de lucro líquido</strong>!"
                    }
                ]
            },
            {
                "id": "p76_q1",
                "page": "Página 76",
                "title": "A Compra da Bicicleta: À Vista vs A Prazo",
                "story": "Uma família quer comprar uma bicicleta para o filho e encontrou duas opções de pagamento:<br>"
                         "• <strong>Preço À Vista (pago na hora):</strong> R$ 280,00<br>"
                         "• <strong>Preço A Prazo:</strong> 3 parcelas de R$ 105,00 no cartão",
                "subquestions": [
                    {
                        "id": "p76_s1",
                        "text": "1. Qual é o valor total da bicicleta comprada A PRAZO?",
                        "type": "input_number",
                        "correct": 315,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "3 parcelas de 105 reais = 3 x 105 = <strong>R$ 315,00</strong>.<br>(3 x 100 = 300; 3 x 5 = 15; 300 + 15 = 315)."
                    },
                    {
                        "id": "p76_s2",
                        "text": "2. Quantos reais a família economiza se decidir pagar À VISTA?",
                        "type": "input_number",
                        "correct": 35,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Diferença = Preço a Prazo - Preço à Vista = 315 - 280 = <strong>R$ 35,00 de economia</strong>!"
                    }
                ]
            },
            {
                "id": "p77_q1",
                "page": "Página 77",
                "title": "O Desafio dos Centavos no Caixa",
                "story": "No supermercado, os preços quase sempre têm centavos! Vamos praticar o troco rápido com centavos:",
                "subquestions": [
                    {
                        "id": "p77_s1",
                        "text": "1. Uma barra de chocolate custa R$ 4,85 e você paga com uma moeda de R$ 5,00. Qual é o troco exato?",
                        "type": "radio",
                        "options": [
                            {"val": "15", "text": "15 centavos (uma moeda de 10¢ e uma de 5¢)", "correct": True},
                            {"val": "25", "text": "25 centavos", "correct": False},
                            {"val": "5", "text": "5 centavos", "correct": False}
                        ],
                        "explain": "5,00 - 4,85 = 0,15 (15 centavos). De 4,85 para 5,00 faltam 15 centavos (85 + 15 = 100 centavos)."
                    },
                    {
                        "id": "p77_s2",
                        "text": "2. Um gibi custa R$ 19,65 e você paga com uma nota de R$ 20,00. Qual é o troco?",
                        "type": "radio",
                        "options": [
                            {"val": "35", "text": "35 centavos (uma moeda de 25¢ e uma de 10¢)", "correct": True},
                            {"val": "45", "text": "45 centavos", "correct": False}
                        ],
                        "explain": "20,00 - 19,65 = 0,35 (35 centavos). 65 + 35 = 100 centavos = 1 real!"
                    }
                ]
            },
            {
                "id": "p78_q1",
                "page": "Página 78",
                "title": "O Gráfico de Poupança da Turma de Amigos",
                "story": "Veja o gráfico com o dinheiro economizado por 4 amigos da turma no mês:<br><br>"
                         "<div class='chart-container'>"
                         "  <div class='bar-row'><span class='bar-label'>Alice</span><div class='bar-track'><div class='bar-fill' style='width:70%; background:#10b981;'>R$ 35,00</div></div></div>"
                         "  <div class='bar-row'><span class='bar-label'>Pedro</span><div class='bar-track'><div class='bar-fill' style='width:100%; background:#3b82f6;'>R$ 50,00</div></div></div>"
                         "  <div class='bar-row'><span class='bar-label'>Bia</span><div class='bar-track'><div class='bar-fill' style='width:50%; background:#f59e0b;'>R$ 25,00</div></div></div>"
                         "  <div class='bar-row'><span class='bar-label'>Lucas</span><div class='bar-track'><div class='bar-fill' style='width:80%; background:#8b5cf6;'>R$ 40,00</div></div></div>"
                         "</div>",
                "subquestions": [
                    {
                        "id": "p78_s1",
                        "text": "1. Quem economizou a MAIOR quantia de dinheiro?",
                        "type": "radio",
                        "options": [
                            {"val": "pedro", "text": "Pedro (R$ 50,00)", "correct": True},
                            {"val": "lucas", "text": "Lucas (R$ 40,00)", "correct": False},
                            {"val": "alice", "text": "Alice (R$ 35,00)", "correct": False},
                            {"val": "bia", "text": "Bia (R$ 25,00)", "correct": False}
                        ],
                        "explain": "Pedro guardou R$ 50,00, a maior barra do gráfico."
                    },
                    {
                        "id": "p78_s2",
                        "text": "2. Qual é a DIFERENÇA entre o valor economizado por Pedro e por Bia?",
                        "type": "input_number",
                        "correct": 25,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Diferença = Pedro (50) - Bia (25) = <strong>R$ 25,00</strong>."
                    },
                    {
                        "id": "p78_s3",
                        "text": "3. Quanto os 4 amigos economizaram JUNTOS?",
                        "type": "input_number",
                        "correct": 150,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Soma de todos: 35 + 50 + 25 + 40.<br>35 + 25 = 60.<br>50 + 40 = 90.<br>60 + 90 = <strong>R$ 150,00 economizados juntos</strong>!"
                    }
                ]
            },
            {
                "id": "p79_q1",
                "page": "Página 79",
                "title": "O Simulador de Troco do Caixa com Menor Número de Notas",
                "story": "Como um caixa profissional, dê o troco usando o <strong>menor número possível de cédulas e moedas</strong>!",
                "subquestions": [
                    {
                        "id": "p79_s1",
                        "text": "1. Compra de R$ 34,00 paga com uma nota de R$ 50,00. O troco é de R$ 16,00. Qual a menor quantidade de notas/moedas?",
                        "type": "radio",
                        "options": [
                            {"val": "10_5_1", "text": "3 peças: 1 cédula de R$ 10 + 1 cédula de R$ 5 + 1 moeda de R$ 1", "correct": True},
                            {"val": "8x2", "text": "8 cédulas de R$ 2 (muitas cédulas)", "correct": False},
                            {"val": "16x1", "text": "16 moedas de R$ 1 (muitas moedas)", "correct": False}
                        ],
                        "explain": "10 + 5 + 1 = 16 reais. São necessárias apenas 3 peças no total!"
                    },
                    {
                        "id": "p79_s2",
                        "text": "2. Compra de R$ 142,00 paga com uma nota de R$ 200,00. Troco de R$ 58,00. Qual a menor combinação?",
                        "type": "radio",
                        "options": [
                            {"val": "50_5_2_1", "text": "4 peças: 1 nota de R$ 50 + 1 nota de R$ 5 + 1 nota de R$ 2 + 1 moeda de R$ 1", "correct": True},
                            {"val": "2x20_18x1", "text": "Muitas notas de 20 e moedas", "correct": False}
                        ],
                        "explain": "50 + 5 + 2 + 1 = 58 reais. Apenas 4 peças!"
                    }
                ]
            },
            {
                "id": "p80_q1",
                "page": "Página 80",
                "title": "A Grande Prova dos Campeões Monetários",
                "story": "🌟 <strong>PARABÉNS POR CHEGAR ATÉ AQUI, ALICE!</strong><br>"
                         "Este é o desafio final que reúne tudo o que aprendemos no Capítulo 9. Resolva estas duas questões finais para conquistar seu Troféu de Mestre!",
                "subquestions": [
                    {
                        "id": "p80_s1",
                        "text": "1. Você tem uma nota de R$ 100,00. Compra 2 livros de R$ 35,00 cada e 1 lanche de R$ 12,00. Quanto vai sobrar de troco?",
                        "type": "input_number",
                        "correct": 18,
                        "unit": "reais",
                        "prefix": "R$",
                        "explain": "Passo 1: Livros = 2 x 35 = R$ 70,00.<br>"
                                   "Passo 2: Total gasto = 70 + 12 = R$ 82,00.<br>"
                                   "Passo 3: Troco = 100 - 82 = <strong>R$ 18,00</strong>!"
                    },
                    {
                        "id": "p80_s2",
                        "text": "2. Na conta 200 - 168 (as 3 bolas de R$ 56), por que o algarismo das dezenas do resultado é 3 e NÃO 4?",
                        "type": "radio",
                        "options": [
                            {"val": "emprestou", "text": "Porque a dezena recebeu 10 da centena, mas teve que emprestar 1 para a unidade, ficando com 9 (9 - 6 = 3)", "correct": True},
                            {"val=regra", "text": "Porque na matemática sempre se diminui 1 por diversão", "correct": False}
                        ],
                        "explain": "Exatamente! Essa é a regra de ouro da subtração com empréstimo / recurso. O 10 virou 9 ao ceder para as unidades, logo 9 - 6 = 3. O troco é R$ 32,00!"
                    }
                ]
            }
        ]
    }
]
