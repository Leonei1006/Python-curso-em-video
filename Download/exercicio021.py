#tocando uma música mp3
from pygame import mixer
mixer.init()
mixer.music.load('exercicio021.mp3')
mixer.music.play()
input('Agora você escuta?')

