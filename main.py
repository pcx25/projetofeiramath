import streamlit as st
from PIL import Image
import random
from perguntas import perguntas  # Importando as perguntas


def jogo_perguntas():
    st.set_page_config(page_title="Jogo de Raciocínio Lógico!", page_icon="🧠")
    st.title("🧠 Jogo de Raciocínio Lógico!")
    st.markdown(
        "<div style='font-size:18px;'>Bem-vindo ao desafio de raciocínio lógico! Teste seus conhecimentos e tente acertar todas as perguntas. 🚀</div>",
        unsafe_allow_html=True,
    )

    # CSS para melhorar a responsividade
    st.markdown(
        """
        <style>
            /* Ajustes de CSS para responsividade */
            @media only screen and (max-width: 600px) {
                h1, h2, h3, h4, h5, h6 { font-size: 16px; }
                .css-18e3th9 { font-size: 14px; }
                .creditos { font-size: 18px; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("Sobre o Jogo")
    st.sidebar.info(
        "🧩 Este jogo de raciocínio lógico foi criado para testar suas habilidades de pensamento crítico. Boa sorte!"
    )

    # Inicializa as variáveis de estado da sessão
    if "pontuacao" not in st.session_state:
        st.session_state.pontuacao = 0
    if "indice_pergunta" not in st.session_state:
        st.session_state.indice_pergunta = 0
    if "perguntas_selecionadas" not in st.session_state:
        # Seleciona aleatoriamente 5 perguntas da lista geral
        st.session_state.perguntas_selecionadas = random.sample(perguntas, k=min(5, len(perguntas)))

    if "quiz_concluido" not in st.session_state:
        st.session_state.quiz_concluido = False
    if "respondeu" not in st.session_state:
        st.session_state.respondeu = False  # Flag para saber se a resposta foi dada

    total_perguntas = len(st.session_state.perguntas_selecionadas)

    if not st.session_state.quiz_concluido:
        pergunta_atual = st.session_state.perguntas_selecionadas[st.session_state.indice_pergunta]

        # Barra de progresso
        progresso = (st.session_state.indice_pergunta + 1) / total_perguntas
        st.progress(progresso)
        st.markdown(f"**Progresso: {st.session_state.indice_pergunta + 1}/{total_perguntas}**")

        # Exibir pergunta
        st.markdown(f"### {pergunta_atual['pergunta']}")
        resposta = st.radio(
            "Escolha uma resposta:",
            pergunta_atual["alternativas"],
            key=f"pergunta_{st.session_state.indice_pergunta}",
        )

        col1, col2 = st.columns(2)

        # Coluna 1: Confirmar Resposta
        with col1:
            if st.button("Confirmar Resposta", key=f"confirmar_{st.session_state.indice_pergunta}"):
                st.session_state.respondeu = True  # Marca que o usuário respondeu
                if resposta == pergunta_atual["resposta"]:
                    st.success("✅ Resposta correta!")
                    st.session_state.pontuacao += 1
                else:
                    st.error(f"❌ Resposta incorreta! A resposta correta era: **{pergunta_atual['resposta']}**.")
                with st.expander("Ver explicação"):
                    st.write(pergunta_atual.get("explicacao", ""))

        # Coluna 2: Próxima Pergunta
        with col2:
            if st.session_state.respondeu:  # Só habilita o botão se a resposta foi dada
                if st.button("Próxima Pergunta", key=f"proxima_{st.session_state.indice_pergunta}"):
                    st.session_state.indice_pergunta += 1
                    st.session_state.respondeu = False
                    if st.session_state.indice_pergunta >= total_perguntas:
                        st.session_state.quiz_concluido = True

    else:
        st.balloons()
        st.markdown(
            f"## 🎉 Parabéns, você concluiu o quiz!\n"
            f"### 🏆 Sua pontuação final: **{st.session_state.pontuacao}/{total_perguntas}**"
        )

        # Botão "Reiniciar Quiz"
        if st.button("Reiniciar Quiz"):
            st.session_state.pontuacao = 0
            st.session_state.indice_pergunta = 0
            st.session_state.perguntas_selecionadas = random.sample(perguntas, k=min(5, len(perguntas)))
            st.session_state.quiz_concluido = False
            st.session_state.respondeu = False

    st.markdown(
        """
        <div class="creditos" style='font-size: 24px; text-align: center;'>
            Criado por: <span style='color: #e74c3c;'>Pedro Cardoso, Gabriel Francisco, Eduarda Reis, Carlos Augusto, Gustavo Freitas, Miguel Nantes - 3°A</span> 🧠
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    jogo_perguntas()
