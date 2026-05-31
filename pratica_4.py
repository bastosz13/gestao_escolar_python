alunos = []

def cadastrar_aluno(nome, nota1, nota2, nota3, nota4):    
    """
     Cadastra um aluno na lista de alunos.

    A função solicita ao usuário o nome do aluno e suas
    quatro notas bimestrais, armazenando os dados em um
    dicionário no formato:

    {
        "nome": str,
        "notas": [float, float, float, float]
    }

    O dicionário é adicionado à lista global 'alunos'.
    """

    aluno = {
        "nome": nome, # o valor 'nome' fornecido pelo usuario é associado à chave {nome}
        "notas": [nota1, nota2, nota3, nota4] #estrutura as notas como valores, com a chave {notas}
    }

    alunos.append(aluno) #adiciona os dados fornecidos ao dicionário alunos.


def calcular_media(aluno):
    """
    Calcula a média de um aluno.

    Args:
        aluno (dict): Dicionário contendo nome e notas do aluno.

    Returns:
        float: Média do aluno.
    """

    soma = sum(aluno["notas"])
    quantidade_notas = len(aluno["notas"])
    media = soma / quantidade_notas

    return media


def verificar_aprovacao(media):
    """
    Verifica se o aluno foi aprovado.

    Args:
        media (float): Média do aluno.

    Returns:
        str: Situação do aluno.
    """

    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Cadastro dos alunos
cadastrar_aluno("Luiz", 10, 7, 5, 3)
cadastrar_aluno("João", 5, 9, 4, 2)
cadastrar_aluno("Maria", 2, 2, 2, 2)

def gerar_relatorio():
    """
    Gera um relatório com as informações de todos os alunos cadastrados.

    Para cada aluno da lista 'alunos', a função:
    - Calcula a média das notas utilizando a função calcular_media().
    - Verifica a situação do aluno utilizando a função verificar_aprovacao().
    - Exibe na tela o nome, as notas, a média e a situação final.

    Returns:
        None
    """ 
    for aluno in alunos:
        media = calcular_media(aluno)
        situacao = verificar_aprovacao(media)

        print(f"\nAluno: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")

gerar_relatorio()

