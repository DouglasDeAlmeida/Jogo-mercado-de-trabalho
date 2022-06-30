# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define felicidade = 50 #vão de 0-100
define saude = 50 #0-100
define dinheiro = 50
define despesa = 1000
define educacao = 0
define salario = 0
define trabalho = 0
define idade = 18
define socio = False
define protagonista = Character("James")
define som = 0.5 #volume para a narração
define sentinela = True
define perdeu_minigame = False
define ciencias_contabeis = False
define ciencia_computacao = False
define curso_gastronomia = False


define desempregado = True
define drogado = False#variavel que verifica se o james é viciado
define reabilitado = 0 #variaavel que vai marcar se o james vai se recuperar do vício em crack
image launch = Movie(play="audio/muppet.webm", pos=(1180, 250), anchor=(0, 0), channel= "movie", size=(300,500))
#define lista = [inicio_Carreira, status,decision_uni]
# The game starts here.
label start:

    play music "audio/Trilha.mp3" volume 0.8
    call prologue
    show screen hbox_screen#mostra a idade
    show screen barraAmizade#mostra os status em formato de barra
    #vou fazer uma lista para cada carreira
    
    #inicio
    $lista_inicial = ['inicio_Carreira','mcdonalds_inicio','crack','ifood1','decision_uni', 'preenchimento']
    $count = 0
    while count < len(lista_inicial):
        call status
        if sentinela is True:
            $renpy.call(label=lista_inicial[count])
            call status
            $renpy.call(label=lista_inicial[count+1])
            $count +=2
            #pause


    if ciencia_computacao == True:
        #lista dos eventos de computação
        $lista_computacao = ['linkedin', 'grupo_caminhada', 'palestra_james', 'thailand', 'covid_25', 'supermercado', 'empresa_rival', 'tinder','palestra_tecnologia',
        'amor_de_escritorio', "bom_trabalho_SC", 'beatriz', 'festa_bernardo', 'programacao', 'drunk_driving', "cinco_anos", "dificuldade_codigo", "vegas", "socio_empresa", "affair", "feedback_empresa", "algoritmo"  ]
        $count = 0
        while count < len(lista_computacao):
            call status
            if sentinela is True:
                $renpy.call(label=lista_computacao[count])
                call status
                $renpy.call(label=lista_computacao[count+1])
                $count +=2




    if ciencias_contabeis == True:
        #lista dos eventos de contabilidade
        $lista_contabilidade = ['estagio', 'grupo_caminhada', 'misto', 'thailand', 'covid_25', 'supermercado', 'raiva', 'tinder', 'guru_investimento', 'amor_de_escritorio', 'excedente', 'beatriz', 'festa_bernardo',
        'cupom_dourado', 'drunk_driving', 'cinco_anos','demissao', 'vegas', 'aposentadoria_chefe', 'affair','doente_para_reuniao', 'evento_final_contabilidade']
        $count = 0
        while count < len(lista_contabilidade):
            call status
            if sentinela is True:
                $renpy.call(label=lista_contabilidade[count])
                call status
                $renpy.call(label=lista_contabilidade[count+1])
                $count +=2


    if curso_gastronomia == True:
        #lista dos eventos de gastronomia
        $lista_gastronomia = ['inicio_gastronomia', 'grupo_caminhada', 'thailand', 'covid_25', 'supermercado', 'ratatouille', 'tinder', 'guru_investimento', 'bom_trabalho', 'waitress', 'beatriz', 'festa_bernardo',
        'compras_restaurante', 'drunk_driving', 'cinco_anos', 'amigo_influencer', 'vegas', 'preparo_prato','affair','jacquin']
        $count = 0
        while count < len(lista_gastronomia):
            call status
            if sentinela is True:
                $renpy.call(label=lista_gastronomia[count])
                call status
                $renpy.call(label=lista_gastronomia[count+1])
                $count +=2

    # This ends the game.

  
            
    return



label prologue:
    scene casa
    play sound "audio/cenario1.flac" volume som 

    "James, teve uma infância difícil, nascido em uma família de baixa renda, incapaz de criá-lo, foi retirado da família e mandado para um orfanato aos 4 anos."
    scene orfanato
    play sound "audio/cenario2.flac" volume som

    "No orfanato James passava o período da manhã aprendendo a ler e fazer contas básicas e no período da tarde podia brincar ou interagir com as outras crianças."

    scene kids
    play sound "audio/cenario3.flac" volume som

    "James não se dava bem com as outras crianças mais velhas e durante 1 ano sofreu na mãos delas, cansado de ser tratado do mesmo jeito, começou a se rebelar e brigar."
    
    scene orphanato
    play sound "audio/cenario4.flac" volume som

    "Todo ato de rebelião de James era denunciado à diretoria do orfanato e James era castigado a passar o dia isolado das outras crianças e com poucos brinquedos à sua disposição, o que acabava deixando-o apenas mais frustrado."
    
    scene professor_pais

    "Devido ao seu comportamento, na hora da adoção James sempre era relatado pela dona do orfanato como uma criança de comportamento rebelde e com pavio curto. Por esse motivo, nenhum adulto desejava adotá-lo."
    
    play sound "audio/cenario5.flac" volume som
    scene aula

    "Aos 6 anos James já havia se acostumado aos castigos, e até a apreciá-los, passou a levar livros de ficção e matemática para o período de isolamento. Inicialmente teve muita dificuldade na leitura, porém , após um tempo começou a entendê-los e adquiriu um domínio na área de exatas superior às demais crianças."

    play sound "audio/cenario6.flac" volume som
    scene familia
    "Ainda assim James continuava com sua fama de rebelde e nenhum adulto queria adotá-lo. Somente aos 10  anos  James foi adotado, por uma família de classe média, que já possuía uma filha mais velha."
    
    play sound "audio/cenario7.flac" volume som
    scene prova
    "Enviaram James para outra escola pública, lá, se aprofundou ainda mais na área de exatas, porém passava dificuldade em matérias de humanas, conseguiu fazer um pequeno grupo de amigos porém não se relacionava bem com a maioria das crianças e professores."
    scene fav_daughter
    "Em casa, era comparado à filha do casal que tirava notas superiores a James em todas as matérias, nunca recebendo reconhecimento pela sua performance acima da média em exatas."
    scene bar2
    play sound "audio/cenario8.flac" volume som
    "Conforme o tempo, James começou a constantemente matar as aulas que não gostava, pedindo para que seus amigos respondessem à chamada em seu nome."
    
    "Fora da aula James saía com o grupo mais velho da escola, os rolês com esta galera variavam bastante. Algumas vezes iam para pizzarias ou festas e outras vezes saíam para beber ou usar drogas ou jogar jogos de apostas."
    scene apostas
    "James sempre dizia não às drogas e bebidas, porém sempre que tinha um trocado entrava para a mesa de apostas."

    play sound "audio/cenario9.flac" volume som

    scene professor
    "Aos 16 anos um professor percebeu o esquema de resposta de chamadas de James e chamou a atenção de seus pais , não só para as faltas em sua matéria, mas para todas as matérias."

    scene father
    "Os pais de James não reagiram bem à notícia, bravo com sua vagabundice seu pai lhe obrigou a trabalhar e ainda ameaçou abandonar o filho caso ele faltasse em mais alguma aula."

    "Com as complicações do emprego, suas notas diminuíram mais uma vez e quase foi reprovado, mas, apesar das dificuldades, James conseguiu se formar aos 18 anos."
    stop sound
    return