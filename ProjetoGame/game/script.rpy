# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonista = Character("James")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/Trilha.mp3" volume 0.1
    scene casa
    #play audio "audio/cenario1.mp3" volume0.3
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    play sound "audio/cenario1.flac" volume 0.5

    "James, teve uma infância difícil, nascido em uma família de baixa renda, incapaz de criá-lo, foi retirado da família e mandado para um orfanato aos 4 anos."
    scene orfanato

    play sound "audio/cenario2.flac" volume 0.5

    "No orfanato James passava o período da manhã aprendendo a ler e fazer contas básicas e no período da tarde podia brincar ou interagir com as outras crianças."
    scene kids

    play sound "audio/cenario3.flac" volume 0.5
    "James não se dava bem com as outras crianças mais velhas e durante 1 ano sofreu na mão delas, cansado de ser tratado do mesmo jeito, começou a se rebelar e brigar."
    
    scene orphanato
    play sound "audio/cenario4.flac" volume 0.5
    "Todo ato de rebelião de James era denunciado à diretoria do orfanato e James era castigado a passar o dia isolado das outras crianças e com poucos brinquedos à sua disposição, o que acabava deixando-o apenas mais frustrado."
    
    "Devido ao seu comportamento, na hora da adoção James sempre era relatado pela dona do orfanato como uma criança de comportamento rebelde e com pavio curto e nenhum adulto desejava adotá-lo."
    
    play sound "audio/cenario5.flac" volume 0.5
    scene sala_aula
    "Com 6 anos James já havia se acostumado aos castigos, e até a apreciá-los, passou a levar livros de ficção e matemática para o período de isolamento , inicialmente teve muita dificuldade na leitura, porém , após um tempo começou a entendê-los e adquiriu um domínio na área de exatas superior às demais crianças."

    play sound "audio/cenario6.flac" volume 0.5
    "Ainda assim James continuava com sua fama de rebelde e nenhum adulto queria adotá-lo. Somente aos 10  anos  James foi adotado , por uma família de classe média , que já possuía uma filha mais velha."
    play sound "audio/cenario7.flac" volume 0.5
    "Enviaram James para outra escola pública, lá, se aprofundou ainda mais na área de exatas, porém passava dificuldade em matérias de humanas , conseguiu fazer um pequeno grupo de amigos porém não se relacionava bem com a maioria das crianças e professores, e em casa era comparado a filha do casal"
    
    "que tirava notas superiores a James em todas as matérias, nunca recebendo reconhecimento pela sua performance acima da média em exatas."
    scene bar2
    play sound "audio/cenario8.flac" volume 0.5
    "Conforme o tempo, James começou a constantemente matar as aulas que não gostava, pedindo para que seus amigos respondessem à chamada em seu nome."
    
    "Fora da aula James saía com o grupo mais velho da escola, os rolês com esta galera variavam bastante. Algumas vezes iam para pizzarias ou festas e outras vezes saíam para beber ou usar drogas ou jogar jogos de apostas."
    scene apostas
    "James sempre dizia não às drogas e bebidas, porém sempre que tinha um trocado entrava para a mesa de apostas."
    scene professor_pais
    play sound "audio/cenario9.flac" volume 0.5
    "Aos 16 anos um professor percebeu o esquema de resposta de chamadas de James e chamou a atenção de seus pais , não só para as faltas em sua matéria, mas para todas as matérias."
    
    "Os pais de Fulano não reagiram bem à notícia, bravo com sua vagabundice seu pai lhe obrigou a trabalhar e ainda ameaçou abandonar o filho caso ele faltasse em mais alguma aula."
    # This ends the game.
    return

#label background:
#    scene orphanato
    