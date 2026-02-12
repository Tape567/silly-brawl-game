@namespace
class SpriteKind:
    UI = SpriteKind.create()
    Weapon = SpriteKind.create()
    HealBullet = SpriteKind.create()
    DrillSuper = SpriteKind.create()
    Obelisk = SpriteKind.create()
    EnemyBullet = SpriteKind.create()
@namespace
class StatusBarKind:
    Ammo = StatusBarKind.create()
    SuperAmmo = StatusBarKind.create()
    ObeliskHealth = StatusBarKind.create()
"""

Visit this link for game development log and details.

https://forum.makecode.com/t/sneak-peek-announcements-remix-of-shape-smasher/40572

(You may have to copy and paste...)

"""
def BodySelect():
    global SelectionMenuBodiesArray, TempNumber, SelectionMenuBodies, SelectionMenuCombinationSprite, SelectionMenuText
    game.set_dialog_frame(img("""
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 5
        1 f f f f f f f f f f f f f 1
        1 f f f f f f f f f f f f f 1
        1 f f f f f f f f f f f f f 1
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """))
    SelectionMenuBodiesArray = []
    TempNumber = 0
    for index in range(len(BodyNamesArray)):
        SelectionMenuBodiesArray.append(miniMenu.create_menu_item(BodyNamesArray[TempNumber], BodyImagesArray[TempNumber]))
        TempNumber += 1
    SelectionMenuBodies = miniMenu.create_menu_from_array(SelectionMenuBodiesArray)
    SelectionMenuBodies.set_frame(assets.image("""
        MenuFrame
        """))
    SelectionMenuBodies.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.BACKGROUND,
        15)
    SelectionMenuBodies.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.FOREGROUND,
        9)
    SelectionMenuBodies.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.BACKGROUND,
        9)
    SelectionMenuBodies.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.FOREGROUND,
        1)
    SelectionMenuBodies.set_menu_style_property(miniMenu.MenuStyleProperty.SCROLL_INDICATOR_COLOR, 9)
    SelectionMenuBodies.set_menu_style_property(miniMenu.MenuStyleProperty.ROWS, 4)
    SelectionMenuBodies.set_menu_style_property(miniMenu.MenuStyleProperty.COLUMNS, 1)
    SelectionMenuBodies.set_menu_style_property(miniMenu.MenuStyleProperty.USE_AS_TEMPLATE, 1)
    
    def on_button_pressed(selection, selectedIndex):
        global _1Body
        _1Body = selectedIndex
        SelectionMenuCombinationSprite.image.draw_transparent_image(BodyImagesArray[selectedIndex], 0, 24)
        SelectionMenuBodies.close()
        pause(5)
        WeaponSelect()
    SelectionMenuBodies.on_button_pressed(controller.A, on_button_pressed)
    
    
    def on_button_pressed2(selection2, selectedIndex2):
        game.show_long_text("" + selection2 + "/ " + str(BodyHealthArray[selectedIndex2]) + " HP, " + str(BodySpeedArray[selectedIndex2]) + " SPD.        " + BodyDescriptionsArray[selectedIndex2],
            DialogLayout.CENTER)
    SelectionMenuBodies.on_button_pressed(controller.B, on_button_pressed2)
    
    SelectionMenuBodies.set_position(81, scene.screen_height() / 2)
    SelectionMenuCombinationSprite = sprites.create(assets.image("""
            CombinationImage
            """),
        SpriteKind.UI)
    SelectionMenuCombinationSprite.set_position(140, 60)
    SelectionMenuText = textsprite.create("Select your body!", 0, 9)
    SelectionMenuText.set_position(80, 8)
# Take a look at the upcoming theme menu's code. The full version will be realeased soon!
def Themes():
    global Thememenu
    SelectionMenuGamemode.x += 200
    SelectionMenuGamemode.set_button_events_enabled(False)
    Thememenu = miniMenu.create_menu(miniMenu.create_menu_item("Basic Black"),
        miniMenu.create_menu_item("LowFi Circles"),
        miniMenu.create_menu_item("Early Background release"),
        miniMenu.create_menu_item("Back"))
    Thememenu.set_title("Themes")
    Thememenu.set_frame(assets.image("""
        MenuFrame0
        """))
    Thememenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.BACKGROUND,
        15)
    Thememenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.FOREGROUND,
        2)
    Thememenu.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.BACKGROUND,
        2)
    Thememenu.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.FOREGROUND,
        1)
    
    def on_button_pressed3(selection3, selectedIndex3):
        global Themeselection
        if selection3 == "Basic Black":
            Themeselection = 0
            game.splash("Set")
        elif selection3 == "LowFi Circles":
            Themeselection = 1
            game.splash("Set")
        elif selection3 == "Early Background release":
            Themeselection = 2
            game.splash("Set")
        elif selection3 == "Back":
            sprites.destroy(Thememenu)
            SelectionMenuGamemode.x += -200
            SelectionMenuGamemode.set_button_events_enabled(True)
        else:
            pass
    Thememenu.on_button_pressed(controller.A, on_button_pressed3)
    
def DefineShape(Image2: Image, Health: number, Speed: number, Name: str, BodyDescription: str, WeaponDescription: str):
    BodyImagesArray.append(Image2)
    BodyHealthArray.append(Health)
    BodySpeedArray.append(Speed)
    BodyNamesArray.append(Name)
    BodyDescriptionsArray.append(BodyDescription)
    WeaponDescriptionsArray.append(WeaponDescription)
def WeaponSelect():
    global SelectionMenuWeapons
    SelectionMenuWeapons = miniMenu.create_menu_from_array(SelectionMenuBodiesArray)
    SelectionMenuWeapons.set_frame(assets.image("""
        MenuFrame
        """))
    SelectionMenuWeapons.set_position(81, scene.screen_height() / 2)
    SelectionMenuText.set_text("Select a Weapon.")
    
    def on_button_pressed4(selection4, selectedIndex4):
        global _1Weapon
        _1Weapon = selectedIndex4
        SelectionMenuCombinationSprite.image.draw_transparent_image(BodyImagesArray[selectedIndex4], 0, 0)
        SelectionMenuWeapons.close()
        Confirmation()
    SelectionMenuWeapons.on_button_pressed(controller.A, on_button_pressed4)
    
    
    def on_button_pressed5(selection5, selectedIndex5):
        game.show_long_text("" + selection5 + "           " + WeaponDescriptionsArray[selectedIndex5],
            DialogLayout.CENTER)
    SelectionMenuWeapons.on_button_pressed(controller.B, on_button_pressed5)
    
def EnemyFactory(EnemyID: number):
    global _3Enemy, _3EnemyHealthBar
    _3Enemy = sprites.create([assets.image("""
                myImage20
                """),
            assets.image("""
                myImage19
                """),
            assets.image("""
                EnemyTri
                """),
            assets.image("""
                myImage18
                """),
            assets.image("""
                EnemyCross
                """)][EnemyID],
        SpriteKind.enemy)
    sprites.set_data_number(_3Enemy, "Damage", [5, 10, 10, 15, 0][EnemyID])
    sprites.set_data_number(_3Enemy, "Speed", [60, 75, 0, 45, 30][EnemyID])
    _3Enemy.follow(_3PlayerBody, sprites.read_data_number(_3Enemy, "Speed"))
    if _1Gamemode == 2:
        _3Enemy.follow(_3Obelisk,
            max(sprites.read_data_number(_3Enemy, "Speed") / 1.5, 30))
    _3EnemyHealthBar = statusbars.create(30, 5, StatusBarKind.enemy_health)
    _3EnemyHealthBar.set_color(2, 15)
    _3EnemyHealthBar.set_bar_border(1, 2)
    _3EnemyHealthBar.max = [100, 20, 100, 300, 10][EnemyID]
    _3EnemyHealthBar.value = _3EnemyHealthBar.max
    _3EnemyHealthBar.attach_to_sprite(_3Enemy)
    sprites.set_data_number(_3Enemy, "EnemyID", EnemyID)
    sprites.set_data_boolean(_3Enemy, "HitRecently", False)
    _3Enemy.fx = 200
    _3Enemy.fy = 200
    if EnemyID == 3:
        _3Enemy.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    tiles.place_on_random_tile(_3Enemy, assets.tile("""
        EnemySpawn
        """))

def on_b_pressed():
    if _1GameStarted:
        if blockSettings.read_string("SaveControls") == "Mobile":
            SuperAtacj()
            
            def on_background():
                music.play(music.create_sound_effect(WaveShape.NOISE,
                        1,
                        5000,
                        255,
                        255,
                        500,
                        SoundExpressionEffect.NONE,
                        InterpolationCurve.LINEAR),
                    music.PlaybackMode.UNTIL_DONE)
            timer.background(on_background)
            
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Startscreen():
    
    def on_background2():
        pass
    timer.background(on_background2)
    
    scene.set_background_image(img("""
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111111111fffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111111111111fffffffffffffff111111fffffff11111fffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff1111111ffffffffffffffffffffffffffffffff111111111ffffffffffff11111111111111ff11111ffffff111111fffffff111111fffffffffffff111111111ffffffffffffff
        ffffffffff11111111111111111fffffffffffffffffffffffffff11111111111111fffffff111111111111111111f11111fffffff11111fffff11111111ffffffffffff1111111111ffffffffffffff
        ffffffffff1111111111111111111fffffffffffffffffffffffff111111111111111fffff1111111111111111111111111fffffff11111fffff11111111ffffffffffff1111111111ffffffffffffff
        ffffff11111111111111111111111fffffffff11111111ffffffff1111111111111111ffff111111111f1111111111111111ffffff11111fffff11111111fffffffffff11111111111ffffffffffffff
        ffffff111111111111111111111111ffffff1111111111111fffff1111111111111111ffff111111ffffff11111111111111fffff111111ffff1111111111ffffffffff11111111111ffffffffffffff
        ffffff111111111111111111111111ffff1111111111111111ffff1111111f11111111ffff111111ffffffff111111111111fffff111111ffff1111111111ffffffffff1111111ffffffffffffffffff
        ffffff111111fffffffffff1111111fff111111111111111111fff11111fffff111111ffff11111ffffffffff11111111111ffff1111111fff111111111111f11111fff1111111ffffffffffffffffff
        ffffff111111fffffffffff1111111fff1111111111111111111ff11111ffffff11111ffff11111ffffffffff11111f111111fff1111111fff111111111111111111fff1111111ffffffffffffffffff
        ffffff111111fffffff11111111111f1111111111111111111111f11111fffff111111fff111111fffffffff111111f111111fff111111ffff111111111111111111fff1111111ffffffffffffffffff
        ffffff111111f11111111111111111f111111111fffff11111111f11111fff11111111fff111111fffffffff111111f111111fff111111ffff111111111111111111fff1111111ffffffffffffffffff
        fffffff11111f1111111111111111111111111fffffff11111111f11111f1111111111fff111111fffffffff111111f111111ff111111ffff1111111111111111111fff1111111ffffffffffffffffff
        fffffff11111f1111111111111111f111111fffffffffff111111f1111111111111111fff111111fffffffff111111ff11111ff111111ffff111111111111111111fffff111111ffffffffffffffffff
        fffffff11111f11111111111111ff1111111ffffffffffff11111f111111111111111ffff11111fffffffff111111fff11111ff111111ffff111111fff111111ffffffff111111ffffffffffffffffff
        fffffff11111f1111111111ffffff1111111fffffffffff111111f111111111111111ffff11111ffffffff1111111fff1111111111111fff1111111fff111111ffffffff111111ffffffffffffffffff
        fffffff111111111111111ffffff1111111ffffffffffff111111f1111111111111111fff11111ffffffff1111111fff111111111111fff1111111fffff11111ffffffff111111ffffffffffffffffff
        fffffff111111111111111ffffff1111111ffffffffffff111111f1111111111111111fff11111fffffff11111111fff111111111111fff1111111fffff11111ffffffff111111ffffffffffffffffff
        fffffff111111f111111111fffff111111fffffffffffff111111f1111111111111111fff11111fffffff1111111ffff111111111111fff1111111ffffffffffffffffff1111111ffffff11111ffffff
        fffffff1111111ff11111111ffff111111fffffffffffff11111ff1111111111111111fff11111ffffff1111111ffffff1111111111ffff111111fffffffffffffffffff111111111111111111ffffff
        ffffffff111111fff111111111ff11111ffffffffffffff11111ff11111ffffff11111fff11111ffffff1111111ffffff1111111111ffff111111fffffffffffffffffff111111111111111111ffffff
        ffffffff111111fff1111111111f11111ffffffffffffff11111ff11111ffffff11111fff11111fffff1111111fffffff1111111111ffff111111ffffffffffffffffffff11111111111111111ffffff
        ffffffff111111ffff111111111f11111fffffffffffff111111ff11111ffffff11111fff111111fff11111111ffffffff11111111fffffffffffffffffffffffffffffff11111111111111111ffffff
        fffffffff11111fffff11111111111111ffffffffffff1111111ff11111fffff111111fff1111111f11111111ffffffffff1111111fffffffffffffffffffffffffffffffff11111111111111fffffff
        fffffffff11111ffffff1111111111111ffffffffffff1111111ff11111fffff111111fff1111111111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffff1111111ffffffffff
        fffffffff111111fffffff111111111111ffffffffff11111111ff111111fff1111111fff111111111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111111fffffff1111111111111fffffffff1111111fff111111ff11111111ffff1111111111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111111ffffffff111111111111ffffffff1111111ffff111111f11111111ffffff111111111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111111fffffffff111111111111fffffff1111111ffff111111111111111fffffff111111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111111ffffffffff1111111111111fff11111111ffffff1111111111111ffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffff11111fffffffffff11111111111111111111111ffffff111111111111ffffffffffffff22222ffffff22222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffff111111111111111111fffffff111111111111ffffffffffffff22222ffffff22222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffff11111111111111111fffffff1111111111ffffffffffffffff22222ffffff22222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffff111111111111111ffffffff111111111fffffffffffffffff22222ffffff22222fffffffffffffffffffffffffff2222222fffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffff11111111111ffffffffffffffffffffffffffffffffffff22222ffffffffffffffffffff2222222fffffffffff2222222fffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222fffffffffffffffffff222222222fffffffff22222222fffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222ffffffffffffffffff22222222222ffffffff22222222fffffffffffffffffffffffffffff
        ffffffffffffffffff22222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222ffffffffffffffffff222222222222fffffff22222222fffffffffffffffffffffffffffff
        fffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222fffffffffffffffff222222222222fffffff222222fffffffffffffffffffffffffffffff
        ffffffffffffffff2222222fffffffffffffffffffffffffffffffffffffffffff22222ffffffffff222222fffffffffffffffff222222222222fffffff22222ffffffffffffffffffffffffffffffff
        fffffffffffffff22222222fffffffffffffffffffffffffffffffffffffffffff22222ffffffffff222222ffff22222ffffffff222222222222fffffff22222ffffffffffffffffffffffffffffffff
        ffffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffff22222ffffffffff222222ffff22222ffffffff22222ff22222fffffff22222ffffffffffffffffffffffffffffffff
        fffffffffffff222222222ffffffffffffffffffffffffffff22222ffffffffff222222fffffffffff22222ffff22222ffffffff22222ff22222fffffff22222ffffffffffffffffffffffffffffffff
        fffffffffffff22222222fffffffffffffff22222fffffffff22222ffffffffff222222fffffffffff22222ffff22222ffffffff22222ff22222fffffff222222fffffffffffffffffffffffffffffff
        fffffffffffff2222222ffffffffffffffff22222fffffffff22222ffffffffff222222f222222222222222ffff22222ffffffff22222ff22222fffffff2222222ffffffffffffffffffffffffffffff
        fffffffffffff222222fffffffffffffffff22222fffffffff22222ffffffffff2222222222222222222222ffff222222ffffff222222f222222fffffff22222222fffffffffffffffffffffffffffff
        fffffffffffff222222fffffffffffffffff222222ffffffff22222ffffffffff22222f22222222222222222fff222222ffffff222222f222222fffffff22222222fffffffffffffffffffffffffffff
        fffffffffffff2222222ffffffffffffffff222222ffffffff222222ffffffff222222f22222222222222222fff2222222fffff2222222222222ffffffff22222222ffffffffffffffffffffffffffff
        fffffffffffff22222222fffffffffffffff222222222222ff222222ffffffff222222f22222222222222222fff2222222fffff2222222222222fffffffff2222222ffffffffffffffffffffffffffff
        ffffffffffffff22222222ffffffffffffff222222222222ff222222fffffff2222222f222222ff222222222ffff222222fffff222222222222ffffffffff2222222ffffffffffffffffffffffffffff
        ffffffffffffff222222222fffffff222222222222222222ff2222222ffffff2222222f22222222222222222ffff222222fffff222222222222ffffffff222222222ffffffffffffffffffffffffffff
        fffffffffffffff222222222ffffff222222222222222222fff222222fffff2222222ff22222222222222ffffffff22222fffff22222222222fffffff22222222222ffffffffffffffffffffffffffff
        ffffffffffffffff222222222fffff222222222222222222fff222222fffff2222222fff2222222222222ffffffff22222fffff2222222222ffffff2222222222222ffffffffffffffffffffffffffff
        fffffffffffffffff222222222ffff2222222222222222fffff2222222fff2222222ffff222222222222ffffffffffffffffffff2222222222222222222222222222ffffffffffffffffffffffffffff
        ffffffffffffffffff22222222ffff2222222222222fffffffff2222222ff2222222fffff2222222222fffffffffffffffffffff2222222222222222222222222fffffffffffffffffffffffffffffff
        fffffffffffffffffff2222222ffffffffffff222222ffffffff22222222f222222ffffff222222222ffffffffffffffffffffff22222222222222222222222fffffffffffffffffffffffffffffffff
        ffffffffffffffffffff222222ffffffffffff222222ffffffff222222222222222fffffffffffffffffffffffffffffffffffffff2222222222222222222fffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff22222ffffffffffff222222fffffffff2222222222222ffffffffffffffffffffffffffffffffffffffff22222222222222222fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff22222ffffffffffff222222ffffffffff222222222222ffffffffffffffffffffffffffffffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff22222fffffffffffff22222fffffffffff22222222222ffffffffffffffffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff222222ffffffffffff222222ffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffff2222222ffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff22222222ffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff222222222ffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffff22222222222fffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffff22222f222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff222222222222222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff22222222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff2222222222222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff2222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff22222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffff222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111fffffffffffffffffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111fff11111111ffffffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff111111111ffffffffffff111111111fff11111111ffffffff111111111fffffffff11111fffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff1111111111fffffffffff1111111111ff111111111fffffff11111111111ffffffff11111fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff11111111111fffffffffff11111111ffff111111111ffffff1111111111111fffffff11111fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff111111ffffffffffffffffff11111111111fffffffffff1111111ffff1111111111fffff11111111111111fffffff11111111ffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff11111111fffff1111111111111111111111fffffffffff111111fffff1111111111fffff11111111111111ff11111111111111fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff11111111111111ff1111111111111111111111fffffffffff1111111ffff111111111ffffff1111111f111111ff11111111111111fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff11111111111111111111111111111111111111fffffffffff11111111fff111111111ffffff111111fff11111ff11111111111111fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff11111111111111111111111111111111111111fffffffffff11111111fff1111111ffffffff111111fff11111ff11111111111111fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff11111111111111111111111111111111111111ffffffffffff1111111fff11111ffffffffff111111fff11111ff11111111111111fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff111111f111111111111111ff1111111111111fffff11111ff11111111fff11111ffffffffff111111fff11111ffffff11111ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff1111111111111111111111ffff1111111111111111111111111111111fff11111111111ffff111111fff11111ffffff11111ffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff111111111111111111111fffff111111111111111111111111111111fff11111111111ffff111111fff11111ffffff11111fffffffffff11111fff11111fff11111ffffffff
        fffffffffffffffffffff11111111111111f1111111ffff111111111111111111111111111111fff11111111111ffff111111fff11111ffffff11111fffffffffff11111fff11111fff11111ffffffff
        fffffffffffffffffffff111111111111fff1111111ffff11111111111111111111111111111ffff11111111111ffff111111ffffffffffffff11111fffffffffff11111fff11111fff11111ffffffff
        fffffffffffffffffffff1111111111fffff1111111fffff1111111111111111111111111fffffff11111111111ffff111111ffffffffffffffffffffffffffffff11111fff11111fff11111ffffffff
        fffffffffffffffffffff1111111fffffffff111111ffffffffffffff1111111111111fffffffffffff1111111fffff111111ffffffffffffffffffffffffffffff11111fff11111fff11111ffffffff
        ffffffffffffffffffffff111111fffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffff111111ffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffff111111ffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffff1111111fffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    pause(2000)
    color.start_fade(color.original_palette, color.black)
    pause(100)
    color.start_fade(color.black, color.original_palette)
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffff111ffffffffffff11fffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffff111fffffffffff1111fffffff1ff1ffffffffff1f1ffffffffffffffffffff11ffffff1fffffffffffffffff1111ffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffff1fffffffff1fffffffff1fff1fff1fff1fff1ffffffff1ff1ffffffffffffffffffffff1ffff1fffffffffffffffff11fff111fffffffffffffffffffffffff
        fffffffffff1fffffffffffffffffffff1fffffffff1ffffffff1ffff1fff1fff1fff1fffffff1ffff1fffffffffffffffffffff1ffff1fffffffffffffffff1fffffff1ffffffffff1fffffffffffff
        fffffffffff1fffffffffffffffffffff1ffffffff11fffffff1fffff1fff1fff1fff1ffffff1fffff1ffffffffffffffffffffff1fff1ffffffffffffffff1fffffffff1ffffffff1ffffffffffffff
        fffffffffff1fff1fffffffffffffffff1ffffff11ffffffff1ffffff1ffff1ff1ffff1ffff1ffffff1ffffffff1ffffffffffffff1f1fffffffffffffffff1fffffffff1fffffff1fffffffffffffff
        fffffffffff1ffff1ffffffffffffffff1ff1111fffffffff1ffffff1fffff1ff1ffff1fff1fffffff1ffffffff1fffffffffffffff11fffffffffffffffff1fffffffff1ffffff1ffffffffffffffff
        fffffffffff1ffff1ffffffffffffffff1ff11fffffffffff1ffffff1fffff1ff1ffff1fff1fffffff1fffffffff1fffffffffffffff1fffffffffffffffff1ffffffff1ffffff1fffffffffffffffff
        fffffffffff1fffff1fffffffffffffff1ffff1ffffffffff1ffff11ffffff1f1fffff1ff1ffffffff1fffffffff1fffffffffffffff11ffffffffffffffff1ffffffff1ff11111111ffffffffffffff
        fffffffffff1ffffff1fffffffffffffff1ffff11fffffff1ffff1ffffffff1f1fffff1f1fffffffff1fffffffff1ffffffffffffff1ff1fffffffffffffff1fffffff1ffffff1fff1ffffffffffffff
        fffffffffff1ffffff1fffffffffffffff1ffffff1ffffff11111fffffffff11ffffff1f1fffffffff1fffffffff1fffffffffffff1fffffffffffffffffff1fffff11fffffff1ffffffffffffffffff
        ffffffffff1ffffffff11fffffffffffff1fffffff1ffffff1ffffffffffff11fffffff1ffffffffff1ffffffffff1fffffffffff11fffffffffffffffffff1fff11ffffffff11ffffffffffffffffff
        ffffffffff1ffff111111fffffffffffff1ffffffff1ffffff1fffffffffff11fffffff1ffffffffff1ffffffffff1fffffffffff1ffffffffffffffffffff1111ffffffffff1fffffffffffffffffff
        ffffffffff1f111ffffff1ffffffffffff1fffffffff1ffffff1ffffff1fff11ffffff11ffffffffff1ffffffffff1fffffffffff1ffffffffffffffffffffffffffffffffff1fffffffffffffffffff
        ffffffffff1ffffffffff1ffffffffffff1ffffffffff11fffff111111ffff11ffffff11ffffffffff11ffffffffff1fffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffff
        ffffffffff1ffffffffff1ffffffffffff1fffffffffff1fffffffffffffffffffffff11ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1ffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffff11ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1fffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1fffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffff11fffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffff11fffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff999ffff999999f999999fffffff999fff9999999999999fff99999999999999fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff99199fff911119f911119fffffff919fff91111111111199ff91111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9911199ff911119f911119ffffff99199ff911111111111199f91111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff991111199f991119f991119ffffff91119ff991111111111119f91111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9911111119ff91119ff91119fffff9911199ff91111111111119f91111111111199fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99111111119ff91119ff91119fffff9111119ff99111111111119f9111119999999ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff991111111199ff91119ff91119ffff991111199ff9111111111119f9111119ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff991111111999fff911199991119ffff911111119ff9911111111119f9111119999999ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff91111111999ffff911111111119fff99111111199ff911111111199f91111111111199fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff991111111199fff911111111119fff91111111119ff99111111199ff91111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff991111111199ff911111111119ff9911111111199ff911119999fff91111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99111111119ff911111111119ff9111111111119ff911119ffffff91111111111199fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9911111119ff911199991119f991111111111199f911119ffffff9111119999999ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99111111199ff91119ff91119f911111111111119f911119ffffff9111119ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99111111199ff991119ff91119f911111111111119f911119ffffff9111119999999ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99111111199ff9911119ff91119f911119999911119f911119ffffff91111111111199fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff9111111199ff99111119ff91119f911119fff911119f911119ffff9991111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff991111199ff991111119ff91119f911119fff911119f911119fff99111111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9911199ff9911111119ff91119f911119fff911119f911119fff91111111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99199fff9111111119ff91119f911119fff911119f911119fff91111111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff999ffff9999999999ff99999f911119fff911119f999999fff99999999999999999fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff911119fff911119ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff911119fff911119ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff9999999999999999999999999999911119999911119999999999999999999999999999fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff9111111111111111111111111111111111111111111111111111111111111111111119fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff9911111111111111111111111111111111111111111111111111111111111111111199fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99111111111111111111111111111111111111111111111111111111111111111199ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff991111111111111111111111111111111111111111111111111111111111111199fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9911111111111111111111111111111111111111111111111111111111111199ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff99111111111111111111111111111111111111111111111111111111111199fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff999999999999999999999999999999999999999999999999999999999999ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff999999999f9999ff9999fff9999999fff999999999f99999f99999f999999999f999999999fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119999119ff991111199ff911111119f91119f91119f911111119f9111111199ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9111991119f99111111199f911111119f91119f91119f911111119f9111111119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9111111119f91119991119f911111119f91119f91119f911111119f9119991119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911199999f9111111119f91119f91119f911199999f91119f91119f911999999f9119f99119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff91119fffff9119119119f91119991119f91119fffff91119991119f9119ffffff9119f99119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911199999f9119119119f91111111119f911199999f91111111119f911999999f9119991119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119119119f91111111119f911111119f91111111119f911111119f9111111199ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119119119f91111111119f911111119f91111111119f911111119f911111999fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff999991119f9119119119f91119991119f999991119f91119991119f911999999f9111111199ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff91119f9119119119f91119f91119fffff91119f91119f91119f9119ffffff9111111119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff999991119f9119119119f91119f91119f999991119f91119f91119f911999999f9119991119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119119119f91119f91119f911111119f91119f91119f911111119f9119f91119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119119119f91119f91119f911111119f91119f91119f911111119f9119f99119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff911111119f9119119119f91119f91119f911111119f91119f91119f911111119f9119ff9119ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffff999999999f9999999999f99999f99999f999999999f99999f99999f999999999f9999ff9999ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff1ffffffffffffffffffffffffffff2222222fffffffffffffffffffffffffffffffffffffffffff2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1ffff1fffffffffffffffffffffffffffff2ffffff2ffffffffffffffffffffffffffffffffffffffffff2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1ffff1fffffffffffffffffffffffffffff2fffffff2ffffffffffffffffffffffffffffffffffffffff22fffffffffffffff2fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1fff1ffffffff1fffffffffffffffffffff2ffffff2fffffffffffffffffffffffffffffffffffffff2f22ffffffff2fffff2ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1f11ffffffffff1ffffffffffffffffffff2ffffff2fffffff2ffffffffffffffffffffff2ffffffff2f22ffffffff2ffff2fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1111fffffffffff1ffffffff1fffffffffff2ffff2fffffffffffffffffffffff2fffffff22ffffff2f2f2fff2ffff2ffff22ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1fff1fffffffffff1fffffff1fffffffffff2fff2ffffffffffffffff2fffffff2ffffff22f2ffff2f2ff2fff2fff22ffffff22ffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1fff11fffffffffff1ffffff1fffffffffff2f2222fffffffffffffff2ffff2ff2ffffff22f2ffff222ff2fff2fff22ffffffff2fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1fffff1fffffffffff1ffff1ffffffffffff2fffff2fffffff2ffffff2ffff2ff2ffffff22ff2ffffffff2fff2ff2f2ffffffff2fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1ffffff1fffffffffff1fff1fffffffffffff2fffff2ffffff2ffffff2ffff2ff22fffff22ff2ffffffff2fff2ff2f2fffffff2ffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1ffffff1ffffffffffff1ff1fffffffffffff2fffff2ffffff2ffffff2ffff2ff22fffff22ff2ffffffff2fff2f2ff2ff22222fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1ffffff1ffffffffffff11f1fffffffffffff2ffff2fffffff2ffffff2ffff2f2f2fffff22ff2ffffffff2ffff2fff2f22fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ffff1ffffffffffffff1f1fffffffffffff2ffff2ffffffff2fffff2fff2ff2f2fffff22fff2ff22fff2fffffffff2fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ffff1ffffffffffffffff1fffffffffffff2ffff2ffffffff2fffff2fff2ff2f2fffff22fff2ffff2ff2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1fff1ffffffffffffffff1ffffffffffffff2fff2fffffffff2fffff2fff2f22ff2ffff22fff22ffff22ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ff1ffffffffffffffff1fffffffffffffff2ff22fffffffff2ffff22fff22ffff2ffff2ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ff1ffffffffffffffff1fffffffffffffff222fffffffffff2fffffffffffffff2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1f1ffffffffffffffff11fffffffffffffffffffffffffffff2ffffffffffffffff22fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    pause(5000)
    color.start_fade(color.original_palette, color.black)
    Prepare()

def on_a_pressed():
    if _1GameStarted:
        if blockSettings.read_string("SaveControls") == "Mobile":
            RegularAttacj()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def SiegeWaveManager():
    global _1Score, WaveStartText
    _1Score += 1
    _3ScoreTracker.set_text("W:" + str(_1Score))
    _3ScoreTracker.set_position(151 - ((len(convert_to_text(_1Score)) - 1) * 5 - (len(convert_to_text(_1Score)) - 1) * 2),
        116)
    WaveStartText = textsprite.create("WAVE " + str(_1Score), 15, 2)
    WaveStartText.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    WaveStartText.set_position(80, 12)
    WaveStartText.lifespan = 5000
    
    def on_background3():
        pause(1000)
        easing.block_ease_by(WaveStartText, 0, -100, 2000, easing.Mode.IN_BACK)
        if _1Score == 1:
            StartWave(3, [0])
        elif _1Score == 2:
            StartWave(5, [0, 0, 0, 1])
        elif _1Score == 3:
            StartWave(6, [0, 1, 1, 1])
        elif _1Score == 4:
            StartWave(7, [0, 0, 1, 1, 4])
        elif _1Score == 5:
            StartWave(3, [3])
        elif _1Score == 6:
            StartWave(2, [3])
            StartWave(4, [1])
        elif _1Score == 7:
            StartWave(4, [0, 1, 3, 4])
        elif _1Score == 8:
            StartWave(8, [0])
        elif _1Score == 9:
            StartWave(5, [3, 1, 0])
        elif _1Score == 10:
            StartWave(3, [3])
            StartWave(5, [4])
        elif _1Score == 11:
            StartWave(9, [4, 1])
        elif _1Score == 12:
            StartWave(8, [0])
            StartWave(4, [1])
            StartWave(2, [3])
        elif _1Score == 13:
            StartWave(6, [3])
        elif _1Score == 14:
            StartWave(8, [1, 1, 3])
        elif _1Score == 15:
            StartWave(10, [1])
            StartWave(5, [3])
            StartWave(5, [4])
        else:
            StartWave(randint(5, 7) + Math.floor(_1Score / 5),
                [randint(0, 1), randint(3, 4), randint(0, 1), randint(3, 4)])
    timer.background(on_background3)
    
def death():
    global _1GameStarted, GameOverMenu
    music.stop_all_sounds()
    sprites.destroy_all_sprites_of_kind(SpriteKind.Obelisk)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Weapon)
    scene.camera_shake(8, 500)
    _1GameStarted = False
    GameOverMenu = miniMenu.create_menu(miniMenu.create_menu_item("Score:" + str(_1Score)),
        miniMenu.create_menu_item("Gamemode:" + ["Original", "Waves", "Base Defend", "Hardcore Legacy"][_1Gamemode]),
        miniMenu.create_menu_item("Controls:" + blockSettings.read_string("SaveControls")),
        miniMenu.create_menu_item("Body:" + BodyNamesArray[_1Body]),
        miniMenu.create_menu_item("Weapon:" + BodyNamesArray[_1Weapon]),
        miniMenu.create_menu_item("Share this score with friends! "))
    GameOverMenu.set_dimensions(140, 100)
    GameOverMenu.set_position(80, 60)
    GameOverMenu.set_menu_style_property(miniMenu.MenuStyleProperty.ROWS, 5)
    GameOverMenu.set_menu_style_property(miniMenu.MenuStyleProperty.COLUMNS, 1)
    GameOverMenu.set_title("YEOWCH! Game Over!")
    GameOverMenu.set_frame(assets.image("""
        MenuFrame
        """))
    GameOverMenu.set_style_property(miniMenu.StyleKind.ALL,
        miniMenu.StyleProperty.BACKGROUND,
        15)
    GameOverMenu.set_style_property(miniMenu.StyleKind.ALL, miniMenu.StyleProperty.FOREGROUND, 9)
    GameOverMenu.set_menu_style_property(miniMenu.MenuStyleProperty.BACKGROUND_COLOR, 15)
    GameOverMenu.set_menu_style_property(miniMenu.MenuStyleProperty.SCROLL_INDICATOR_COLOR, 0)
    GameOverMenu.z = 999
    GameOverMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    
    def on_background4():
        music.play(music.create_song(hex("""
                00f5000408010207001c00020a006400f401640000040000000000000000000000000000000003120001000200012404000500012209000a00011e09010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800240000000100010302000300010205000600010306000700010a09000a0001080c000d000114
                """)),
            music.PlaybackMode.UNTIL_DONE)
        pause(1000)
        Gameoversong()
    timer.background(on_background4)
    
    
    def on_background5():
        pause(500)
        
        def on_button_pressed6(selection6, selectedIndex6):
            color.start_fade_from_current(color.black, 500)
            pause(500)
            game.reset()
        GameOverMenu.on_button_pressed(controller.A, on_button_pressed6)
        
    timer.background(on_background5)
    

def on_on_overlap(sprite, otherSprite):
    if not (_1Gamemode == 3):
        spriteutils.set_velocity_at_angle(sprite,
            spriteutils.angle_from(sprite, otherSprite),
            0 - spriteutils.speed(sprite))
sprites.on_overlap(SpriteKind.enemy, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    if not (IsPlayerImmune):
        if _1Gamemode == 3:
            _3HealthBar.value += 0 - 0.7
        else:
            _3HealthBar.value += 0 - sprites.read_data_number(otherSprite2, "Damage")
            sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.EnemyBullet, on_on_overlap2)

def GamemodeSelect():
    global SelectionMenuGamemode
    if Themeselection == 0:
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """))
    elif Themeselection == 1:
        scene.set_background_image(img("""
            888888888888888888888888855555558888f88888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            8888888885588888888888885555555588888f8888888888888888888558888888888558888888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            88888888555555555888888855555558888888f888888888888888885555558888885555588888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            888888855555555555888888555555588885555555888888888888885555555888885555558888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            888888855555555555888888555555888885555555888888f5fffff85555555888885555558888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            88888885555555555588888855555888888555555588888f8555555f5555555588855555588888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            8888888555555555558888888888888888855555558888f885555558f555555588855555888888888f8888888888888888888888888888888888888888888888888888888f888f888888888888888888
            888888855555555555888888555555888885555555888f88855555588f55555588555555888888888f88888888888888888888888888888888888888888888888888888888f88f888888888888888888
            888888855555555888888888555555588888555555888f88855555558f85555558555558888888888f88888888888888888888888888888888888888888888888888888888f88f888888888888888888
            888888855555558888888888555555558888555555888f88855555558f88555555555588888888888f888888888888888888888888888888888888888888888888888888888f8f888888888888888888
            888888885555555888888888555555558888555555f88f88855555558f88855555555588888888888f888888888888888888888888888888888888888888888888888888888f8f888888888888888888
            888888888555555888888888855555558888555555f88f88855555558f888885555558888888888888f88888888888888888888888888888888888888fffffffff8888888888f8888888888888888888
            888888888555555555888888855555558888555555f88f88855555558f888888555558888888888888f888888888888888888888888888888888888ff888888888ff88888888ff888888888888888888
            8888888888555555555588888555555588885555558f8f88855555555f888888855558888888888888f88888888888888888888888888888888888f8888888888888f8888888f8f88888888888888888
            8888888888555555555558888555555588885555558f88f888555555588855888555588888888888888f888888888888888888888888888888888f888888888888888f88888f888ff888888888888888
            8888888885555555555558888555555558885555588f888f88555555555555588555588888888888888f88888888888888888888888888888888f88888888888888888f8888f88888ff88888888888ff
            88888885555555555555588885555555588855555888f888ff555555555555588555588888888888888f8888888888888888888888888888888f8888888888888888888f888f8888888fffffffffff88
            888885555555555555555888855555555888555555555558885555555555555885555888888888888888f888888888888888888888888888888f8888888888888888888f88f888888888888888888888
            888885555555555555555888855555555888555555555558885555555555555585555888888888888888f88888888888888888888888888888f888888888888888888888f8f888888888888888888888
            8888855555555555555588888555555558885555555555588855555555555555888888888888888888888f8888888888888888888888888888f888888888888888888888ff8888888888888888888888
            88888555555555555555888885555555588855555555555588555555555555558888888888888888888888f888888888888888888888888888f888888888888888888888f88888888888888888888888
            88888855555555555558888885555555588855555555555588555555555555555888888888888888888888f888888888888888888888888888f888888888888888888888f88888888888888888888888
            888888555555555555588888855555555888555555555555885555555555558888888888888888888888888f88888888888888888888888888f88888888888888888888ff88888888888888888888888
            8888888555555555555888888555555888885555555555588888888888888888888888888888888888888888f8888888888888888888888888f8888888888888888888f8f88888888888888888888888
            88888888555555555888888888888888888855555555558888888888888888888888888888888888888888888f888888888888888888888888f888888888888888888f88f88888888888888888888888
            88888888855555558888888888888888888855555588f888888888888888888888888888888888888888888888f88888888888888888888888f88888888888888888f888f88888888888888888888888
            88888888888888888888888888888888888888888888f888888888888888888888fffffff888888888888888888f8888888888888888888888f8888888888888888f8888f88888888888888888888888
            88888888888888888888888888888888888888888888f8888888888888888888ff8888888ff88888888888888888f8888888888888888888888f88888888888888f8888f888888888888888888888888
            88888888888888888888888888888888888888888888f888888888888888888f88888888888f88888888888888888ff88888888888888888888f888888888888ff88888f888888888888888888888888
            88888888866666666666668888888888888888888888f888888888888888888f88888888888f8888888888888888888f88888888888888888888f8888888888f888888f8888888888888888888888888
            88888888866666666666666888888888888888888888f88888888888888888f8888888888888f8888888888888888888ff8888888888888888888f8888888ff888888f88888888888888888888888888
            88888888866666666666666688888888888888888888f8888888888888666668888888888888f888888888888888888888fff88888888888888888f888fff8888888f888888888888888888888888888
            88888888866666666666666668888888888888888888f8888888888888666668888888888888f888888888888888888888888fff888888888888888fff88888888ff8888888888888888888888888888
            88888888866666666666666668888888888888888888f8888888888888666668888888888888f888888888888888888888888888fffffffffffffff88fffffffff888888888888888888888888888888
            88888888866666688666666668888886668888888888f8868888888668666668888888888888f88888888888888888888888888888888888888888888888888888888888888888888888888888888888
            8888888886666668866666666888886888668888886f68868886688668666668888888888888f88888888888888888888888888888888888888888888888888888888888888888888888888888888888
            8888888888666666666666666888886888868888868f68868886688688666668888888888888f88888888888888888888888888888888888888888888888888888888888888888888888888888888888
            8888888888666666666666666888886888868888868f6886886868868866666f88888888888f888888888888888888888888888888888888888888888888888888888888888888888888888888888888
            888888888866666666666666666888688866888868f86886886868688866666f88888888888f888888888888888888888888888888888888888888888888888888888888888888888888888888888888
            8888888888666666666666666668886666888886666668868688686888666668ff8888888ff8888888888888888888888888888888888888888888888888888888888888888888888888888888888888
            888888888866666666666666666886668888888688f66886868868688866666888fffffff888888888888888888888888fffffffffff8888888888888888888888888888888888888888888888888888
            88888888886666666666666666688688688888868fff6fff66ff686888666668888888888888888888888888888888fff88888888888fff8888888888888888888888888888888888888888888888888
            888888888866666688888666666886888688886fff86688866886f688866666888888888888888888888888888888f88888888888888888f888888888888888888888888888888888888888888888888
            8888888888866666888666666668668886688f688f8688886688866f886666688888888888888888888888888888f8888888888888888888f88888888888888888888888888888888888888888888888
            888888888886666666666666666888888888f688f866888888888688f866666666666666888888888888888888ff888888888888888888888ff888888888888888888888888888888888888888888888
            8888888888866666666666666688888888ff6688f8888888888888888f66666666666666888888888888888888f88888888888888888888888f888888888888888888888888888888888888888888888
            8888888888866666666666666688888888f8688f8888888888888888886666666666666688888888888888888f8888888888888888888888888f88888888888888888888888888888888888888888888
            888888888886666666666666688888888f8888f8888888888888888888666666666666668888888888888888f888888888888888888888888888f8888888888888888888888888888888888888888888
            88888888888666666666666888888888f88888f888888888888888888866666666666666888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            8888888888888888888888888888888f88888f88888888888888888888888f8888888888888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            8888888888888888888888888888888f8888f888888888888888888888888f8888888888888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            8888888888888888888888888888888f8888f888888888888888888888888f888888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888f8888f88888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888f888f888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888f88f8888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888f8f88888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888ff888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888888f8888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            88888888888888888888888888888ff8888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888888ff8f8888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            88888888888888888888888888f888f8888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            888888888888888888888888ff8888f8888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888f88888888888888888888888888888888888888888
            88888888888888888888888f888888f8888888888888888888888888888888f888888888888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            888888888888888888888ff88888888f88888888888888888888888888888f8888888888888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            888888888888888888fff8888888888f88888888888888888888888888888f8888888888888888888888888f88888888888888888888888888888f888888888888888888888888888888888888888888
            888888888888888fff8888888888888f88888888888888888888888888888f88888888888888888888888888f888888888888888888888888888f8888888888888888888888888888888888888888888
            888888888888fff88888888888888888f888888888888888888888888888f8888888888888888888888888888f8888888888888888888888888f88888888888888888fffffffffffffffffff88888888
            ffffffffffff888888888888888888888f8888888888888888888888888f888888888888888888888888888888f88888888888888888888888f8888888888888fffff8888888888888888888fffff888
            8888888888888888888888888888888888f88888888888888888888888f8888888888888888888888888888888ff888888888888888888888ff8888888888fff88888888888888888888888888888fff
            8888888888888888888888888888888888ff888888888888888888888ff888888888888888888888888888888888f8888888888888888888f8888888888ff88888888888888888888888888888888888
            888888888888888888888888888888888888f8888888888888888888f888888888888888888888888888888888888f88888888888888888f888888888ff8888888888888888888888888888888888888
            8888888888888888888888888888888888888f88888888888888888f88888888888888888888888888888888888888fff88888888888fff88888888ff888888888888888888888888888888888888888
            88888888888888888888888888888888888888fff88888888888fff888888888888888888888888888888888888888888fffffffffff888888888ff88888888888888888888888888888888888888888
            88888888888888888888888888888888888888888fffffffffff888888888888888888888888888888888888888888888888888888888888888ff8888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888ff8888888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888
            88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888
            8888fffffffffffffffff8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888
            ffff88888888888888888ffff88888888888888888888888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888
            8888888888888888888888888ff88888888888888888888888888888888888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888
            888888888888888888888888888ff88888888888888888888888888888888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888888
            88888888888888888888888888888ff88888888888888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888ff88888888888888888888888888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888
            888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888ff888888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888
            888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888888
            88888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888888888f88888888888888888888fffffff88888888888888888888888888888888
            888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888f8888888888888888888f8888888f8888888888888888888888888888888
            8888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888888f8888888888888888888f888888888f888888888888888888888888888888
            88888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888f8888888888888888888f888888888f888888888888888888888888888888
            888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888f88888888888888888888f888888888f888888888888888888888888888888
            888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888888f88888888888888888888f888888888f888888888888888888888888888888
            8888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888888f888888888888888888888f888888888f888888888888888888888888888888
            88888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888888f888888888888888888888f888888888f88888888fffffff888888888888888
            88888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888f8888888888888888888888f888888888f888888ff8888888ff8888888888888
            888888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888888888f88888888888888888888888f8888888f888888f88888888888f888888888888
            888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888888f8888888888888888888888888fffffff8888888f88888888888f888888888888
            8888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888f8888888888888f88888888888
            8888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888f8888888888888f88888888888
            88888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888f888888888888888888888888888888888888888f8888888888888f88888888888
            88888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888888f888888888888888888888888888888888888888f8888888888888f88888888888
            888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888f888888888888888888888888888888888888888f8888888888888f88888888888
            888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888f888888888888888888888888888888888888888f8888888888888f88888888888
            888888888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888f888888888888888888888888888888888888888f8888888888888f88888888888
            888888888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888f88888888888888888888888888888888888888888f88888888888f888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f88888888888888888888888888888888888888888f88888888888f888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888ff8888888ff8888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f88888888888888888888888888888888888888888888fffffff888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888888888888888888888888888f8888888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888
            """))
    elif Themeselection == 2:
        scene.set_background_image(img("""
            888888888888888888888888888888888888888888888888888888888888888d55555555555555555555555555555555555555577999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888d55555555555555555555555555555555555555799999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888d55555555555555555555555555555555555577999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888888888d5555555555555555555555555555555557799999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888888888d5555555555555555555555555555555579999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888888888d5555555555555555555555555555557799999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888888d555555555555555555555555555579999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888888d555555555555555555555555557799999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888888d555555555555555555555555579999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888888d555555555555555555555555799999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888888d555555555555555555555577999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555555555555555557999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555555555555555579999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555555555555557799999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555555555555579999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d5555555555555557999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d5555555555555579999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d5555555555555799999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55555555555579999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55555555555799999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555555779999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555555557999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d5555555799999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55555579999999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55555799999999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d555557999999999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d5555799999999999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55579999999999999999999999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d55799999999999999992222222222299999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d579999999999999999999999999999222999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888888d7999999999999999999999999999999929999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888888888887999999999999999999999999999999999999999999999999999999999999966bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888887d9999999999999222299999999299999999999999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            888888888888888888888888888888888888888888888888888888888888888887d99999999999229999999999992999999999999299999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888887d99999999999299999999999999299999999999929999999999999999999999999966bbbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888878d999999999929999999999999992999999999999299999999999999999999999999996bbbbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888788d99999999992999999999999999299999999999929999999999999999999999999999966bbbbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888888788d9999999992999999999999999929999999999992999999999999999929999999999999966bbbbbbbbbbbbbbbbbbbbb
            88888888888888888888888888888888888888888888888888888888888887888d9999999992999999999999999929999999999992999999999999999992299999999999999666bbbbbbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888887888d9999999999299999999999999999299999999999299999999999999999992299999999999999966b6bbbbbbbbbbbbbb
            8888888888888888888888888888888888888888888888888888888888878888d9999999999299999999999999999299999999999299999999999999999999929999999999999999b466666666666666
            8888888888888888888888888888888888888888888888888888888888878888d9999999999929999999999999999299999999999299999999999299999999992999999999999999b444444444444444
            888888888888888888888888888888888888888888888888888888888878888d99999999999929999999999999999299999999999299999999999299999999999299999999999999b444444444444444
            888888888888888888888888888888888888888888888888888888888788888d99999999999929999999999999999299999999999299999999999299999999999929999999999999b444449994499944
            888888888888888888888888888888888888888888888888888888888788888d99999999999992999999999999999299999999999299999999999299999999999992999999999999b444449994444499
            88888888888888888888888888888888888888888888888888888888788888d999999999999999229999999999999299999999999299999999999299999999999999229999999929b444949944444449
            88888888888888888888888888888888888888888888888888888887888888d999999999999999992999999999999299999999999299999999999299999999999999992999999929b444949994444444
            88888888888888888888888888888888888888888888888888888887888888d999999999999999999299999999999299999999999299999999999299999999999999999299999929b444944494444449
            8888888888888888888888888888888888888888888888888888887888888d9999999999999999999922999999999299999999999299999999999299999999999999999929999929b444944994444449
            8888888888888888888888888888888888888888888888888888887888888d9999999999999999999999299999999299999999999299999999999299999999999999999929999929b444999444444449
            888888888888888888888888888888888888888888888888888887888888d99999999999999999999999299999999299999999999299999999999299999999999999999992999299b444444444449994
            888888888888888888888888888888888888888888888888888878888888d99999999999999999999999299999999299999999999299999999999299999999999999999992999299b444444444444444
            88888888888888888888888888888888888888888888888888887888888d9999999999999999999999992999999992999999999929999999999992999999999999999999999929999b44444499944449
            88888888888888888888888888888888888888888888888888878888888d9999999999999999999999992999999929999999299929999999999992299999999999999999999299999b44444444494449
            7777777777777777788888888888888888888888888888888887888888d99999999999999999999999929999222222222222999922222222222222299922222222299999999299999b44444444994449
            2222222222222222277778888888888888888888888888888878888888d99999999999999999999999929999999299999999999999999999999999222299999999929999999299999b44444499444449
            222222222222222222222777888888888888888888888888887888888d9999999999999999999999992999999922999999999999999999999999999999999999999999999929999999b4444499444494
            22222222222222222222222277788888888888888888888887888888d99999999999999999999999229999999999999999999999999999999999999999999999999999999929999999b4444494944494
            22222222222222222222222222277888888888888888888887888888d999999999999999999992229999999999999999999999999999999999999999999999999999999999299999999b444494944494
            2222222222222222222222222222277888888888888888887888888d9999999999999299922229999999999999999999999999999999999999999999999999999999999992999999999b444494494499
            222222222222222222222222222222277888888888888888788888d999999999999992222999999999999999999999999999999999999999999999999999999999999999929999999999b44494449449
            222222222222222222222222222222222778888888888887888888d999999999999999999999999999999999999999999999999999999999999999999999999999999999929999999999b44494449444
            22222222222222222222222222222222222788888888888788888d99999999999999999999999999999999999999999999999999999999999999999999999999999999999299999999999b4494444444
            2222222222222222222222222222222222227888888888878888d9999999999999999999999999999999999999999999999999999999999999999999999999999999999929999999999999b444444494
            222222222222222222222222222222222222277888888878888d999999999999999999999999999999999999999999999999999999999999999999999999999999999999299999999999999b44444449
            222222222222222222222222222222222222222788888878888d999999999999999999999999999999999999999999999999999999999999999999999999999999999999299999999999999b44444444
            22222222222222222222222222222222222222227888878888d99999999999999999999999999999999999999999999999999999999999999999999999999999999999929999999999999999b4444444
            2222222222222222222222222222222222222222278887888d9999999999999999999999999999999999999999999999999999999999999999999999999999999999992999999999999299999b444444
            222222222222222222222222222222222222222222787888d999999999999999999999999999999999999999999999999999999999999999999999999999999999999229999999999992999999bb4444
            22222222222222222222222222222222222222222227788d999999999999999999999999292222222229999999999999999999999999999999999999999999999999929999999999999299999999b444
            2222222222222222222222222222222222222222222278d99999999999999999999999992299999999929999992222222222999999999999999999999999999999992299999999999999299999999b44
            222222222222222222222222222222222222222222272d9999999999999999999999999922999999999299999992999999929999999999999999999999999999999229999999999999992999999999bb
            22222222222222222222222222222222222222222227d7799999999999999999999999992299999999299999999299999992999999999999999999999999999999929999999999999999299999999999
            222222222222222222222222222222222222222222d777779999999999999999999999992299999999299999999299999929999999999992999999999999999999299999999999999999299999999999
            22222222222222222222222222222222222222222d7777777999999999999999999999992999999992999999999299992299999999999992999999999999999999999999999999999999299999999999
            222222222222222222222222222222222222222dd77777777999999999999999999999992999999992999999999299999999999999999929999999999999999999999999999992999999299999999999
            22222222222222222222222222222222222222d7777777777799999999999999999999992999999229999999999299299999999999999299299999999999999999999999999992999999299999999999
            222222222222222222222222222222222222dd77777777777779999999999999999999992999922999999999999292999999999999999299299999999999999999999999999922299999299999999999
            22222222222222222222222222222222222d7777777777777777999999999999999999992992299999999999999229999999999999999299299999999992999999999999999929999999299999999999
            222222222222222222222222222222222dd77777777777777777999999999999999999992222222299999999999299999999999999999299299999999992999999999999999299999999299999999999
            2222222222222222222222222222222dd7777777777777777777799999999999999999992999999922299999999229999999999999992999929999999992999999999999999299999999299999999999
            22222222222222222222222222222dd777777777777777777777799999999999999999992999999999922999999229999999999999992999929999999992999999999999999299999999299999999999
            222222222222222222222222222dd77777777777777777777777779999999999999999992999999999999299999292999999999999992999929999999992999999999999999299999999299999999999
            222222222222222222222222ddd7777777777777777777777777779999999999999999992999999999999299999299299999999999922222222292999992999999999999999299999999299999999999
            222222222222222222222ddd7777777777777777777777777777777999999999999999992999999999999299999299929999999999929999929922999999299999922999992999999999299999999999
            222222222222222222ddd7777777777777777777777777777777777999999999999999992999999999999299999299929999999999929999929999999999299999299299992999999999299999999999
            2222222222222ddddd7777777777777777777777777777777777777799999999999999992999999999999299999299992999999999299999992999999999299992999299992999999999299999999999
            ddddddddddddd777777777777777777777777777777777777777777799999999999999992999999999999299999299999299999999299999992999999999929992999299929999999999299999999999
            7777777777777777777777777777777777777777777777777777777799999999999999992999999999992999999299999299999992999999992999999999929992999929929999999999299999999999
            7777777777777777777777777777777777777777777777777777777779999999999999929999999999929999999299999929999992999999992999999999929992999929929999999999929999999999
            7777777777777777777777777777777777777777777777777777777779999999999999929999999999929999999299999929999992999999992999999999929929999929929999999999929999999999
            7777777777777777777777777777777777777777777777777777777779999999999999929999999999299999999299999992999992999999992999999999929929999992929999999999929999999999
            7777777777777777777777777777777777777777777777777777777777999999999999929999999999299999999299999992999929999999922999999999992929999992299999999999922999992222
            7777777777777777777777777777777777777777777777777777777777999999999999929999999999299999922999999999299929999999999999999999992229999999999999999999992222229999
            7777777777777777777777777777777777777777777777777777777777999999999999929999999992999999992999999999299229999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777999999999999299999999929999999992999999999229299999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999299999992299999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999992999999229999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999992222222999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777799999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            7777777777777777777777777777777777777777777777777777777777999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            """))
    else:
        pass
    
    def on_background6():
        music.play(music.create_song(hex("""
                0078000408020109010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800370000000100010608000900010610001100010618001900010620002100020608280029000106300031000106340035000105380039000106
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    timer.background(on_background6)
    
    color.start_fade(color.original_palette, color.arcade)
    game.splash("Select a gamemode.")
    SelectionMenuGamemode = miniMenu.create_menu(miniMenu.create_menu_item("Original", assets.image("""
            Icon
            """)),
        miniMenu.create_menu_item("Waves", assets.image("""
            Icon1
            """)),
        miniMenu.create_menu_item("Base Defend", assets.image("""
            Icon0
            """)),
        miniMenu.create_menu_item("Hardcore Legacy", assets.image("""
            Icon2
            """)),
        miniMenu.create_menu_item("Enemy Catalog",
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d f f f d d d . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d f f f d d d . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d f f f d d d . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d d d d d d d . . . .
                . . f d d d d d d d d d . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)),
        miniMenu.create_menu_item("Lobby Songs",
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . 9 9 9 9 . . . .
                . . . . . . . . 9 . . . . . . .
                . . . . . . 9 9 9 . . . . . . .
                . . . . . 9 . . 9 . . . . . . .
                . . . . . 9 . . 9 . . . . . . .
                . . . . . 9 . . 9 . . . . . . .
                . . . . . . 9 9 9 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)),
        miniMenu.create_menu_item("Lobby Themes",
            img("""
                . . 7 7 7 7 7 7 7 7 7 7 7 7 . .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
                . . . . . . e e e e e . . . . .
                . . . . . . e e e e e . . . . .
                . 7 7 7 7 . e e e e e . . . . .
                . 7 7 7 7 . e e e e e . . . . .
                . 7 7 7 7 . e e e e e . . . . .
                . . e e . . e e e e e . . . . .
                . . e e . . e e e e e . . . . .
                . . e e . . e e e e e . . . . .
                """)))
    SelectionMenuGamemode.set_frame(assets.image("""
        MenuFrame0
        """))
    SelectionMenuGamemode.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.BACKGROUND,
        15)
    SelectionMenuGamemode.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.FOREGROUND,
        2)
    SelectionMenuGamemode.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.BACKGROUND,
        2)
    SelectionMenuGamemode.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.FOREGROUND,
        1)
    SelectionMenuGamemode.set_position(80, 60)
    
    def on_button_pressed7(selection7, selectedIndex7):
        if selection7 == "Enemy Catalog":
            Enemycatalog()
        elif selection7 == "Lobby Songs":
            game.splash("This is coming soon!")
            game.show_long_text("But you can change that!", DialogLayout.CENTER)
            game.show_long_text("You can submit your songs to this game's forum's topic to have chance to be added here!",
                DialogLayout.CENTER)
            game.show_long_text("Check out the game's code notes for more details and link. ",
                DialogLayout.CENTER)
        elif selection7 == "Lobby Themes":
            game.show_long_text("This is still working on.", DialogLayout.BOTTOM)
            game.show_long_text("So you may notice that the themes don't save, as we are working on that!",
                DialogLayout.BOTTOM)
            Themes()
        else:
            
            def on_throttle():
                global Songchoice, _1Gamemode
                if selection7 == "Waves":
                    Songchoice = 1
                elif selection7 == "Base Defend":
                    Songchoice = 2
                elif selection7 == "Hardcore Legacy":
                    Songchoice = 3
                else:
                    pass
                game.set_dialog_frame(img("""
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    f f f f f f f f f f f f f f f
                    """))
                game.set_dialog_text_color(1)
                game.show_long_text("Press B to learn about the abilities of each character.",
                    DialogLayout.BOTTOM)
                color.start_fade(color.original_palette, color.black, 250)
                pause(250)
                sprites.destroy(SelectionMenuText)
                SelectionMenuGamemode.close()
                _1Gamemode = selectedIndex7
                pause(5)
                BodySelect()
                color.start_fade(color.black, color.original_palette, 250)
            timer.throttle("dont break things pls", 500, on_throttle)
            
    SelectionMenuGamemode.on_button_pressed(controller.A, on_button_pressed7)
    
def Gameoversong():
    global Playgameoversong
    Playgameoversong = True

def on_mouse_left_button_pressed(x, y):
    if _1GameStarted:
        if blockSettings.read_string("SaveControls") == "PC":
            RegularAttacj()
browserEvents.mouse_left.on_event(browserEvents.MouseButtonEvent.PRESSED,
    on_mouse_left_button_pressed)

def on_addsystemmenuentry_block():
    if game.ask("Are you sure?", "A= Yes B= No"):
        game.reset()
    else:
        pass
scene.addSystemMenuEntry_block(img("""
        . . . . . . . . . . . . . . . . .
        . . 4 4 4 . . . . . . 4 . 4 4 . .
        . 4 . . . . . 4 4 . . 4 . 4 . 4 .
        . 4 4 4 4 . . 4 . 4 . 4 . 4 . 4 .
        . 4 . . . . . 4 . 4 . 4 . 4 . 4 .
        . 4 . . . . . 4 . 4 4 . . 4 4 4 .
        . . 4 4 4 . . . . . . . . . . . .
        . . . . . . 2 2 2 . . . . . . . .
        . 2 2 2 . . 2 . . 2 . 2 2 . 2 2 .
        . 2 . . . . 2 2 2 2 . 2 . 2 . 2 .
        . 2 . . . . 2 . . 2 . . . . . . .
        . 2 f f f f f . . . . 2 2 2 . . .
        . 2 . . . 2 . f . . . 2 . . . . .
        . 2 . . . 2 . f . . . 2 2 2 . . .
        . 2 2 2 2 2 . f . . . 2 . . . . .
        . . . . . . . . . . . 2 2 2 . . .
        . . . . . . . . . . . . . . . . .
        """),
    "End Game",
    on_addsystemmenuentry_block)

def on_on_overlap3(sprite3, otherSprite3):
    _3HealthBar.value += sprites.read_data_number(sprite3, "Damage") / 10
    if sprite3.image.equals(assets.image("""
        DrillProjectile
        """)):
        if not (sprites.read_data_boolean(otherSprite3, "HitRecently")):
            sprites.set_data_boolean(otherSprite3, "HitRecently", True)
            statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite3).value += 0 - sprites.read_data_number(sprite3, "Damage")
            
            def on_background7():
                
                def on_after():
                    sprites.set_data_boolean(otherSprite3, "HitRecently", False)
                timer.after(150, on_after)
                
            timer.background(on_background7)
            
    else:
        sprites.destroy(sprite3)
        statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite3).value += 0 - sprites.read_data_number(sprite3, "Damage")
    if statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite3).value <= 0:
        sprites.destroy(otherSprite3)
sprites.on_overlap(SpriteKind.HealBullet, SpriteKind.enemy, on_on_overlap3)

def on_on_zero(status):
    global RespawnText
    if _1Gamemode == 2:
        RespawnText = textsprite.create("Respawning in 3", 15, 2)
        RespawnText.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
        RespawnText.set_position(80, 12)
        _3PlayerBody.set_flag(SpriteFlag.INVISIBLE, True)
        _3PlayerWeapon.set_flag(SpriteFlag.INVISIBLE, True)
        _3PlayerBody.set_flag(SpriteFlag.GHOST, True)
        _3PlayerWeapon.set_flag(SpriteFlag.GHOST, True)
        controller.move_sprite(_3PlayerBody, 0, 0)
        
        def on_after2():
            RespawnText.set_text("Respawning in 2")
            
            def on_after3():
                RespawnText.set_text("Respawning in 1")
                
                def on_after4():
                    _3HealthBar.value = _3HealthBar.max
                    _3PlayerBody.set_flag(SpriteFlag.INVISIBLE, False)
                    _3PlayerWeapon.set_flag(SpriteFlag.INVISIBLE, False)
                    _3PlayerBody.set_flag(SpriteFlag.GHOST, False)
                    _3PlayerWeapon.set_flag(SpriteFlag.GHOST, False)
                    RespawnText.set_text("Take care!")
                    RespawnText.set_position(80, 12)
                    RespawnText.lifespan = 6000
                    easing.block_ease_by(RespawnText, 0, -50, 4000, easing.Mode.IN_BACK)
                    controller.move_sprite(_3PlayerBody, _2BaseSpeed, _2BaseSpeed)
                    tiles.place_on_random_tile(_3PlayerBody, assets.tile("""
                        SiegeObeliskSpawn
                        """))
                timer.after(1000, on_after4)
                
            timer.after(1000, on_after3)
            
        timer.after(1000, on_after2)
        
    else:
        death()
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def Enemycatalog():
    global Enemycatalogmenu
    game.splash("Learn about the enemies.")
    SelectionMenuGamemode.x += 200
    SelectionMenuGamemode.set_button_events_enabled(False)
    Enemycatalogmenu = miniMenu.create_menu(miniMenu.create_menu_item("Dia", assets.image("""
            myImage19
            """)),
        miniMenu.create_menu_item("Kubo", assets.image("""
            myImage20
            """)),
        miniMenu.create_menu_item("Ragey", assets.image("""
            myImage18
            """)),
        miniMenu.create_menu_item("RedSprites", assets.image("""
            EnemyCross
            """)),
        miniMenu.create_menu_item("Poopy", assets.image("""
            EnemyTri
            """)),
        miniMenu.create_menu_item("Back"))
    Enemycatalogmenu.set_frame(img("""
        5 2 2 2 2 2 2 2 2 2 2 2 2 2 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 f f f f f f f f f f f f f 9
        5 3 3 3 3 3 3 3 3 3 3 3 3 3 3
        """))
    Enemycatalogmenu.set_menu_style_property(miniMenu.MenuStyleProperty.HEIGHT, 50)
    Enemycatalogmenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.BACKGROUND,
        15)
    Enemycatalogmenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.FOREGROUND,
        2)
    Enemycatalogmenu.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.BACKGROUND,
        2)
    Enemycatalogmenu.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.FOREGROUND,
        1)
    Enemycatalogmenu.set_position(80, 50)
    game.set_dialog_frame(img("""
        b d d b d d d d d d d d d d b
        b d d d b d d d d d d d d d b
        b d d d d d d d d d d d d d b
        b d d d d d d d d d d d d d b
        5 d d d d d d d d d d d d d 5
        b d d d d d d d d d d d d d b
        5 d d d d d d d d d d d d d 5
        b d d d d d d d d d d d d d b
        b d d d d d d d d d d d d d b
        b d d d d d d d d d d d d d b
        d d d d d d d d d d d d d d d
        b d d d d d d d d d d d d d b
        5 d d d d d d d d d d d d d 5
        b d d d d d d d d d d d d d b
        b d d d d d d d d d d d d d b
        """))
    
    def on_button_pressed8(selection8, selectedIndex8):
        if selection8 == "Dia":
            game.show_long_text("Dia is the beautiful diamond sparkling in the arena. A little tougher than the others, the speed is remarkable and the strength is buffed! Good luck getting past her.",
                DialogLayout.CENTER)
        elif False:
            game.splash("")
        elif selection8 == "Kubo":
            game.show_long_text("Kubo is the basic cube there is. Originally, it was another recently forgotten enemy called Silly Bird that took his place, but this is the canon enemy of all of Silly Brawl!",
                DialogLayout.CENTER)
        elif selection8 == "Ragey":
            game.show_long_text("The true arena king. This strong, tough, angry rectangle wants to crush you in this fierce battle of Silly Brawl. The hardest enemy of all, this angry shape has high hopes for crushing YOU! Good luck defeating him!",
                DialogLayout.CENTER)
        elif selection8 == "RedSprites":
            game.show_long_text("A swarm of RedSprites, coming in hot!", DialogLayout.CENTER)
            game.show_long_text("These RedSprites sure are a pet peeve in this game. They come out everywhere, they have high speed-what else? ",
                DialogLayout.CENTER)
            game.show_long_text("Inspired by a forum user, legend has it that RedSprites are a complication for the brain. That means they're a big brain teaser for the mind!",
                DialogLayout.CENTER)
            game.show_long_text("(Wait, was that really from a legend?)",
                DialogLayout.BOTTOM)
        elif selection8 == "Back":
            sprites.destroy(Enemycatalogmenu)
            SelectionMenuGamemode.x += -200
            SelectionMenuGamemode.set_button_events_enabled(True)
        elif selection8 == "Poopy":
            game.show_long_text("Let's be honest-this guy is REALLY poopy.",
                DialogLayout.CENTER)
            game.show_long_text("Poopy just stays in one spot and just chills there, shooting projectiles at you. Yes, you can damage him, but can that really stop him anyways?",
                DialogLayout.CENTER)
        else:
            pass
    Enemycatalogmenu.on_button_pressed(controller.A, on_button_pressed8)
    
def Songs():
    if Songchoice == 1:
        music.play(music.create_song(hex("""
                002c010408320604001c00100500640000041e000004000000000000000000000000000a0400043000c003c8030116e003e8030116000408040116200428040116c004c8040116e004e804011600050805011620052805011605001c000f0a006400f4010a0000040000000000000000000000000000000002fa01c002c802010ac802d002010ad002d802010dd802e002010ce002e802010ae802f002010af002f802010df8020003010c4003480301164803500301165003580301195803600301186003680301166803700301167003780301197803800301188003880301168803900301169003980301199803a0030118a003a8030114a803b0030116b003b8030118b803c0030116c003c8030116c803d0030116d003d8030119d803e0030118e003e8030116e803f0030116f003f8030119f803000401180004080401160804100401161004180401191804200401142004280401162804300401193004380401183804400401164004480401164804500401165004580401195804600401186004680401166804700401167004780401197804800401188004880401168804900401169004980401199804a0040118a004a8040114a804b0040116b004b804021618b804c004021618c004c8040116c804d0040116d004d8040119d804e0040118e004e8040116e804f0040116f004f8040119f8040005011800050805011608051005011610051805011918052005011820052805011628053005011630053805019538054005011640054805010a48055005010a50055805010a60056805010a68057005010a70057805010a80058805010a88059005010a90059805010aa005a805010aa805b005010ab005b805010a06001c00010a006400f401640000040000000000000000000000000000000002b00400000800010a08001000010a10001800010a18002000010a20002800010a28003000010a30003800010a38004000010a40004800010a48005000010a50005800010a58006000010a60006800010a68007000010a70007800010a78008000010a80008800010a88009000010a90009800010a9800a000010aa000a800010aa800b000010ab000b800010ab800c000010ac000c800010ac800d000010ad000d800010ad800e000010ae000e800010ae800f000010af000f800010af8000001010a00010801010a08011001010a10011801010a18012001010a20012801010a28013001010a30013801010a38014001010a40014801010a48015001010a50015801010a58016001010a60016801010a68017001010a70017801010a78018001010a80018801010a88019001010a90019801010a9801a001010aa001a801010aa801b001010ab001b801010ab801c001010ac001c801010ac801d001010ad001d801010ad801e001010ae001e801010ae801f001010af001f801010af8010002010a00020802010a08021002010a10021802010a18022002010a20022802010a28023002010a30023802010a38024002010a40024802010a48025002010a50025802010a58026002010a60026802010a68027002010a70027802010a78028002010a80028802010a88029002010a90029802010a9802a002010aa002a802010aa802b002010ab002b802010ab802c002010ac002c802010ac802d002010ad002d802010dd802e002010ce002e802010ae802f002010af002f802010df8020003010c00030803011608031003011610031803011918032003011820032803011628033003011630033803011938034003011840034803010a48035003010a50035803010a58036003010a60036803010a68037003010a70037803010a78038003010a80038803010a88039003010a90039803010a9803a003010aa003a803010aa803b003010ab003b803010ab803c003010ac003c803010ac803d003010ad003d803010ad803e003010ae003e803010ae803f003010af003f803010af8030004010a00040804010a08041004010a10041804010a18042004010a20042804010a28043004010a30043804010a38044004010a40044804010a48045004010a50045804010a58046004010a60046804010a68047004010a70047804010a78048004010a80048804010a88049004010a90049804010a9804a004010aa004a804010aa804b004010ab004b804010ab804c004010ac004c804010ac804d004010ad004d804010ad804e004010ae004e804010ae804f004010af004f804010af8040005010a00050805010a08051005010a10051805010a18052005010a20052805010a28053005010a30053805010a38054005010a40054805010a48055005010a50055805010a58056005010a60056805010a68057005010a70057805010a78058005010a80058805010a88059005010a90059805010a9805a005010aa005a805010aa805b005010ab005b805010ab805c005010ac005c805010ac805d005010ad005d805010ad805e005010ae005e805010ae805f005010af005f805010af8050006010a00060806010a08061006010a10061806010a18062006010a20062806010a28063006010a30063806010a38064006010a07001c00020a006400f401640000040000000000000000000000000000000003700500000400010a04000800010c08000c00010d0c001000011110001400010f14001800010d18001c00010c1c002000010c20002400010a24002800010c28002c00010d2c003000011130003400010f34003800010d38003c00010c3c004000010c40004400011644004800011848004c0001194c005000011d50005400011b54005800011958005c0001185c006000011860006400011664006800011868006c0001196c007000011d70007400011b74007800011978007c0001187c008000011880008400010a84008800010c88008c00010d8c009000011190009400010f94009800010d98009c00010c9c00a000010ca000a400010aa400a800010ca800ac00010dac00b0000111b000b400010fb400b800010db800bc00010cbc00c000010cc000c4000116c400c8000118c800cc000119cc00d000011dd000d400011bd400d8000119d800dc000118dc00e0000118e000e4000116e400e8000118e800ec000119ec00f000011df000f400011bf400f8000119f800fc000118fc000001011800010401011b04010801011d08010c01011e0c011001012210011401012014011801011e18011c01011d1c012001011d20012401011b24012801011d28012c01011e2c013001012230013401012034013801011e38013c01011d3c014001011d40014401010a44014801010c48014c01010d4c015001011150015401010f54015801010d58015c01010c5c016001010c60016401010a64016801010c68016c01010d6c017001011170017401010f74017801010d78017c01010c7c018001010c80018401010a90019401010aa001a401010ab001b401010ac001c401010ac401c801010cc801cc01010dcc01d0010111d001d401010fd401d801010dd801dc01010cdc01e001010ce001e401010ae401e801010ce801ec01010dec01f0010111f001f401010ff401f801010df801fc01010cfc010002010c00020402010a10021402010a20022402010a30023402010a40024402020a1644024802020c1848024c02020d194c02500202111d50025402020f1b54025802020d1958025c02020c185c026002020c1860026402020a1664026802020c1868026c02020d196c02700202111d70027402020f1b74027802020d1978027c02020c187c028002020c1880028402020a1684028802020c1888028c02020d198c02900202111d90029402020f1b94029802020d1998029c02020c189c02a002020c18a002a402020a16a402a802020c18a802ac02020d19ac02b00202111db002b402020f1bb402b802020d19b802bc02020c18bc02c002020c1840054405020a1644054805020c1848054c05020d194c05500502111d50055405020f1b54055805020d1958055c05020c185c056005020c1860056405020a1664056805020c1868056c05020d196c05700502111d70057405020f1b74057805020d1978057c05020c187c058005020c1880058405020a1684058805020c1888058c05020d198c05900502111d90059405020f1b94059805020d1998059c05020c189c05a005020c18a005a405020a16a405a805020c18a805ac05020d19ac05b00502111db005b405020f1bb405b805020d19b805bc05020c18bc05c005020c18c005c405020a16c405c805020c18c805cc05020d19cc05d00502111dd005d405020f1bd405d805020d19d805dc05020c18dc05e005020c18e005e405020a16e405e805020c18e805ec05020d19ec05f00502111df005f405020f1bf405f805020d19f805fc05020c18fc050006020c1800060406020a1604060806020c1808060c06020d190c06100602111d10061406020f1b14061806020d1918061c06020c181c062006020c1820062406020a1624062806020c1828062c06020d192c06300602111d30063406020f1b34063806020d1938063c06020c183c064006020c1808001c000e050046006603320000040a002d0000006400140001320002010002980140024802010a48025002010a50025802010a60026802010a68027002010a70027802010a80028802010a88029002010a90029802010aa002a802010aa802b002010ab002b802010ac002c402010ac402c802010cc802cc02010dcc02d0020111d002d402010fd402d802010dd802dc02010cdc02e002010ce002e402010ae402e802010ce802ec02010dec02f0020111f002f402010ff402f802010df802fc02010cfc020003010c00030403010a04030803010c08030c03010d0c031003011110031403010f14031803010d18031c03010c1c032003010c20032403010a24032803010c28032c03010d2c033003011130033403010f34033803010d38033c03010c3c034003010c40054805010a48055005010a50055805010a60056805010a68057005010a70057805010a80058805010a88059005010a90059805010aa005a805010aa805b005010ab005b805010ac005c805010ac805d005010ad005d805010ae005e805010ae805f005010af005f805010a00060806010a08061006010a10061806010a20062806010a28063006010a30063806010a09010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800c40a00000100030001020c000d000300010210001100030001021c001d000300010220002100030001022c002d000300010230003100030001023c003d0003000102400041000200024400450001054800490001054c004d00010550005100060002060708095400550001055800590001055c005d000105600061000200026400650001056800690001056c006d00010570007100060002060708097400750001057800790001057c007d000105800081000200028400850001058800890001058c008d00010590009100060002060708099400950001059800990001059c009d000105a000a100020002a400a5000105a800a9000105ac00ad000105b000b10006000206070809b400b5000105b800b9000105bc00bd000105c000c100020002c400c5000105c800c9000105cc00cd000105d000d10006000206070809d400d5000105d800d9000105dc00dd000105e000e100020002e400e5000105e800e9000105ec00ed000105f000f10006000206070809f400f5000105f800f9000105fc00fd000105000101010200020401050101050801090101050c010d0102000210011101060002060708091401150101051801190101051c011d01020002200121010200022401250101052801290101052c012d0102000230013101060002060708093401350101053801390101053c013d01020002400141010200024401450101054801490101054c014d01010550015101060002060708095401550101055801590101055c015d010105600161010200026401650101056801690101056c016d01010570017101060002060708097401750101057801790101057c017d010105800181010200028401850101058801890101058c018d01010590019101060002060708099401950101059801990101059c019d010105a001a101020002a401a5010105a801a9010105ac01ad010105b001b10106000206070809b401b5010105b801b9010105bc01bd010105c001c101020002c401c5010105c801c9010105cc01cd010105d001d10106000206070809d401d5010105d801d9010105dc01dd010105e001e101020002e401e5010105e801e9010105ec01ed010105f001f10106000206070809f401f5010105f801f9010105fc01fd01010500020102060002060708090402050201050802090201050c020d02010510021102060002060708091402150201051802190201051c021d02010520022102060002060708092402250201052802290201052c022d02010530023102060002060708093402350201053802390201053c023d02010540024102030001024402450201054802490201054c024d0201055002510207000102060708095402550201055802590201055c025d02010560026102030001026402650201056802690201056c026d0201057002710207000102060708097402750201057802790201057c027d02010580028102030001028402850201058802890201058c028d0201059002910207000102060708099402950201059802990201059c029d020105a002a10203000102a402a5020105a802a9020105ac02ad020105b002b1020700010206070809b402b5020105b802b9020105bc02bd020105c002c10203000102c402c5020105c802c9020105cc02cd020105d002d1020700010206070809d402d5020105d802d9020105dc02dd020105e002e10203000102e402e5020105e802e9020105ec02ed020105f002f1020700010206070809f402f5020105f802f9020105fc02fd02010500030103030001020403050301050803090301050c030d0301051003110307000102060708091403150301051803190301051c031d03010520032103030001022403250301052803290301052c032d0301053003310307000102060708093403350301053803390301053c033d03010540034103040e0001024403450301054803490301054c034d03010550035103040e0001025403550301055803590301055c035d03010560036103040e0001026403650301056803690301056c036d03010570037103040e0001027403750301057803790301057c037d03010580038103040e0001028403850301058803890301058c038d03010590039103040e0001029403950301059803990301059c039d030105a003a103040e000102a403a5030105a803a9030105ac03ad030105b003b103040e000102b403b5030105b803b9030105bc03bd030105c003c103040e000102c403c5030105c803c9030105cc03cd030105d003d103040e000102d403d5030105d803d9030105dc03dd030105e003e103040e000102e403e5030105e803e9030105ec03ed030105f003f103040e000102f403f5030105f803f9030105fc03fd03010500040104040e0001020404050401050804090401050c040d04010510041104040e0001021404150401051804190401051c041d04010520042104040e0001022404250401052804290401052c042d04010530043104040e0001023404350401053804390401053c043d04010540044104040e0001024404450401054804490401054c044d04010550045104080e000102060708095404550401055804590401055c045d04010560046104040e0001026404650401056804690401056c046d04010570047104080e000102060708097404750401057804790401057c047d04010580048104040e0001028404850401058804890401058c048d04010590049104080e000102060708099404950401059804990401059c049d040105a004a104040e000102a404a5040105a804a9040105ac04ad040105b004b104080e00010206070809b404b5040105b804b9040105bc04bd040105c004c104040e000102c404c5040105c804c9040105cc04cd040105d004d104080e00010206070809d404d5040105d804d9040105dc04dd040105e004e104040e000102e404e5040105e804e9040105ec04ed040105f004f104080e00010206070809f404f5040105f804f9040105fc04fd04010500050105040e0001020405050501050805090501050c050d05010510051105080e000102060708091405150501051805190501051c051d05010520052105040e0001022405250501052805290501052c052d05010530053105080e000102060708093405350501053805390501053c053d05010540054105040e0001024405450501054805490501054c054d05010550055105090e00010203060708095405550501055805590501055c055d05010560056105040e0001026405650501056805690501056c056d05010570057105090e00010203060708097405750501057805790501057c057d05010580058105040e0001028405850501058805890501058c058d05010590059105090e00010203060708099405950501059805990501059c059d050105a005a105040e000102a405a5050105a805a9050105ac05ad050105b005b105090e0001020306070809b405b5050105b805b9050105bc05bd050105c005c105040e000102c405c5050105c805c9050105cc05cd050105d005d105090e0001020306070809d405d5050105d805d9050105dc05dd050105e005e105040e000102e405e5050105e805e9050105ec05ed050105f005f105090e0001020306070809f405f5050105f805f9050105fc05fd05010500060106040e0001020406050601050806090601050c060d06010510061106090e00010203060708091406150601051806190601051c061d06010520062106040e0001022406250601052806290601052c062d06010530063106090e00010203060708093406350601053806390601053c063d060105
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif Songchoice == 2:
        music.play(music.create_song(hex("""
                00f40104080100
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                002c010408320901001c000f05001202c102c201000405002800000064002800031400060200040c0000000400010a60046404011602001c000c960064006d019001000478002c010000640032000000000a060005120080008400010a80018801010a70057805010a03001c0001dc00690000045e0100040000000000000000000005640001040003530204000800010a14001800010a24002800010a34003800010a44004800010a54005800010a64006800010a74007800010a84008800010a94009800010aa400a800010ab400b800010ac400c800010ad400d800010ae400e800010af400f800010a04010801010a14011801010a24012801010a34013801010a44014801010a54015801010a64016801010a74017801010a84018801010a94019801010aa401a801010ab401b801010ac401c801010ad401d801010ae401e801010af401f801010a04020802010a14021802010a24022802010a34023802010a44024802010a54025802010a64026802010a74027802010a84028802010a94029802010aa402a802010ab402b802010ac402c802010ad402d802010ae402e802010af402f802010a04030803010a14031803010a24032803010a34033803010a44034803010a54035803010a64036803010a74037803010a84038803010a94039803010aa403a803010ab403b803010ac403c803010ad403d803010ae403e803010af403f803010a04040804010a14041804010a24042804010a34043804010a44044804010a54045804010a64046804010a74047804010a84048804010a94049804010aa404a804010ab404b804010ad404d804020a22dc04e0040122e404e804010af404f804010a04050805010a14051805010a24052805010a34053805010a44054805010a54055805010a64056805010a74057805010a94059805010aa405a805010ab405b805010ac405c805010ad405d805010ae405e805010af405f805010a04060806010a14061806010a24062806010a34063806010a04001c00100500640000041e000004000000000000000000000000000a040004590200000400010a10001400010a20002400010a30003400010a40004400010a50005400010a60006400010a70007400010a80008400010a90009400010aa000a400010ab000b400010ac000c400010ad000d400010ae000e400010af000f400010a00010401010a10011401010a20012401010a30013401010a40014401010a50015401010a60016401010a70017401010a80018401010a90019401010aa001a401010ab001b401010ac001c401010ad001d401010ae001e401010af001f401010a00020402010a10021402010a20022402010a30023402010a40024402010a50025402010a60026402010a70027402010a80028402010a90029402010aa002a402010ab002b402010ac002c402010ad002d402010ae002e402010af002f402010a00030403010a10031403010a20032403010a30033403010a40034403010a50035403010a60036403010a70037403010a80038403010a90039403010aa003a403010ab003b403010ac003c403010ad003d403010ae003e403010af003f403010a00040404010a10041404010a20042404010a30043404010a40044404010a50045404010a60046404010a70047404010a80048404010a90049404010aa004a404010ab004b404010ad004d404020a22d404d8040122d804dc040122dc04e0040122e004e404010af004f404010a00050405010a10051405010a20052405010a30053405010a40054405010a50055405010a60056405010a90059405010aa005a405010ab005b405010ac005c405010ad005d405010ae005e405010af005f405010a00060406010a10061406010a20062406010a30063406010a05001c000f0a006400f4010a00000400000000000000000000000000000000028d01aa03ac030125ac03ae030124ae03b0030122b803ba030125ba03bc030124bc03be030122c803ca030125ca03cc030124cc03ce030122ce03d0030122d003d2030122d203d4030122d403d6030122d603d8030122d803da030122da03dc030122dc03de030122de03e0030122e003e203022224e203e4030124e403e6030124e603e8030124e803ea030122ea03ec030122ec03ee030122ee03f0030122f003f2030125f203f4030125f403f6030125f603f8030125f803fa030127fa03fc030127fc03fe030127fe030004012700040204012502040404012504040604012506040804012508040a0401240a040c0401240c040e0401240e041004012410041204012412041404012414041604012416041804012418041a0401241a041c0401241c041e0401241e042004012420042204012422042404012424042604012726042804012728042a0401272a042c0401272c042e0401272e043004012730043204012732043404012734043604012536043804012538043a0401253a043c0401253c043e0401253e044004012506001c00010a006400f4016400000400000000000000000000000000000000025604c001c801010ad001d801010ae001e801010af001f801010a00020802010a08021002010a10021802010a18022002010a20022802010a28023002010a30023802010a38024002010a40024802010a48025002010a50025802010a58026002010a60026802010a68027002010a70027802010a78028002010a80028802010a88029002010a90029802010a9802a002010a00030803011108031003010f10031803010d18032003010c20032803010a40034403010a44034803010a48034c03010d4c035003010c50035403010c54035803010a58035c03010a5c036003010a60036403010a64036803010a68036c03010d6c037003010c70037403010c74037803010a78037c03010a7c038003010a80038403010c84038803010a88038c03010c8c039003010a90039403010c94039803010a98039c03010c9c03a003010aa003a403010ca403a803010aa803ac03010cac03b003010db003b4030111b403b8030112b803bc030111bc03c003010fc003c403010dc403c803010cc803cc03010ccc03d003010dd003d403010cd403d8030108d803dc03010adc03e003010ae003e803010ae803f003010af003f803010af8030004010a00040804010a08041004010a10041804010a18042004010a20042404010c24042804010a28042c04010a2c043004010c30043404010d34043804010d38043c0401163c044004011640044404010f44044804010d48044c04010f4c045004010d50045404010c54045804010c58045c04010a5c046004010a60046404010a64046804010a68046c04010a6c047004010a70047404010a74047804010a78047c04010a7c048004010a80048404010c84048804010a88048c04010c8c049004010a90049404010c94049804010a98049c04010a9c04a004010ca004a404010aa404a804010ca804ac04010aac04b004010ab004b404010ab404b804010ab804bc04010abc04c004010ad004d8040116d804e0040116e004e804010ae804f004010af004f804010af8040005010a00050805010a08051005010a10051805010a18052005010a20052805010a28053005010a30053805010a38054005010a40054805010a48055005010a50055805010a58056005010a60056805010a68057005010a70057805010a80058805011688058c05010a8c059005010a90059405010a94059805010a98059c05010a9c05a005010aa005a405010aa405a805010ca805ac05010aac05b005010cb005b405010ab405b805010cb805bc05010dbc05c005010cc005c405010ac405c805010ac805cc05010acc05d005010cd005d405010dd405d805010dd805dc05010cdc05e005010ae005e405010ae405e805010ae805ec05010aec05f005010af005f405010af405f805010af805fc05010afc050006010a00060406010a04060806010c08060c06010d0c061006011110061406010f14061806010d18061c06010c1c062006010c20062406010a24062806010c28062c06010d2c063006011130063406010f34063806010d38063c06010c3c064006010a07001c00020a006400f4016400000400000000000000000000000000000000031d05f000f400011800010401011900020402020c1810021402020d1918021c020118200224020216243002340202192538023c02011840024402011850025402011858025c0201195c026002011860026402011864026802011868026c02011670027402011678028002011680028402012284028802010d88028c0201258c029002010d90029402012498029c0201229c02a0020122a002a4020122a402a802010da802ac020129ac02b002010db002b4020127b402b802010db802bc020125bc02c0020124c002c4020122c402c802010dc802cc020125cc02d002010dd002d4020124d402d802010dd802dc020122dc02e0020122e002e4020122e402e8020122e802ec02010dec02f0020127f002f402010df402f8020125f802fc02020f1dfc020003012400030403021d2904030803011908030c03021b270c03100301181003140302192514031803011618031c03021824200324030216222403280302162228032c030219252c033003021824300334030218243403380302162238033c030216223c03400302162240034403010a44034803010a48034c03010d4c035003010c50035403010c54035803010a58035c03010a5c036003010a60036403020a1664036803020a1668036c03020d196c037003020c1870037403020c1874037803020a1678037c03020a167c038003020a168003840302182484038803011688038c0301168c039003011690039403021b2794039803011698039c0301169c03a0030116a003a403021925b003b403021e2ac003c403021d29d003d4030116d403d8030116e003e8030116f003f4030116f403f80301160004080401161004140401161404180401162004280402162528042c0401242c043004012730043404012734043804012938043c0401253c044004012540044404012a44044804012a48044c0401294c045004012950045404012754045804012758045c0401255c046004012260046404012264046804012468046c0401246c04700401257004740401257404780401a178047c0401a17c04800401228004840402162584048804012588048c0401298c049004012990049404012794049804011498049c0401249c04a0040124a004a404012aa404a804012aa804ac04012aac04b004012ab004b4040129b404b8040129b804bc040127bc04c0040127c004c4040125c404c8040125c804cc040125cc04d0040125d004d8040116d804e0040116e404e8040124e804ec040124ec04f0040124f004f4040124f404f8040125f804fc040125fc040005012500050405012504050805012408050c0501240c051005012410051405012414051805012218051c0501221c05200501222005240501a12405280501a128052c0501a12c05300501a180058805011688058c05012a8c059005012a90059405012994059805012998059c0501279c05a0050127a005a405010aa405a805010aa805ac05010aac05b005010ab405b805021622b805bc05021622bc05c005021622c005c405021622c405c805021e2ac805cc05021d29cc05d005021e2ad005d405021d29d405d805021b27d805dc05021d29dc05e005021b27e005e405021d29e405e805021b27e805ec0502192aec05f005021b2af005f40502192af405f805021b2af805fc05021829fc050006021929000604060218290406080602192908060c060216270c061006021825100614060216251406180602182518061c060219271c062006021b272006240602192724062806021b2728062c0601272c063006012530063406012434063806012438063c0601223c064006012208001c000e050046006603320000040a002d00000064001400013200020100020f02f001f801010a00020402012210021402012518021c02012420022402012230023402012538023c02012440024402012240034403010a44034803010a48034c03010d4c035003010c50035403010c54035803010a58035c03010a5c036003010a60036403010a64036803010a68036c03010d6c037003010c70037403010c74037803010a78037c03010a7c038003010a80038403010a84038803010a88038c03010d8c039003010c90039403010c94039803010a98039c03010a9c03a003010aa003a803030a1925a803b003010ab003b803030a1e2ab803c003010ac003c803030a1d29c803d003010ad003d803010ad803e003010a80048404011680058805011688058c05010f90059405010f98059c05010fa005a405010fa805ac05010fb005b405010fb405b805021622b805bc05021622bc05c005021622c005c405021622c405c805021e2ac805cc05021d29cc05d005021e2ad005d405021d29d405d805021b27d805dc05021d29dc05e005021b27e005e405021d29e405e805021b27e805ec0502192aec05f005021b2af005f40502192af405f805021b2af805fc05021829fc050006021929000604060218290406080602192908060c060216270c061006021825100614060216251406180602182518061c060219271c062006021b272006240602192724062806021b2728062c0601272c063006012530063406012434063806012438063c06012209010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800190c00000100030001020400050001050800090001050c000d000300010210001100010514001500010518001900030001021c001d000300010220002100030001022400250001052800290001052c002d000300010230003100010534003500010538003900030001023c003d000300010240004100030001024400450001054800490001054c004d000300010250005100010554005500010558005900030001025c005d000300010260006100030001026400650001056800690001056c006d000300010270007100010574007500010578007900030001027c007d000300010280008100030001028400850001058800890001058c008d000300010290009100010594009500010598009900030001029c009d0003000102a000a10003000102a400a5000105a800a9000105ac00ad0003000102b000b1000105b400b5000105b800b90003000102bc00bd0003000102c000c10003000102c400c5000105c800c9000105cc00cd0003000102d000d1000105d400d5000105d800d90003000102dc00dd0003000102e000e10003000102e400e5000105e800e9000105ec00ed0003000102f000f1000105f400f5000105f800f90003000102fc00fd000300010200010101030001020401050101050801090101050c010d010300010210011101010514011501010518011901030001021c011d010300010220012101030001022401250101052801290101052c012d010300010230013101010534013501010538013901030001023c013d010300010240014101030001024401450101054801490101054c014d010300010250015101010554015501010558015901030001025c015d010300010260016101030001026401650101056801690101056c016d010300010270017101010574017501010578017901030001027c017d010300010280018101030001028401850101058801890101058c018d010300010290019101010594019501010598019901030001029c019d0103000102a001a10103000102a401a5010105a801a9010105ac01ad0103000102b001b1010105b401b5010105b801b90103000102bc01bd0103000102c001c101030001020002010207000102060708090402050204000102050802090204000102050c020d020204051002110201051402150207000102060708091802190201051c021d0201052002210207000102060708092402250204000102052802290204000102052c022d020204053002310201053402350207000102060708093802390201053c023d0201054002410204000102054402450201054802490201054c024d020400010205500251020400010205540255020800010205060708095802590201055c025d02040001020560026102050001020509640265020204056802690201056c026d0204000102057002710205000102050974027502010578027902030405097c027d020105800281020400010209840285020105880289020500010205098c028d0201059002910208000102060708090a940295020105980299020500010205099c029d020105a002a10203000102a402a50203040508a802a902050001020508ac02ad0206120001020508b002b10206010406070809b402b50203010508b802b9020400010205bc02bd02020508c002c10203000102c402c502020005c802c90203000405cc02cd020105d002d1020700010206070809d402d5020105d802d902050506070809dc02dd020400010205e002e1020400010205e402e502020506e802e902050001020506ec02ed02020506f002f102080001020305070809f402f5020105f802f9020105fc02fd0208000102050708090a000301030400010205040305030105080309030900010205060708090a0c030d0301051003110308000102050708090a140315030105180319030a1700010205060708090a1c031d0301052003210308000102040508090a24032503020506280329030305060b2c032d030205063003310308000102040708090a34033503020506380339030305060b3c033d03020506400341030300010244034503020506480349030205064c034d0305000102050650035103070001020607080954035503020506580359030500010205065c035d03050001020506600361030604050708090a6403650301056803690305000102050a6c036d0301057003710305000102040574037503020506780379030605060708090a7c037d0302050680038103040001020584038503050001020405880389030304050a8c038d0301059003910308000102050607080994039503020405980399030500010304059c039d030400010205a003a1030400010205a403a503020506a803a903050001020406ac03ad0303040506b003b103020608b403b503050001020405b803b903020506bc03bd0306000102040509c003c1030400010204c403c503020506c803c903050001020506cc03cd0306000102050609d003d103050001020405d403d503020506d803d903050001020405dc03dd0303040509e003e103050001020305e403e5030400010205e803e9030400010205ec03ed030400010205f003f103050001020305f403f5030400010205f803f9030400010205fc03fd030400010205000401040500010204050404050404000102050804090404000102050c040d040400010205100411040500010203051404150404000102051804190404000102051c041d04040001020520042104050001020405240425040400010205280429040500010204052c042d04040001020530043104050001020405340435040400010205380439040500010204053c043d0406000102030405400441040500010204054404450401054804490404000102054c044d040400010205500451040505060708095404550404000102055804590404000102055c045d0402010560046104080001020506070809640465040202056804690404000102056c046d040202057004710408000102050608090a740475040302050678047904030205067c047d040500010205068004810402010584048504050001020405880489040203058c048d0408000102050708090a900491040202059404950408000102050708090b9804990404000102059c049d040105a004a104050001020405a404a504020305a804a9040400010205ac04ad04020105b004b10406010506070809b404b5040400010205b804b904020105bc04bd040400010205c004c1040105d004d1040105d404d50403000102d804d9040105dc04dd040400010205e004e104050001020508e404e5040400010205e804e9040400010206ec04ed040400010205f004f104070001020608090af404f5040400010205f804f9040400010206fc04fd04040001020500050105070001020608090a0405050504000102050805090504000102060c050d05040001020510051105070001020608090a1405150504000103051805190504000102061c051d05040001020520052105070001020508090a220523050300010224052505040001020526052705030001022805290504000102052a052b05030001022c052d0504000102052e052f0503000102800581050b000102030405060708090a880589050500010205078c058d0501059005910504000102059405950501059805990504000102059c059d05050001020305a005a1050400010205a405a50503040507a805a90506000102050709ac05ad050105b005b1050b000102030405060708090ab405b5050400010205b805b905050001020508bc05bd05050001020508c005c105050001020508c405c5050400010205c805c90506000102040506cc05cd050400010205d005d1050400010205d405d5050400010205d805d9050400010205dc05dd050400010205e005e1050400010205e405e5050400010205e805e9050400010205ec05ed050400010205f005f1050900010204050708090af405f5050400010205f805f9050400010205fc05fd0505000102030500060106040001020502060306010504060506050001020509080609060500010205090c060d060500010205090e060f06010510061106040001020514061506050001020509180619060500010205091a061b0601051c061d060500010205092006210604000102052406250604000102052806290604000102052a062b06030001022c062d0604000102052e062f060400010205300631060400010205320633060300010234063506040001020536063706030001023806390604000102053a063b060400010205
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif Songchoice == 3:
        music.play(music.create_song(hex("""
                00f40104080100
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                005e010408320a00001c00010a006400f401640000040000000000000000000000000005000004780020042404010a30043404010a40044404010a50045404010a60046404012264046804012268046c0401226c047004012270047404012274047804012278047c0401227c048004012280048404012284048804012288048c0401228c049004012290049404012294049804012298049c0401229c04a004012201001c000f05001202c102c20100040500280000006400280003140006020004540010031803010a600364030116800384030116a003a4030116c003c4030118e003e403011920042404010a30043404010a40044404010a50045404010a600464040116800484040122e005e405012a00062006012502001c000c960064006d019001000478002c010000640032000000000a0600050c0080048404010a3c064006011603001c0001dc00690000045e0100040000000000000000000005640001040003250020042404010a30043404010a40044404010a50045404010a60046404020a2220064006012204001c00100500640000041e000004000000000000000000000000000a0400044e0020032803012528033003012430033803012250045404012260046404012268046c04012270047404012278047c04012280048404012288048c04012290049404012298049c04012220064006010a05001c000f0a006400f4010a0000040000000000000000000000000000000002a60200000400011604000800011608000c0001160c001000011610001400011614001800011618001c0001161c002000011620002400010a28002c00010a30003400010a38003c00010a40004400010a48004c00010a50005400010a58005c00010a60006400010a68006c00010a70007400010a78007c00010a80008400010a88008c00010a90009400010a98009c00010aa000a400010aa800ac00010ab000b400010ab800bc00010ac000c400010ac800cc00010ad000d400010ad800dc00010ae000e400010ae800ec00010af000f400010af800fc00010a00010401011604010801011608010c0101160c011001011610011401011614011801011618011c0101161c012001011620022402010a28022c02010a30023402010a38023c02010a40024402010a48024c02010a50025402010a58025c02010a60026402010a68026c02010a70027402010a78027c02010a80028402010a88028c02010a90029402010a98029c02010aa002a402010aa802ac02010ab002b402010ab802bc02010ac002c402010ac802cc02010ad002d402010ad802dc02010ae002e402010ae802ec02010af002f402010af802fc02010a00030403010a08030c03010a10031803010a78037c03010a80038403010a88038c03010a90039403010a98039c03010aa003a403010aa403a803010aa803ac03010aac03b003010ab003b403010ab803bc03010ad803dc03010ae003e403010ae803ec03010af003f403010af803fc03010a00040404010a04040804010a08040c04010a0c041004010a10041404010a18041c04010a28042c04010a38043c04010a48044c04010a58045c04010a60046404010a68046c04010a6c047004010a7c048004010c80048404010d84048804010c88048c04010d8c049004010c90049804010a90059405011198059c05011120064006010a06001c00010a006400f401640000040000000000000000000000000000000002ec01200024000116300034000116400044000116500054000116600064000116700074000116800084000116900094000116a000a4000116b000b4000116c000c4000116d000d4000116e000e4000116f000f4000116200124010108300134010108400144010108500154010108600164010108700174010108800184010108900194010108a001a4010108b001b4010108c001c4010108d001d4010108e001e4010108f001f4010108000204020108100214020108200224020116300234020116400244020116500254020116600264020116700274020116800284020116900294020116a002a4020116b002b4020116c002c4020116d002d4020116e002e4020116f002f402011600030403011610031803010a20032403010a28032c03010a30033403010a40034403010a48034c03010a4c035003010a50035403010a54035803010a58035c03010a60036403010a70037403010a80038403010a90039403010aa003a403010a28042c04010a38043c04010a48044c04010a58045c04010a60046404010a64046804010a68046c04010a6c047004010a70047404010a74047804010a78047c04010a7c048004010a80048404010a84048804010a88048c04010a8c049004010a90049404010a94049804010a98049c04010a9c04a004010a00062006010d20064006010a07001c00020a006400f4016400000400000000000000000000000000000000032d0400000400011604000800011608000c0001160c001000011610001400011614001800011618001c0001161c002000011600010401011604010801011608010c0101160c011001011610011401011614011801011618011c0101161c01200101162001240102161928012c0101162c01340101163c014001011840014401011944014801011848014c0101194c015001011850015801011660016401011964016801011b68016c01011d6c017001011b70017401011d74017801011b78017c01011d7c018001011b80018401011988018c010118900198010116a001a4010119a401a801011ba801ac01011dac01b001011bb001b401011db401b801011bb801bc01011dbc01c001011bc001c4010119c801cc010118d001d801011be001e4010119e401e801011be801ec01011dec01f001011bf001f401011df401f801011bf801fc01011dfc010002011e00020402012004020802012208020c0201220c021002012210021802012220022402012528022c0201222c02340201223c024002012440024402012544024802012448024c0201254c025002012450025802012260026402012764026802012968026c0201276c027002012970027402012774027802012978027c0201277c028002012980028402012588028c020124900298020122a002a4020127a402a8020129a802ac020127ac02b0020129b002b4020127b402b8020129b802bc020127bc02c0020129c002c4020125c802cc020124d002d8020127e002e4020127e402e8020129e802ec020127ec02f0020129f002f4020127f402f8020129f802fc020127fc020003012900030403012508030c03012410031803010a60046404012268046c0401226c04740401227c048004012480048404012584048804012488048c0401258c0490040124900498040122a004a4040122a804ac040122ac04b4040122bc04c0040124c004c4040125c404c8040124c804cc040125cc04d0040124d004d8040122e004e4040127e404e8040129e804ec04012aec04f0040129f004f4040127f404f804012af804fc040127fc040005012900050405012508050c05012410051405012918052005010520052405012724052805012928052c0501272c053005012930053405012734053805012938053c0501273c054005012240054405012748054c05012550055405012458055c05012460056405012764056805012968056c0501276c057005012970057405012774057805012978057c0501277c058005012280058405012788058c05012590059405012998059c050129a005a4050122a405a5050122a805ac050122ac05b8050122b805bc050124bc05c0050125c005c4050124c405c8050125c805cc050124cc05d4050122d405d8050122d805d9050122d905da050122da05db050122db05dc050122dc05dd050122dd05de050122de05df050122df05e0050122e0050006012a00062006012520064006012208001c000e050046006603320000040a002d0000006400140001320002010002400100000400011604000800011608000c0001160c001000011610001400011614001800011618001c0001161c002000011600010401011604010801011608010c0101160c011001011610011401011614011801011618011c0101161c012001011620012401021619a001a40102161938034003010a60036403010a68036c03010a6c037403010a78037c03010a80038403010a88038c03010a90039403010a98039c03010aa003a403010aa403a803010aa803ac03010aac03b003010ab003b403010ab803bc03010ac003c403010ac803cc03010acc03d403010ad803dc03010ae003e403010ae803ec03010af003f403010af803fc03010a00040404010a04040804010a08040c04010a0c041004010a10041404010a18041c04010a64046804011674047804011678047c04011880048404011888048c0401189804a004011609010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000c0a20002100050001020507240025000205072800290004030507092c002d00020507300031000600010205070a340035000205073800390004030507093c003d0002050740004100050001020507440045000205074800490004030507094c004d00020507500051000600010205070a540055000205075800590004030507095c005d0002050760006100050001020507640065000305070968006900030507096c006d00020507700071000600010205070a740075000205077800790004030507097c007d0002050780008100050001020507840085000205078800890004030507098c008d00020507900091000600010205070a940095000205079800990004030507099c009d00020507a000a100050001020507a400a50003050709a800a90003050709ac00ad00020507b000b1000600010205070ab400b500020507b800b90003050709bc00bd00020507c000c100050001020507c400c50003050709c800c900020507cc00cd00020507d000d1000600010205070ad400d500020507d800d90003050709dc00dd00020507e000e100050001020507e400e50003050709e800e90003050709ec00ed00020507f000f1000600010205070af400f500020507f800f90003050709fc00fd00020507000101010500010205070401050103050709080109010500010205070c010d01020507100111010600010205070a1401150102050718011901060001020507091c011d0102050720012101030001023001310103000102400141010300010250015101030001026001610103000102700171010300010280018101030001029001910103000102a001a10103000102b001b10103000102c001c10103000102d001d10103000102e001e10103000102f001f10103000102000201020300010210021102030001022002210205000102050724022502020507280229020305070a2c022d02020507300231020600010205070934023502020507380239020305070a3c023d020205074002410205000102050744024502020507480249020305070a4c024d0202050750025102060001020507095402550203050709580259020305070a5c025d020205076002610205000102050764026502020507680269020305070a6c026d02020507700271020600010205070974027502020507780279020305070a7c027d020205078002810205000102050784028502020507880289020305070a8c028d0202050790029102060001020507099402950203050709980299020305070a9c029d02020507a002a102050001020507a402a502020507a802a9020305070aac02ad02020507b002b10206000102050709b402b502020507b802b9020305070abc02bd02020507c002c102050001020507c402c502020507c802c9020305070acc02cd02020507d002d10206000102050709d402d50203050709d802d9020305070adc02dd02020507e002e102050001020507e402e502020507e802e9020305070aec02ed02020507f002f10206000102050709f402f502020507f802f9020305070afc02fd020205070003010305000102050704030503020507080309030305070a0c030d0302050720032103030001022803290303000102300331030300010240034103040001020344034503020509480349030a000102030405060708094c034d030500010203055003510306000102030509540355030a0001020304050607080958035903060001020305095c035d030105600361030400010203640365030105680369030205096c036d030105700371030a00010203040506070809740375030105780379030205097c037d030105800381030400010203840385030105880389030205098c038d030105900391030a00010203040506070809940395030105980399030205099c039d030105a003a10303000102a403a5030105a803a903020509ac03ad030105b003b1030a00010203040506070809b403b5030105b803b903020509bc03bd030105c003c10303000102c403c5030105c803c903020509cc03cd030105d003d1030a00010203040506070809d403d5030105d803d903020509dc03dd030105e003e10303000102e403e5030105e803e903020509ec03ed030105f003f1030a00010203040506070809f403f5030105f803f903020509fc03fd0301050004010403000102040405040105080409040205090c040d040105100411040a00010203040506070809140415040105180419040205091c041d040105200421040a00010203040506070809300431040a00010203040506070809400441040a00010203040506070809500451040a000102030405060708096004610405000102050764046504050001020507680469040500010205076c046d04050001020507700471040a00010203040506070809720473040300010274047504050001020507780479040500010205077c047d040500010205077e047f0403000102800481040500010205078204830403000102840485040500010205078604870403000102880489040600010205070a8a048b04030001028c048d040500010205078e048f0403000102900491040a000102030405060708099204930403000102940495040500010205079604970403000102980499040600010205070a9a049b04030001029c049d040500010205079e049f0403000102a004a10406000102050607a204a30403000102a404a50403000102a804a90406000102050607ac04ad0406000102050607b004b10406000102050607b404b50403050607b804b90406000102050607bc04bd0403000102c004c10406000102050607c404c50403000102c804c90403050607cc04cd0406000102050607d004d10406000102050607d404d50403050607d804d90406000102050607dc04dd0403000102e004e10406000102050607e404e50403000102e804e90403050607ec04ed0406000102050607f004f10406000102050607f404f50403050607f804f90406000102050607fc04fd04030001020005010506000102050607040505050300010208050905030506070c050d05060001020506071005110506000102050607140515050305060718051905060001020506071c051d05030001022005210506000102050607240525050300010228052905030506072c052d05060001020506073005310506000102050607340535050305060738053905060001020506073c053d05030001024005410506000102050607440545050300010248054905030506074c054d05060001020506075005510506000102050607540555050305060758055905060001020506075c055d05030001026005610506000102050607640565050300010268056905030506076c056d05060001020506077005710506000102050607740575050305060778057905060001020506077c057d05030001028005810506000102050607840585050300010288058905030506078c058d05060001020506079005910506000102050607940595050305060798059905060001020506079c059d0503000102a005a10506000102050607
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    else:
        pass
def Menuthemesong():
    pass
def Prepare():
    global _1GameStarted, Title, BodyImagesArray, BodyHealthArray, BodySpeedArray, BodyNamesArray, BodyDescriptionsArray, AmmoReloadArray, SuperReloadArray
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    color.start_fade(color.white, color.original_palette)
    if False:
        blockSettings.clear()
    scene.set_background_color(15)
    game.set_dialog_frame(assets.image("""
        MenuFrame
        """))
    game.set_dialog_text_color(9)
    _1GameStarted = False
    Title = sprites.create(assets.image("""
        myImage17
        """), SpriteKind.UI)
    Title.z = 999
    effects.blizzard.start_screen_effect()
    music.play(music.create_song(hex("""
            00a00004080c0401001c000f05001202c102c2010004050028000000640028000314000602000468010600080001ab08000c00012c0c001200012a12001800012918001e00012a22002c00012930003400012034003600012236003c0001253c004200012742004800012548004a0001a84a004e00012952005c0001276600680001ab68006c00012c6c007200012a72007800012978007e00012a82008c00012990009400011e94009600012296009c0001259c00a2000127a200a8000125a800aa0001a8aa00ae000129b200bc000125c000c4000129c400c600012ac600c80001abca00d200012cd800dc000127dc00de0001a8de00e0000129e200ea00012cf000f4000125f400f6000127f600f8000129fa000201012c02010601012908010e01012a12011a01012920012401012924012601012a2601280101ab2a013201012c38013c0101273c013e0101a83e014001012942014a01012c5001540101255401560101a85601580101295a016201012a62016601012768016c0101246e01720101257401780101277a017e01012c05001c000f0a006400f4010a0000040000000000000000000000000000000002d8000000060001190c001200011d18001c00011622002c0001193000360001123c004200011648004e00011452005c0001186000660001196c007200011d78007e00011682008c0001199000960001129c00a2000116a800ae000114b200bc000119c000c6000119ca00d200011dd800de000119e200ea00019cf000f6000119fa000201011d02010601011908010e01011612011a01011d2001260101162a013201011938013e01019542014a0101195001560101125a016201011662016601011268016c0101146e01720101167401780101187a017e01011407001c00020a006400f401640000040000000000000000000000000000000003fc0000000600011d0c001200012018001e00011e22002c00011d30003400011236003a0001163c004000011942004600011d48004e00011d52005c00011b60006600011d6c007200012078007e00011e82008c00011d90009400011296009a0001169c00a0000119a200a600011da800ae00011bb200bc000119c000c600011dca00d2000120d800de00019ce200ea000120f000f600011dfa000201012002010601011d08010e01012212011a01012020012601011d2a013201012038013e01019c42014a01012050015201011b52015401019c54015601011b5a016201011962016601011668016c0101186e017201011974017801011b7a017e01019c09010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8006502000001000200010600070001060a000b0001060c000d000104120013000106160017000200011c001d000200011e001f0001062200230001062400250001042a002b0001062e002f000106300031000200013600370001063a003b0001063c003d000104420043000106460047000200014c004d000200014e004f0001065200530001065400550001045a005b0001065e005f000106600061000200016600670001066a006b0001066c006d000104720073000106760077000200017c007d000200017e007f0001068200830001068400850001048a008b0001068e008f000106900091000200019600970001069a009b0001069c009d000104a200a3000106a600a700020001ac00ad00020001ae00af000106b200b3000106b400b5000104ba00bb000106be00bf000106c000c100020001c600c7000106ca00cb000106cc00cd000104d200d3000106d600d700020001dc00dd00020001de00df000106e200e3000106e400e5000104ea00eb000106ee00ef000106f000f100020001f600f7000106fa00fb000106fc00fd000104020103010106060107010200010c010d010200010e010f0101061201130101061401150101041a011b0101061e011f010106200121010200012601270101062a012b0101062c012d010104320133010106360137010200013c013d010200013e013f0101064201430101064401450101044a014b0101064e014f010106500151010200015601570101065a015b0101065c015d010104600161010104620163010106660167010200016c016d010200016e016f010106720173010200017401750101047801790101067a017b0101047e017f010106
            """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    
    def on_pause_until():
        pass
    pause_until(on_pause_until)
    
    music.stop_all_sounds()
    effects.blizzard.end_screen_effect()
    color.start_fade(color.original_palette, color.black, 250)
    pause(250)
    sprites.destroy(Title)
    BodyImagesArray = []
    BodyHealthArray = []
    BodySpeedArray = []
    BodyNamesArray = []
    BodyDescriptionsArray = []
    # Ammo Reload -
    # How much ammo should reload per second (100 = 1 ammo)
    AmmoReloadArray = [150, 200, 150, 100, 150, 130, 180, 100, 150]
    # Super Reload -
    # How many seconds it takes to reload (basically just a cooldown now
    SuperReloadArray = [10, 20, 5, 7, 20, 5, 15, 25, 20]
    DefineShape(assets.image("""
            myImage12
            """),
        70,
        120,
        "Dash",
        "SUPER: Shoot circles in all directions around you.",
        "Shoot a circle that bounces on walls.")
    DefineShape(assets.image("""
            myImage5
            """),
        130,
        85,
        "Basic Box",
        "SUPER: Heal some HP. Healing ammount lowers with each use.",
        "Shoot a close-ranged box. High damage.")
    DefineShape(assets.image("""
            myImage14
            """),
        100,
        100,
        "Dlitch",
        "SUPER: Shoot 4 high-damage stars around you.",
        "Shoot multiple stars in a spread pattern.")
    DefineShape(assets.image("""
            myImage6
            """),
        110,
        90,
        "CubeChick",
        "SUPER: Slam the ground, pushing enemies away.",
        "Slam the ground, damaging ALL enemies nearby. Long reload.")
    DefineShape(assets.image("""
            myImage9
            """),
        90,
        90,
        "Cubo",
        "SUPER: Shoot a bee that heals you on hit.",
        "Shoot many bees in front of you.")
    DefineShape(assets.image("""
            myImage7
            """),
        70,
        110,
        "Void",
        "SUPER: Dash through enemies with invincibility.",
        "Shoot a segmented beam with high damage. May require aiming.")
    DefineShape(assets.image("""
            myImage8
            """),
        110,
        95,
        "Feesh",
        "SUPER: Dive underwater to become invincible and faster briefly.",
        "Shoot bubbles ahead of you.")
    DefineShape(assets.image("""
            BodyFlame
            """),
        75,
        115,
        "Kirbo",
        "SUPER: Shoot waves of fire around you. Looong cooldown.",
        "Shoot a stream of fire ahead.")
    DefineShape(assets.image("""
            BodyArrow
            """),
        95,
        105,
        "Reflect",
        "SUPER: Dash to your cursor, then shoot arrows around.",
        "Shoot a fast arrow. Can hit from far away.")
    pause(5)
    if blockSettings.exists("SaveControls"):
        GamemodeSelect()
        color.start_fade(color.black, color.original_palette, 250)
    else:
        color.start_fade(color.black, color.original_palette, 0)
        sprites.destroy(Title)
        pause(20)
        if game.ask("Use PC controls?", "Change via menu."):
            blockSettings.write_string("SaveControls", "PC")
        else:
            blockSettings.write_string("SaveControls", "Mobile")
        color.start_fade(color.original_palette, color.black, 250)
        pause(250)
        GamemodeSelect()
        color.start_fade(color.black, color.original_palette, 250)
def ShootBullet(Angle: number, Image22: Image, Shooter: Sprite, Lifespan: number, Sped: number, Damage: number, NumberOfBullets: number, BulletDelay: number):
    
    def on_background8():
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                1600,
                1,
                255,
                76,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
    timer.background(on_background8)
    
    
    def on_throttle2():
        global Bullet
        for index2 in range(NumberOfBullets):
            Bullet = sprites.create(Image22, SpriteKind.projectile)
            Bullet.set_stay_in_screen(False)
            Bullet.z = -1
            if Bullet.image.equals(assets.image("""
                BodyWheely
                """)):
                Bullet.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
            else:
                Bullet.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            spriteutils.place_angle_from(Bullet, Angle, -4, Shooter)
            spriteutils.set_velocity_at_angle(Bullet, Angle, Sped)
            Bullet.lifespan = Lifespan
            sprites.set_data_number(Bullet, "Damage", Damage)
            Bullet.image.replace(1, 9)
            pause(BulletDelay)
    timer.throttle("Shooting", 10, on_throttle2)
    

def on_on_overlap4(sprite4, otherSprite4):
    spriteutils.set_velocity_at_angle(sprite4,
        spriteutils.angle_from(sprite4, otherSprite4),
        0 - 250)
    
    def on_throttle3():
        ObeliskHealthBar.value += 0 - sprites.read_data_number(sprite4, "Damage")
        scene.camera_shake(6, 400)
    timer.throttle("DamageObelisk", 100, on_throttle3)
    
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Obelisk, on_on_overlap4)

def on_display_updated(status2, image2):
    image2.draw_line(9, 0, 9, 9, 12)
    image2.draw_line(20, 0, 20, 9, 12)
    image2.draw_rect(0,
        0,
        image.get_dimension(image2, image.Dimension.WIDTH),
        image.get_dimension(image2, image.Dimension.HEIGHT),
        1)
statusbars.on_display_updated(StatusBarKind.Ammo, on_display_updated)

def on_mouse_move(x2, y2):
    if blockSettings.read_string("SaveControls") == "PC":
        if _1GameStarted:
            _3Cursor.set_position(x2 + (scene.camera_property(CameraProperty.X) - scene.screen_width() / 2),
                y2 + (scene.camera_property(CameraProperty.Y) - scene.screen_height() / 2))
browserEvents.on_mouse_move(on_mouse_move)

"""

Chaos Foretold by TeddyB!

"""
def Seigesong():
    pass

def on_menu_pressed():
    scene.openSystemMenu_block()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def Confirmation():
    global SelectionMenuConfirmation
    music.stop_all_sounds()
    easing.block_ease_to(SelectionMenuCombinationSprite,
        scene.screen_width() / 2,
        scene.screen_height() / 2,
        500,
        easing.Mode.IN_SINE)
    SelectionMenuText.set_text("Confirm setup?")
    SelectionMenuText.set_position(80, 8)
    SelectionMenuConfirmation = miniMenu.create_menu(miniMenu.create_menu_item("Yessir!"),
        miniMenu.create_menu_item("NO!!!"))
    SelectionMenuConfirmation.set_frame(assets.image("""
        MenuFrame
        """))
    SelectionMenuConfirmation.set_menu_style_property(miniMenu.MenuStyleProperty.ROWS, 2)
    SelectionMenuConfirmation.set_menu_style_property(miniMenu.MenuStyleProperty.COLUMNS, 1)
    SelectionMenuConfirmation.set_position(84, 100)
    
    def on_button_pressed9(selection9, selectedIndex9):
        if selectedIndex9 == 0:
            
            def on_background9():
                scene.camera_shake(2, 500)
            timer.background(on_background9)
            
            SelectionMenuText.set_text("Time to play!")
            SelectionMenuText.set_position(80, 8)
            SelectionMenuConfirmation.close()
            easing.block_ease_to(SelectionMenuCombinationSprite,
                scene.screen_width() / 2,
                -20,
                1000,
                easing.Mode.IN_CUBIC)
            
            def on_after5():
                color.start_fade(color.original_palette, color.black, 500)
                
                def on_after6():
                    sprites.destroy(SelectionMenuText)
                    sprites.destroy(SelectionMenuConfirmation)
                    sprites.destroy(SelectionMenuCombinationSprite)
                    StartGame()
                    color.start_fade(color.black, color.original_palette, 250)
                    Songs()
                timer.after(500, on_after6)
                
            timer.after(500, on_after5)
            
        else:
            SelectionMenuText.set_text("Let's start over...")
            SelectionMenuText.set_position(80, 8)
            easing.block_ease_to(SelectionMenuCombinationSprite,
                scene.screen_width() / 2,
                scene.screen_height() + 20,
                1000,
                easing.Mode.OUT_CIRC)
            SelectionMenuConfirmation.close()
            
            def on_after7():
                color.start_fade(color.original_palette, color.black, 500)
                
                def on_after8():
                    sprites.destroy(SelectionMenuConfirmation)
                    sprites.destroy(SelectionMenuCombinationSprite)
                    sprites.destroy(SelectionMenuText)
                    BodySelect()
                    color.start_fade(color.black, color.original_palette, 250)
                timer.after(500, on_after8)
                
            timer.after(500, on_after7)
            
    SelectionMenuConfirmation.on_button_pressed(controller.A, on_button_pressed9)
    
def Legacysong2():
    
    def on_background10():
        global Legacysong
        Legacysong = 1
    timer.background(on_background10)
    
def Wavessong():
    pass
def StartGame():
    global Menusongplay, _2BaseHealth, _2BaseSpeed, _3PlayerBody, _3PlayerWeapon, Hud, _3Cursor, _3HealthBar, _3AmmoBar, _3SuperBar, IsPlayerImmune, _1GameStarted, _3ScoreTracker, _1Score, _3Obelisk, ObeliskHealthBar
    music.stop_all_sounds()
    
    def on_background11():
        pass
    timer.background(on_background11)
    
    Menusongplay = 2
    _2BaseHealth = BodyHealthArray[_1Body]
    _2BaseSpeed = BodySpeedArray[_1Body]
    _3PlayerBody = sprites.create(BodyImagesArray[_1Body], SpriteKind.player)
    controller.move_sprite(_3PlayerBody, _2BaseSpeed, _2BaseSpeed)
    _3PlayerWeapon = sprites.create(BodyImagesArray[_1Weapon], SpriteKind.Weapon)
    _3PlayerWeapon.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    if _1Gamemode == 0:
        music.play(music.create_song(hex("""
                00b4000408020105001c000f0a006400f4010a0000040000000000000000000000000000000002600000000400012c04000800012a08000c0001290c001000012710001400012514001800012418001c0001221c002000012020002400011e24002800011d28002c00011b2c003000011930003400011834003800011638003c0001143c0040000112
                """)),
            music.PlaybackMode.UNTIL_DONE)
        tiles.set_current_tilemap(tilemap("""
            12x12
            """))
        scene.camera_follow_sprite(_3PlayerBody)
        music.play(music.create_song(hex("""
                00b4000408040205001c000f0a006400f4010a0000040000000000000000000000000000000002660000000400010508000c00010510001400010518001c00010520002400010528002c00010530003400010538003c00010840004400010548004c00010550005400010558005c00010560006400010568006c00010570007400010578007c0001057c008000010809010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800f700000001000400010206040005000106080009000500010206080c000d000106100011000400010206140015000106180019000500010206081c001d000106200021000400010206240025000106280029000500010206082c002d000106300031000400010206340035000106380039000500010206083c003d000106400041000400010206440045000106480049000500010206084c004d000106500051000400010206540055000106580059000500010206085c005d0001066000610004000102066400650001066800690004000102066c006d000106700071000500010206087400750001067800790004000102067c007d000106
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif _1Gamemode == 1:
        tiles.set_current_tilemap(tilemap("""
            12x12
            """))
        scene.camera_follow_sprite(_3PlayerBody)
    elif _1Gamemode == 2:
        tiles.set_current_tilemap(tilemap("""
            Siege
            """))
        scene.camera_follow_sprite(_3PlayerBody)
    elif _1Gamemode == 3:
        music.play(music.create_song(hex("""
                002c010408010206001c00010a006400f401640000040000000000000000000000000000000002060000000400010a07001c00020a006400f401640000040000000000000000000000000000000003060000000400010a
                """)),
            music.PlaybackMode.UNTIL_DONE)
        tiles.set_current_tilemap(tilemap("""
            Legacy
            """))
    scene.set_background_color(15)
    Hud = sprites.create(assets.image("""
        HUDbar
        """), SpriteKind.UI)
    Hud.set_position(80, 116)
    Hud.z = 99
    Hud.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    for value in tiles.get_tiles_by_type(assets.tile("""
        WallTile
        """)):
        tiles.set_wall_at(value, True)
    _3PlayerBody.set_position(tileUtil.tilemap_property(tileUtil.current_tilemap(), tileUtil.TilemapProperty.COLUMNS) * 16 / 2,
        tileUtil.tilemap_property(tileUtil.current_tilemap(), tileUtil.TilemapProperty.ROWS) * 16 / 2)
    tiles.place_on_random_tile(_3PlayerBody, assets.tile("""
        SiegeObeliskSpawn
        """))
    _3Cursor = sprites.create(assets.image("""
        crosshair
        """), SpriteKind.UI)
    _3HealthBar = statusbars.create(60, 5, StatusBarKind.health)
    _3HealthBar.set_color(9, 8)
    _3HealthBar.set_bar_border(1, 9)
    _3HealthBar.max = _2BaseHealth
    _3HealthBar.value = _2BaseHealth
    _3HealthBar.set_position(80, 117)
    _3HealthBar.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    _3HealthBar.z = 100
    _3AmmoBar = statusbars.create(30, 5, StatusBarKind.Ammo)
    _3AmmoBar.set_color(1, 12)
    _3AmmoBar.set_bar_border(1, 1)
    _3AmmoBar.max = 300
    _3AmmoBar.value = 300
    _3AmmoBar.attach_to_sprite(_3Cursor, -23, 0)
    _3SuperBar = statusbars.create(30, 5, StatusBarKind.SuperAmmo)
    _3SuperBar.set_color(9, 8)
    _3SuperBar.set_bar_border(1, 9)
    _3SuperBar.max = 100
    _3SuperBar.value = 100
    _3SuperBar.attach_to_sprite(_3Cursor, -28, 0)
    IsPlayerImmune = False
    _1GameStarted = True
    _3ScoreTracker = textsprite.create("Infinite", 0, 1)
    _3ScoreTracker.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    _3ScoreTracker.set_position(151, 116)
    _1Score = 0
    _3ScoreTracker.z = 100
    if _1Gamemode == 1 or _1Gamemode == 2:
        _3ScoreTracker.set_text("W:0")
    if _1Gamemode == 2:
        _3Obelisk = sprites.create(assets.image("""
                SiegeObelisk
                """),
            SpriteKind.Obelisk)
        ObeliskHealthBar = statusbars.create(50, 6, StatusBarKind.ObeliskHealth)
        ObeliskHealthBar.set_color(9, 8)
        ObeliskHealthBar.set_bar_border(1, 9)
        ObeliskHealthBar.attach_to_sprite(_3Obelisk)
        ObeliskHealthBar.max = 200
        ObeliskHealthBar.value = 200
        tiles.place_on_random_tile(_3Obelisk, assets.tile("""
            SiegeObeliskSpawn
            """))
        SiegeWaveManager()
    if _1Gamemode == 1:
        DefaultWaveManager()

def on_mouse_right_button_pressed(x3, y3):
    if _1GameStarted:
        if blockSettings.read_string("SaveControls") == "PC":
            SuperAtacj()
            
            def on_background12():
                music.play(music.create_sound_effect(WaveShape.NOISE,
                        1,
                        5000,
                        255,
                        255,
                        500,
                        SoundExpressionEffect.NONE,
                        InterpolationCurve.LINEAR),
                    music.PlaybackMode.UNTIL_DONE)
            timer.background(on_background12)
            
browserEvents.mouse_right.on_event(browserEvents.MouseButtonEvent.PRESSED,
    on_mouse_right_button_pressed)

def DefaultWaveManager():
    global _1Score, WaveStartText
    _1Score += 1
    _3ScoreTracker.set_text("W:" + str(_1Score))
    _3ScoreTracker.set_position(151 - ((len(convert_to_text(_1Score)) - 1) * 5 - (len(convert_to_text(_1Score)) - 1) * 2),
        116)
    WaveStartText = textsprite.create("WAVE " + str(_1Score), 15, 2)
    WaveStartText.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    WaveStartText.set_position(80, 12)
    WaveStartText.lifespan = 5000
    
    def on_background13():
        pause(1000)
        easing.block_ease_by(WaveStartText, 0, -100, 2000, easing.Mode.IN_BACK)
        if _1Score == 1:
            StartWave(5, [0])
        elif _1Score == 2:
            StartWave(7, [0, 0, 0, 1])
        elif _1Score == 3:
            StartWave(3, [1, 2, 3])
        elif _1Score == 4:
            StartWave(2, [2])
        elif _1Score == 5:
            StartWave(6, [1, 2, 1, 0, 3])
        elif _1Score == 6:
            StartWave(4, [4, 3, 3])
        elif _1Score == 7:
            StartWave(10, [0, 0, 0, 1])
        elif _1Score == 8:
            StartWave(5, [0, 1, 2, 3, 4])
        elif _1Score == 9:
            StartWave(5, [3])
        elif _1Score == 10:
            StartWave(15, [0, 0, 0, 0, 1, 1, 2, 3])
        elif _1Score == 11:
            StartWave(2, [3])
            StartWave(8, [4])
        elif _1Score == 12:
            StartWave(14, [4])
            StartWave(1, [0])
        elif _1Score == 13:
            StartWave(7, [3, 3, 2, 1])
        elif _1Score == 14:
            StartWave(8, [3, 1])
        elif _1Score == 15:
            StartWave(4, [2])
        else:
            StartWave(randint(4, 8) + Math.floor(_1Score / 10),
                [randint(0, 4), randint(1, 4), randint(1, 2), randint(2, 3)])
    timer.background(on_background13)
    

def on_on_overlap5(sprite5, otherSprite5):
    spriteutils.set_velocity_at_angle(otherSprite5,
        spriteutils.angle_from(sprite5, otherSprite5),
        310)
sprites.on_overlap(SpriteKind.DrillSuper, SpriteKind.enemy, on_on_overlap5)

def RegularAttacj():
    if _3AmmoBar.value >= 100:
        _3AmmoBar.value += -100
        if _1Weapon == 0:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    BodyWheely
                    """),
                _3PlayerWeapon,
                1750,
                150,
                125,
                1,
                0)
        elif _1Weapon == 1:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    BodyBoxer0
                    """),
                _3PlayerWeapon,
                200,
                250,
                200,
                1,
                0)
        elif _1Weapon == 2:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileStar
                    """),
                _3PlayerWeapon,
                650,
                300,
                25,
                3,
                0.4,
                2,
                100)
        elif _1Weapon == 3:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    DrillProjectile
                    """),
                _3PlayerWeapon,
                150,
                0,
                100,
                1,
                0)
        elif _1Weapon == 4:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileBee
                    """),
                _3PlayerWeapon,
                750,
                110,
                25,
                5,
                0.2,
                1,
                0)
        elif _1Weapon == 5:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    RhombusProjectile
                    """),
                _3PlayerWeapon,
                800,
                170,
                20,
                10,
                25)
        elif _1Weapon == 6:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileFeesh
                    """),
                _3PlayerWeapon,
                1000,
                130,
                45,
                3,
                0.2,
                1,
                0)
        elif _1Weapon == 7:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileFlame
                    """),
                _3PlayerWeapon,
                500,
                150,
                10,
                3,
                0.2,
                4,
                30)
        elif _1Weapon == 8:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileArrow
                    """),
                _3PlayerWeapon,
                1500,
                170,
                125,
                1,
                0)

def on_on_destroyed(sprite6):
    global _1Score
    if _1Gamemode == 1:
        if len(sprites.all_of_kind(SpriteKind.enemy)) == 0:
            DefaultWaveManager()
            _3HealthBar.value += 10
    if _1Gamemode == 2:
        if len(sprites.all_of_kind(SpriteKind.enemy)) == 0:
            SiegeWaveManager()
    if _1Gamemode == 0 or _1Gamemode == 3:
        _1Score += 1
        _3ScoreTracker.set_text("S:" + str(_1Score))
        _3ScoreTracker.set_position(151 - ((len(convert_to_text(_1Score)) - 1) * 5 - (len(convert_to_text(_1Score)) - 1) * 2),
            116)
    music.play(music.create_sound_effect(WaveShape.NOISE,
            5000,
            1,
            72,
            255,
            500,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_overlap6(sprite7, otherSprite6):
    if sprite7.image.equals(assets.image("""
        DrillProjectile
        """)):
        if not (sprites.read_data_boolean(otherSprite6, "HitRecently")):
            sprites.set_data_boolean(otherSprite6, "HitRecently", True)
            statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite6).value += 0 - sprites.read_data_number(sprite7, "Damage")
            
            def on_background14():
                
                def on_after9():
                    sprites.set_data_boolean(otherSprite6, "HitRecently", False)
                timer.after(150, on_after9)
                
            timer.background(on_background14)
            
    else:
        sprites.destroy(sprite7)
        statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite6).value += 0 - sprites.read_data_number(sprite7, "Damage")
    if statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite6).value <= 0:
        sprites.destroy(otherSprite6)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap6)

def on_on_overlap7(sprite8, otherSprite7):
    if not (IsPlayerImmune):
        if _1Gamemode == 3:
            _3HealthBar.value += 0 - 0.4
        else:
            spriteutils.set_velocity_at_angle(sprite8,
                spriteutils.angle_from(sprite8, otherSprite7),
                0 - 150)
            
            def on_throttle4():
                _3HealthBar.value += 0 - sprites.read_data_number(sprite8, "Damage")
                scene.camera_shake(2, 200)
            timer.throttle("damage", 200, on_throttle4)
            
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap7)

def ShootBulletWallPattern(Angle2: number, Image23: Image, Shooter2: Sprite, Lifespan2: number, Sped2: number, Damage2: number, NumberOfBullets2: number, BulletSpacing: number, Repetitions: number, RepetitionDelay: number):
    global AngleIncrement, Bullet, TempImage
    for index3 in range(Repetitions):
        if NumberOfBullets2 % 2 == 1:
            AngleIncrement = 0 - BulletSpacing * Math.floor(NumberOfBullets2 / 2)
        else:
            AngleIncrement = 0 - BulletSpacing * Math.floor(NumberOfBullets2 / 2)
            AngleIncrement += BulletSpacing / 2
        for index4 in range(NumberOfBullets2):
            Bullet = sprites.create(Image23, SpriteKind.projectile)
            Bullet.set_stay_in_screen(False)
            Bullet.z = -1
            if Bullet.image.equals(assets.image("""
                BodyWheely
                """)):
                Bullet.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
            else:
                Bullet.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            TempImage = Bullet.image.clone()
            TempImage.replace(1, 9)
            Bullet.set_image(TempImage)
            spriteutils.place_angle_from(Bullet, Angle2 + AngleIncrement, -4, Shooter2)
            spriteutils.set_velocity_at_angle(Bullet, Angle2 + AngleIncrement, Sped2)
            Bullet.lifespan = Lifespan2
            sprites.set_data_number(Bullet, "Damage", Damage2)
            AngleIncrement += BulletSpacing
        pause(RepetitionDelay)
def SuperAtacj():
    global _1HealingDecay, Bullet, IsPlayerImmune
    if _3SuperBar.value >= 99.5:
        _3SuperBar.value = 0
        if _1Body == 0:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    BodyWheely
                    """),
                _3PlayerBody,
                2500,
                100,
                50,
                12,
                100,
                1,
                0)
        elif _1Body == 1:
            _3PlayerBody.start_effect(effects.hearts, 500)
            for index5 in range(5):
                _3HealthBar.value += 8 - min(_1HealingDecay, 7)
                pause(5)
            _1HealingDecay += 1.5
        elif _1Body == 2:
            ShootBulletWallPattern(spriteutils.degrees_to_radians(45),
                assets.image("""
                    BodyStar
                    """),
                _3PlayerBody,
                1000,
                200,
                100,
                4,
                33,
                1,
                0)
        elif _1Body == 3:
            Bullet = sprites.create(assets.image("""
                    DrillSuper
                    """),
                SpriteKind.DrillSuper)
            Bullet.z = -1
            spriteutils.place_angle_from(Bullet, 0, 0, _3PlayerBody)
            Bullet.lifespan = 150
        elif _1Body == 4:
            ShootBullet(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileBee
                    """),
                _3PlayerBody,
                3500,
                110,
                150,
                1,
                0)
            Bullet.image.replace(9, 7)
            Bullet.set_kind(SpriteKind.HealBullet)
        elif _1Body == 5:
            IsPlayerImmune = True
            controller.move_sprite(_3PlayerBody, 0, 0)
            spriteutils.set_velocity_at_angle(_3PlayerBody,
                spriteutils.angle_from(_3PlayerBody, _3Cursor),
                350)
            
            def on_after10():
                global IsPlayerImmune
                IsPlayerImmune = False
                spriteutils.set_velocity_at_angle(_3PlayerBody, 0, 0)
                controller.move_sprite(_3PlayerBody, _2BaseSpeed, _2BaseSpeed)
            timer.after(200, on_after10)
            
        elif _1Body == 6:
            
            def on_throttle5():
                global IsPlayerImmune
                IsPlayerImmune = True
                _3PlayerBody.set_image(assets.image("""
                    FeeshDive
                    """))
                controller.move_sprite(_3PlayerBody, _2BaseSpeed + 50, _2BaseSpeed + 50)
                
                def on_after11():
                    global IsPlayerImmune
                    IsPlayerImmune = False
                    _3PlayerBody.set_image(BodyImagesArray[_1Body])
                    controller.move_sprite(_3PlayerBody, _2BaseSpeed, _2BaseSpeed)
                timer.after(3000, on_after11)
                
            timer.throttle("FisjDive", 3000, on_throttle5)
            
        elif _1Body == 7:
            ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                assets.image("""
                    ProjectileFlame
                    """),
                _3PlayerBody,
                750,
                60,
                10,
                24,
                500,
                7,
                250)
        elif _1Body == 8:
            controller.move_sprite(_3PlayerBody, 0, 0)
            if not (tiles.tile_at_location_is_wall(_3Cursor.tilemap_location())):
                _3PlayerBody.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            spriteutils.move_to(_3PlayerBody, spriteutils.pos(_3Cursor.x, _3Cursor.y), 350)
            
            def on_after12():
                _3PlayerBody.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, False)
                controller.move_sprite(_3PlayerBody, _2BaseSpeed, _2BaseSpeed)
                ShootBulletWallPattern(spriteutils.angle_from(_3PlayerBody, _3Cursor),
                    assets.image("""
                        ProjectileArrow
                        """),
                    _3PlayerBody,
                    1400,
                    120,
                    50,
                    6,
                    200,
                    1,
                    0)
            timer.after(350, on_after12)
            
def StartWave(EnemyCount: number, EnemyArray: List[number]):
    
    def on_background15():
        pass
    timer.background(on_background15)
    
    for index6 in range(EnemyCount):
        EnemyFactory(EnemyArray._pick_random())

def on_addsystemmenuentry_block2():
    if blockSettings.exists("SaveControls"):
        if blockSettings.read_string("SaveControls") == "PC":
            blockSettings.write_string("SaveControls", "Mobile")
        else:
            blockSettings.write_string("SaveControls", "PC")
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.UNTIL_DONE)
scene.addSystemMenuEntry_block(img("""
        . . . b b b b b b b b b . . . .
        . . b 1 d d d d d d d 1 b . . .
        . b 1 1 1 1 1 1 1 1 1 1 1 b . .
        . b d b c c c c c c c b d b . .
        . b d c 9 9 9 9 9 9 9 c d b . .
        . b d c 9 d 9 9 9 9 9 c d b . .
        . b d c 9 9 9 9 9 9 9 c d b . .
        . b d c 9 9 9 9 9 9 9 c d b . .
        . b d c 9 9 9 9 9 9 9 c d b . .
        . b d c c c c c c c c c d b . .
        . c b b b b b b b b b b b c . .
        c b c c c c c c c c c c c b c .
        c 1 d d d d d d d d d d d 1 c .
        c 1 d 1 1 d 1 1 d 1 1 d 1 1 c .
        c b b b b b b b b b b b b b c .
        c c c c c c c c c c c c c c c .
        """),
    "SWITCH CONTROLS",
    on_addsystemmenuentry_block2)

def on_on_zero2(status3):
    death()
statusbars.on_zero(StatusBarKind.ObeliskHealth, on_on_zero2)

def on_overlap_tile(sprite9, location):
    if not (sprites.has_flag(_3PlayerBody, SpriteFlag.GHOST_THROUGH_WALLS)):
        if not (tiles.tile_at_location_is_wall(_3PlayerBody.tilemap_location())):
            tiles.place_on_tile(_3PlayerBody, _3PlayerBody.tilemap_location())
        elif not (tiles.tile_at_location_is_wall(_3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.TOP))):
            tiles.place_on_tile(_3PlayerBody,
                _3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.TOP))
        elif not (tiles.tile_at_location_is_wall(_3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.LEFT))):
            tiles.place_on_tile(_3PlayerBody,
                _3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.LEFT))
        elif not (tiles.tile_at_location_is_wall(_3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.RIGHT))):
            tiles.place_on_tile(_3PlayerBody,
                _3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.RIGHT))
        elif not (tiles.tile_at_location_is_wall(_3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM))):
            tiles.place_on_tile(_3PlayerBody,
                _3PlayerBody.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        WallTile
        """),
    on_overlap_tile)

_1HealingDecay = 0
TempImage: Image = None
AngleIncrement = 0
_3SuperBar: StatusBarSprite = None
_3AmmoBar: StatusBarSprite = None
Hud: Sprite = None
_2BaseHealth = 0
Menusongplay = 0
Legacysong = 0
SelectionMenuConfirmation: miniMenu.MenuSprite = None
_3Cursor: Sprite = None
ObeliskHealthBar: StatusBarSprite = None
Bullet: Sprite = None
SuperReloadArray: List[number] = []
AmmoReloadArray: List[number] = []
Title: Sprite = None
Enemycatalogmenu: miniMenu.MenuSprite = None
_2BaseSpeed = 0
_3PlayerWeapon: Sprite = None
RespawnText: TextSprite = None
Playgameoversong = False
Songchoice = 0
_3HealthBar: StatusBarSprite = None
IsPlayerImmune = False
GameOverMenu: miniMenu.MenuSprite = None
WaveStartText: TextSprite = None
_3ScoreTracker: TextSprite = None
_1Score = 0
_1GameStarted = False
_3EnemyHealthBar: StatusBarSprite = None
_3Obelisk: Sprite = None
_1Gamemode = 0
_3PlayerBody: Sprite = None
_3Enemy: Sprite = None
_1Weapon = 0
SelectionMenuWeapons: miniMenu.MenuSprite = None
WeaponDescriptionsArray: List[str] = []
Themeselection = 0
Thememenu: miniMenu.MenuSprite = None
SelectionMenuGamemode: miniMenu.MenuSprite = None
SelectionMenuText: TextSprite = None
BodyDescriptionsArray: List[str] = []
BodySpeedArray: List[number] = []
BodyHealthArray: List[number] = []
SelectionMenuCombinationSprite: Sprite = None
_1Body = 0
SelectionMenuBodies: miniMenu.MenuSprite = None
BodyImagesArray: List[Image] = []
BodyNamesArray: List[str] = []
TempNumber = 0
SelectionMenuBodiesArray: List[miniMenu.MenuItem] = []
Startscreen()

def on_update_interval():
    if _1GameStarted:
        _3AmmoBar.value += AmmoReloadArray[_1Weapon] / 10
        _3SuperBar.value += 100 / (SuperReloadArray[_1Body] * 10)
game.on_update_interval(100, on_update_interval)

def on_update_interval2():
    if _1GameStarted:
        if _1Gamemode == 0:
            if Math.percent_chance(40):
                EnemyFactory(0)
            else:
                EnemyFactory([0, 1, 2, 3, 4]._pick_random())
game.on_update_interval(1500, on_update_interval2)

def on_update_interval3():
    for value2 in sprites.all_of_kind(SpriteKind.enemy):
        if sprites.read_data_number(value2, "EnemyID") == 4:
            for value22 in sprites.all_of_kind(SpriteKind.enemy):
                if spriteutils.distance_between(value2, value22) <= 45:
                    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, value22).value += 10
                    value22.start_effect(effects.hearts, 100)
game.on_update_interval(250, on_update_interval3)

# Boss Fight by TeddyB!

def on_forever():
    if Legacysong == 1:
        pass
forever(on_forever)

def on_forever2():
    if Playgameoversong:
        music.play(music.create_song(hex("""
                0078000408040208001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80036006000610001036400650001036800690001086c006d0001066e006f000105700071000106720073000105740075000103780079000108
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040307001c00020a006400f4016400000400000000000000000000000000000000032a0008001000011610002000011820003000011930004000011b40005000011960007000011970008000011808001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80081010000010001030200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f401640000040000000000000000000000000005000004780012001400012214001600012016001800011e18001a00011d1c001e0001a120002200012232003400012234003600012036003800011e38003a00011d3c003e00011b40004200011952005400011954005600011b56005800011d58005a00011e5c005e00011d60006200011e7000720001a178007a00011d05001c000f0a006400f4010a00000400000000000000000000000000000000023c000400080001220c00100001222400280001222c003000012238003c0001244400480001254c00500001256400680001276c007000012778007c00012907001c00020a006400f4016400000400000000000000000000000000000000032a0008001000011610002000011820003000011930004000011b40005000011960007000011970008000011808001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80081010000010001030200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f401640000040000000000000000000000000005000004780012001400012214001600012016001800011e18001a00011d1c001e0001a120002200012232003400012234003600012036003800011e38003a00011d3c003e00011b40004200011952005400011954005600011b56005800011d58005a00011e5c005e00011d60006200011e7000720001a178007a00011d05001c000f0a006400f4010a00000400000000000000000000000000000000023c000400080001220c00100001222400280001222c003000012238003c0001244400480001254c00500001256400680001276c007000012778007c00012907001c00020a006400f401640000040000000000000000000000000000000003330008001000011610002000011820003000011930004000011b40005000011d50006000011b6000700002191e7000800003181da108001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80081010000010001030200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f401640000040000000000000000000000000005000004200100000200011602000400011b04000600011d08000a0001160a000c00011b0c000e00011d10001200019512001400011b14001600011d18001a0001951a001c00011b1c001e00011d20002200011422002400011b24002600011d28002a0001142a002c00011b2c002e00011d30003200019332003400011b34003600011d38003a0001933a003c00011b3c003e00011d40004200011642004400011b44004600011d48004a0001164a004c00011b4c004e00011d50005200011452005400011b54005600011d58005a0001145a005c00011b5c005e00011d60006200011262006400011b64006600011d68006a0001126a006c00011b6c006e00011d70007200011172007400011b74007600011d78007a0001147a007c00011b7c007e00011d05001c000f0a006400f4010a0000040000000000000000000000000000000002300000001000012210002000012420003000012530004000012740005000012550006000012760007000012570008000012407001c00020a006400f40164000004000000000000000000000000000000000338000000080003161d2208001000011610002000019520003000011430004000019340005000011250006000011160007000019070008000011108001c000e050046006603320000040a002d00000064001400013200020100020c0000001000010a40005000010609010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8009a000000010001030400050001030800090001080e000f000103140015000103180019000203082000210001032400250001032800290001082e002f000103340035000103380039000203083e003f0001034000410001034400450001034800490001084e004f0001035400550001035800590002030860006100010364006500010368006900010870007100010374007500010378007900020308
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f4016400000400000000000000000000000000050000041c0100000200011602000400011b04000600011d08000a0001160a000c00011b0c000e00011d10001200019512001400011b14001600011d18001a0001951a001c00011b1c001e00011d20002200011422002400011b24002600011d28002a0001142a002c00011b2c002e00011d30003200019332003400011b34003600011d38003a0001933a003c00011b3c003e00011d40004200011642004400011b44004600011d48004a0001164a004c00011b4c004e00011d50005200011452005400011b54005600011d58005a0001145a005c00011b5c005e00011d60006200011262006400011b64006600011d68006a0001126a006c00011b6c006e00011d70007200011172007400011b74007600020f1d760078000120780080000211a105001c000f0a006400f4010a0000040000000000000000000000000000000002300000001000012210002000012420003000012530004000012740005000012550006000012760007000012570008000012407001c00020a006400f401640000040000000000000000000000000000000003300008001000011610002000019520003000011430004000019340005000011250006000011160007000019070008000011108001c000e050046006603320000040a002d00000064001400013200020100020c0000001000010a40005000010609010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800da0000000100020305040005000103080009000205080e000f000103100011000105140015000103180019000303050820002100020305240025000103280029000205082e002f00010330003100010534003500010338003900030305083e003f0001034000410002030544004500020305480049000205084c004d0001054e004f0001035000510001055400550002030558005900030305085c005d0001056000610002030562006300010564006500020305660067000105680069000205086a006b0001056c006d0001056e006f000105700071000403050708
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f40164000004000000000000000000000000000500000440000000100003161d221000200003141b242000300003121e25300040000395a1274000500003161d255000600003111b246000700003121d257000800003951e2705001c000f0a006400f4010a0000040000000000000000000000000000000002600004000800012508000c00012714001800012518001c00012724002800012528002c00012734003800012538003c00012744004800012548004c00012754005800012558005c00012764006800012568006c00012774007800012578007c00012707001c00020a006400f401640000040000000000000000000000000000000003300008001000011610001800011818002000011920003000011b30004000011d40005000011960007000011970008000011b08001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010c40005000010d50006000010d60007000010f70008000011109010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800bb00000001000203040400050001060800090001060c000d0002030410001100020708140015000106180019000106200021000203042400250001062800290001062c002d0002030430003100020708340035000106380039000106400041000203044400450001064800490001064c004d0002030450005100020708540055000106580059000106600061000203046400650001066800690001066c006d00020304700071000207087400750001067800790001067c007d00020708
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040600001c00010a006400f40164000004000000000000000000000000000500000440000000100003161d221000200003141b242000300003121e25300040000395a1274000500003161d255000600003111b246000700003121d257000800003951e2702001c000c960064006d019001000478002c010000640032000000000a060005240000001000012910002000012720003000012a30005000012960007000012c70008000012a05001c000f0a006400f4010a0000040000000000000000000000000000000002600004000800012508000c00012714001800012518001c00012724002800012528002c00012734003800012538003c00012744004800012548004c00012754005800012558005c00012764006800012568006c00012774007800012578007c00012707001c00020a006400f401640000040000000000000000000000000000000003300008001000011610001800011818002000011920003000011b30004000011d40005000011960007000011970008000011b08001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010c40005000010d50006000010d60007000010f70008000011109010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800bd00000001000203040400050001060800090001060c000d0002030410001100020708140015000106180019000106200021000203042400250001062800290001062c002d0002030430003100020708340035000106380039000106400041000203044400450001064800490001064c004d0002030450005100020708540055000106580059000106600061000203046400650001066800690001066c006d000203047000710002070874007500020708780079000207087c007d00020708
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040307001c00020a006400f4016400000400000000000000000000000000000000032a0008001000011610002000011820003000011930004000011b40005000011960007000011970008000011808001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80081010000010001030200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f401640000040000000000000000000000000005000004780012001400012214001600012016001800011e18001a00011d1c001e0001a120002200012232003400012234003600012036003800011e38003a00011d3c003e00011b40004200011952005400011954005600011b56005800011d58005a00011e5c005e00011d60006200011e7000720001a178007a00011d05001c000f0a006400f4010a00000400000000000000000000000000000000023c000400080001220c00100001222400280001222c003000012238003c0001244400480001254c00500001256400680001276c007000012778007c00012907001c00020a006400f4016400000400000000000000000000000000000000032a0008001000011610002000011820003000011930004000011b40005000011960007000011970008000011808001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80081010000010001030200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040500001c00010a006400f401640000040000000000000000000000000005000004600006000800011b08000a00011d16001800011b18001a00011d26002800011b28002a00011d36003800011b38003a00011d46004800011b48004a00011d56005800011b58005a00011d66006800011b68006a00011d76007800011b78007a00011d03001c0001dc00690000045e0100040000000000000000000005640001040003240010002000011620003000011930004000011b40005000011d60007000011e7000800001a107001c00020a006400f401640000040000000000000000000000000000000003c00000000400011604000800011808000c0001190c001000011b10001400011614001800011818001c0001191c002000011b20002400011624002800011828002c0001192c003000011b30003400011634003800011838003c0001193c004000011b40004400011644004800011848004c0001194c005000011b50005400011654005800011858005c0001195c006000011b60006400011664006800011868006c0001196c007000011b70007400011674007800011978007c00011d7c00800001a108001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010c20003000010d30004000010f40005000011150006000011260007000011470008000019509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800ea000000010001030400050001030800090001080c000d0001060e000f0001031200130001061400150001031800190001081c001d0001062000210001032400250001032800290001082c002d0001062e002f0001033200330001063400350001033800390001083c003d0001064000410001034400450001034800490001084c004d0001064e004f0001035000510001065200530001065400550001035800590001085c005d0001066000610001036400650001036800690001086c006d0001066e006f0001037200730001067400750001037800790001087a007b0001067c007d0001037e007f000108
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040700001c00010a006400f401640000040000000000000000000000000005000004540006000800011b08000a00011d16001800011b18001a00011d26002800011b28002a00011d36003800011b38003a00011d46004800011b48004a00011d66006800011b68006a00011d76007800011b78007a00011d02001c000c960064006d019001000478002c010000640032000000000a060005360010002000012c20003000012a30004000012950005400012a54005800012958005c0001275c006000012960007000012770008000012903001c0001dc00690000045e01000400000000000000000000056400010400032b0000001000012210002000012420003000012530004000012740005000012960007000012a7000800002a12505001c000f0a006400f4010a00000400000000000000000000000000000000022a0000001000012210002000012020003000012230004000012440005000012560007000012470008000012507001c00020a006400f401640000040000000000000000000000000000000003a80000000400011604000800011808000c0001190c001000011b10001400011614001800011818001c0001191c002000011b20002400011624002800011828002c0001192c003000011b30003400011634003800011838003c0001193c004000011b40004400011644004800011848004c0001194c005000011b60006400011664006800011868006c0001196c007000011b70007400011674007800011978007c00011d7c00800001a108001c000e050046006603320000040a002d0000006400140001320002010002310000001000010a10002000010c20003000010d30004000010f4000500001115000600002081260007000011470008000019509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80006010000010001030400050001030800090001080c000d0001060e000f0001031200130001061400150001031800190001081c001d0001062000210001032400250001032800290001082c002d0001062e002f0001033200330001063400350001033800390001083c003d0001064000410001034400450001034800490001084c004d0001064e004f00010350005100060304050607085200530001055400550001035600570001055800590001035a005b0001055c005d0001035e005f00010560006100060304050607086400650001036800690001086c006d0001066e006f0001037200730001067400750001037800790001087a007b0001067c007d0001037e007f000108
                """)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_song(hex("""
                0078000408040600001c00010a006400f40164000004000000000000000000000000000500000407000000080002162202001c000c960064006d019001000478002c010000640032000000000a060005060000001000012205001c000f0a006400f4010a0000040000000000000000000000000000000002060000001000011607001c00020a006400f401640000040000000000000000000000000000000003300000000800012208001000011610002000011820003000011930004000011b40005000011960007000011970008000011808001c000e050046006603320000040a002d0000006400140001320002010002300000001000010a10002000010520003000010a30004000010540005000010650006000010660007000018970008000010509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800860100000100060304050607080200030001060400050001030600070001060800090001080a000b0001060c000d0001060e000f0001081000110001061200130001081400150001061600170001031800190001081a001b0001061c001d0001031e001f0001062000210001032200230001062400250001032600270001062800290001082a002b0001062c002d0001062e002f0001083000310001063200330001083400350001063600370001033800390001083a003b0001063c003d0001033e003f0001064000410001034200430001064400450001034600470001064800490001084a004b0001064c004d0001064e004f0001085000510001065200530001085400550001065600570001035800590001085a005b0001065c005d0001035e005f0001066000610001036200630001066400650001036600670001066800690001086a006b0001066c006d0001066e006f000108700071000106720073000108740075000106760077000103780079000206087a007b0001067c007d0001067e007f000106
                """)),
            music.PlaybackMode.UNTIL_DONE)
forever(on_forever2)

def on_forever3():
    pass
forever(on_forever3)

# Dynamical by InvalidProject!

def on_forever4():
    pass
forever(on_forever4)

def on_update_interval4():
    global Bullet
    if _1GameStarted:
        if _1Gamemode == 3:
            if Math.percent_chance(60):
                EnemyFactory(0)
            else:
                EnemyFactory([0, 1, 2, 3]._pick_random())
        for value3 in sprites.all_of_kind(SpriteKind.enemy):
            if sprites.read_data_number(value3, "EnemyID") == 2:
                Bullet = sprites.create(assets.image("""
                        TriBullet
                        """),
                    SpriteKind.EnemyBullet)
                Bullet.set_stay_in_screen(False)
                Bullet.z = -1
                Bullet.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
                spriteutils.place_angle_from(Bullet, 0, 0, value3)
                spriteutils.set_velocity_at_angle(Bullet, spriteutils.angle_from(value3, _3PlayerBody), 65)
                Bullet.lifespan = 3000
                sprites.set_data_number(Bullet, "Damage", 15)
game.on_update_interval(1000, on_update_interval4)

def on_on_update():
    if _1GameStarted:
        spriteutils.place_angle_from(_3PlayerWeapon,
            spriteutils.angle_from(_3PlayerBody, _3Cursor),
            20,
            _3PlayerBody)
        if blockSettings.read_string("SaveControls") == "Mobile":
            if controller.up.is_pressed():
                _3Cursor.set_position(_3PlayerBody.x, _3PlayerBody.y - 45)
            elif controller.down.is_pressed():
                _3Cursor.set_position(_3PlayerBody.x, _3PlayerBody.y + 45)
            elif controller.left.is_pressed():
                _3Cursor.set_position(_3PlayerBody.x - 45, _3PlayerBody.y)
            elif controller.right.is_pressed():
                _3Cursor.set_position(_3PlayerBody.x + 45, _3PlayerBody.y)
        for value4 in sprites.all_of_kind(SpriteKind.projectile):
            if tiles.tile_at_location_is_wall(value4.tilemap_location()):
                sprites.destroy(value4)
game.on_update(on_on_update)
