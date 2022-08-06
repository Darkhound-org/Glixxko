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
    
    lovp_dir = cwd+"/Logs/webm.log"
    logging.basicConfig(filename=lovp_dir, level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="w")
    logging.info("Called 'webm.py'")   
    logging.info("User input '9'")
    try: 

                media_t_webm = input("Path to input file [default: file dialog]: ") or easygui.fileopenbox()
                out_media_wex = input("Output file name [default: output-webm]: ") or "output-webm"
                out_media = out_media_wex+".webm"
                command ='ffpb -i ' + media_t_webm +' '+ out_media +' '+ '-qscale 0'
                subprocess.run(command)
                
                    

                print("Process completed...!") 
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_coin_double1.wav')
                mixer.music.play()
                logging.info(media_t_webm+" succesfully converted to"+ out_media)   
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
        logging.info("User canceled the operation. ") 
        time.sleep(0.1) 

    except ValueError:
        print("Invalid input..!") 
        time.sleep(0.1) 

if __name__=="__main__":
    main()


