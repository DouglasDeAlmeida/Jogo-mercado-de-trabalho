image tb = "images/21/mesa.jpg"
style button_text:
    color "#fff"
    hover_color "#ddd"
screen jogadas:
    if btnn<5:
        textbutton "Outra carta" xalign .5 yalign .5 action [SetVariable("karta"+str(btnn),renpy.random.randint(2,11)),SetVariable("kartam"+str(btnn),renpy.random.choice([100,200,300,400])),SetVariable("kart"+str(btnn),renpy.random.randint(2,11)),SetVariable("kartm"+str(btnn),renpy.random.choice([100,200,300,400])),SetVariable("btnn",btnn+1),Jump("jogar")]
    textbutton "Terminar" xalign .5 yalign .54 action Jump("terminar")
screen cartas:
    hbox xalign .1:
        add "images/21/" + str(kart1+kartm1)+".png"
        add "images/21/" + str(kart2+kartm2)+".png"
        add "images/21/" + str(kart3+kartm3)+".png"
        add "images/21/" + str(kart4+kartm4)+".png"
    hbox xalign .1 yalign .70:
        add "images/21/" + str(karta1+kartam1)+".png"
        add "images/21/" + str(karta2+kartam2)+".png"
        add "images/21/" + str(karta3+kartam3)+".png"
        add "images/21/" + str(karta4+kartam4)+".png"
label comecar_21:
    $ vitorias = 0

    "Ganhe 3 vezes no Blackjack, prove que você é sortudo e você obterá sucesso!"

    call vinteeum(True)
    call vinteeum
    call vinteeum

    hide screen cartas
    
    if vitorias >= 3:
        "Parabéns, você ganhou 3 vezes no Blackjack"
        scene jacquin
        "Jacquin gostou da comida e lhe dá uma estrela michelin. "
        jump final_feliz_gastronomia
    else:
        "Perdeu tudo"
        scene jacquin
        $dinheiro = 0
        "Jacquin te chama de incopetente e dedica um episódio completo de seu programa para criticar o seu restaurante"
        "O restaurante é fechado e todos foram demitidos, incluindo James."
        jump morte_sem_dinheiro
    return
label vinteeum(primeira_jogada=False):
    scene tb
    $ btnn=2
    $ kart1=renpy.random.randint(2,11)
    $ kartm1=renpy.random.choice([100,200,300,400])
    $ karta1=renpy.random.randint(2,11)
    $ kartam1=renpy.random.choice([100,200,300,400])
    $ kart2=0
    $ kart3=0
    $ kart4=0
    $ kartm2=0
    $ kartm3=0
    $ kartm4=0
    $ karta2=0
    $ karta3=0
    $ karta4=0
    $ kartam2=0
    $ kartam3=0
    $ kartam4=0
    $ cpupoint=kart1
    $ ipoint=karta1
    if not primeira_jogada:
        e "Jogue novamente!"
label jogo_info:
    show screen cartas
    show screen jogadas
    e " Dealer - [cpupoint]\n Minha mão - [ipoint]"
    jump jogo_info
label jogar:
    if cpupoint>16:
        if btnn==4:
            $ kart3=0
            $ kartm3=0
        if btnn==5:
            $ kart4=0
            $ kartm4=0
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if cpupoint>21:
        if kart1==11:
            $ kart1=1
        elif kart2==11:
            $ kart2=1
        elif kart3==11:
            $ kart3=1
        elif kart4==11:
            $ kart4=1
        $ cpupoint=kart1+kart2+kart3+kart4
    if ipoint>21:
        if karta1==11:
            $ karta1=1
        elif karta2==11:
            $ karta2=1
        elif karta3==11:
            $ karta3=1
        elif karta4==11:
            $ karta4=1
        $ ipoint=karta1+karta2+karta3+karta4
    jump jogo_info
label terminar:
    hide screen jogadas
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if ipoint>21:
        if cpupoint>21:
            e "Empate"
        else:
            e "Perdeu"
    elif cpupoint>21:
        e "Ganhou"
        $ vitorias += 1
    elif ipoint==cpupoint:
        e "Empate"
    elif ipoint>cpupoint:
        if cpupoint<17:
            if kart2==0:
                $ kart2=renpy.random.randint(2,11)
                $ kartm2=renpy.random.choice([100,200,300,400])
                jump terminar
            elif kart3==0:
                $ kart3=renpy.random.randint(2,11)
                $ kartm3=renpy.random.choice([100,200,300,400])
                jump terminar
            elif kart4==0:
                $ kart4=renpy.random.randint(2,11)
                $ kartm4=renpy.random.choice([100,200,300,400])
                jump terminar
        $ vitorias += 1
        e "Ganhou"
    else:
        e "Perdeu"
    return
