define casado = False
define namorando = False


label tinder:
    scene thinking
    
    "estou me sentindo solitário, será que devo baixar um aplicativo de relacionamentos?"
    menu:
        "baixar o tinder!":
            call gabriela
        "não baixar":
            pass
    return


label gabriela:
    scene namorada
    
    "Gabriela a mulher que você encontrou através do Tinder disse que a menstruação dela está atrasada"
    scene pregnant
    menu:
    
        "Pedir para ela fazer um aborto":
            "Ela é uma pessoa conservadora e achou sua ideia absurda, ela não só terá a criança como ainda ficou puta contigo"
            
        "Ter o bebê":
            pass
    scene baby  
    "Nove meses depois nasce a filhinha de James"
          
    $dinheiro -= 15
    return

label amor_de_escritorio:
    scene trabalho_olhar
    "a Amanda, sua colega de trabalho, não para de olhar e sorrir para você além de ser sempre muito simpática. Você acha que ela tem uma queda por ti."
    menu:
        "Convidá-la para um encontro":
            "Ela aceita e em pouco tempo os dois iniciam um namoro"
            $felicidade += 5 
            pass
        "Continuar na sua":
            pass
    return

label affair:
    scene traicao
    "James descobre que sua esposa está o traindo com o professor de tênis dela"
    menu:
        "pedir divórcio":
            $felicidade -= 15
            pass
        "perdoar ela":
            $felicidade -= 10
            pass

    return


label cinco_anos:
    if namorando == True:
        scene casamento
        centered "Hoje James completa 5 anos de namoro, ele sente que sua namorada está esperando que ele a peça em casamento"
        menu:
            "Pedi-la em casamento":
                $felicidade += 5
                $dinheiro -= 5
                $casado = True
                pass
            "Falar que você não esta pronto pra abrir mão do sexo":
                "Sua namorada termina com você e procura alguém que queira casar com ela"
                $felicidade -= 10
    return


label vegas:
    if casado == True:
        scene casino
        "James e sua esposa viajam para las vegas junto com seus amigos, lá eles resolvem aproveitar ao máximo a experiência, vão para cassinos, bebem muito e fazem diversas loucuras"
        "No mês seguinte casal descobre que conceberam um bebê nessa viagem. A esposa de James está grávida e mais 8 meses depois nasce o bebê"
        scene baby
        $dinheiro -= 15
    return
    #scene casamento
    #
