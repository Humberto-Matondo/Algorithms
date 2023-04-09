from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        self._login = False
        self._totAssistido = 0
    
    def login(self):
        if self._login == False:
            self._login = True
            return self._login
        print(f"O Estudante '{self._nome}' ja fez o Login.")
    
    def Login_OFF(self):
        if self._login == True:
            self._login = False
            return self._login
        print(f"O Estudante '{self._nome}'não fez o Login.")

    def viuMaisUm(self):
        self._totAssistido += 1
        return self._totAssistido
