label tinder:
    scene thinking
    
    "estou me sentindo solitário, será que devo baixar um aplicativo de relacionamentos?"
    menu:
        "baixar o tinder!":
            call gabriela
        "não baixar":
            pass


label gabriela:
    scene namorada
    
    "Gabriela a mulher que você encontrou através do Tinder disse que a menstruação dela está atrasada"
    scene pregnant
    menu:
    
        "Pedir para ela fazer um aborto":
            "Ela é uma pessoa conservadora e achou sua ideia absurda, ela não só terá a criança como ainda ficou puta contigo"
            
        "Ter o bebê":
            scene baby
            pass
    return

label amor_de_escritorio:
    "a Amanda não para de olhar e sorrir para você além de ser sempre muito simpática. Você acha que ela tem uma queda por ti."
    menu:
        "Convidá-la para um encontro":
            pass
        "Continuar na sua":
            pass


label affair:
    "James descobre que sua esposa está o traindo com o professor de tênis dela"
    menu:
        "pedir divórcio":
            $felicidade -= 15
            pass
        "perdoar ela":
            $felicidade -= 10
            pass