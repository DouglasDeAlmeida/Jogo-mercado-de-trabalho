
#TODO: fazer um marcador oculto de trabalho (confiança do seu atual chefe contigo)
label inicio_Carreira:
    scene thinking #imagem de fundo
    protagonista "Não consigo passar mais nem um minuto nessa casa, preciso de um lugar pra mim. Tenho um pouco de dinheiro que ganhei ajudando meu pai, entretanto, não é muito."
    return
    
label mcdonalds_inicio:
    if desempregado:
        scene teste
        $idade = 18.2
        "James está com fome e vai ao McDonald's ao entrar no estabelecimento vê um cartaz de contratação."
        menu:
            protagonista"o que devo fazer?"

            "aceitar emprego no McDonalds":
                'James aceita a proposta e começa a trabalhar no Mcdonalds'
                $dinheiro += 10
                $felicidade -= 2
                $desempregado = False
            "Continuar procurando emprego":
                $dinheiro -= 2
    return

label decision_uni:
    scene thinking
    $idade = 21
    protagonista "Será que eu uso o dinheiro que eu guardei nos ultimos meses para começar uma faculdade ? "
    menu:
        "Começar uma graduação":
            
            call faculdade
        "Não é o momento certo":
            pass
    return

label ifood1:
    if desempregado:

        scene ifood
        'Caminhando na cidade James escutou que dá pra ganhar uma grana fácil virando entregador de ifood.'
        menu:
            "Tornar-se entregador do ifood":
                protagonista"peguei imprestada a bicicleta da minha irmã para virar entregador do ifood"
                $dinheiro +=10
                $felicidade -= 4    
                $desempregado = False

            "recusar":
                $dinheiro -= 2
                
    return

label jogo_do_bixo:
    scene jogo_bicho
    $ sorte = renpy.random.random()

    if sorte >= 0.9:
        $ dinheiro = dinheiro + 5000
        "Não acredito, eu ganheiii!"
    else:
        "perdi"
        $ dinheiro = dinheiro - 2000
    #passar um ano
    return

label faculdade:
    scene universidade
    protagonista"Qual curso devo fazer?"
    menu:
        "Ciências Contabeis":
            scene contabilidade
            $ciencias_contabeis = True
            $ciencia_computacao = False
            $curso_gastronomia = False


        "Sistemas de Informação":
            scene computing
            $ciencias_contabeis = False
            $ciencia_computacao = True
            $curso_gastronomia = False

        "Gastronomia":
            scene restaurante
            $ciencias_contabeis = False
            $ciencia_computacao = False
            $curso_gastronomia = True


        "Ciência da Computação":
            scene computing
            $ciencias_contabeis = False
            $ciencia_computacao = True
            $curso_gastronomia = False



    
    return 

label play_pong:

    window hide  
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

scene eileen_img
if _return == "eileen":

    e "Perdeu, Otário!"

else:

    e "Você ganhou, parabéns!"



#TODO: abaixo estão as escolhas sobre carreira que ainda não foram implementadas.


label covid_25:
    scene covid
    protagonista"não estou me sentindo muito bem, acho que contraí a nova variante da Covid-25"
    menu:
        "pedir para trabalhar de casa pro chefe":
            pass
            #mais dinheiro, menos saúde
            $dinheiro += 5
            $saude -=2
        "ir ao trabalho mesmo assim":
            pass
            # risco de contaminar o escritório com essa nova variante muito mais letal
            "Você contaminou o escritório todo com a sua nova variante, que por sinal é muito mais letal."
            "devido a complicações gerada pela covid-38 o seu chefe morre e você assume o lugar dele"
            #mais dinheiro , menos saúde
            $dinheiro += 5
            $saude -= 5
        "não trabalhar":
            pass
            #menos dinheiro, mais saúde, menos marcador de trabalho
            $dinheiro -= 5
            $saude +=2
            $trabalho -= 3

    return

label guru_investimento:
    scene guru_investimento
    "Você leu em um cartaz sobre um tal “Guru dos investimentos” , uma palestra paga, com o guru Gian Buffoni"
    menu:
        "Ir à palestra.":
            #menos dinheiro
            $dinheiro -= 10
            "Você aprendeu uma lição de vida: Gastar dinheiro na palestra do “guru do investimento” não é um bom investimento."
            
        "Ignorar.":
            pass
    return
