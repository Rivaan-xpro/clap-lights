def on_sound_loud():
    global lightsOn
    lightsOn = not (lightsOn)
    if lightsOn:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        basic.clear_screen()
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

lightsOn = False
input.set_sound_threshold(SoundThreshold.LOUD, 150)

def on_forever():
    pass
basic.forever(on_forever)
