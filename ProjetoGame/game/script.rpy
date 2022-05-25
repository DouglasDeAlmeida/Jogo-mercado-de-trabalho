﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

define protagonista = Character("James")
define som = 0.5 #volume para a narração

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/Trilha.mp3" volume 0.1
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    call prologue
    call inicio_Carreira
    call morte_sem_dinheiro
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

    "James não se dava bem com as outras crianças mais velhas e durante 1 ano sofreu na mão delas, cansado de ser tratado do mesmo jeito, começou a se rebelar e brigar."
    
    scene orphanato
    play sound "audio/cenario4.flac" volume som

    "Todo ato de rebelião de James era denunciado à diretoria do orfanato e James era castigado a passar o dia isolado das outras crianças e com poucos brinquedos à sua disposição, o que acabava deixando-o apenas mais frustrado."
    
    scene professor_pais

    "Devido ao seu comportamento, na hora da adoção James sempre era relatado pela dona do orfanato como uma criança de comportamento rebelde e com pavio curto e nenhum adulto desejava adotá-lo."
    
    play sound "audio/cenario5.flac" volume som
    scene aula

    "Com 6 anos James já havia se acostumado aos castigos, e até a apreciá-los, passou a levar livros de ficção e matemática para o período de isolamento , inicialmente teve muita dificuldade na leitura, porém , após um tempo começou a entendê-los e adquiriu um domínio na área de exatas superior às demais crianças."

    play sound "audio/cenario6.flac" volume som
    scene familia
    "Ainda assim James continuava com sua fama de rebelde e nenhum adulto queria adotá-lo. Somente aos 10  anos  James foi adotado , por uma família de classe média , que já possuía uma filha mais velha."
    
    play sound "audio/cenario7.flac" volume som
    scene prova
    "Enviaram James para outra escola pública, lá, se aprofundou ainda mais na área de exatas, porém passava dificuldade em matérias de humanas , conseguiu fazer um pequeno grupo de amigos porém não se relacionava bem com a maioria das crianças e professores."
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