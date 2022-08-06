def main():
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    import logging
    import os
    cwd = os.getcwd()
    if not os.path.exists("Logs"):
       os.makedirs("Logs")
    lo_dir = cwd+"/Logs/choice.log"
    logging.basicConfig(filename=lo_dir, level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="w")
   
    logging.info("Called 'choice.py'")         
    table = Table(title="| Convert to |")

    table.add_column("#", justify="left", style="cyan", no_wrap=True)
    table.add_column("Format", justify="right", style="magenta")

    table.add_row("1]", "mov")
    table.add_row("2]", "mp4")
    table.add_row("3]", "mkv")
    table.add_row("4]", "avi")
    table.add_row("5]", "m4v")
    table.add_row("6]", "wmv")
    table.add_row("7]", "flv")
    table.add_row("8]", "ts")
    table.add_row("9]", "webm")
    table.add_row("10]", "gif")
    table.add_row("11]", "quit")



    console = Console()
    console.print(table)
    logging.info("Printed supported formats.")

if __name__ == "__main__":
    main()    
