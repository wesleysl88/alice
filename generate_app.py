# -*- coding: utf-8 -*-
"""
Full application generator for Alice's 3rd Grade Math - Sistema Monetário
"""
import json
import os

missions_data = [
    {
        "id": "missao-1",
        "number": 1,
        "title": "Ilha 1: O Surgimento do Dinheiro e Nosso Sistema",
        "pages_label": "Páginas 54 a 58 do Livro",
        "desc": "A vitrine da loja de brinquedos, o presente da amiga, do escambo ao Pix, a regra da vírgula e o cofrinho da Sara!",
        "color": "#059669",
        "icon": "🪙",
        "questions": [
            {
                "id": "p54_q1",
                "page": "Página 54",
                "title": "A Vitrine da Loja de Brinquedos da Sara",
                "story": "Sara e o pai foram à loja de brinquedos para escolher um presente. Na prateleira, eles observaram quatro brinquedos:<br><br>"
                         "<div class='toy-grid'>"
                         "  <div class='toy-card'><span class='toy-icon'>🧸</span><div class='toy-name'>Ursinho de Pelúcia</div><div class='toy-price'>R$ 65,00</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>⚽</span><div class='toy-name'>Bola Colorida</div><div class='toy-price'>R$ 20,00</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>🐰</span><div class='toy-name'>Bicho de Pelúcia</div><div class='toy-price'>R$ 85,25</div></div>"
                         "  <div class='toy-card'><span class='toy-icon'>👧</span><div class='toy-name'>Boneca Grande</div><div class='toy-price'>R$ 120,50</div></div>"
                         "</div>",
                "prompt": "Observe os preços na vitrine e responda:",
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
                        "explain": "Comparando os números: R$ 120,50 é o maior número de todos (possui 1 centena, 2 dezenas e centavos). Ordem decrescente: R$ 120,50 > R$ 85,25 > R$ 65,00 > R$ 20,00."
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
                        "explain": "O menor valor entre todos os brinquedos é R$ 20,00 (Bola Colorida)."
                    },
                    {
                        "id": "p54_s3",
                        "text": "3. O pai de Sara disse que o presente deve custar ATÉ R$ 100,00. Quais brinquedos eles podem escolher sem ultrapassar esse valor?",
                        "type": "checkbox",
                        "options": [
                            {"val": "bola", "text": "Bola Colorida (R$ 20,00)", "correct": True},
                            {"val": "urso", "text": "Ursinho de Pelúcia (R$ 65,00)", "correct": True},
                            {"val": "coelho", "text": "Bicho de Pelúcia (R$ 85,25)", "correct": True},
                            {"val": "boneca", "text": "Boneca Grande (R$ 120,50)", "correct": False}
                        ],
                        "explain": "Podem escolher qualquer brinquedo com preço menor ou igual a R$ 100,00: a Bola (20 < 100), o Urso (65 < 100) e o Bicho de Pelúcia (85,25 < 100). Apenas a Boneca Grande de R$ 120,50 ultrapassa o valor!"
                    }
                ]
            },
            {
                "id": "p55_q1",
                "page": "Página 55",
                "title": "O Presente de R$ 85,25 para a Melhor Amiga",
                "story": "Sara escolheu comprar o bicho de pelúcia de <strong>R$ 85,25</strong> para sua melhor amiga.<br>Qual das opções abaixo mostra a <strong>quantia exata</strong> desse valor para pagar no caixa sem receber troco?",
                "subquestions": [
                    {
                        "id": "p55_s1",
                        "text": "Marque um X na opção correta:",
                        "type": "radio_cards",
                        "options": [
                            {
                                "val": "op1",
                                "title": "Opção A (Cédulas e Moeda)",
                                "bills": [50, 20, 10, 5],
                                "coins": [0.25],
                                "desc": "Cédulas: 50 + 20 + 10 + 5 = 85 reais<br>Moeda: 25 centavos<br><strong>Total: R$ 85,25</strong>",
                                "correct": True
                            },
                            {
                                "val": "op2",
                                "title": "Opção B (Cédulas e Moeda)",
                                "bills": [50, 20, 20, 5],
                                "coins": [0.25],
                                "desc": "Cédulas: 50 + 20 + 20 + 5 = 95 reais<br>Moeda: 25 centavos<br><strong>Total: R$ 95,25</strong>",
                                "correct": False
                            }
                        ],
                        "explain": "Na Opção A: 50 + 20 = 70. 70 + 10 = 80. 80 + 5 = 85 reais. Mais a moeda de 25 centavos: temos exatamente <strong>R$ 85,25</strong>!<br>Na Opção B, 50 + 20 + 20 + 5 = 95 reais, passando 10 reais do valor da compra."
                    }
                ],
                "caderno": "✏️ Atividade do Livro/Caderno: No livro há uma etiqueta para você pesquisar um brinquedo de até R$ 100,00 e desenhar as cédulas para pagar sem troco."
            },
            {
                "id": "p56_q1",
                "page": "Página 56",
                "title": "História do Dinheiro: Como Tudo Começou",
                "story": "Sara e o pai usaram cédulas e moedas para pagar o presente. Mas nem sempre o dinheiro foi como é atualmente!",
                "subquestions": [
                    {
                        "id": "p56_s1",
                        "text": "1. Antes de o dinheiro existir, as pessoas trocavam produtos (por exemplo, um agricultor trocava trigo por peixe com um pescador). Qual é o nome desse tipo de troca?",
                        "type": "radio",
                        "options": [
                            {"val": "escambo", "text": "Escambo", "correct": True},
                            {"val": "troco", "text": "Troco", "correct": False},
                            {"val": "cifrao", "text": "Cifrão", "correct": False},
                            {"val": "extenso", "text": "Extenso", "correct": False}
                        ],
                        "explain": "O escambo é a troca direta de mercadorias sem a utilização de dinheiro."
                    },
                    {
                        "id": "p56_s2",
                        "text": "2. Por que as pessoas sentiram a necessidade de inventar moedas e cédulas?",
                        "type": "radio",
                        "options": [
                            {"val": "necessidade", "text": "Porque nem sempre a outra pessoa queria o produto oferecido e era difícil saber quantos peixes valiam um saco de trigo", "correct": True},
                            {"val": "banco", "text": "Porque os pescadores não gostavam de pescar", "correct": False}
                        ],
                        "explain": "Com as moedas de metal marcado (ouro, prata) e depois as cédulas, cada produto passou a ter um preço fixo, facilitando as trocas justas."
                    },
                    {
                        "id": "p56_s3",
                        "text": "3. Atualmente, além de moedas e cédulas de papel, quais outras formas usamos para pagar?",
                        "type": "checkbox",
                        "options": [
                            {"val": "pix", "text": "Pix (transferência instantânea pela internet)", "correct": True},
                            {"val": "cartao", "text": "Cartão de débito ou de crédito", "correct": True},
                            {"val": "troca_peixe", "text": "Troca de peixes por trigo no shopping", "correct": False}
                        ],
                        "explain": "Hoje usamos dinheiro em espécie, cartões magnéticos e pagamentos digitais instantâneos como o Pix."
                    }
                ]
            },
            {
                "id": "p57_q1",
                "page": "Página 57",
                "title": "Nosso Dinheiro e a Regra da Vírgula",
                "story": "No Brasil, nosso dinheiro se chama <strong>Real (R$)</strong>. Ele é composto de moedas e cédulas.<br>"
                         "Observe como o preço da boneca da Sara é escrito: <strong>R$ 85,25</strong>.",
                "subquestions": [
                    {
                        "id": "p57_s1",
                        "text": "1. Qual é a regra fundamental da VÍRGULA no dinheiro?",
                        "type": "radio",
                        "options": [
                            {"val": "separa", "text": "A vírgula separa a quantia inteira em REAIS (à esquerda) da quantia em CENTAVOS (à direita)", "correct": True},
                            {"val": "enfeite", "text": "A vírgula serve apenas para separar números pares de números ímpares", "correct": False}
                        ],
                        "explain": "Regra de ouro: Em R$ 85,25, temos 85 REAIS e 25 CENTAVOS. A vírgula é quem faz essa divisão precisa!"
                    },
                    {
                        "id": "p57_s2",
                        "text": "2. A boneca mais cara da vitrine custava R$ 120,50. É possível pagar essa quantia exata usando APENAS CÉDULAS, sem usar moedas e sem receber troco?",
                        "type": "radio",
                        "options": [
                            {"val": "nao", "text": "Não, porque não existe cédula de centavos (os 50 centavos exigem moedas)", "correct": True},
                            {"val": "sim", "text": "Sim, pagando com notas de 2 reais", "correct": False}
                        ],
                        "explain": "Exatamente! A menor cédula é de R$ 2,00. Os 50 centavos são fração de real e exigem moeda (uma de 50¢ ou duas de 25¢)."
                    },
                    {
                        "id": "p57_s3",
                        "text": "3. Como lemos o valor R$ 85,25 por extenso?",
                        "type": "radio",
                        "options": [
                            {"val": "oitenta_e_cinco", "text": "Oitenta e cinco reais e vinte e cinco centavos", "correct": True},
                            {"val": "oitenta_vinte", "text": "Oitenta e cinco reais e vinte centavos", "correct": False},
                            {"val": "oitocentos", "text": "Oitocentos e cinquenta e dois reais", "correct": False}
                        ],
                        "explain": "Lê-se a parte inteira dos reais (oitenta e cinco reais) e em seguida os centavos (vinte e cinco centavos)."
                    }
                ]
            },
            {
                "id": "p58_q1",
                "page": "Página 58",
                "title": "O Cofrinho da Sara na Loja de Brinquedos",
                "story": "Sara levou a quantia de <strong>R$ 80,00</strong> que guardou no cofrinho para comprar um brinquedo para si mesma.<br>"
                         "Ela viu três opções:<br>"
                         "• Boneca: <strong>R$ 85,25</strong><br>"
                         "• Bicho de pelúcia (Urso): <strong>R$ 65,00</strong><br>"
                         "• Jogo 4 em 1 Clássicos: <strong>R$ 35,00</strong>",
                "subquestions": [
                    {
                        "id": "p58_s1",
                        "text": "1. Sara pode comprar a boneca de R$ 85,25 com os R$ 80,00 que tem?",
                        "type": "radio",
                        "options": [
                            {"val": "nao", "text": "Não, porque R$ 85,25 é maior que R$ 80,00 (faltam R$ 5,25)", "correct": True},
                            {"val": "sim", "text": "Sim, o dinheiro é suficiente", "correct": False}
                        ],
                        "explain": "85,25 > 80,00. O dinheiro dela não é suficiente para a boneca."
                    },
                    {
                        "id": "p58_s2",
                        "text": "2. Sara decidiu comprar o bicho de pelúcia de R$ 65,00. Quanto dinheiro vai SOBRAR para ela?",
                        "type": "input_money",
                        "correct": 15.00,
                        "explain": "Subtração armada: 80 - 65 = R$ 15,00.<br>C D U:<br>80 vira 7 dezenas e 10 unidades.<br>10 - 5 = 5 (unidades)<br>7 - 6 = 1 (dezenas)<br>Vai sobrar: <strong>R$ 15,00</strong>."
                    },
                    {
                        "id": "p58_s3",
                        "text": "3. Para pagar os R$ 65,00 sem receber troco, quais notas ela pode entregar?",
                        "type": "radio",
                        "options": [
                            {"val": "3x20_1x5", "text": "Três cédulas de R$ 20,00 e uma de R$ 5,00 (20 + 20 + 20 + 5 = 65)", "correct": True},
                            {"val": "2x20_1x10", "text": "Duas cédulas de R$ 20,00 e uma de R$ 10,00 (dá 50 reais)", "correct": False}
                        ],
                        "explain": "3 x 20 = 60 reais. 60 + 5 = R$ 65,00 exatos!"
                    }
                ]
            }
        ]
    }
]

print("Missions 1 loaded. Appending missions 2 to 5...")
