define felicidade = 50 #vão de 0-100
define saude = 50 #0-100
define dinheiro = 4000
define despesa = 1000
define salario = 0

label inicio_Carreira:
    scene thinking
    protagonista "Não consigo passar mais nem um minuto nessa casa, preciso de um lugar pra mim. Tenho um pouco de dinheiro que ganhei ajudando meu pai, entretanto, não é muito."
    menu:
        "Eu posso aceitar um emprego no McDonalds.":
            call mcdonalds1
            
        "Vou virar entregador do Ifood.":
            call ifood1
        "vou jogar no bixo":
            call jogo_do_bixo
            pass

    "passaram-se 1 ano"
    #call tempo(12)
    scene thinking
    protagonista "Será que eu uso o dinheiro que eu guardei nos ultimos meses para começar uma faculdade ? "
    menu:
        "Começar uma graduação":
            pass
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
    scene deliveryman
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
    $despesa = despesa + 200



label status:
    if felicidade <= 0:
        return #colocar aqui o final triste
    elif saude <=0:
        return # colocar aqui o ataque cardíaco
    elif dinheiro <= 0:
        return #colocar aqui o final sem dinheiro
    else:
        return #aqui significa que o jogo pode continuar sem problema.


label despesas(x):
    $despesa = despesa - x
    return 

init python: 
    def tempo(x):
        for i in range(x):
            dinheiro = dinheiro - despesa + salario
        return dinheiro