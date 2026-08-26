// ============================================================
// CENA ATUAL E CHECKPOINT
// ============================================================

let cenaAtual = "inicio";

let checkpoint = "inicio";


// ============================================================
// PEGAR ELEMENTOS
// ============================================================

function el(id) {

    return document.getElementById(id);

}


// ============================================================
// IMAGEM
// ============================================================

function mostrarImagem(caminho) {

    el("imagem-cena").src = caminho;

}


// ============================================================
// AUDIO
// ============================================================

function trocarAudio(caminho) {

    const audio = el("audio-fundo");

    audio.src = caminho;

    audio.play().catch(() => {

        console.log(
            "O audio sera iniciado apos interacao do jogador."
        );

    });

}


// ============================================================
// CENAS DO JOGO
// ============================================================

const scenes = {


    // ========================================================
    // INICIO
    // ========================================================

    inicio: {

        titulo: "AS CRONICAS DE AETHERION",

        texto: `

Aetherion esta em perigo.

Mordrak, o Rei Sombrio, esta retornando.

Os quatro Cristais Elementais foram espalhados pelo continente.

Voce precisa recuperar:

Cristal da Terra
Cristal da Agua
Cristal do Fogo
Cristal do Ar

Sua jornada esta prestes a comecar.
`,

        imagem: "assets/imagens/inicio_aetherion.png",

        audio: "assets/audios/inicio.mp3",

        opcoes: [

            [
                "COMECAR AVENTURA",
                "nivel_1"
            ]

        ]

    },


    // ========================================================
    // NIVEL 1
    // ========================================================

    nivel_1: {

        titulo: "NIVEL 1 - FLORESTA DE ELDORIA",

        texto: `

Voce chega a uma vila proxima a Floresta de Eldoria.

Criaturas das sombras estao atacando os moradores.

O caminho para a floresta esta logo a frente.

O que voce fara?
`,

        imagem: "assets/imagens/nivel_1_floresta.png",

        audio: "assets/audios/floresta.mp3",

        checkpoint: true,

        opcoes: [

            [
                "AJUDAR OS MORADORES",
                "ajudar_moradores"
            ],

            [
                "ENTRAR NA FLORESTA",
                "nivel_2"
            ]

        ]

    },


    ajudar_moradores: {

        titulo: "A VILA ESTA SEGURA",

        texto: `

Voce derrota as criaturas e protege os moradores.

Eles agradecem sua ajuda.

Agora voce pode continuar sua jornada.
`,

        imagem: "assets/imagens/nivel_1_floresta.png",

        opcoes: [

            [
                "SEGUIR PARA O TEMPLO",
                "nivel_2"
            ]

        ]

    },


    // ========================================================
    // NIVEL 2
    // ========================================================

    nivel_2: {

        titulo: "NIVEL 2 - TEMPLO DA TERRA",

        texto: `

Voce entra no Templo da Terra.

Dois caminhos aparecem diante de voce.

Um caminho parece instavel.

O outro possui marcas antigas nas paredes.
`,

        imagem: "assets/imagens/templo_terra.png",

        audio: "assets/audios/templo.mp3",

        checkpoint: true,

        opcoes: [

            [
                "CAMINHO INSTAVEL",
                "game_over"
            ],

            [
                "SEGUIR AS MARCAS ANTIGAS",
                "cristal_terra"
            ]

        ]

    },


    cristal_terra: {

        titulo: "CRISTAL DA TERRA",

        texto: `

As marcas levam voce ate uma sala secreta.

No centro dela esta o Cristal da Terra.

Voce conquista o primeiro Cristal Elemental.
`,

        imagem: "assets/imagens/templo_terra.png",

        opcoes: [

            [
                "CONTINUAR",
                "nivel_3"
            ]

        ]

    },


    // ========================================================
    // NIVEL 3
    // ========================================================

    nivel_3: {

        titulo: "NIVEL 3 - FROSTPEAK",

        texto: `

As montanhas de Frostpeak estao cobertas por gelo.

Durante a subida, voce encontra Lyra cercada por monstros.
`,

        imagem: "assets/imagens/frostpeak.png",

        audio: "assets/audios/montanha.mp3",

        checkpoint: true,

        opcoes: [

            [
                "AJUDAR LYRA",
                "ajudar_lyra"
            ],

            [
                "CONTINUAR SOZINHO",
                "cristal_agua"
            ]

        ]

    },


    ajudar_lyra: {

        titulo: "UMA NOVA ALIADA",

        texto: `

Voce derrota os monstros.

Lyra agradece e acompanha voce.

Juntos, voces continuam a subida.
`,

        imagem: "assets/imagens/frostpeak.png",

        opcoes: [

            [
                "CONTINUAR A JORNADA",
                "cristal_agua"
            ]

        ]

    },


    cristal_agua: {

        titulo: "CRISTAL DA AGUA",

        texto: `

No topo da montanha voce encontra o segundo cristal.

O Cristal da Agua agora esta em suas maos.

Voce segue para o proximo templo.
`,

        imagem: "assets/imagens/frostpeak.png",

        opcoes: [

            [
                "SEGUIR PARA O VULCAO",
                "nivel_4"
            ]

        ]

    },


    // ========================================================
    // NIVEL 4
    // ========================================================

    nivel_4: {

        titulo: "NIVEL 4 - VULCAO INFERNIS",

        texto: `

O calor aumenta a cada passo.

Um enorme Guardiao de Fogo bloqueia seu caminho.

Voce precisa decidir como enfrenta-lo.
`,

        imagem: "assets/imagens/vulcao_infernis.png",

        audio: "assets/audios/vulcao.mp3",

        checkpoint: true,

        opcoes: [

            [
                "ATACAR DIRETAMENTE",
                "game_over"
            ],

            [
                "USAR OS PODERES DOS CRISTAIS",
                "cristal_fogo"
            ]

        ]

    },


    cristal_fogo: {

        titulo: "CRISTAL DO FOGO",

        texto: `

O Guardiao de Fogo e derrotado.

Voce encontra o terceiro Cristal Elemental.

O poder do fogo agora faz parte da sua jornada.
`,

        imagem: "assets/imagens/vulcao_infernis.png",

        opcoes: [

            [
                "CONTINUAR",
                "nivel_5"
            ]

        ]

    },


    // ========================================================
    // NIVEL 5
    // ========================================================

    nivel_5: {

        titulo: "NIVEL 5 - O TORNADO DOS VENTOS",

        texto: `

O Guardiao do Ar desafia voce para uma corrida.

O primeiro que chegar as nuvens vence.

Quando voce comeca a ganhar, ele lanca destrocos do tornado em sua direcao.

Voce precisa agir rapidamente.
`,

        imagem: "assets/imagens/tornado.png",

        audio: "assets/audios/tornado.mp3",

        checkpoint: true,

        opcoes: [

            [
                "CRIAR UM CAMINHO COM A TERRA",
                "vencer_tornado"
            ],

            [
                "CRIAR PLATAFORMAS DE GELO",
                "vencer_tornado"
            ],

            [
                "USAR O PODER DO FOGO PARA ACELERAR",
                "vencer_tornado"
            ],

            [
                "ATRAVESSAR OS DESTROCOS",
                "game_over"
            ]

        ]

    },


    vencer_tornado: {

        titulo: "VITORIA SOBRE O TORNADO",

        texto: `

Voce consegue evitar os destrocos.

Usando seus poderes, voce cria um caminho ate as nuvens.

O Guardiao reconhece sua vitoria.

Voce conquista o Cristal do Ar.

Agora os quatro Cristais Elementais foram reunidos.
`,

        imagem: "assets/imagens/tornado.png",

        opcoes: [

            [
                "SEGUIR PARA O CASTELO SOMBRIO",
                "nivel_6"
            ]

        ]

    },


    // ========================================================
    // NIVEL 6
    // ========================================================

    nivel_6: {

        titulo: "NIVEL 6 - CASTELO SOMBRIO",

        texto: `

Voce finalmente chega ao Castelo Sombrio.

Criaturas bloqueiam a entrada.

A fortaleza de Mordrak esta diante de voce.
`,

        imagem: "assets/imagens/castelo_sombrio.png",

        audio: "assets/audios/castelo.mp3",

        checkpoint: true,

        opcoes: [

            [
                "ENFRENTAR OS GUARDAS",
                "nivel_7"
            ],

            [
                "TENTAR ENTRAR SOZINHO",
                "game_over"
            ]

        ]

    },


    // ========================================================
    // NIVEL 7
    // ========================================================

    nivel_7: {

        titulo: "NIVEL 7 - MORDRAK",

        texto: `

No topo do Castelo Sombrio, Mordrak espera.

A batalha final comeca.

Mordrak lanca uma poderosa esfera de energia negra.
`,

        imagem: "assets/imagens/mordrak.png",

        audio: "assets/audios/batalha_final.mp3",

        checkpoint: true,

        opcoes: [

            [
                "DESVIAR E CONTRA ATACAR",
                "mordrak_fase_2"
            ],

            [
                "DEFENDER DIRETAMENTE",
                "game_over"
            ]

        ]

    },


    mordrak_fase_2: {

        titulo: "MORDRAK - FASE 2",

        texto: `

Mordrak cria uma poderosa tempestade negra.

Trovoes atingem o campo de batalha.
`,

        opcoes: [

            [
                "USAR O PODER DO AR",
                "mordrak_fase_3"
            ],

            [
                "CRIAR UM ESCUDO DE PEDRA",
                "game_over"
            ]

        ]

    },


    mordrak_fase_3: {

        titulo: "MORDRAK - ILUSOES",

        texto: `

Cinco copias de Mordrak aparecem.

Voce precisa descobrir como quebrar a ilusao.
`,

        opcoes: [

            [
                "ATACAR UM DOS CLONES",
                "game_over"
            ],

            [
                "UNIR OS QUATRO PODERES ELEMENTAIS",
                "mordrak_final"
            ]

        ]

    },


    mordrak_final: {

        titulo: "ECLIPSE FINAL",

        texto: `

Mordrak prepara seu ataque mais poderoso.

ECLIPSE FINAL!

Esta e sua ultima oportunidade.
`,

        opcoes: [

            [
                "TENTAR REBATER O ATAQUE",
                "game_over"
            ],

            [
                "UNIR OS QUATRO CRISTAIS",
                "arche_form"
            ]

        ]

    },


    arche_form: {

        titulo: "ARCHE FORM",

        texto: `

Os quatro Cristais Elementais comecam a brilhar.

Terra.
Agua.
Fogo.
Ar.

Os poderes se unem.

Uma nova energia desperta.

ARCHE FORM!

Mordrak finalmente e derrotado.
`,

        imagem: "assets/imagens/arche_form.png",

        opcoes: [

            [
                "RESTAURAR A PAZ",
                "vitoria"
            ]

        ]

    },


    vitoria: {

        titulo: "AETHERION ESTA EM PAZ",

        texto: `

Mordrak foi derrotado.

Os monstros desapareceram.

As vilas foram reconstruidas.

A paz voltou para Aetherion.

Voce se tornou uma lenda.

FIM.
`,

        imagem: "assets/imagens/aetherion_paz.png",

        opcoes: [

            [
                "JOGAR NOVAMENTE",
                "reiniciar"
            ]

        ]

    },


    game_over: {

        titulo: "GAME OVER",

        texto: `

Voce foi derrotado.

Mas sua jornada ainda nao terminou.

Voce pode voltar ao ultimo checkpoint.
`,

        opcoes: [

            [
                "VOLTAR AO CHECKPOINT",
                "voltar_checkpoint"
            ],

            [
                "REINICIAR O JOGO",
                "reiniciar"
            ]

        ]

    }

};


// ============================================================
// MOSTRAR CENA
// ============================================================

function mostrarCena(nome) {

    cenaAtual = nome;

    const cena = scenes[nome];


    // ATUALIZAR CHECKPOINT

    if (cena.checkpoint === true) {

        checkpoint = nome;

    }


    // TITULO

    el("titulo-cena").innerText =
        cena.titulo;


    // TEXTO

    el("texto-cena").innerText =
        cena.texto;


    // IMAGEM

    if (cena.imagem) {

        mostrarImagem(
            cena.imagem
        );

    }


    // AUDIO

    if (cena.audio) {

        trocarAudio(
            cena.audio
        );

    }


    // OPCOES

    atualizarBotoes(
        cena.opcoes
    );

}


// ============================================================
// ATUALIZAR BOTOES
// ============================================================

function atualizarBotoes(opcoes) {

    for (let numero = 1; numero <= 4; numero++) {

        const botao =
            el("opcao" + numero);

        const indice =
            numero - 1;


        if (indice < opcoes.length) {

            botao.innerText =
                opcoes[indice][0];

            botao.style.display =
                "block";

        }

        else {

            botao.style.display =
                "none";

        }

    }

}


// ============================================================
// ESCOLHER OPCAO
// ============================================================

function escolherOpcao(numero) {

    const cena =
        scenes[cenaAtual];


    const indice =
        numero - 1;


    if (indice < cena.opcoes.length) {

        const acao =
            cena.opcoes[indice][1];


        executarAcao(
            acao
        );

    }

}


// ============================================================
// EXECUTAR ACAO
// ============================================================

function executarAcao(acao) {


    // VOLTAR AO CHECKPOINT

    if (acao === "voltar_checkpoint") {

        mostrarCena(
            checkpoint
        );

    }


    // REINICIAR

    else if (acao === "reiniciar") {

        checkpoint = "inicio";

        mostrarCena(
            "inicio"
        );

    }


    // IR PARA OUTRA CENA

    else if (scenes[acao]) {

        mostrarCena(
            acao
        );

    }

}


// ============================================================
// EVENTOS DOS BOTOES
// ============================================================

el("opcao1").addEventListener(
    "click",
    function () {

        escolherOpcao(1);

    }
);


el("opcao2").addEventListener(
    "click",
    function () {

        escolherOpcao(2);

    }
);


el("opcao3").addEventListener(
    "click",
    function () {

        escolherOpcao(3);

    }
);


el("opcao4").addEventListener(
    "click",
    function () {

        escolherOpcao(4);

    }
);


// BOTAO CHECKPOINT

el("checkpoint").addEventListener(
    "click",
    function () {

        mostrarCena(
            checkpoint
        );

    }
);


// BOTAO REINICIAR

el("reiniciar").addEventListener(
    "click",
    function () {

        checkpoint = "inicio";

        mostrarCena(
            "inicio"
        );

    }
);


// ============================================================
// INICIAR JOGO
// ============================================================

mostrarCena(
    "inicio"
);