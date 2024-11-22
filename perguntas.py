perguntas = [
    # Nível 1 (Fácil)
    {
        "pergunta": "Nível 1: Qual é o próximo número na sequência: 2, 4, 6, 8, ?",
        "alternativas": ["12", "10", "9", "11"],
        "resposta": "10",
        "explicacao": "A sequência adiciona 2 a cada número: 2 + 2 = 4, 4 + 2 = 6, etc.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Se um trem leva 3 minutos para passar por um túnel, quanto tempo ele levará para passar por dois túneis idênticos?",
        "alternativas": ["3 minutos", "6 minutos", "5 minutos", "4 minutos"],
        "resposta": "6 minutos",
        "explicacao": "Cada túnel leva 3 minutos, então 2 túneis levarão 6 minutos.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Qual é o número que é metade de 10?",
        "alternativas": ["2", "10", "5", "7"],
        "resposta": "5",
        "explicacao": "Metade de 10 é 5.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Um pai tem 5 filhos: Ana, Beto, Carla e Diego. Qual, é o nome do quinto filho?",
        "alternativas": ["Carlos", "João", "Eduardo", "Qual"],
        "resposta": "Qual",
        "explicacao": "O nome do quinto filho está na pergunta: 'Qual'.",
        "nivel": 1
    },
    {
        "pergunta": "Nível 1: Um pato tem duas patas. Quantas patas têm três patos?",
        "alternativas": ["12", "9", "6", "3"],
        "resposta": "6",
        "explicacao": "Cada pato tem 2 patas, então 3 patos têm 2 x 3 = 6 patas.",
        "nivel": 1
    },

    # Nível 2 (Médio)
    {
        "pergunta": "Nível 2: Complete a sequência: 1, 1, 2, 3, 5, 8, ?",
        "alternativas": ["11", "13", "10", "12"],
        "resposta": "13",
        "explicacao": "Esta é a sequência de Fibonacci: cada número é a soma dos dois anteriores.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Se você tem 3 maçãs e pega 2, quantas você tem agora?",
        "alternativas": ["1", "5", "3", "2"],
        "resposta": "2",
        "explicacao": "Se você pega 2 maçãs, você fica com 2 maçãs, independentemente de quantas havia antes.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Qual é o número seguinte na sequência: 10, 20, 30, 40, ?",
        "alternativas": ["50", "45", "55", "60"],
        "resposta": "50",
        "explicacao": "A sequência soma 10 a cada número.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Qual número é menor do que 30, mas maior do que 20, e divisível por 3?",
        "alternativas": ["21", "27", "22", "24"],
        "resposta": "27",
        "explicacao": "O número 27 é divisível por 3 e está entre 20 e 30.",
        "nivel": 2
    },
    {
        "pergunta": "Nível 2: Se 1 é igual a 3, 2 é igual a 3, 3 é igual a 5, e 4 é igual a 4, quanto é 5?",
        "alternativas": ["3", "5", "6", "4"],
        "resposta": "4",
        "explicacao": "A resposta é o número de letras na palavra do número: 'cinco' tem 4 letras.",
        "nivel": 2
    },

    # Nível 3 (Difícil)
    {
        "pergunta": "Nível 3: Qual é o próximo número na sequência: 2, 4, 8, 16, ?",
        "alternativas": ["18", "24", "20", "32"],
        "resposta": "32",
        "explicacao": "Cada número é multiplicado por 2.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Um homem tem 4 filhas, e cada filha tem um irmão. Quantos filhos ele tem?",
        "alternativas": ["8", "5", "4", "9"],
        "resposta": "5",
        "explicacao": "Cada filha tem o mesmo irmão, então são 4 filhas e 1 irmão.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Qual é o próximo número na sequência: 3, 6, 12, 24, ?",
        "alternativas": ["48", "50", "30", "36"],
        "resposta": "48",
        "explicacao": "Cada número é multiplicado por 2.",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: Em um aquário há 10 peixes. Se 2 peixes se afogarem, quantos restam?",
        "alternativas": ["0", "8", "5", "10"],
        "resposta": "10",
        "explicacao": "Peixes não se afogam!",
        "nivel": 3
    },
    {
        "pergunta": "Nível 3: O que vem a seguir: A, C, E, G, ?",
        "alternativas": ["H", "K", "I", "J"],
        "resposta": "I",
        "explicacao": "A sequência pula uma letra: A, (B), C, (D), E, (F), G, (H), I.",
        "nivel": 3
    },

    # Nível 4 (Muito Difícil)
    {
        "pergunta": "Nível 4: Qual é o próximo número: 1, 3, 6, 10, 15, ?",
        "alternativas": ["19", "20", "21", "22"],
        "resposta": "21",
        "explicacao": "Cada número é a soma dos números naturais: 1, 1+2, 1+2+3, etc.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Se ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?",
        "alternativas": ["Sexta-feira", "Sábado", "Quarta-feira", "Quinta-feira"],
        "resposta": "Quarta-feira",
        "explicacao": "Ontem sendo amanhã implica que hoje é quarta-feira.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Qual número preenche o espaço: 2, 6, 12, 20, 30, ?",
        "alternativas": ["40", "45", "42", "35"],
        "resposta": "42",
        "explicacao": "A sequência segue a fórmula n(n+1), onde n é 1, 2, 3, 4, etc.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: Três gatos pegam três ratos em três minutos. Quantos minutos 100 gatos levarão para pegar 100 ratos?",
        "alternativas": ["30", "100", "3", "10"],
        "resposta": "3",
        "explicacao": "Cada gato pega um rato em 3 minutos. Portanto, 100 gatos pegam 100 ratos em 3 minutos.",
        "nivel": 4
    },
    {
        "pergunta": "Nível 4: O que vem a seguir: 1, 4, 9, 16, 25, ?",
        "alternativas": ["49", "40", "30", "36"],
        "resposta": "36",
        "explicacao": "A sequência são quadrados perfeitos: 1², 2², 3², 4², 5², 6².",
        "nivel": 4
    },

    # Nível 5 (Extremo)
    {
        "pergunta": "Nível 5: Qual é o próximo número na sequência: 1, 1, 2, 6, 24, ?",
        "alternativas": ["72", "120", "96", "48"],
        "resposta": "120",
        "explicacao": "A sequência é a fatorial: 1!, 2!, 3!, 4!, etc.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Quantos zeros há no final de 100! (100 fatorial)?",
        "alternativas": ["24", "25", "22", "23"],
        "resposta": "24",
        "explicacao": "O número de zeros é o número de vezes que 100 pode ser dividido por 5 (e seus múltiplos): 100/5 + 100/25 = 24.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Qual é o número que, dividido por 2, 3, 4, 5 e 6, deixa sempre resto 1?",
        "alternativas": ["61", "120", "31", "121"],
        "resposta": "121",
        "explicacao": "O número 121 deixa resto 1 quando dividido por 2, 3, 4, 5 e 6.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Um trem de 150 metros cruza um túnel de 300 metros a 90 km/h. Quanto tempo ele leva?",
        "alternativas": ["18s", "12s", "20s", "15s"],
        "resposta": "18s",
        "explicacao": "Distância total: 150 + 300 = 450m. Velocidade: 90 km/h = 25 m/s. Tempo: 450/25 = 18s.",
        "nivel": 5
    },
    {
        "pergunta": "Nível 5: Qual é o menor número positivo que é divisível por 1 a 10?",
        "alternativas": ["210", "2520", "120", "1260"],
        "resposta": "2520",
        "explicacao": "2520 é o MMC (mínimo múltiplo comum) de 1 a 10.",
        "nivel": 5
    }
]
