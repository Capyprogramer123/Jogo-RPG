import streamlit as st
from pathlib import Path


# =========================================================
# CONFIGURACAO DA PAGINA
# =========================================================

st.set_page_config(
    page_title="As Cronicas de Aetherion",
    page_icon="A",
    layout="centered"
)


# =========================================================
# PASTAS DO PROJETO
# =========================================================

BASE = Path(__file__).parent

PASTA_IMAGENS = BASE / "assets" / "imagens"
PASTA_AUDIOS = BASE / "assets" / "audios"


# =========================================================
# FUNCOES AUXILIARES
# =========================================================

def mostrar_imagem(nome):

    caminho = PASTA_IMAGENS / nome

    if caminho.exists():
        st.image(str(caminho), use_container_width=True)

    else:
        st.warning(f"Imagem nao encontrada: {nome}")


def tocar_musica(nome):

    caminho = PASTA_AUDIOS / nome

    if caminho.exists():

        with open(caminho, "rb") as audio:
            st.audio(audio.read())

    else:
        st.info(f"Audio nao encontrado: {nome}")


def mudar_cena(nova_cena):

    st.session_state.cena = nova_cena
    st.rerun()


def game_over():

    mudar_cena("game_over")


def reiniciar_jogo():

    st.session_state.clear()
    st.rerun()


# =========================================================
# INICIALIZACAO DAS VARIAVEIS
# =========================================================

if "cena" not in st.session_state:
    st.session_state.cena = "inicio"


if "checkpoint" not in st.session_state:
    st.session_state.checkpoint = "nivel_1"


if "ajuda_moradores" not in st.session_state:
    st.session_state.ajuda_moradores = False


if "lyra_aliada" not in st.session_state:
    st.session_state.lyra_aliada = False


# CRISTAIS

if "cristal_terra" not in st.session_state:
    st.session_state.cristal_terra = False


if "cristal_agua" not in st.session_state:
    st.session_state.cristal_agua = False


if "cristal_fogo" not in st.session_state:
    st.session_state.cristal_fogo = False


if "cristal_ar" not in st.session_state:
    st.session_state.cristal_ar = False


# =========================================================
# BARRA DE STATUS
# =========================================================

def mostrar_status():

    st.sidebar.title("Status do Heroi")

    st.sidebar.subheader("Cristais")

    if st.session_state.cristal_terra:
        st.sidebar.write("Terra: SIM")
    else:
        st.sidebar.write("Terra: NAO")

    if st.session_state.cristal_agua:
        st.sidebar.write("Agua: SIM")
    else:
        st.sidebar.write("Agua: NAO")

    if st.session_state.cristal_fogo:
        st.sidebar.write("Fogo: SIM")
    else:
        st.sidebar.write("Fogo: NAO")

    if st.session_state.cristal_ar:
        st.sidebar.write("Ar: SIM")
    else:
        st.sidebar.write("Ar: NAO")

    st.sidebar.divider()

    st.sidebar.subheader("Aliados")

    if st.session_state.ajuda_moradores:
        st.sidebar.write("Moradores: Aliados")

    if st.session_state.lyra_aliada:
        st.sidebar.write("Lyra: Aliada")

    if (
        not st.session_state.ajuda_moradores
        and not st.session_state.lyra_aliada
    ):
        st.sidebar.write("Voce ainda nao possui aliados.")


mostrar_status()


# =========================================================
# TELA INICIAL
# =========================================================

if st.session_state.cena == "inicio":

    mostrar_imagem("Tela inicial")

    st.title("AS CRONICAS DE AETHERION")

    st.subheader("A Queda do Rei Sombrio")

    st.write("""
    Ha milhares de anos, quatro Cristais Elementais protegiam
    o continente de Aetherion.

    Terra
    Agua
    Fogo
    Ar

    Agora, o poderoso Rei Sombrio Mordrak esta retornando.

    Sua missao e recuperar os quatro Cristais Elementais,
    atravessar os sete niveis e impedir que Mordrak conquiste
    Aetherion.
    """)

    tocar_musica("01_A_Jornada_Comeca.mid")

    if st.button("COMECAR AVENTURA"):

        mudar_cena("nivel_1")


# =========================================================
# NIVEL 1
# =========================================================

elif st.session_state.cena == "nivel_1":

    st.session_state.checkpoint = "nivel_1"

    st.title("NIVEL 1 - FLORESTA DE ELDORIA")

    mostrar_imagem("Cena 1")

    tocar_musica("02_Floresta_de_Eldoria.mid")

    st.write("""
    Voce chega a uma pequena vila proxima a Floresta de Eldoria.

    Criaturas das sombras estao atacando os moradores.

    Ao fundo, a floresta guarda o caminho para o primeiro templo.
    """)

    escolha = st.radio(
        "O que voce fara?",
        [
            "Ajudar os moradores",
            "Entrar diretamente na floresta"
        ]
    )

    if st.button("Confirmar escolha"):

        if escolha == "Ajudar os moradores":

            st.session_state.ajuda_moradores = True

            st.success("""
            Voce derrota as criaturas e protege a vila.

            Os moradores prometem ajuda-lo quando precisar.
            """)

        else:

            st.info("""
            Voce decide seguir diretamente para a floresta.

            Voce economiza tempo, mas deixa os moradores para tras.
            """)

        mudar_cena("nivel_2")


# =========================================================
# NIVEL 2 - TEMPLO DA TERRA
# =========================================================

elif st.session_state.cena == "nivel_2":

    st.session_state.checkpoint = "nivel_2"

    st.title("NIVEL 2 - TEMPLO DA TERRA")

    mostrar_imagem("ChatGPT Imagem 20 de ago. de 2026, 18_09_05.png")

    tocar_musica("03_Templo_da_Terra.mid")

    st.write("""
    Voce entra em uma enorme sala construida em pedra.

    Dois caminhos aparecem diante de voce.
    """)

    escolha = st.radio(
        "Qual caminho voce escolhe?",
        [
            "Caminho da Esquerda",
            "Caminho da Direita"
        ]
    )

    if st.button("Avancar pelo templo"):

        if escolha == "Caminho da Esquerda":

            mudar_cena("game_over")

        else:

            st.session_state.cristal_terra = True

            mostrar_imagem("Cena 2")

            st.success("""
            Voce enfrenta as criaturas de pedra e encontra
            o primeiro Cristal Elemental!

            CRISTAL DA TERRA CONQUISTADO!
            """)

            mudar_cena("nivel_3")


# =========================================================
# NIVEL 3 - FROSTPEAK
# =========================================================

elif st.session_state.cena == "nivel_3":

    st.session_state.checkpoint = "nivel_3"

    st.title("NIVEL 3 - MONTANHAS DE FROSTPEAK")

    mostrar_imagem("Cena 3")

    tocar_musica("04_Montanhas_de_Frostpeak.mid")

    st.write("""
    As Montanhas de Frostpeak sao cobertas por gelo e neve.

    Durante a subida, voce encontra uma jovem arqueira
    chamada Lyra cercada por monstros.
    """)

    escolha = st.radio(
        "O que voce fara?",
        [
            "Ajudar Lyra",
            "Continuar sozinho"
        ]
    )

    if st.button("Continuar"):

        if escolha == "Ajudar Lyra":

            st.session_state.lyra_aliada = True

            st.success("""
            Voce derrota os monstros.

            Lyra agradece e decide acompanha-lo.
            """)

        else:

            st.info("""
            Voce continua sozinho pelas montanhas.
            """)

        st.session_state.cristal_agua = True

        st.success("CRISTAL DA AGUA CONQUISTADO!")

        mudar_cena("nivel_4")


# =========================================================
# NIVEL 4 - VULCAO INFERNIS
# =========================================================

elif st.session_state.cena == "nivel_4":

    st.session_state.checkpoint = "nivel_4"

    st.title("NIVEL 4 - VULCAO INFERNIS")

    mostrar_imagem("Cena 4")

    tocar_musica("05_Vulcao_Infernis.mid")

    st.write("""
    Voce chega ao Vulcao Infernis.

    Um enorme Guardiao de Fogo bloqueia seu caminho.
    """)

    escolha = st.radio(
        "Como voce enfrenta o Guardiao?",
        [
            "Atacar diretamente",
            "Usar os Cristais Elementais"
        ]
    )

    if st.button("Iniciar batalha"):

        if escolha == "Atacar diretamente":

            mudar_cena("game_over")

        else:

            st.session_state.cristal_fogo = True

            st.success("""
            Voce combina os poderes da Terra e da Agua.

            O Guardiao e derrotado!

            CRISTAL DO FOGO CONQUISTADO!
            """)

            mudar_cena("nivel_5")


# =========================================================
# NIVEL 5 - CORRIDA DO TORNADO
# =========================================================

elif st.session_state.cena == "nivel_5":

    st.session_state.checkpoint = "nivel_5"

    st.title("NIVEL 5 - O TORNADO DOS VENTOS")

    mostrar_imagem("Cena 5")

    tocar_musica("06_Tornado_dos_Ventos.mid")

    st.write("""
    Um enorme tornado aparece diante de voce.

    No centro dele esta o Guardiao do Ar.

    Ele desafia voce para uma corrida.

    Quem chegar primeiro as nuvens vence.
    """)

    escolha = st.radio(
        "Qual sera sua decisao?",
        [
            "Aceitar a corrida",
            "Recusar e atacar o Guardiao"
        ]
    )

    if st.button("Fazer escolha"):

        if escolha == "Recusar e atacar o Guardiao":

            mudar_cena("game_over")

        else:

            mudar_cena("tornado_destrocos")


# =========================================================
# NIVEL 5 - DESTROCOS DO TORNADO
# =========================================================

elif st.session_state.cena == "tornado_destrocos":

    st.title("CORRIDA - DESTROCOS")

    st.write("""
    Voce comeca a ultrapassar o Guardiao.

    Percebendo que esta perdendo, ele lanca destrocos
    do tornado em sua direcao!

    Voce precisa agir rapidamente.
    """)

    escolha = st.radio(
        "Como voce evita os destrocos?",
        [
            "Criar caminhos com a Terra",
            "Criar plataformas de gelo",
            "Usar o superaquecimento para aumentar sua velocidade"
        ]
    )

    if st.button("Usar poder"):

        if escolha == "Usar o superaquecimento para aumentar sua velocidade":

            st.session_state.cristal_ar = True

            st.success("""
            Voce usa o poder do Cristal do Fogo para
            aumentar drasticamente sua velocidade.

            Voce atravessa os destrocos e alcanca as nuvens!

            CRISTAL DO AR CONQUISTADO!
            """)

            mudar_cena("nivel_6")

        else:

            mudar_cena("game_over")


# =========================================================
# NIVEL 6 - CASTELO SOMBRIO
# =========================================================

elif st.session_state.cena == "nivel_6":

    st.session_state.checkpoint = "nivel_6"

    st.title("NIVEL 6 - CASTELO SOMBRIO")

    mostrar_imagem("Cena 6")

    tocar_musica("07_Castelo_Sombrio.mid")

    st.write("""
    Voce finalmente chega ao Castelo Sombrio de Mordrak.

    Um exercito de criaturas protege a entrada.
    """)

    if (
        st.session_state.ajuda_moradores
        or st.session_state.lyra_aliada
    ):

        escolha = st.radio(
            "Voce possui aliados. O que fara?",
            [
                "Enfrentar os guardas",
                "Pedir ajuda aos aliados"
            ]
        )

        if st.button("Entrar no castelo"):

            if escolha == "Pedir ajuda aos aliados":

                st.success("""
                Seus aliados distraem os guardas.

                Voce consegue entrar no Castelo Sombrio!
                """)

            else:

                st.info("""
                Voce usa seus quatro poderes para derrotar
                os guardas.
                """)

            mudar_cena("nivel_7")

    else:

        st.warning("""
        Voce esta sozinho.

        Nao ha ninguem para ajuda-lo.
        """)

        if st.button("Enfrentar os guardas"):

            mudar_cena("nivel_7")


# =========================================================
# NIVEL 7 - MORDRAK
# =========================================================

elif st.session_state.cena == "nivel_7":

    st.session_state.checkpoint = "nivel_7"

    st.title("NIVEL 7 - MORDRAK, O REI SOMBRIO")

    mostrar_imagem("Cena 7 parte 1")

    tocar_musica("08_Mordrak_Rei_Sombrio.mid")

    st.write("""
    No topo do Castelo Sombrio, Mordrak espera por voce.

    A batalha final comeca!

    Ele lanca uma poderosa bola de fogo negra.
    """)

    escolha = st.radio(
        "O que voce faz?",
        [
            "Defender-se",
            "Desviar e contra-atacar"
        ]
    )

    if st.button("Agir"):

        if escolha == "Defender-se":

            mudar_cena("game_over")

        else:

            mudar_cena("mordrak_fase_2")


# =========================================================
# MORDRAK - FASE 2
# =========================================================

elif st.session_state.cena == "mordrak_fase_2":

    st.title("MORDRAK - TORMENTA NEGRA")

    st.write("""
    Mordrak cria nuvens carregadas de energia.

    Trovoes negros comecam a cair sobre voce!
    """)

    mostrar_imagem("Cena 7 parte 2")

    escolha = st.radio(
        "Como voce reage?",
        [
            "Rebater as nuvens usando o poder do Ar",
            "Criar um escudo de pedra"
        ]
    )

    if st.button("Continuar batalha"):

        if escolha == "Rebater as nuvens usando o poder do Ar":

            mudar_cena("mordrak_fase_3")

        else:

            mudar_cena("game_over")


# =========================================================
# MORDRAK - FASE 3
# =========================================================

elif st.session_state.cena == "mordrak_fase_3":

    st.title("MORDRAK - A ILUSAO")

    st.write("""
    Mordrak abre um portal sombrio.

    Cinco versoes dele aparecem ao seu redor.
    """)

    mostrar_imagem("Cena 7 parte 3")

    escolha = st.radio(
        "Como voce enfrenta os clones?",
        [
            "Atacar um dos clones",
            "Usar os quatro poderes elementais"
        ]
    )

    if st.button("Quebrar a ilusao"):

        if escolha == "Usar os quatro poderes elementais":

            mudar_cena("mordrak_final")

        else:

            mudar_cena("game_over")


# =========================================================
# MORDRAK - BATALHA FINAL
# =========================================================

elif st.session_state.cena == "mordrak_final":

    st.title("ECLIPSE FINAL")

    st.write("""
    Mordrak assume sua forma mais poderosa.

    Ele prepara seu ataque final:

    ECLIPSE FINAL!
    """)

    mostrar_imagem("Cena 7 parte final")

    escolha = st.radio(
        "Qual sera seu ultimo movimento?",
        [
            "Tentar rebater o ataque",
            "Unir os quatro Cristais Elementais"
        ]
    )

    if st.button("ATAQUE FINAL"):

        todos_cristais = (
            st.session_state.cristal_terra
            and st.session_state.cristal_agua
            and st.session_state.cristal_fogo
            and st.session_state.cristal_ar
        )

        if (
            escolha == "Unir os quatro Cristais Elementais"
            and todos_cristais
        ):

            mudar_cena("arche_form")

        else:

            mudar_cena("game_over")


# =========================================================
# ARCHE FORM
# =========================================================

elif st.session_state.cena == "arche_form":

    st.title("ARCHE FORM")

    mostrar_imagem("mordrak_derrotado.png")

    mostrar_imagem("Arché form vencendo o Mordrak")

    tocar_musica("09_Arche_Form.mid")

    st.write("""
    Os quatro Cristais Elementais comecam a brilhar.

    Terra
    Agua
    Fogo
    Ar

    Os poderes se unem.

    Uma energia completamente nova desperta dentro de voce.

    ARCHE FORM!
    """)

    if st.button("DERROTAR MORDRAK"):

        mudar_cena("vitoria")


# =========================================================
# VITORIA
# =========================================================

elif st.session_state.cena == "vitoria":

    st.title("AETHERION ESTA EM PAZ")

    mostrar_imagem("Restaurando a paz")

    tocar_musica("10_Aetherion_em_Paz.mid")

    st.write("""
    Mordrak foi derrotado.

    O poder das sombras desaparece.

    Os quatro Cristais Elementais restauram o equilibrio
    de Aetherion.

    As criaturas desaparecem.

    As vilas sao reconstruidas.

    A paz retorna ao continente.

    Voce se torna o novo Guardiao dos Quatro Cristais.

    Sua historia sera lembrada por muitas geracoes.

    FIM
    """)

    if st.button("JOGAR NOVAMENTE"):

        reiniciar_jogo()


# =========================================================
# GAME OVER
# =========================================================

elif st.session_state.cena == "game_over":

    st.title("GAME OVER")

    st.error("""
    Sua jornada terminou... por enquanto.
    """)

    st.write(
        f"Seu ultimo checkpoint foi: "
        f"{st.session_state.checkpoint}"
    )

    coluna_1, coluna_2 = st.columns(2)

    with coluna_1:

        if st.button("VOLTAR AO CHECKPOINT"):

            mudar_cena(
                st.session_state.checkpoint
            )

    with coluna_2:

        if st.button("REINICIAR O JOGO"):

            reiniciar_jogo()