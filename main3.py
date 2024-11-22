import random
import pandas as pd
import streamlit as st

# --- Estilo ---
st.set_page_config(page_title="Simulador LBFF", page_icon="🔥", layout="wide")
st.markdown(
    """
    <style>
    .header {
        color: #ff6600;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .subheader {
        font-size: 25px;
        font-weight: bold;
        color: #0066cc;
        text-align: center;
    }
    .card {
        background-color: #f4f4f4;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 30px;
    }
    .table {
        margin-top: 20px;
        overflow-x: auto;
        overflow-y: auto;
    }
    .highlight {
        background-color: #ffcc00; /* Cor amarela para os 12 primeiros */
        color: black; /* Texto em preto para melhor contraste */
    }
    .top-12 {
        background-color: #4CAF50; /* Verde suave */
        color: white; /* Texto branco para bom contraste */
    }
    </style>
    """, unsafe_allow_html=True
)

# --- Times participantes ---
teams = [
    "LOUD", "FLAMENGO", "SCCP", "LOS GRANDES", "JACOBINA",
    "INCO GAMING", "JUVE", "TECTOY CRIPZ", "MINERS", "PAIN GAMING",
    "FLUXO", "E1", "TEAM SOLID", "MIBR", "ANTISSOCIAL",
    "INFLUENCE RAGE", "ALFA34", "MAGIC SQUAD"
]

# --- Divisão em grupos ---
groups = {
    "A": teams[:6],
    "B": teams[6:12],
    "C": teams[12:]
}

# --- Pontuação por colocação ---
placement_points = {
    1: 12, 2: 9, 3: 8, 4: 7, 5: 6,
    6: 5, 7: 4, 8: 3, 9: 2, 10: 1,
    11: 0, 12: 0
}


# --- Funções ---
def calculate_points(placement, kills):
    """Calcula os pontos (colocação + kills)."""
    return placement_points.get(placement, 0) + kills


def generate_kills(total_kills):
    """Distribui os kills entre as equipes de forma variável (total de kills por rodada entre 45 e 55)."""
    kills = []
    remaining_kills = total_kills
    for i in range(12):  # 12 equipes
        kills_for_team = random.randint(2, 6)  # Cada time pode pegar entre 2 e 6 kills
        remaining_kills -= kills_for_team
        kills.append(kills_for_team)

    # Caso reste algum kill, distribui para os times com maior colocação
    for i in range(remaining_kills):
        kills[i % 12] += 1

    return kills


# --- Estado do campeonato ---
if "current_day" not in st.session_state:
    st.session_state.current_day = 1
if "day_results" not in st.session_state:
    st.session_state.day_results = []  # Para armazenar os resultados de cada dia
if "team_points" not in st.session_state:
    st.session_state.team_points = {team: 0 for team in teams}  # Armazenar pontos totais de cada equipe
if "team_kills" not in st.session_state:
    st.session_state.team_kills = {team: 0 for team in teams}  # Armazenar kills totais de cada equipe
if "team_booyahs" not in st.session_state:
    st.session_state.team_booyahs = {team: 0 for team in teams}  # Contagem de booyahs
if "team_rounds" not in st.session_state:
    st.session_state.team_rounds = {team: 0 for team in teams}  # Contagem de rodadas disputadas
if "team_group" not in st.session_state:
    # Armazenar o grupo de cada equipe
    st.session_state.team_group = {team: group for group, teams_list in groups.items() for team in teams_list}

if "teams_played_today" not in st.session_state:
    st.session_state.teams_played_today = set()  # Para garantir que as equipes joguem o mesmo número de partidas

if "group_combinations" not in st.session_state:
    # Lista de combinações possíveis de grupos
    st.session_state.group_combinations = [("A", "B"), ("A", "C"), ("B", "C")]


# --- Função para simular o dia ---
def simulate_day():
    """Simula o dia de campeonato com 6 rodadas e exibe quais grupos se enfrentam."""
    # Garantir que os confrontos de grupos não se repitam até que todas as possibilidades tenham sido utilizadas
    if st.session_state.group_combinations:
        selected_groups = st.session_state.group_combinations.pop(0)  # Remove o primeiro confronto da lista
    else:
        # Se todos os confrontos foram usados, recomeçamos a lista
        st.session_state.group_combinations = [("A", "B"), ("A", "C"), ("B", "C")]
        selected_groups = st.session_state.group_combinations.pop(0)

    group_1, group_2 = selected_groups
    playing_teams = groups[group_1] + groups[group_2]

    # Garantir que nenhuma equipe jogue mais de uma vez
    if len(st.session_state.teams_played_today) >= len(teams):
        st.session_state.teams_played_today.clear()  # Resetar o set quando todas as equipes jogarem

    # Exibir os grupos que estão se enfrentando neste dia
    st.markdown(f"**Grupos se enfrentando no Dia {st.session_state.current_day}:**")
    st.markdown(f"Grupo {group_1} vs Grupo {group_2}")

    round_results = []
    for round_num in range(1, 7):  # 6 rodadas por dia
        shuffled_teams = random.sample(playing_teams, len(playing_teams))
        placements = [i % 12 + 1 for i in range(len(playing_teams))]  # Colocações de 1 a 12

        # Gerar o total de kills para a rodada (entre 45 e 55)
        total_kills = random.randint(45, 55)

        # Distribuir kills pelas equipes
        kills = generate_kills(total_kills)

        round_result = []
        for i, team in enumerate(shuffled_teams):
            placement = placements[i]
            team_kills = kills[i]
            points = calculate_points(placement, team_kills)
            is_booyah = 1 if placement == 1 else 0  # Se for 1º lugar, marca Booyah
            round_result.append({
                "Rodada": round_num, "Equipe": team, "Colocação": placement,
                "Abates": team_kills, "Pontos": points, "Booyah": is_booyah,
                "Posição Final": f"{placement}º"
            })

            # Atualizar dados do time
            st.session_state.team_points[team] += points
            st.session_state.team_kills[team] += team_kills
            st.session_state.team_booyahs[team] += is_booyah
            st.session_state.team_rounds[team] += 1
            st.session_state.teams_played_today.add(team)

        # Salvar resultados por rodada
        st.session_state.day_results.append(pd.DataFrame(round_result))

    st.session_state.current_day += 1


# --- Botão para avançar para o próximo dia ---
if st.session_state.current_day <= 36:
    if st.button("Avançar para o próximo dia", key="next_day"):
        simulate_day()

# --- Exibir resultados do dia atual ---
if st.session_state.day_results:
    st.markdown('<div class="subheader">Resultados do Dia {}</div>'.format(st.session_state.current_day - 1),
                unsafe_allow_html=True)
    for i, round_results in enumerate(st.session_state.day_results[-6:], 1):
        st.markdown(f"**Rodada {i}:**")
        st.dataframe(round_results)

# --- Exibir Tabela Geral ---
general_table = pd.DataFrame({
    "Equipe": teams,
    "Pontos": list(st.session_state.team_points.values()),
    "Kills": list(st.session_state.team_kills.values()),
    "Booyahs": list(st.session_state.team_booyahs.values()),
    "Rodadas": list(st.session_state.team_rounds.values()),
    "Grupo": [st.session_state.team_group[team] for team in teams]
})

general_table = general_table.sort_values(by=["Pontos"], ascending=False).reset_index(drop=True)

# Exibir a Tabela Geral com destaque para o Top 12
st.markdown("<div class='header'>Tabela Geral</div>", unsafe_allow_html=True)
st.dataframe(general_table)
