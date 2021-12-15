
import os
from bottle import Bottle, request, template, debug,route, error, run
import requests

#app = Bottle()
@route('/hello/')
@route('/hello/<name>')
def hello(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)
    #return 'Hello World'


@route('/')
def index():
    return '''
<h1>Seja bem vindo(a) ao mini site. </h1>
    Uma foto de doguinho aleatória, <a href="foto?tipo=aleatoria">clique aqui </a> <br>
    Ou escolha por uma raça: <br>
    <form action="foto" method="POST">
    <select name="raca" id="tipo">
      <option value="akita">Akita</option>
      <option value="mix">Sem Raça</option>
      <option value="labrador">Labrador</option>
      <option value="husky">Husky</option>
    </select>
    <input value="Enviar" type="submit" />
    </form>
'''
    
@route('/foto', method='POST')
@route('/foto', method='GET')
def exibe_foto():
    raca = str(request.forms.get('raca'))
    tipo = str(request.params.get('tipo'))
    if "aleatoria" in tipo:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        status = response.json().get("status")
        if "success" in status:
            img = response.json().get("message");
            return template(" <img src=\"{{im}}\" alt=''><br><br><a href=\"/\">Voltar </a> <br>", im=img) 
        else:
            return template("Erro ao buscar a imagem. <br><br><a href=\"/\">Voltar </a>")
    response = requests.get('https://dog.ceo/api/breed/' + raca + '/images/random')
    status = response.json().get("status")
    if "success" in status:
        img = response.json().get("message");
        return template(" <img src=\"{{im}}\" alt=''><br><br><a href=\"/\">Voltar </a> <br>", im=img)    
    

        
@error(404)
def error404(error):
    return 'Página não encontrada.'

#debug(True)  
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

