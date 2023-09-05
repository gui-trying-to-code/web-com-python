from flask import Flask

app = Flask("my app")

posts = [
    {
        'titulo' : "TESTE 1",
        'texto' : "teste do post"
    }
]
@app.route('/')
def exibirEntradas ():
    entradas = posts
    return str(entradas)