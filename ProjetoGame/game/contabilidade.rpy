label estagio:
    scene estagio_contabilidade
    "James recebe uma proposta de estágio interessante para trabalhar no setor de contabilidade em uma empresa de papéis chamada Dunder Mifflin, ele se interessa pelo cargo e aceita a proposta."
    return

label misto:
    scene misto
    "James decidiu fazer um misto-quente na chapa durante o seu intervalo do trabalho, 
    mas de repente o seu chefe entrou na cozinha oferecendo lições de vida para crescer na carreira baseado na experiência que ele teve." 
    $idade = 24
    menu:
        "aceitar os ensinamentos do chefe":
            scene misto2
            " Você se realiza que não agregou nada do que o chefe te disse, e ouve sirene tocando dentro do edifício, que acabou causando um incêndio devido a chapa ligada"
            
            $felicidade -= 5
            $trabalho -= 5
        "recusar os ensinamentos do chefe":
            "Você volta ao trabalho para finalizar os treinamentos obrigatórios enquanto come o misto-quente que fez"
            $saude += 5
    return
label raiva:
    scene raiva1
    "Uma funcionária da empresa de James foi mordida por um morcego e precisou tomar uma vacina anti-rábica, então, 
    o chefe de James tem a ideia de organizar com o pessoal do escritório uma corrida beneficente contra raiva humana (apesar de ser uma doença praticamente extinta)"
    $idade = 26
    menu:
        "Não participar da corrida, pois não vê necessidade nela":
            "Seu chefe não gostou de sua atitude"
            $trabalho -= 5
        "Participar da corrida só para não desagradar seu chefe":
            scene raiva2
            "James havia acabado de almoçar e foi correr de estômago cheio, no meio da corrida ele começa a passar mal e vomitar"
            $saude -= 3
            $trabalho += 5
    return
label excedente:
    scene estagio_contabilidade2
    "James percebeu que o escritório deve gastar um excedente de 10.000 ou poderá perder este dinheiro no próximo orçamento do ano, sendo que apenas ele sabe disso."
    $idade = 29
    menu:
        protagonista"O que devo fazer"
        " Informar ao chefe que o escritório tem um excedente.":
            "O chefe agradece por ter reparado nesse detalhe e compra uma copiadora nova para o escritório usando o excedente"
            $trabalho += 15
        "Desviar o excedente para a minha conta corrente":
            "Você foi pego no mês seguinte pois o seu colega de trabalho de contábeis percebeu esse detalhe"
            $trabalho -= 20
            $dinheiro -= 10
            $felicidade -= 10
    return

label cupom_dourado:
    scene cupom
    "James teve uma ideia para tentar alavancar as vendas de sua empresa: colocar um cupom dourado dentro de um pacote de papéis aleatório, e quem comprar esse pacote específico garante 50 por cento de desconto na compra de novos papéis da empresa durante 1 ano."
    "James chega a comentar a ideia com Jim, seu colega de trabalho, porém tem medo de que a ideia acabe dando errado dependendo de qual cliente consiga o cupom (se for um dos principais clientes da empresa, eles podem acabar tendo prejuízo ao invés de lucro)"
    $idade = 31
    menu:
        "Persistir com a ideia e contá-la para seu chefe":
            "seu chefe gostou da ideia do bilhete e implementou. A ideia foi um sucesso e a empresa lucrou bastante. Seu chefe decide aumentar seu salário para 20 por cento a mais que o atual"
            $dinheiro = dinheiro * 1.2
            $felicidade += 10
            $trabalho += 20
        "Desistir da ideia":
            "Seu colega Jim te passa a perna e conta pro chefe a ideia do cupom como se fosse dele, a ideia dá certo e ele recebe os créditos no seu lugar, você fala pro chefe que a ideia é sua, porém ele não acredita em você"
            $felicidade -= 5
    return 

label demissao:
    scene contabilidade_empresa
    $idade = 34
    "A empresa de James está passando por dificuldades financeiras e precisará demitir um funcionário para equilibrar as despesas. Kevin, colega de James da área de contabilidade, é um péssimo contador e tem dificuldade de resolver até problemas de matemática básica."
    menu:
        "Indicar Kevin para ser demitido":
            "Seu chefe segue sua indicação e resolve demitir Kevin. Ele por sua vez descobre que você o indicou para ser demitido, e antes de embora conta para o chefe sobre todas as vezes que você fingiu estar doente para não ir trabalhar"
            $felicidade -= 5
            $trabalho -= 5
        "Ficar na sua e não influenciar na decisão":
            pass
    return

label doente_para_reuniao:
    scene reuniao_contabilidade
    $idade = 36 
    "James está doente porém hoje foi marcada uma reunião importante, junto com os chefes e outros funcionários sobre o futuro da empresa."
    menu:
        "ir à reunião":
            "James vai a reunião e debate com seus funcionários o futuro da empresa, depois de muito bater boca, James tem um plano de como melhorar os lucros da empresa. Inclusive, seu chefe resolve adotar sua ideia ,porém, no meio do debate James desmaia e é levado ao hospital."
            " Após uma semana, James acorda, ele estava com um problema de pressão e o nervosismo da reunião exaltou este problema. O hospital lhe cobra caro pelo atendimento."
            $saude -= 15
            $felicidade -= 5
            $trabalho += 15
            $dinheiro -= 15
        "Ir para o hospital":
            "James vai para o hospital, o médico diz que é um problema de pressão básica, lhe receita um remédio caro e lhe manda pra casa."
            "Na empresa, um dos funcionários sugere usar o capital da empresa para investir em criptomoedas, o chefe adota a ideia  e sem saber o que está fazendo quebra a cara. "
            $saude += 10
            $dinheiro -= 5
            $trabalho -= 5
    return
label aposentadoria_chefe:
    $idade = 34 #TODO: alterar essa idade
    scene demitido
    "O chefe de James se aposentou e saiu do cargo, a empresa está procurando alguem para substituí-lo"
    if trabalho >= 50:
        "Devido ao seu bom trabalho James foi promovido a gerente"
        $dinheiro += 25
        $felicidade += 10
    else:
        "James é visto como alguem que não tem muito comprometindo com o trabalho, por isso, não conseguiu a vaga de gerente."
        $felicidade -= 10
    return
label evento_final_contabilidade:
    $idade += 4
    scene amigo_pesquisa
    centered "A empresa em que James trabalha está falindo."
    "James tem uma última carta na manga, ele usa todos os recursos da empresa na tentativa de reinventá-la para que a empresa se encaixe nos tempos modernos."
    "Ele tenta implementar um site para vender papéis online de forma automática e eficaz. E ele precisa contratar profissionais de TI para isso, mesmo com a empresa não tendo verba para contratar novas pessoas naquele momento."
    #TODO: colocar minigame aqui
    call play_pong
    if perdeu_minigame:
        
        scene amigo_pesquisa
        centered "{size=+100}A empresa faliu.{/size}"
        "Os funcionários recolhem seus pertences, em uma cena horrível, alguns saem chorando, outros tem ataque de pânico, com medo de não ter o que comer no amanhã."
        "Os funcionários mais próximos de James batem boca com ele, afirmando que ele é o culpado pelo fracasso da empresa, seu funcionário mais leal nem olha na cara de James ao sair"
        "O dia se passa, mas o evento repercute, toda noite James rememora o evento,  o dinheiro não lhe ameniza a culpa."
        centered "Embora financeiramente estável, James viverá para sempre com culpa das suas escolhas."
        jump morte_infelicidade
    else:
        scene james_ceo
        play music "audio/audio_vitoria.mp3" volume 0.8
        centered "Com a ajuda de James a empresa continua de pé."
        
        "Todos os funcionários aplaudem James, seu funcionário mais leal, lhe dá um abraço, James continua a trabalhar na empresa por mais um tempo e depois se aposenta.
        Nesse dia a equipe faz um bolo para James e todos festejam, não só isso mas o chefe da empresa, Michael, vem dos EUA para o Brasil apenas para parabenizar James."
        "Michael tira uma foto de James e faz um mural na parede da empresa imortalizando James como o melhor gerente da empresa."
        
        centered "James conseguiu se tornar financeiramente estável, e vive a vida feliz com suas conquistas."

        $ renpy.full_restart()