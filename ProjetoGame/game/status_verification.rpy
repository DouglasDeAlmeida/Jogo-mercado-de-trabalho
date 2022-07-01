label despesas(x):
    $despesa = despesa - x
    return despesa

label tempo(x):
    $ count = 1
    
    while count <= x:
        $dinheiro = dinheiro - despesa + salario
        $trabalho += 5 #a cada ano empregado aumenta o marcador de trabalho
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
        jump morte_sem_dinheiro #colocar aqui o final sem dinheiro
        $sentinela = false
    else:
        return #aqui significa que o jogo pode continuar sem problema.


#colocar um trilha sonora triste nestas 3 primeiras
label morte_infelicidade:
    scene morte_felicidade
    play sound "audio/morte_infelicidade.mp3" volume som
    "Você se enforcou na sua sala devido a sua depressão."
    $ renpy.full_restart()
label morte_sem_saude:
    scene morte_saude
    play sound "audio/morte_saude.mp3" volume som
    "Você teve uma parada cardíaca devido ao alto estresse."
    $ renpy.full_restart()
label morte_sem_dinheiro:
    scene morte_pobre
    play sound "audio/morte_dinheiro1.mp3" volume som
    
    "Você foi à falência, sem dinheiro para pagar o aluguel ou comer teve que ir para às ruas. "
    play sound "audio/morte_dinheiro2.mp3" volume som
    "Em uma noite outro mendigo te esfaqueou até a morte para ficar com a sua barraca em baixo da ponte."
    $ renpy.full_restart()
