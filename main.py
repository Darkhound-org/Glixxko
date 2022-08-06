# main file 
# Executes other scripts using subprocess.call()
def main():
     import subprocess
     import os
     import time
     from rich.logging import RichHandler
     cwd = os.getcwd()
     import logging
     import contextlib
     with contextlib.redirect_stdout(None):
          import pygame
     from pygame import mixer
     from console import console
     logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
     log = logging.getLogger("rich")
     log.info("'main.py' calling all scripts.")               

     try:
        subprocess.call("start.py", shell=True)        

     except FileNotFoundError:    
        log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
        log.exception("Operation cancelled..!!!")
        mixer.init()
        mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
        mixer.music.play()      

     try:
        subprocess.call("choice.py", shell=True)

     except FileNotFoundError:    
        log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
        log.exception("Operation cancelled..!!!")
        mixer.init()
        mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
        mixer.music.play()  

     list_2 =[]
     choice = 0 
     while choice != "11": 
        choice = console.input(">> ") 
        if choice == "1":
            try:
                log.info("Calling 'mov.py'...") 
                subprocess.call("mov.py", shell=True)
            except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()  

        elif choice =="2":


            try: 
               log.info("Calling 'mp4.py'...")
               subprocess.call("mp4.py", shell=True)  
            except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()  

        elif choice =="3":
            try: 
               log.info("Calling 'mkv.py'...")
               subprocess.call("mkv.py", shell=True)  
            except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()  

        elif choice =="4":
          try: 
               log.info("Calling 'avi.py'...")
               subprocess.call("avi.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()  

        elif choice =="5":
                    
          try: 
               log.info("Calling 'm4v.py'...")
               subprocess.call("m4v.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()  

        elif choice =="6":
          try: 
               log.info("Calling 'wmv.py'...")
               subprocess.call("wmv.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play() 

        elif choice =="7":
          try: 
               log.info("Calling 'flv.py'...")
               subprocess.call("flv.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play() 

        elif choice =="8":
          try: 
               log.info("Calling 'ts.py'...")
               subprocess.call("ts.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play() 

        elif choice =="9":
          try: 
               log.info("Calling 'webm.py'...")
               subprocess.call("webm.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()   

        elif choice =="10":
          try: 
               log.info("Calling 'gif.py'...")
               subprocess.call("gif.py", shell=True)  

          except FileNotFoundError:    

                log.error("[bold red blink]!...File not found...![/]", extra={"markup": True}) 
                log.exception("Operation cancelled..!!!")
                mixer.init()
                mixer.music.load(cwd+'\elements\sfx_sounds_error1.wav')
                mixer.music.play()         

        elif choice =="11":
           break

        elif choice =="":
         list_k =[]
         ch = 0 
         while ch != "n": 
            ch = input("Are you sure you want to quit? [n/y][default: n]")
            if ch =="y":
               time.sleep(0.1)
               exit()
   
            if ch =="n":
               break
            if ch =="":
               break






              



if __name__=="__main__":
    main()        


