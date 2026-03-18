import discord
from discord.ext import commands
import requests
import random

ARMAS = ["Acha",
"Arco",
"Arco Composto",
"Baioneta",
"Balestra",
"Bastão",
"Bastão Policial",
"Bazuca",
"Besta",
"Cajado",
"Corrente",
"Espada",
"Espingarda",
"Espingarda de Cano Duplo",
"Estilinguw",
"Faca",
"Florete",
"Fuzil de Assalto",
"Fuzil de Caça",
"Fuzil de Precisão",
"Gadanho",
"Gancho de Carne",
"Katana",
"Lança",
"Lança-Chamas",
"Maça",
"Machadinha",
"Machado",
"Machete",
"Marreta",
"Martelo",
"Metralhadora",
"Montante",
"Motosserra",
"Nunchaku",
"Picareta",
"Pistola",
"Pistola Pesada",
"Pregador Pneumático",
"Punhal",
"Revólver",
"Revólver Compacto",
"Shuriken",
"Submetralhadora"]

ITENS = ["A Antena",
"A Primeira Adaga",
"Agrupador Ritualístico",
"Amarras de (Elemento)",
"Amarras Mortais",
"Ampulheta do Tempo Sofrido",
"Amuleto Sinalizador de (Elemento)",
"Anéis de Elo Mental",
"Arcabuz dos Moretti",
"Arpão do Pescador",
"Arreio Neural",
"Bateria Reversa",
"Câmera de Aura Paranormal",
"Câmera Obscura",
"Casaco de Lodo",
"Catalisador Ritualístico",
"Centrifugador Existencial",
"Colar Banhado em Sangue",
"Coletora",
"Combustível de Sangue",
"Componentes Ritualísticos de Conhecimento",
"Componentes Ritualísticos de Energia",
"Componentes Ritualísticos de Morte",
"Componentes Ritualísticos de Sangue",
"Conector de Membros",
"Coração Pulsante",
"Coroa de Espinhos",
"Crânio Espiral",
"Dedo Decepado",
"Dose D'A Praga",
"Elmo do Colosso",
"Emissor de Pulsos Paranormais",
"Enxame Fantasmagórico",
"Escuta de Ruídos Paranormais",
"Espelho Refletor",
"Faca Predadora",
"Faixas da Vidência",
"Frasco de Lodo",
"Frasco de Vitalidade",
"Fuzil Alheio",
"Injeção de Lodo",
"Instantâneo Mortal",
"Jaqueta de Veríssimo",
"Lanterna Reveladora",
"Ligação Direta Infernal",
"Machado do Mutilador",
"Mandíbula Agonizante",
"Manoplas do Colosso",
"Marreta Transtornada",
"Máscara das Pessoas nas Sombras",
"Medidor de Condição Vertebral",
"Munição Jurada",
"Óculos que Viram Mortes Demais",
"Pé de Morto",
"Peitoral da Segunda Chance",
"Pen Drive Selado",
"Pergaminho da Pertinácia",
"Pérola de Sangue",
"Pingente da Lua Dourada",
"Projétil de Lodo",
"Punhal X",
"Punhos Enraivecidos",
"Rádio Chiador",
"Relógio do Arnaldo",
"Repositório do Fracasso",
"Retalho Tenebroso",
"Rubra",
"Scanner de Manifestação Paranormal de (Elemento)",
"Selos Paranormais",
"Seringa de Transfiguração",
"Sniper Fantasma",
"Tábula do Saber Custoso",
"Taco de Baseball Energizado",
"Talismã da Sorte",
"Teclado de Conexão Neural",
"Tela do Pesadelo",
"Valete da Salvação",
"Veículo Energizado",
"Vislumbre do Fim",
]

TRILHAS_COMBATENTE = ["Agente Secreto",
"Aniquilador",
"Caçador",
"Comandante de Campo",
"Guerreiro",
"Monstruoso",
"Operações Especiais",
"Tropa de Choque"
]

TRILHAS_OCULTISTA = ["Conduíte",
"Exorcista",
"Flagelador",
"Graduado",
"Intuitivo",
"Lâmina Paranormal",
"Maledictólogo",
"Possuído",
"Parapsicólogo",
]

TRILHAS_ESPECIALISTA = ["Atirador de Elite",
"Bibliotecário",
"Infiltrador",
"Médico de Campo",
"Muambeiro",
"Negociador",
"Perseverante",
"Técnico",
]

TRILHA_MUNDANO = ['Durão', 'Esperto', 'Exotérico']

ORIGENS = ["Acadêmico",
"Agente de Saúde",
"Amigo dos Animais",
"Amnésico",
"Artista",
"Astronauta",
"Atleta",
"Blaster",
"Body Builder",
"Chef",
"Chef do Outro Lado",
"Cientista Forense",
"Colegial",
"Cosplayer",
"Criminoso",
"Cultista Arrependido",
"Desgarrado",
"Diplomata",
"Dublê",
"Engenheiro",
"Escritor",
"Executivo",
"Experimento",
"Explorador",
"Fanático por Criaturas",
"Ferido por Ritual",
"Fotógrafo",
"Gaudério Abutre",
"Ginasta",
"Inventor Paranormal",
"Investigador",
"Jornalista",
"Jovem Místico",
"Legista do Turno da Noite",
"Lutador",
"Magnata",
"Mateiro",
"Mercenário",
"Mergulhador",
"Militar",
"Motorista",
"Nerd Entusiasta",
"Operário",
"Personal Trainer",
"Policial",
"Professor",
"Profetizado",
"Psicólogo",
"Religioso",
"Repórter Investigativo",
"Revoltado",
"Servidor Público",
"T.I.",
"Teórico da Conspiração",
"Trabalhador Rural",
"Trambiqueiro",
"Transtornado Arrependido",
"Universitário",
"Vítima"
]

CLASSES = ['Ocultista', 'Combatente', 'Especialista', 'Mundano']

PODER_OCULTISTA = ["Camuflar Ocultismo",
"Criar Selo",
"Deixe os Sussurros Guiarem",
"Dominar Habilidade Ritualística",
"Domínio Esotérico",
"Envolto do Mistério",
"Especialista em Elemento",
"Estalos Macabros",
"Ferramentas Paranormais",
"Fluxo de Poder",
"Guiado pelo Paranormal",
"Identificação Paranormal",
"Improvisar Componentes",
"Intuição Paranormal",
"Liturgia de Fortalecimento Ritualístico",
"Mestre em Elemento",
"Minha Dor me Impulsiona",
"Nos Olhos do Monstro",
"Olhar Sinistro",
"Reter Ritual de Combate",
"Ritual Intenso",
"Ritual Potente",
"Ritual Predileto",
"Saúde Sobrenatural",
"Sentido Premonitório",
"Sincronia Paranormal",
"Tatuagem Ritualística",
"Traçado Conjuratório"
]

PODER_COMBATENTE = ["Apego Angustiado",
"Armamento Pesado",
"Ataque de Oportunidade",
"Caminho para Força",
"Ciente das Cicatrizes",
"Combate Defensivo",
"Correria Desesperada",
"Engolir o Choro",
"Golpe Demolidor",
"Golpe Pesado",
"Golpes de Arena",
"Incansável",
"Instintos de Fuga",
"Marteladas",
"Mochileiro",
"Paranoia Defensiva",
"Predador Perfeito",
"Presteza Atlética",
"Proteção Pesada",
"Reflexos Defensivos",
"Sacrificar os Joelhos",
"Segurar o Gatilho",
"Sem Tempo, Irmão",
"Tanque de Guerra",
"Tiro Certeiro",
"Tiro de Cobertura",
"Valentão"
]

PODER_ESPECIALISTA = ["Acolher o Terror",
"Assassinato Furtivo",
"Balística Avançada",
"Conhecimento Aplicado",
"Contatos Oportunos",
"Disfarce Sutil",
"Esconderijo Desesperado",
"Especialista Diletante",
"Especialista em Matar",
"Flashback",
"Hacker",
"Leitura Fria",
"Mãos Firmes",
"Mãos Rápidas",
"Mochila de Utilidades",
"Movimento Tático",
"Na Trilha Certa",
"Nerd",
"Ninja Urbano",
"Pensamento Ágil",
"Perito em Explosivos",
"Plano de Fuga",
"Primeira Impressão",
"Remoer Memórias",
"Resistir à Pressão"
]

PODER_PARANORMAL = ["Absorver Conhecimento",
"Afortunado",
"Anatomia Insana",
"Antecipar Vitalidade",
"Apatia Herege",
"Arma de Sangue",
"Aura de Pavor",
"Campo Protetor",
"Causalidade Fortuita",
"Combatente de Arena",
"Conexão Empática",
"Desejo Diabólico",
"Disparo da Morte",
"Encarar a Morte",
"Engolir Sangue",
"Escapar da Morte",
"Espreitar da Besta",
"Expansão de Conhecimento",
"Filho da Dor",
"Golpe de Sorte",
"Instintos Sanguinários",
"Manipular Entropia",
"Novo Caminho",
"Percepção Paranormal",
"Potencial Aprimorado",
"Potencial Reaproveitado",
"Precognição ",
"Predador de Sangue",
"Pressão Atmosférica",
"Resistir a <Elemento>",
"Sabor do Silêncio",
"Sangue de Ferro",
"Sangue Fervente",
"Sangue Vivo",
"Sede de Vingança",
"Sensitivo",
"Surto Temporal",
"Valer-se do Caos",
"Visão do Oculto",
"Zona dos Sussurros"
]

PODER_GERAL = ["Acrobático",
"Arte da Música Macabra",
"Artista Marcial",
"Ás do Volante",
"Atlético",
"Atraente",
"Combater com Duas Armas",
"Corpo Fechado",
"Dedos Ágeis",
"Detector de Mentiras",
"Especialista de Emergências",
"Especialista em Correntes",
"Esquiva Tática",
"Estágio Terminal",
"Estigmado",
"Foco em Perícia",
"Informado",
"Interrogador",
"Inventário Organizado",
"Kian Vai Nos Salvar",
"Mentiroso Nato",
"Movimentação Tática",
"Observador",
"Pai de Pet",
"Palavras de Devoção",
"Palpite Confiante",
"Parceiro",
"Pensamento Tático",
"Personalidade Esotérica",
"Persuasivo",
"Pesquisador Científico",
"Prática com Materiais Ritualísticos",
"Previsões de Emergência",
"Proativo",
"Racionalidade Inflexível",
"Rato de Computador",
"Resposta Rápida",
"Revidar Violento",
"Saque Rápido",
"Sentido Tático",
"Sentidos Aguçados",
"Sintonização Mental com Arma",
"Sintonização Mental com Proteção",
"Sobrevivencialista",
"Sorrateiro",
"Talentoso",
"Teimosia Obstinada",
"Tenacidade",
"Tiro Certeiro",
"Tratamento de Emergência",
"Vitalidade Reforçada",
"Vontade Inabalável",
]

poder1 = None
poder2 = None
poder3 = None
trilha = None

imagem = None

class Ordem(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
     @commands.command()
     async def ordembuild(self, ctx):
          arma = random.choice(ARMAS)
          item1 = random.choice(ITENS)
          item2 = random.choice(ITENS)
          origem = random.choice(ORIGENS)
          classe = random.choice(CLASSES)
          if classe == 'Ocultista':
               poder1 = random.choice(PODER_PARANORMAL)
               poder2 = random.choice(PODER_OCULTISTA)
               poder3 = random.choice(PODER_GERAL)
               trilha = random.choice(TRILHAS_OCULTISTA)
               imagem = discord.File("discord_bot\cogs\imagens\ocultista.png", filename="imagem.png")

          elif classe == 'Combatente':
               poder1 = random.choice(PODER_PARANORMAL)
               poder2 = random.choice(PODER_COMBATENTE)
               poder3 = random.choice(PODER_GERAL)
               trilha = random.choice(TRILHAS_COMBATENTE)
               imagem = discord.File("discord_bot\cogs\imagens\combatente.png", filename="imagem.png")
         
          elif classe == 'Especialista':
               poder1 = random.choice(PODER_PARANORMAL)
               poder2 = random.choice(PODER_ESPECIALISTA)
               poder3 = random.choice(PODER_GERAL)
               trilha = random.choice(TRILHAS_ESPECIALISTA) 
               imagem = discord.File("discord_bot\cogs\imagens\especialista.png", filename="imagem.png")
        
          else:
               trilha = random.choice(TRILHA_MUNDANO)
               poder1 = "Empenho"
               poder2 = None
               poder3 = None
               imagem = discord.File("discord_bot\cogs\imagens\mundano.png", filename="imagem.png")

          buildordem = discord.Embed(
               title = "Personagem Aleatório",
               description= 'Dá as informações aleatoriamente para montar uma ficha de Ordem Paranormal.',
               color = discord.Color.purple()
          )
          buildordem.set_image(url="attachment://imagem.png")
          buildordem.add_field(
               name = "Classe",
               value = f"**{classe}**",
               inline=False
          )
          buildordem.add_field(
               name="Trilha",
               value= f"**{trilha}**",
               inline = False
          )
          buildordem.add_field(
               name = "Poderes",
               value = f'**{poder1}**\n**{poder2}**\n**{poder3}**',
               inline = False
          )

          await ctx.reply(embed=buildordem, file=imagem)


async def setup(bot):
    await bot.add_cog(Ordem(bot))