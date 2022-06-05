label thailand:
    scene thai
    "depois de uma viajem relaxante para a tailândia você se sente muito mais feliz. "
    $felicidade += 10 
    
    scene prostituta
    "Entretanto, durante sua estadia em Bankok você contraiu gonorreia de uma prostituta"
    
    $saude -= 10
    return
label grupo_caminhada:
    scene caminhada
    "Seu amigo Bernardo te convidou para participar do grupo de caminhada"
    menu:
        "participar":
            $felicidade += 5
            
            $saude += 5
            
            pass
        "recusar":
            pass
    return

label supermercado:
    scene comprar_leite
    protagonista "Tenho que ir ao supermercado para comprar leite"
    menu:
        "Comprar o leite mais barato":
            pass
            
            $dinheiro -=50
            # 50% de chance de comprar leite estragado
                # menos saúde se for o caso
                # TALVEZ: caso não esteja estragado aumentar saúde
        "Comprar o leite mais caro":
            pass
            
            $dinheiro -=100
            $saude += 5 
            #um pouco mais de saude
    return

label festa_bernardo:
    scene festa
    "Seu melhor amigo está dando uma festa o que você faz"
    $ sorte = renpy.random.random()
    menu:
        "Dizer ao chefe que você está doente e não poderá ir trabalhar":
            #50% de chance dele liberar
            $ sorte = renpy.random.random()
            
            if sorte >= 0.5:
                "Seu chefe te liberou"
            
                #mais felicidade, um pouco menos no marcador de trabalho
                $felicidade += 5
                $trabalho -= 3
            if sorte < 0.5:
                "Infelizmente seu chefe disse que tem uma demanda urgente e precisa que você trabalhe de casa"
                menu:
                    "Trabalhar":
                        
                        $felicidade -= 10
                        $trabalho += 3
                        $dinheiro += 1000
                        #menos felicidade, um pouco mais no marcador de trabalho, mais dinheiro

                    "Dizer que não pode e ir à festa":
                        
                        $felicidade += 5
                        $trabalho -= 10
                        $dinheiro -= 2000
                        #mais felicidade, muito menos no marcador de trabalho, menos dinheiro.
        "Pedir ao seu chefe para ser liberado um pouco mais cedo do trabalho":
            
            #50% de chance dele liberar
            if sorte >= 0.5:
                "Seu chefe te liberou"
                $felicidade += 5
                $trabalho += 2
                $dinheiro += 500
                #Um pouco mais de felicidade,um pouco menos no marcador de trabalho, Mais dinheiro
            
            if sorte < 0.5:
                "Você decide que desobedecer seu chefe para ficar por pouco tempo na festa não valeria a pena."
                $felicidade -= 10
                $trabalho += 3
                $dinheiro += 1000
                #Menos felicidade, Mais marcador de trabalho, Mais dinheiro

        "Ignorar a festa e continuar trabalhando":
            $dinheiro += 1000
            $trabalho += 10
            $felicidade -= 10

    return

label drunk_driving:
    scene police_stoping_james
    play sound "audio/POLICIA.mp3" volume 0.4
    "James é parado pela polícia dirigindo embriagado e terá que depor no trubunal"
    scene judment
    menu:
        protagonista"Qual advogado devo contratar"

        "Contratar o melhor advogado que conseguir achar":
            "O advogado que James contratou conseguiu livrar a pele dele nos tribunais"
            $dinheiro -= 15000
        "Poupar dinheiro e contratar qualquer advogado":
            scene prison2
            "James é condenado e preso por alguns dias. Seu chefe fica furioso ao saber disso"
            $felicidade-=5
            $trabalho -= 10
    
    #call status
    return

label beatriz:
    scene opera_outside
    "James reencontra sua amiga de infância, Beatriz, que coincidentemente se mudou para perto de onde mora. Agora ela é uma cantora de ópera, e o convida para ir de graça num show que ela irá fazer."
    "porém, o show é no mesmo horário em que você havia prometido jogar futebol com o Bernardo."
    stop music
    menu:
        protagonista"O que devo fazer?"
        
        "Ir ao show de ópera":
            scene opera_inside

            show launch
            protagonista"meu deus, que show hilário. A Beatriz canta igual um muppet"
            #som beatriz
            $felicidade += 2
        "Ir jogar futebol":
            #som futbol
            play sound "audio/futebol.mp3" volume 0.2
            scene soccer2
            "James acaba torcendo feio o pé jogando bola"
            $felicidade -= 5
            $saude -= 20
    play music "audio/Trilha.mp3" volume 0.8
    stop sound

    return

label crack:
    scene crack_img
    "Batendo a perna pela cidade em busca de dinheiro, James chega em um beco.
    Ao se deparar onde ele está James dá meia volta e anda rapidamente, porém em sua fuga, uma mão lhe puxa o braço.
    "
    "Era seu amigo da escola Gustavo, vocês conversam brevemente e vendo o desespero de James, Gustavo lhe oferece crack para acalmar os nervos."
    menu:
        "Aceitar o Crack":
            "James fuma o crack, por um breve instante sua angústia por buscar emprego some, James deita no chão e aprecia o momento.
            Após 1 hora James acorda com dor de cabeça, ao mexer no bolso não consegue achar sua carteira.
            "
            $felicidade += 5
            $saude -= 15
            
            $dinheiro -= 2000
            $drogado = True
        "Recusar a proposta":
            "Apesar de sua aparência, James diz que nunca usou nenhuma droga e que hoje não irá cruzar essa linha."
    return

label crack2:
    if drogado is True:

        scene crack_img
        "James sente abstinência e vai em busca do seu amigo Gustavo para mais crack.
        Se ele não satisfazer seu desejo, se sentirá muito mais infeliz.
        "
        menu:
            "Aceitar o Crack":
                "James fuma o crack e se sente melhor
                "
                $felicidade += 5
                $saude -= 15
                
                $dinheiro -= 2000
                $drogado = True
            "Recusar a proposta":
                "James diz não às drogas"
                $felicidade = felicidade/3
                $reabilitado += 1
                if reabilitado >=2:
                    $drogado=False 
    return