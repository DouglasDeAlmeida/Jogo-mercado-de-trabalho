label socio_empresa:
    
    "Um amigo de James abriu um novo negócio, começando do zero, e o chamou para ser sócio, porém é um negócio com riscos de dar errado"
    menu:
        "Aceitar a proposta":
            $dinheiro -= 5
            $socio = True
        "Recusar":
            $socio = False
            pass

    return


label feedback_empresa:
    "O negócio de seu amigo está dando certo está dando certo e ele está lucrando bastante"
    if socio:
        $dinheiro += 30
        $felicidade += 5
    else:
        protagonista"Que pena que não investi."
        $felicidade -= 15

label dificuldade_codigo:
    $idade = 33
    "James está tendo dificuldades em realizar um código, desesperado, pesquisa na internet o que precisa."
    "depois de uma longa pesquisa James acha um código que parece ter tudo que precisa para realizar a tarefa, porém não entende como ele funciona."
    menu:
        "copiar o código":
            $sorte = renpy.random.random()
            "James copia o código sem modificar nada e envia para seu chefe como se fosse de sua autoria."
            if sorte >= 0.5:
                "O chefe recebe seu código e tem uma sensação de deja vu , curioso, pesquisa na internet e acha um stack overflow com um código igual ao que James mandou, no dia seguinte dá uma bronca em James"
                $trabalho -= 15
            if sorte < 0.5:
                "O chefe olha o código e fica impressionado com os esforços de James. No dia seguinte parabeniza James pelo bom trabalho"
                $trabalho += 15

            
        "Não copiar e tentar fazer algo do zero":
            "James se esforça para resolver o problema que lhe foi dado mas é incapaz de fazer progresso."
            "No dia seguinte James explica sua situação descrevendo o que tentou fazer e finalizando dizendo que não foi capaz de criar o código que seu chefe pediu."
            "Seu chefe fica bravo com James, porém ao ver seu esforço também sente um pouco de compaixão, James se safou dessa vez."
    return




label programacao:
    $idade = 30
    "James se encarregou de fazer uma programação e apresentar seus resultados para seu chefe. A prazo para finalizar esse código é hoje, porém James ainda não terminou e está quase na hora dele ser liberado do trabalho"
    menu: 
        "Ficar mais tempo no trabalho até resolver o código":
            "Você consegue entregar o código porém fica exausto de tanto trabalhar neste dia"
            $saude -= 5
            $trabalho += 5
        "Ir embora no horário de sempre e adiar a entrega do código":
            $saude += 5
            $trabalho -= 5
    return
label linkedin:
    $idade = 23
    define linkedin_account = False
    menu:
        protagonista"Devo criar um Linkedin?"

        "sim":
            $linkedin_account = True
        "não":
            pass
    
    if linkedin_account:
        "Você entra no Linkedin e descobre uma grande oportunidade para iniciar a carreira estagiando na IBM. Você vai bem na entrevista de emprego e consegue o trabalho."
        call tempo(12)
        "Um ano se passa e a IBM resolve te efetivar como profissional da empresa"
        $dinheiro += 10
        #$salario = 10000
    if linkedin_account == False:
        "Caso James não tenha Linkedin: James é indicado por um amigo para trabalhar numa empresa de médio porte. Apesar de não ser o jeito perfeito de iniciar a carreira, James resolve abraçar a oportunidade"
        #$salario = 4000
        $dinheiro += 4

    return




label bom_trabalho_SC:
    $idade = 29
    #"Passando-se uns anos, se o marcador de James estiver acima da metade, ele será promovido a um cargo melhor e será mais bem pago"
    if trabalho >= 50:
        "Você foi promovido a um cargo melhor"
        #$salario = 15000
        $dinheiro += 15
        $felicidade +=10
    return


label palestra_tecnologia:
    $idade = 28
    scene conferencia_tec
    "Você leu em um cartaz sobre uma palestra de tecnologia paga"
    
    menu:
        "participar":
            #mais educação
            #menos dinheiro
            #talvez aumentar o marcador de trabalho
            $dinheiro -= 10
            pass
        "recusar":
            pass
    return


label empresa_rival:
    $idade = 27
    "Uma empresa rival da empresa em que James trabalha o faz uma proposta, com um salário maior ao que ele recebe"
    menu:
        "aceitar a proposta":
            "Você aceita o emprego com maior salário, porém não curte muito o ambiente interno da empresa e sente saudades de seu emprego antigo"
            #$salario = salario*1.2
            $dinheiro = dinheiro*1.2
            $felicidade -=5
        "Recusar proposta":
            "Seu chefe gostou da sua posição de fidelidade em relação à empresa em que você trabalha "
            $trabalho += 10

    return


label palestra_james:
    "James foi convidado a dar uma palestra sobre tecnologia para jovens aprendizes da área. É a primeira grande palestra que James irá apresentar em sua vida."
    menu:
        "Recusar o convite, pois não se sente preparado.":
            "seu chefe fica desapontado contigo"
            $trabalho -= 5
        "Aceitar o convite":
            menu:
                "Passar as madrugadas anteriores praticando para mandar bem na hora":
                    "Seu chefe gostou de seu desempenho na apresentação"
                    $saude -= 5
                    $felicidade += 5
                    $trabalho += 10
                "Não se preparar direito antecipadamente, pois James confia em seu potencial":
                    "Seu chefe achou que você deveria ter se saído melhor na apresentação"
                    $trabalho -=5
    return

                
label algoritmo:
    scene algoritmo_james
    "James construiu um algoritmo com o objetivo de prever se um indivíduo é criminoso ou não baseado em alguns dados da pessoa."
    call comecar_21 from _call_comecar_21#verificar esse from
    return

label final_feliz_tecnologia:
    scene james_ceo
    play music "audio/audio_vitoria.mp3" volume 0.8
    centered"James é CEO / sócio de uma grande empresa e alcança o status de milionário"
    return

label final_triste_tecnologia:
    "James é um diretor de TI de sua empresa e têm um dinheiro mais que suficiente para sustentar a si mesmo"



