from time import time


def main():
    import easygui
    import os
    import logging
    import contextlib
    import ffpb
    import subprocess
    import time
    with contextlib.redirect_stdout(None):
          import pygame
    from pygame import mixer
    cwd = os.getcwd()
    if not os.path.exists("Logs"):
       os.makedirs("Logs")

    lok_dir = cwd+"/Logs/mkv.log"
    logging.basicConfig(filename=lok_dir, level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="w")
   
    logging.info("Called 'mkv.py'")   
    logging.info("User input '3'")
    try: 

                media_t_mkv = input("Path to input file [default: file dialog]:") or easygui.fileopenbox()
                out_media_wex = input("Output file name [default: output-mkv]: ") or "output-mkv"
                out_media = out_media_wex+".mkv"
                command ='ffpb -i ' + media_t_mkv +' '+ out_media +' '+ '-qscale 0'
                subprocess.run(command)
                    

                print("Process completed...!") 
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_coin_double1.wav')
                mixer.music.play()
                logging.info(media_t_mkv+" succesfully converted to"+ out_media)
                time.sleep(0.1)   

    except FileNotFoundError:
        print("!...File not found...! Check log for details.") 
        logging.info("File required for conversion not found. Operation cancelled..!")
        mixer.init()
        mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
        mixer.music.play()
        time.sleep(0.1)

    except TypeError:
        print("No files selected.") 
        mixer.init()
        mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
        mixer.music.play()
        logging.info("User canceled the operation.")
        time.sleep(0.1)

    except ValueError:
        print("Invalid input..!")  
        time.sleep(0.1)   

if __name__=="__main__":
    main()        

