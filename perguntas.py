perguntas = [
    # Nível 1 (Fácil)
    {
        "pergunta": "Nível 1: Qual é o próximo número na sequência: 2, 4, 6, 8, ?",
        "alternativas": ["10", "12", "9", "11"],
        "resposta": "10",
        "explicacao": "A sequência adiciona 2 a cada número: 2 + 2 = 4, 4 + 2 = 6, etc.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Se um trem leva 3 minutos para passar por um túnel, quanto tempo ele levará para passar por dois túneis idênticos?",
        "alternativas": ["6 minutos", "3 minutos", "5 minutos", "4 minutos"],
        "resposta": "6 minutos",
        "explicacao": "Cada túnel leva 3 minutos, então 2 túneis levarão 6 minutos.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Qual é o número que é metade de 10?",
        "alternativas": ["5", "2", "7", "10"],
        "resposta": "5",
        "explicacao": "Metade de 10 é 5.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Um pai tem 5 filhos: Ana, Beto, Carla e Diego. Qual é o nome do quinto filho?",
        "alternativas": ["Eduardo", "João", "Carlos", "Qual"],
        "resposta": "Qual",
        "explicacao": "O nome do quinto filho está na pergunta: 'Qual'.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Um pato tem duas patas. Quantas patas têm três patos?",
        "alternativas": ["6", "3", "9", "12"],
        "resposta": "6",
        "explicacao": "Cada pato tem 2 patas, então 3 patos têm 2 x 3 = 6 patas.",
        "nivel": 1
    },
    # Nível 2 (Médio)
    {
        "pergunta": "Nível 2: Complete a sequência: 1, 1, 2, 3, 5, 8, ?",
        "alternativas": ["13", "11", "10", "12"],
        "resposta": "13",
        "explicacao": "Esta é a sequência de Fibonacci: cada número é a soma dos dois anteriores.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Se você tem 3 maçãs e pega 2, quantas você tem agora?",
        "alternativas": ["2", "3", "1", "5"],
        "resposta": "2",
        "explicacao": "Se você pega 2 maçãs, você fica com 2 maçãs, independentemente de quantas havia antes.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Qual é o número seguinte na sequência: 10, 20, 30, 40, ?",
        "alternativas": ["50", "60", "45", "55"],
        "resposta": "50",
        "explicacao": "A sequência soma 10 a cada número.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Qual número é menor do que 30, mas maior do que 20, e divisível por 3?",
        "alternativas": ["21", "27", "24", "22"],
        "resposta": "27",
        "explicacao": "O número 27 é divisível por 3 e está entre 20 e 30.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Se 1 é igual a 3, 2 é igual a 3, 3 é igual a 5, e 4 é igual a 4, quanto é 5?",
        "alternativas": ["4", "3", "5", "6"],
        "resposta": "4",
        "explicacao": "A resposta é o número de letras na palavra do número: 'cinco' tem 4 letras.",
        "nivel": 2
    },
    # Nível 3 (Difícil)
    {
        "pergunta": "Nível 3: Qual é o próximo número na sequência: 2, 4, 8, 16, ?",
        "alternativas": ["32", "24", "20", "18"],
        "resposta": "32",
        "explicacao": "Cada número é multiplicado por 2.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Um homem tem 4 filhas, e cada filha tem um irmão. Quantos filhos ele tem?",
        "alternativas": ["4", "5", "8", "9"],
        "resposta": "5",
        "explicacao": "Cada filha tem o mesmo irmão, então são 4 filhas e 1 irmão.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Qual é o próximo número na sequência: 3, 6, 12, 24, ?",
        "alternativas": ["48", "30", "36", "50"],
        "resposta": "48",
        "explicacao": "Cada número é multiplicado por 2.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Em um aquário há 10 peixes. Se 2 peixes se afogarem, quantos restam?",
        "alternativas": ["10", "8", "5", "0"],
        "resposta": "10",
        "explicacao": "Peixes não se afogam!",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: O que vem a seguir: A, C, E, G, ?",
        "alternativas": ["I", "H", "J", "K"],
        "resposta": "I",
        "explicacao": "A sequência pula uma letra: A, (B), C, (D), E, (F), G, (H), I.",
        "nivel": 3
    },
    # Nível 4 (Muito Difícil)
    {
        "pergunta": "Nível 4: Qual é o próximo número: 1, 3, 6, 10, 15, ?",
        "alternativas": ["21", "20", "19", "22"],
        "resposta": "21",
        "explicacao": "Cada número é a soma dos números naturais: 1, 1+2, 1+2+3, etc.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Se ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?",
        "alternativas": ["Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"],
        "resposta": "Quarta-feira",
        "explicacao": "Ontem sendo amanhã implica que hoje é quarta-feira.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Qual número preenche o espaço: 2, 6, 12, 20, 30, ?",
        "alternativas": ["42", "35", "40", "45"],
        "resposta": "42",
        "explicacao": "A sequência segue a fórmula n(n+1), onde n é 1, 2, 3, 4, etc.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Três gatos pegam três ratos em três minutos. Quantos minutos 100 gatos levarão para pegar 100 ratos?",
        "alternativas": ["3", "100", "30", "10"],
        "resposta": "3",
        "explicacao": "Cada gato pega um rato em 3 minutos. Portanto, 100 gatos pegam 100 ratos em 3 minutos.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: O que vem a seguir: 1, 4, 9, 16, 25, ?",
        "alternativas": ["36", "49", "30", "40"],
        "resposta": "36",
        "explicacao": "A sequência são quadrados perfeitos: 1², 2², 3², 4², 5², 6².",
        "nivel": 4
    },
    # Nível 5 (Extremo)
    {
        "pergunta": "Nível 5: Qual é o próximo número na sequência: 1, 1, 2, 6, 24, ?",
        "alternativas": ["120", "48", "36", "72"],
        "resposta": "120",
        "explicacao": "É a sequência de fatoriais: 1!, 2!, 3!, 4!, 5! = 120.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: O relógio marca 3:15. Qual o ângulo entre os ponteiros?",
        "alternativas": ["7.5°", "12°", "30°", "0°"],
        "resposta": "7.5°",
        "explicacao": "O ponteiro das horas está 1/4 do caminho entre 3 e 4, ou 7.5°.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Um número é dividido por 3 e resulta em 8 com resto 1. Qual é o número?",
        "alternativas": ["25", "24", "20", "18"],
        "resposta": "25",
        "explicacao": "8 x 3 = 24, e somando o resto (1), temos 25.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Complete: 2, 4, 8, 14, 22, ?",
        "alternativas": ["32", "36", "30", "26"],
        "resposta": "32",
        "explicacao": "Cada número soma 2, 4, 6, 8, 10, etc.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: O que vem a seguir: 3, 5, 11, 29, ?",
        "alternativas": ["47", "41", "53", "37"],
        "resposta": "47",
        "explicacao": "Os números seguem o padrão: (2^n) - 1, sendo n = 2, 3, 5, 7, 11...",
        "nivel": 5
    }
]
