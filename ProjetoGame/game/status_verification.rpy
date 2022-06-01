label despesas(x):
    $despesa = despesa - x
    return despesa

label tempo(x):
    $ count = 1
    while count < x:
        $dinheiro = dinheiro - despesa + salario
        $count +=1
    return dinheiro

label status:
    if felicidade <= 0:
        jump morte_infelicidade #colocar aqui o final triste
        $sentinela = false
    elif saude <=0:
        jump morte_sem_saude# colocar aqui o ataque cardíaco
        $sentinela = false
    elif dinheiro <= 0:
        jump morte_sem_saude #colocar aqui o final sem dinheiro
        $sentinela = false
    else:
        return #aqui significa que o jogo pode continuar sem problema.




#colocar um trilha sonora triste nestas 3 primeiras
label morte_infelicidade:
    scene morte_felicidade
    "Você se enforcou na sua sala devido a sua depressão."
    $ renpy.full_restart()
label morte_sem_saude:
    scene morte_saude
    "Você teve uma parada cardíaca no trabalho devido ao alto estresse"
    $ renpy.full_restart()
label morte_sem_dinheiro:
    scene morte_pobre
    "Você foi à falência, sem dinheiro para pagar o aluguel ou comer teve que ir para às ruas. Em uma noite outro mendigo te esfaqueou até a morte para ficar com a sua barraca em baixo da ponte."
    $ renpy.full_restart()
