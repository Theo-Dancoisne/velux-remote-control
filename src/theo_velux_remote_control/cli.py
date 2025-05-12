import typer
from .velux import *


app = typer.Typer()


@app.command()
def open():
    v_open()

@app.command()
def close():
    v_close()

@app.command()
def stop():
    v_stop()

@app.command()
def clean():
    v_cleanup()



if __name__ == "__main__": app()
