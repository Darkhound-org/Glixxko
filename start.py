from art import *
def main():
    from tqdm import tqdm
    import logging
    import contextlib
    import time
    import os
    with contextlib.redirect_stdout(None):
          import pygame
    from pygame import mixer
    cwd = os.getcwd()
    if not os.path.exists("Logs"):
       os.makedirs("Logs")

    log_dir = cwd+"\Logs\start.log"   
    logging.basicConfig(filename=log_dir, level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="w")   
    mixer.init()    
    mixer.music.load(cwd+'\elements\sfx_sound_poweron.wav')    
    mixer.music.play() 
    art_start=text2art("GLIXXKO")
    for i in tqdm (range (51), 
                desc="Launching Glixxko....", 
                ascii=False, ncols=100):
        time.sleep(0.03)
    mixer.init()    
    mixer.music.load(cwd+'\elements\sfx_sound_poweron.wav')    
    mixer.music.play() 
    logging.info("Called 'start.exe' . Progress bar loaded.Application ready for launch.") 
    print(art_start , "\xa9 2022") , print("Darkhound-org")
    logging.info("Launched version DDMMHH. , Executable directory: {0}".format(cwd))
if __name__ == "__main__":
    main()   