from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades
import json

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):

    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first() #pega o objeto
            response = { #devolve um dicionário
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        # tratar erro AttributeError - quando não encontra a pessoa
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    #método de ALTERAÇÃO
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        # dados = json.loads(request.data)
        # --> posso usar assim, como abaixo, mas se mandar em outro formato vai dar erro
        dados = request.json
        #só vou alterar o q ele informar
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {
            'status': 'sucesso',
            'mensagem': 'Pessoa {} excluída com sucesso'.format(pessoa.nome)
        }

#fazer método pra listar tudo e inserir pessoa
class ListaPessoas(Resource):

    def get(self):
        pessoas = Pessoas.query.all()
            #como aqui é teste, estamos trazendo todos, mas na prática ter cuidado
        #poderia ser
        # for i in pessoas:
        #     lista.apend('nome': i.nome)
        #mas vamos de for in line (uma linha só)
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

#NÁO FUNCIONOU - náo acha nome em atividade.pessoa
#só vou trazer a lista e permitir inclusão
class ListaAtividades(Resource):

    def get(self):
        atividades = Atividades.query.all()
        pessoa = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome} for i in atividades] #faltou: 'pessoa': i.pessoa.nome
        return response

    def post(self):
        dados = request.json
        # jeito do prof - não funcionou pra mim
            # pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        pessoa = Pessoas(nome=dados['pessoa'])
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
