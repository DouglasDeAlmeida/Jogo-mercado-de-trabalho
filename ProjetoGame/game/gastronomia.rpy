label inicio_gastronomia:
    $idade = 24
    scene cozinha
    "James conseguiu uma oportunidade para cozinhar num restaurante de pequeno porte, porém nesse estabelecimento, James vai ficando estressado pois trabalha muitas horas por dia e recebe pouco"
    $salario = 2000
    $dinheiro += 5
    $felicidade -= 5
    $trabalho += 5
    return


label jacquin:
    scene jacquin
    "O chef Jacquin  do “pesadelo na cozinha”  veio avaliar o restaurante em que James trabalha."
    #colocar aqui o minigame
    if win:
        "Jacquin gostou da comida e lhe dá uma estrela michelin. "
        jump final_feliz_gastronomia
    else:
        "Jacquin te chama de incopetente e dedica um episódio completo de seu programa para criticar o seu restaurante"
        "O restaurante é fechado e todos foram demitidos, incluindo James."
        jump morte_sem_dinheiro

    return
label amigo_influencer:
    scene amigo_influencer1
    "Os negócios estão lento, checando as redes sociais, você repara um nome familiar e descobre que um dos seus amigos da escola virou um famoso influencer. "
    "Você entra em contato e pede para que ele venha ao seu restaurante e grave uma review."
    scene amigo_influencer2
    "Michel vem ao seu restaurante e não fica impressionado com a comida, porém diz que sua opinião pode ser facilmente influenciada."

    menu:
        "subornar ele":
            $dinheiro -= 25
            $trabalho += 35
        "pedir que seu amigo pague a conta e se retire.":
            "Seu amigo bravo da forma que foi tratado dá um chilique na rede social dizendo que é um crime esse restaurante ainda estar aberto.
            Seu chefe ao descobrir que você ferrou com a reputação do restaurante lhe expulsa do estabelecimento.
            "
            $dinheiro = 0
            jump morte_sem_dinheiro
    return


label preparo_prato:
    scene prato
    "James estava com problemas no preparo de um prato, uma outra cozinheira vendo sua dificuldade ficou com pena e preparou o seu pedido sozinha sem os outros verem. 
    O cliente que recebeu o prato gostou muito da comida e pediu para o garçom chamar o chef para parabenizá-lo."
    $felicidade+=5
    $trabalho += 5
    return


label ratatouille:
    scene rato
    "Você estava quase terminando de preparar uma sopa e decidiu ir ao banheiro enquanto esperava ela esquentar.
    Quando você volta para sua estação, vê um rato largando diversos ingredientes na sopa."
    menu:
        protagonista "o que farei com o rato?"

        "Matar o rato e jogar a sopa fora":
            "Você acaba fazendo uma confusão tentando matar o rato chamando a atenção do seu chefe , no momento que o seu chefe chega na cozinha ele vê você jogando a sopa no lixo e fica frustrado e desconta o preço da sopa do seu salário."
            $dinheiro -= 50
            $trabalho -= 1
        "Fingir que nada aconteceu e entregar a sopa ao garçom.":
            scene rato2
            "Os clientes reclamam de que a sopa está com gosto horrível, pagam pela comida mas reclamam com o chefe e criticam o restaurante nas redes sociais. Consequentemente seu chefe fica frustrado com a sua incapacidade de preparar uma sopa."
            $trabalho -=5
        "Curioso com o comportamento do rato e se sentindo inspirado em um filme, você tenta colocá-lo debaixo do seu chapéu de cozinheiro e deixa ele te guiar.":
            "Ao ver você se aproximando o rato tenta correr, você consegue pegar o rato mas em sua perseguição causou uma bagunça, derrubando diversos instrumentos de cozinha, seu chefe ao escutar o barulho vai em direção a cozinha." 
            "Ao chegar na cozinha seu chefe lhe vê tentando botar um rato na cabeça, em choque com a situação James apertou o rato que está em sua mão, em resposta, o rato morde a sua mão e sai correndo."
            "Seu chefe briga com você e te inscreve em um hospital psiquiátrico, além disso o rato lhe infectou com hantavírus (ou Peste bubônica), uma doença incurável."
            $trabalho -= 10
            $saude -= 20
            $dinheiro -= 1000
            $felicidade -= 50
    return


label bom_trabalho:
    #TODO: IMAGEM
    if trabalho >= 40:
        "Devido ao seu esforço você recebeu uma oportunidade de trabalho em um restaurante de luxo"
        $salario = 5000
        $felicidade += 5
    return

label waitress:
    scene garconete
    protagonista"Acho que a Julia, a garçonete, está afim de mim, ela não vive me olhando e sempre puxa papo comigo."
    menu:
        "Dar em cima da garçonete":
            "Acontece que ela estava apenas sendo educada. Sua atitude irritou Julia e ela te denunciou pro gerente, pois achou seu comportamento inadequado"
            $felicidade -= 5
            $trabalho -= 5
        "não fazer nada":
            pass
    return

label compras_restaurante:
    scene comprar_ingredientes
    "James foi comprar comida para o restaurante com o budget de seu chefe"      
    menu:
        "Comprar ingredientes mais baratos e manter o dinheiro que sobrar para si mesmo":
            "Uma família inteira de clientes ficou com caganeira por causa de um prato que James  fez, eles entraram com um processo no restaurante.
            O restaurante perde dinheiro e o dono desconta tudo no salário de James.
            "
            $dinheiro -= 10000
            if trabalho <= 30:
                "Você foi demitido"
                jump morte_sem_dinheiro
        "Gastar todo o dinheiro em ingredientes mais caros":
            $trabalho +=5
    return



label promotion_chef:
    "Devido ao seu bom trabalho você foi promovido a chef"
    $salario = 20000
    $felicidade += 20
    return


#Continuação de um evento do cenário neutro
label restaurant_automation:
    #Em um evento futuro, o restaurante onde James trabalha passa por um processo de automação. Dependendo de como está o marcador de trabalho,
    # James pode ser substituído pela máquina e ser demitido (fim de jogo)  ou ser um dos únicos funcionários que continuará trabalhando no estabelecimento.
    #scene automation_gastro





label final_feliz_gastronomia:
    "James torna-se um chef de um grande restaurante, conhecido no país inteiro, considerado um dos melhores de sua profissão"
    #TODO: adicionar imagem
    play music "audio/audio_vitoria.mp3" volume 0.8
    $ renpy.full_restart()
