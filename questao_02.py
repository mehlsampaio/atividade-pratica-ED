class ElementosDaLista:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


# Tabela Hash de endereçamento em cadeia

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        nodo = ElementosDaLista(sigla, nomeEstado)
        if self.head is None:
            self.head = nodo
            return 0
        else:
            nodo.proximo = self.head
            self.head = nodo
            return 0

class TabelaHash:
    def __init__(self):
        self.posicao = 10
        self.comprimento = 0
        self.obj = [ListaEncadeadaSimples() for i in range(0, self.posicao)]

    def funcaoHash(self, k):
        if k == "DF":
            return 7
        else:
            k = list(k)
            return(ord(k[0]) + ord(k[1])) % self.posicao

    def inserir(self, sigla, nomeEstado):
        pos = self.funcaoHash(sigla)
        self.obj[pos].inserir(sigla, nomeEstado)
        self.comprimento += 1

    def imprimir(self):
        for i in range(0, self.posicao):
            print(f"{i}:", end=" ")
            atual = self.obj[i].head
            while atual:
                print(f"{atual.sigla} ->", end=" ")
                atual = atual.proximo
            print("None")


# Inserindo estados do Brasil

tabela = TabelaHash()

tabela.inserir("AC", "Acre")
tabela.inserir("AL", "Alagoas")
tabela.inserir("AP", "Amapá")
tabela.inserir("AM", "Amazonas")
tabela.inserir("BA", "Bahia")
tabela.inserir("CE", "Ceará")
tabela.inserir("DF", "Distrito Federal")
tabela.inserir("ES", "Espírito Santo")
tabela.inserir("GO", "Goiás")
tabela.inserir("MA", "Maranhão")
tabela.inserir("MT", "Mato Grosso")
tabela.inserir("MS", "Mato Grosso do Sul")
tabela.inserir("MG", "Minas Gerais")
tabela.inserir("PA", "Pará")
tabela.inserir("PB", "Paraíba")
tabela.inserir("PR", "Paraná")
tabela.inserir("PE", "Pernambuco")
tabela.inserir("PI", "Piauí")
tabela.inserir("RJ", "Rio de Janeiro")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("RS", "Rio Grande do Sul")
tabela.inserir("RO", "Rondônia")
tabela.inserir("RR", "Roraima")
tabela.inserir("SC", "Santa Catarina")
tabela.inserir("SP", "São Paulo")
tabela.inserir("SE", "Sergipe")
tabela.inserir("TO", "Tocantins")
tabela.inserir("MS", "Mehl Da Costa Sampaio")


tabela.imprimir()

