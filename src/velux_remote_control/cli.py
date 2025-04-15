import typer
from .velux import Velux


app = typer.Typer()


@app.command()
def open():
    Velux.open()

@app.command()
def close():
    Velux.close()

@app.command()
def stop():
    Velux.stop()

@app.command()
def clean():
    Velux.cleanup()



if __name__ == "__main__": app()