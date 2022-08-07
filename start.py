from art import *
def main():
    from tqdm import tqdm
    import logging
    import contextlib
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    import time
    import os
    from rich.progress import track
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
    def process_data():
        time.sleep(0.03)
    for _ in track(range(51), description='[blue]Launching GLIXXKO...'):
              process_data()
    mixer.init()    
    mixer.music.load(cwd+'\elements\sfx_sound_poweron.wav')    
    mixer.music.play() 
    logging.info("Called 'start.py' . Progress bar loaded.Project ready.") 
    
    print(art_start,"\xa9 2022") , print("Darkhound-org")
    logging.info("Launched version 071039.")

if __name__ == "__main__":
    main()   
