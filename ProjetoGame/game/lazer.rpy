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
    menu:
        "Dizer ao chefe que você está doente e não poderá ir trabalhar":
            #50% de chance dele liberar

            #liberou
                #mais felicidade, um pouco menos no marcador de trabalho
            
            #não liberou
                "Infelizmente seu chefe disse que tem uma demanda urgente e precisa que você trabalhe de casa"
                menu:
                    "Trabalhar":
                        pass
                        #menos felicidade, um pouco mais no marcador de trabalho, mais dinheiro

                    "Dizer que não pode e ir à festa":
                        pass
                        #mais felicidade, muito menos no marcador de trabalho, menos dinheiro.
        "Pedir ao seu chefe para ser liberado um pouco mais cedo do trabalho":
            
            #50% de chance dele liberar
            
            #liberou
                #Um pouco mais de felicidade,um pouco menos no marcador de trabalho, Mais dinheiro
            #não liberou
                "Você decide que desobedecer seu chefe para ficar por pouco tempo na festa não valeria a pena."
                    
                #Menos felicidade, Mais marcador de trabalho, Mais dinheiro

        "Ignorar a festa e continuar trabalhando":
            pass
            #menos felicidade
            #mais marcador de trabalho 
            #mais dinheiro
    return

