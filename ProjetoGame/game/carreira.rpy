
#TODO: fazer um marcador oculto de trabalho (confiança do seu atual chefe contigo)
label inicio_Carreira:
    scene thinking #imagem de fundo
    protagonista "Não consigo passar mais nem um minuto nessa casa, preciso de um lugar pra mim. Tenho um pouco de dinheiro que ganhei ajudando meu pai, entretanto, não é muito."
    menu:
        "Eu posso aceitar um emprego no McDonalds.":
            call mcdonalds1
            
        "Vou virar entregador do Ifood.":
            call ifood1
        "vou jogar no bixo":
            call jogo_do_bixo
            
        "Jogar ping pong":
            call play_pong
    scene clock1        
    "passaram-se 1 ano"
    call tempo(12)
    return

label decision_uni:
    scene thinking
    protagonista "Será que eu uso o dinheiro que eu guardei nos ultimos meses para começar uma faculdade ? "
    menu:
        "Começar uma graduação":
            
            call faculdade
        "Não é o momento certo":
            pass
    return


label mcdonalds1:
    scene teste
    'agora sou garçom'
    $ salario = 1500
    $ felicidade = felicidade - 2
    return

label ifood1:
    scene ifood
    'ifood'
    $ salario = 1200
    $ felicidade = felicidade - 4
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
    return

label faculdade:
    scene universidade
    protagonista"Qual curso devo fazer?"
    menu:
        "Ciências Contabeis":
            scene contabilidade
            #aqui seria bom registrar que ele fez esta escolha 
        "Sistemas de Informação":
            scene computing
            #aqui seria bom registrar que ele fez esta escolha 
        "Gastronomia":
            scene restaurante
            #aqui seria bom registrar que ele fez esta escolha 
        "Ciência da Computação":
            scene computing
            #aqui seria bom registrar que ele fez esta escolha 
    $despesa = despesa + 250
    call tempo(12)
    "fim da faculdade (APAGAR DEPOIS)"
    
    return 

label play_pong:

    window hide  
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

scene eileen_img
if _return == "eileen":

    e "Perdeu Otário!"

else:

    e "Você ganhou, parabens!"



#TODO: abaixo estão as escolhas sobre carreira que ainda não foram implementadas.

label palestra_tecnologia:
    scene conferencia_tec
    "Você leu em um cartaz sobre uma palestra de tecnologia paga"
    
    menu:
        "participar":
            #mais educação
            #menos dinheiro
            $dinheiro -= 1000
            pass
        "recusar":
            pass

label covid_38:
    protagonista"não estou me sentindo muito bem, acho que contraí a nova variante da Covid-38"
    menu:
        "pedir para trabalhar de casa pro chefe":
            pass
            #mais dinheiro, menos saúde
        "ir ao trabalho mesmo assim":
            pass
            # risco de contaminar o escritório com essa nova variante muito mais letal
            "Você contaminou o escritório todo com a sua nova variante, que por sinal é muito mais letal."
            "devido a complicações gerada pela covid-38 o seu chefe morre e você assume o lugar dele"
                #mais dinheiro , menos saúde
        "não trabalhar":
            pass
            #menos dinheiro, mais saúde, menos marcador de trabalho

    return

label guru_investimento:
    "Você leu em um cartaz sobre um tal “Guru dos investimentos” , uma palestra paga, com o guru Gian Buffoni"
    menu:
        "Ir à palestra.":
            #menos dinheiro
            $dinheiro -= 1000
            "Você aprendeu uma lição de vida: Gastar dinheiro na palestra do “guru do investimento” não é um bom investimento."
            pass
        "Ignorar.":
            pass
