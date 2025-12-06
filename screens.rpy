# screens.rpy - simple emotion HUD
screen emotion_hud():
    frame:
        xalign 0.98
        yalign 0.02
        has vbox
        text "Эмоции:"
        bar value VariableValue("calmness", 100) range 100
        bar value VariableValue("vulnerability", 0) range 100
        bar value VariableValue("willpower", 50) range 100
