class Card:
    def __init__(self):
        self.image = load_image('Penrir.png')
        self.x, self.y = 300, 400

    def update(self):
        pass

    def click(self):
        self.image = load_image('vane.png')
        print('Click success')

    def OntheMouse(self):
        self.image = load_image('Penrir_extension.png')
        print('Mouse is overrapped')

    def Mouse_is_Out(self):
        self.image = load_image('Penrir.png')

    def draw(self):
        self.image.draw(self.x, self.y)