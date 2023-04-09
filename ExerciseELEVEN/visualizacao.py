class Visualizacao():
    def __init__(self, espectador, video):
        self._espectador = espectador
        self._video = video

    @property
    def espectador(self):
        return self._espectador

    @espectador.setter
    def espectador(self, espectador):
        self._espectador = espectador
        return self._espectador

    @property
    def video(self):
        return self._video
    
    @video.setter
    def video(self, video):
        self._video = video
        return self._video
    