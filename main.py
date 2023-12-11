import pgzrun
from pgzero.actor import Actor


def draw():
    luigi.draw()


WIDTH, HEIGHT = 800, 600
TITLE = "Python Taha"
luigi = Actor("")
pgzrun.go()
