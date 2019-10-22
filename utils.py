from models import Pessoas

#insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Rosana', idade=32) #id, por ser PK, já vai ser inserido automaticamente
    print(pessoa)
    pessoa.save()

# realiza consulta na tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    # for i in pessoas:
    #     print(i.nome)
    print(pessoas)

    # pessoa = Pessoas.query.filter_by(nome='Rosana')
    # for p in pessoa:
    #     print(p)

    pessoa = Pessoas.query.filter_by(nome='Rosana').first() #ele pega o primeiro registro, caso tenham mais de 1 com mesmo nome
    print(pessoa.idade)

# altera dados na tabela Pessoa
def altera_pessoa():
    # pessoa = Pessoas.query.filter_by(nome='Rosana').first()
    # pessoa.idade = 21
    # pessoa.save()

    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Rafa'
    pessoa.save()

# exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafa').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()
