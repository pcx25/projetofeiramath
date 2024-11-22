import streamlit as st
import random
import time


# Função para inicializar o estado do jogo
def iniciar_jogo():
    return {
        "nome": "",
        "vida": 100,
        "energia": 100,
        "arma": "faca",
        "localizacao": "início",
        "historia": [],
        "inimigos_derrotados": 0,
    }


# Função para exibir o nome do jogador
def obter_nome():
    nome = st.text_input("Digite seu nome:", "")
    if nome:
        return nome
    return None


# Função para exibir a introdução do jogo
def introducao():
    st.title("Aventura na Terra Desolada")
    st.write(
        "Você acorda em um mundo desolado. Sua missão: sobreviver e descobrir o segredo por trás deste apocalipse.")
    st.write("Você está em um local desconhecido. O que você fará?")
    st.write("Use as opções abaixo para começar sua jornada.")


# Função para mostrar opções de ação
def exibir_opcoes():
    st.write("Escolha sua ação:")
    opcoes = ["Explorar", "Atacar", "Descansar", "Inventário"]
    escolha = st.radio("O que você deseja fazer?", opcoes)
    return escolha


# Função para simular uma batalha
def batalha():
    inimigo = random.choice(["Zumbi", "Bandidos", "Monstro Mutante"])
    inimigo_vida = random.randint(30, 100)
    dano_jogador = random.randint(10, 30)

    st.write(f"Você encontra um {inimigo}!")
    st.write(f"{inimigo} tem {inimigo_vida} de vida.")

    while inimigo_vida > 0:
        st.write(f"\nSua vida: {jogo['vida']}")
        st.write(f"Vida do {inimigo}: {inimigo_vida}")

        escolha = st.radio("O que você fará?", ["Atacar", "Fugir"])

        if escolha == "Atacar":
            dano_inimigo = random.randint(5, 20)
            inimigo_vida -= dano_jogador
            jogo["vida"] -= dano_inimigo

            st.write(f"Você atacou! Causou {dano_jogador} de dano.")
            st.write(f"{inimigo} atacou de volta e causou {dano_inimigo} de dano!")
            st.write(f"Você tem {jogo['vida']} de vida restante.")

            if jogo["vida"] <= 0:
                st.write("Você foi derrotado!")
                return False

            if inimigo_vida <= 0:
                st.write(f"Você derrotou o {inimigo}!")
                jogo["inimigos_derrotados"] += 1
                return True

        elif escolha == "Fugir":
            st.write("Você tenta fugir, mas o inimigo te persegue! A batalha continua.")

    return False


# Função para exibir o inventário do jogador
def inventario():
    st.write("Seu inventário:")
    st.write(f"Arma: {jogo['arma']}")
    st.write(f"Vida: {jogo['vida']}")
    st.write(f"Energia: {jogo['energia']}")
    st.write(f"Inimigos derrotados: {jogo['inimigos_derrotados']}")


# Função para explorar o mundo
def explorar():
    evento = random.choice(
        ["Você encontra um baú de suprimentos!", "Você encontra um inimigo!", "Você encontra uma fonte de energia!"])
    st.write(evento)

    if evento == "Você encontra um baú de suprimentos!":
        suprimento = random.choice(["Poção de Vida", "Arma Melhor", "Armadura"])
        st.write(f"Você recebeu um {suprimento}.")
        if suprimento == "Poção de Vida":
            jogo["vida"] += 30
        elif suprimento == "Arma Melhor":
            jogo["arma"] = "Espada"
        elif suprimento == "Armadura":
            jogo["vida"] += 20
    elif evento == "Você encontra um inimigo!":
        if not batalha():
            return "Você foi derrotado."
    elif evento == "Você encontra uma fonte de energia!":
        energia = random.randint(10, 50)
        jogo["energia"] += energia
        st.write(f"Você recuperou {energia} de energia!")


# Função principal do jogo
def jogar():
    global jogo
    if not jogo["nome"]:
        nome = obter_nome()
        if nome:
            jogo["nome"] = nome
            jogo["historia"].append(f"{nome} começa sua jornada na Terra Desolada.")

    introducao()
    escolha = exibir_opcoes()

    if escolha == "Explorar":
        resultado = explorar()
        if resultado == "Você foi derrotado.":
            st.write("Fim de jogo.")
            return
    elif escolha == "Atacar":
        batalha()
    elif escolha == "Descansar":
        jogo["vida"] += 20
        jogo["energia"] += 20
        st.write("Você descansou e recuperou um pouco da sua energia e vida.")
    elif escolha == "Inventário":
        inventario()


# Inicializa o jogo
if 'jogo' not in st.session_state:
    st.session_state.jogo = iniciar_jogo()

# Inicia a jogabilidade
jogo = st.session_state.jogo
jogar()

