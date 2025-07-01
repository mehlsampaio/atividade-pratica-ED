# Criando cada elemento da lista encadeada
class PacientesDaListaEncadeada:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __repr__(self):
        return f"{self.cor},{self.numero}"

# Criando a lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contadorA = 201
        self.contadorV = 1

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(repr(nodo))
            nodo = nodo.proximo
        nodos.append("None")
        return "->".join(nodos)

# Função para inserir paciente
    def inserirPaciente(self):

        def inserirComPrioridade():
            if self.head is None:
                self.head = nodo
                return

            if self.head.cor == "V":
                nodo.proximo = self.head
                self.head = nodo
                return

            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo

            nodo.proximo = atual.proximo
            atual.proximo = nodo

        def inserirSemPrioridade():
            if self.head is None:
                self.head = nodo
                return
            nodo_novo = self.head
            while nodo_novo.proximo is not None:
                nodo_novo = nodo_novo.proximo
            nodo_novo.proximo = nodo


        escolha = input("Qual é o cartão do paciente? A para amarelo e V para verde").upper()
        if escolha == "V":
            numero = self.contadorV
            self.contadorV += 1
        elif escolha == "A":
            numero = self.contadorA
            self.contadorA += 1
        else:
            print("Digite um cartão válido...")
            return

        nodo = PacientesDaListaEncadeada(numero=numero, cor=escolha)

        if escolha == "V":
            inserirSemPrioridade()
        elif escolha == "A":
            inserirComPrioridade()
        else:
            print("Digite um cartão válido...")
            return

# Função que mostra a lista de espera
    def imprimirListaDeEspera(self):
        atual = self.head
        if atual is None:
            print("A lista de pacientes está vazia no momento.")
            return

        linha = "Lista de espera: "
        while atual is not None:
            linha += f"[{atual}] → "
            atual = atual.proximo

        linha += "None"
        print(linha)


# Função para atender paciente
    def atenderPaciente(self):
        if self.head is None:
            print("A lista de pacientes está vazia no momento.")
            return
        paciente = self.head
        self.head = self.head.proximo  #elimina o primeiro da fila
        print(f"Próximo paciente: {paciente}")


# Criando o objeto da lista encadeada
lista = ListaEncadeada()


# Menu
while True:
    print("1 - Inserir Paciente")
    print("2 - Mostrar lista de espera")
    print("3 - Chamar Paciente")
    print("4 - Sair do programa")

    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            lista.inserirPaciente()
        elif opcao == 2:
            lista.imprimirListaDeEspera()
        elif opcao == 3:
            lista.atenderPaciente()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente")
    except ValueError:
        print("Digite uma opção válida")


