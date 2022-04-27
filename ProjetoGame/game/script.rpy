# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonista = Character("Fulano")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/Trilha.mp3" volume 0.2
    scene casa

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Fulano , teve uma infância difícil, nascido em uma família de baixa renda, incapaz de criá-lo, foi retirado da família e mandado para um orfanato aos 4 anos.
"
    scene orfanato
    "No orfanato Fulano passava o período da manhã aprendendo a ler e fazer contas básicas e no período da tarde podia brincar ou interagir com as outras crianças."
    scene kids
    "Fulano não se dava bem com as outras crianças mais velhas e durante 1 ano sofreu na mão delas, cansado de ser tratado do mesmo jeito, começou a se rebelar e brigar."
    scene orphanato
    "Todo ato de rebelião de fulano era denunciado à diretoria do orfanato e Fulano era castigado a passar o dia isolado das outras crianças e com poucos brinquedos à sua disposição, o que acabava deixando-o apenas mais frustrado."
    # This ends the game.
    return

#label background:
#    scene orphanato
    