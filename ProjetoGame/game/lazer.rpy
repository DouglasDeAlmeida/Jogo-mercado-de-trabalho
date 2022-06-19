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
    stop music
    play sound "audio/supermercado.mp3" volume 0.5
    protagonista "Tenho que ir ao supermercado para comprar leite"
    menu:
        "Comprar o leite mais barato":
            pass
            
            $dinheiro -=5
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
    play sound "audio/festa.mp3" volume 0.3
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
                $dinheiro += 10
                #Menos felicidade, Mais marcador de trabalho, Mais dinheiro

        "Ignorar a festa e continuar trabalhando":
            $dinheiro += 10
            $trabalho += 10
            $felicidade -= 10
    stop sound
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
            $dinheiro = dinheiro/3
        "Poupar dinheiro e contratar qualquer advogado":
            scene prision2
            "James é condenado e preso por alguns dias. Seu chefe fica furioso ao saber disso"
            $felicidade-=5
            $trabalho -= 10
    stop sound
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
    stop sound        
    play music "audio/Trilha.mp3" volume 0.8
    

    return

label crack:
    $idade = 19
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
            call crack2
        "Recusar a proposta":
            "Apesar de sua aparência, James diz que nunca usou nenhuma droga e que hoje não irá cruzar essa linha."
    return

label crack2:
    if drogado is True:

        scene crack_img
        "James sente abstinência e vai em busca do seu amigo Gustavo para mais crack.
        "
        protagonista "Sinto que se não satisfazer meu desejo, me sentirei muito mais infeliz."
        menu:
            "Aceitar o Crack":
                "James fuma o crack e se sente melhor
                "
                $felicidade += 5
                $saude -= 15
                
                $dinheiro -= 2000
                $drogado = True
                #call etBilu
            "Recusar a proposta":
                "James diz não às drogas"
                $felicidade = felicidade/3
                $reabilitado += 1
                if reabilitado >=2:
                    $drogado=False 
    return


label etBilu:
    scene floresta_bilu2
    "James acorda no meio de uma floresta, confuso, procura uma saída."
    "Após caminhar um pouco ele sente uma corrente de ar, desesperado por reencontrar a civilização, James vai em direção à corrente."
    scene floresta_bilu
    "James chega em uma planície e descobre que o vento vinha de uma nave alienígena aterrissando, James observa o evento atentamente atrás de uma árvore. "
    "De dentro da nave sai um alienígena, em segundos o alien vira sua atenção a James e lhe faz um sinal para se aproximar."
    scene bilu_out2
    "James hesita inicialmente porém pensa que se o alien fosse violento já teria o eliminado, partindo dessa suposição James se aproxima do alien."
    "Há uma barreira linguística entre os dois e James decide nomear seu novo companheiro de Bilu, Bilu pede para seu novo amigo lhe acompanhar à nave e James o segue."
    "Lá dentro há diversas máquinas bizarras, Bilu cutuca James e aponta para uma poltrona com um capacete cheio de fios.
    "
    menu:
        "ir para a poltrona e colocar o capacete":
            "James põe o capacete e fecha os olhos. Ao abrir os olhos novamente ele está no espaço, James observa o passado da terra como um espectador,
            anos se passam em microsegundos, James presencia tudo desde o surgimento dos primeiros organismos até a completa destruição do planeta (todo este processo sendo narrado por Morgan Freeman), sobrecarregado de informação James desmaia."
            $dinheiro -= 15
            $saude -= 10
            $felicidade += 15
            "ele acorda no meio da rua com uma dor de cabeça, ao seu lado seu amigo Gustavo desmaiado, ambos sem carteira. Após essa experiência James se sente mais motivado porém também começou a sentir dores de cabeça frequentemente."
            " Devido à dor de cabeça, james decidiu ir ao médico. O médico diagnosticou James com ansiedade e receitou que ele tomasse 25 mg de “Agomelatina” diariamente ao se deitar durante duas semanas."
        #"Com medo do que a máquina de Bilu é capaz James corre da nave":
        "Correr da nave":
            "James vê que a saída está se fechando e corre o mais rápido possível como se sua vida dependesse disso. "
            "A escotilha está quase fechada e James pula por cima sem perceber que a nave estava voando, James cai e vê sua vida passando na frente dos seus olhos, ele recorda tudo:
                do seu tempo no orfanato, da sua vida escolar, de todas as angústias e momentos felizes que passou, James relutante fecha os olhos e aceita seu destino"
            "Ao abrir os olhos novamente James percebe que se encontra em um local familiar, ao seu lado seu amigo Gustavo James checa o seu bolso e novamente sente falta da sua carteira."
            $dinheiro -= 15
            $saude -= 10
            $felicidade += 15
    return



label evento_galatico:
    #TODO
    return