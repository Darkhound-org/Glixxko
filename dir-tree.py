# app to list the recquired dir tree of Glixxko
print("""

Glixxko/
    |
    |--- elements/
    |            |
    |            |--- info.txt
    |            |--- sfx_coin_double1.wav
    |            |--- sfx_menu_move4.wav
    |            |--- sfx_sounds_error1.wav
    |            |--- sfx_sounds_interaction21.wav
    |            |--- sfx_sounds_pause4_in.wav
    |            |--- sfx_sound_poweron.wav
    |            └── sfx_sound_shutdown1.wav
    |
    |---    .gitattributes
    |---     avi.py
    |---    choice.py
    |---     console.py
    |---     elements
    |---     ffmpeg.exe
    |---     flv.py
    |---     gif.py
    |---     LICENSE
    |---     m4v.py
    |---     main.py
    |---     mkv.py
    |---     mov.py
    |---     mp4.py
    |---     README.md
    |---     requirements.txt
    |---     runtime.txt
    |---     start.py
    |---     ts.py
    |---     version-info.txt
    |---     webm.py
    |---     dir-tree.exe
    └──     wmv.py







""")
list_t = []
ch = 0
while ch !="q":
    ch =input("Do you want to quit? [s(stay)/q(quit)][default: s(stay)] ")
    if ch =="s":
        pass

    elif ch =="":
        pass

    elif  ch =="q":
     
       break