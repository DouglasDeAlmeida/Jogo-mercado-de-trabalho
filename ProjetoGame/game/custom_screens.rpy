screen hbox_screen:


    hbox:
        xalign 1.0

        yalign 0.01
        spacing 10

        #text "dinheiro: [dinheiro] " color "#da1e1e" 
        #text "felicidade: [felicidade] " color "#da1e1e" 
        #text "saúde: [saude] " color "#da1e1e" 
        text "Idade: [idade] " color "#da1e1e" 



screen barraAmizade:
    frame:
        hbox:
            spacing 2
            vbox:
                spacing 1
                text "Felicidade" size 20

                #$ ui.vbar(100, felicidade, xmaximum=5, ymaximum=200, top_bar=Frame("images/screens/top.png", 25, 25), bottom_bar=Frame("images/screens/bottom.png", 25, 25), xalign=0.5, yalign=0.5)
                $ui.bar(100, felicidade, xmaximum=200, ymaximum=2, right_bar=Frame("images/screens/right.png", 25, 25), left_bar=Frame("images/screens/left.png", 25, 25), xalign=0.5, yalign=0.5)
                text "Saúde" size 20
                $ ui.bar(100, saude, xmaximum=200, ymaximum=2, right_bar=Frame("images/screens/right.png", 25, 25), left_bar=Frame("images/screens/left.png", 25, 25), xalign=0.5, yalign=0.5)
                text "Dinheiro" size 20
                $ ui.bar(100, dinheiro, xmaximum=200, ymaximum=5, right_bar=Frame("images/screens/right.png", 10, 10), left_bar=Frame("images/screens/left.png", 10, 10), xalign=0.5, yalign=0.5)

        
                
