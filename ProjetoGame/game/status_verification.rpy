
init python: 

    def status():
        if felicidade <= 0:
            return #colocar aqui o final triste
        elif saude <=0:
            return # colocar aqui o ataque cardíaco
        elif dinheiro <= 0:
            return #colocar aqui o final sem dinheiro
        else:
            return #aqui significa que o jogo pode continuar sem problema.


    def despesas(x):
        despesa = despesa - x
        return despesa
    def tempo(x):
        for i in range(x):
            dinheiro = dinheiro - despesa + salario
        return dinheiro


#colocar um trilha sonora triste nestas 3 primeiras
label morte_infelicidade:
    scene morte_felicidade
    "Você se enforcou na sua sala devido a sua depressão."
label morte_sem_saude:
    scene morte_saude
    "Você teve uma parada cardíaca no trabalho devido ao alto estresse"

label morte_sem_dinheiro:
    scene morte_pobre
    "Você foi à falência, sem dinheiro para pagar o aluguel ou comer teve que ir para às ruas. Em uma noite outro mendigo te esfaqueou até a morte para ficar com a sua barraca em baixo da ponte."
    return