class Suspeito:
    def __init__(self, nome, genero, cabelo, comida, esporte, hobby, musica):
        self.nome = nome
        self.genero = genero
        self.cabelo = cabelo
        self.comida = comida
        self.esporte = esporte
        self.hobby = hobby
        self.musica = musica

    def __repr__(self):
        # representação para o programador
        return f"Suspeito(nome='{self.nome}')"


# cria uma lista de suspeitos 
suspeitos = [
    # cria um objeto que representa um suspeito
    Suspeito(
        nome="Michael Schwade",
        genero="Homem",
        cabelo="Preto",
        comida="Mineira",
        esporte="Volei",
        hobby="Apostador",
        musica="Rock",
    ),
    Suspeito(
        nome="Maxime Donnay",
        genero="Homem",
        cabelo="Castanho",
        comida="Frutos do mar",
        esporte="Basquete",
        hobby="Apostador",
        musica="Rock",
    ),
    Suspeito(
        nome="Benjamin Hana",
        genero="Homem",
        cabelo="Preto",
        comida="Coreana",
        esporte="Badminton",
        hobby="Apostador",
        musica="Country",
    ),
    Suspeito(
        nome="Karl La Fong",
        genero="Homem",
        cabelo="Preto",
        comida="Mexicana",
        esporte="Futebol",
        hobby="Vidente",
        musica="Rock",
    ),
    Suspeito(
        nome="Alexander Graham Edison",
        genero="Homem",
        cabelo="Castanho",
        comida="Mineira",
        esporte="Basquete",
        hobby="Reparador",
        musica="Opera",
    ),
    Suspeito(
        nome="Ken Hartley Reed",
        genero="Homem",
        cabelo="Castanho",
        comida="Frutos do mar",
        esporte="Basquete",
        hobby="Explorador",
        musica="Classica",
    ),
    Suspeito(
        nome="Sheriff Paul Drive",
        genero="Homem",
        cabelo="Loiro",
        comida="Coreana",
        esporte="Volei",
        hobby="Reparador",
        musica="Country",
    ),
    Suspeito(
        nome="Mylar Naugahyde",
        genero="Homem",
        cabelo="Loiro",
        comida="Mineira",
        esporte="Volei",
        hobby="Apostador",
        musica="Opera",
    ),
  
    Suspeito(
        nome="Titus Candy",
        genero="Homem",
        cabelo="Ruivo",
        comida="Frutos do mar",
        esporte="Futebol",
        hobby="Explorador",
        musica="Classica",
    ),
    Suspeito(
        nome="Sven Galli",
        genero="Homem",
        cabelo="Ruivo",
        comida="Mexicana",
        esporte="Badminton",
        hobby="Vidente",
        musica="Rock",
    ),
    Suspeito(
        nome="Carmen Sandiego",
        genero="Mulher",
        cabelo="Preto",
        comida="Mexicana",
        esporte="Basquete",
        hobby="Apostador",
        musica="Classica",
    ),
    Suspeito(
        nome="Gypsy Rose Lasagna",
        genero="Mulher",
        cabelo="Preto",
        comida="Mexicana",
        esporte="Basquete",
        hobby="Vidente",
        musica="Rock",
    ),
    Suspeito(
        nome="Polly Esther Fabrique",
        genero="Mulher",
        cabelo="Castanho",
        comida="Frutos do mar",
        esporte="Volei",
        hobby="Vidente",
        musica="Opera",
    ),
    Suspeito(
        nome="B.B.D. O'Brien",
        genero="Mulher",
        cabelo="Castanho",
        comida="Frutos do mar",
        esporte="Volei",
        hobby="Explorador",
        musica="Classica",
    ),
    Suspeito(
        nome="Heidi Gosikh",
        genero="Mulher",
        cabelo="Loiro",
        comida="Mineira",
        esporte="Badminton",
        hobby="Reparador",
        musica="Country",
    ),
    Suspeito(
        nome="Venus H.Pencil",
        genero="Mulher",
        cabelo="Loiro",
        comida= "Mineira",
        esporte="Badminton",
        hobby="Reparador",
        musica="Opera",
    ),
    Suspeito(
        nome="Wendy Pauper",
        genero="Mulher",
        cabelo="Ruivo",
        comida="Coreana",
        esporte="Futebol",
        hobby="Apostador",
        musica="Rock",
    ),
    Suspeito(
        nome="Brenda Vanderbilt",
        genero="Mulher",
        cabelo="Ruivo",
        comida="Coreana",
        esporte="Futebol",
        hobby="Explorador",
        musica="Country",
    ),  
]

GENEROS = ("mulher", "homem")
CABELOS = ("ruivo", "loiro", "castanho", "preto")
COMIDAS = ("mineira", "mexicana", "coreana", "frutos do mar")
ESPORTES = ("badminton", "futebol", "basquete", "volei")
MUSICAS = ("classica", "country", "opera", "rock")
HOBBIES = ("apostador", "explorador", "vidente", "reparador")
OPCOES = ("sim", "nao")


class Pais:
    def __init__(self, nome, texto, moeda, bandeira, cultura, tesouro):
        self.nome = nome
        self.texto = texto
        self.moeda = moeda
        self.bandeira = bandeira
        self.cultura = cultura
        self.tesouro = tesouro

paises = [
    
    Pais(
        nome="Russia",
        texto="Chandram Brambachandra Chandra Bendram.",
        moeda="rublo.",
        bandeira="branca, azul e vermelha",
        cultura="o vulcão Koryaksky.",
        tesouro="o figurino do Vitas em 7th Element.",
    ),

     Pais(
        nome="Mexico",
        texto="Y a mucha honra! María la del Barrio soy.",
        moeda="peso.",
        bandeira="verde, branca e vermelha",
        cultura="Acapulco.",
        tesouro="o roteiro original da nova novela da Televisa.",
    ),
     Pais(
        nome="Brasil",
        texto="HueHue br br.",
        moeda="real.",
        bandeira="verde, amarela, azul e branca",
        cultura="o Rio Amazonas.",
        tesouro="os memes da Gretchen.",
    ),
    Pais(
        nome="China",
        texto="I have to have my China!",
        moeda="renminbi.",
        bandeira="vermelha",
        cultura="os principios do confucionismo.",
        tesouro="as perucas de Ice Fantasy.",
    ),
]



