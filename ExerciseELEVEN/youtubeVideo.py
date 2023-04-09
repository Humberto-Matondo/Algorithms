from accoesVideo import AccoesVideo


class Video(AccoesVideo):
    def __init__(self):
        self._titulo = ''
        self.views = 0
        self.likes = 0
        self.unlikes = 0
        self._reproduzindo = False
        self.acoes = AccoesVideo()

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        return self._titulo

    def metodo_views(self):
        self.views += 1
        return self.views

    def metodo_likes(self):
        if self.acoes.like == True:
            self.likes += 1
            return self.likes

    def metodo_unlikes(self):
        if self.acoes.unLike == True:
            self.unlikes += 1
            return self.unlikes

    def reproduzir(self):
        if self._reproduzindo == False:
            self._reproduzindo = True
            return self._reproduzindo

    def parar_Reproducao(self):
        if self._reproduzindo == True:
            self._reproduzindo = False
            return self._reproduzindo
