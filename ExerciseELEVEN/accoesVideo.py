class AccoesVideo():
    def __init__(self):
        self._play = True
        self._pause = False
        self._like = False
        self._unLike = False
       
    def play(self):
        if self._play == False:
            self._pause = False
            self._play = True
            print('PLAY')
        print("JA ESTA EM PLAY")

    def pause(self):
        if self._pause == False:
            self._pause = True
            self._play == False 
            print('PAUSE')
        print("JA ESTA EM PAUSE")

    def like(self):
        if self._like == False:
            self.unLike = False
            self._like = True
            return self._like
        print("JA TEM LIKE")
        

    def unLike(self):
        if self._unLike == False:
            self.like = False
            self._unLike = True
            return self._unLike
        print("UNLIKE")
