import pygame as pg
import cv2

# def accelerate_conversion(image, width, height, color_coeff, step):
#     array_of_values = []
#     for x in range(0, width, step):
#         for y in range(0, height, step):
#             r, g, b = image[x, y] // color_coeff
#             if r + g + b:
#                 array_of_values.append(((r, g, b), (x, y)))
#     return array_of_values
#

class ArtConverter:
    def __init__(self, path='image/car22.jpg', font_size=12, color_lvl=8):
        pg.init()
        self.path = path
        #self.image = cv2.imread(path) #массив numpay
        self.image = self.get_image()
        # self.COLOR_LVL = color_lvl
        # self.image, self.gray_image = self.get_image()
        #self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.ASCII_CHARS = ' ixzao*#MW&8%B@$'
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = pg.font.SysFont('Сourier', font_size, bold=True)#шрифт
        self.CHAR_STEP = int(font_size * 0.6)#Шаг
        self.REFEREND_ASCII_CHIRS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]
        #self.PALETTE, self.COLOR_COEFF = self.create_palette()


    def draw_converted_image(self):
        char_indices = self.image // self.ASCII_COEFF#значение пикслей
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indices[x, y]
                if char_index:
                    self.surface.blit(self.REFEREND_ASCII_CHIRS[char_index],(x, y ))


        # image, gray_image = self.get_image()
        # array_of_values = accelerate_conversion(image, gray_image, self.WIDTH, self.HEIGHT,
        #                                         self.COLOR_COEFF, self.ASCII_COEFF, self.CHAR_STEP)
        # for char_index, color, pos in array_of_values:
        #         char = self.ASCII_CHARS[char_index]
        #         self.surface.blit(self.PALETTE[char][color], pos)




    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        # ret, self.cv2_image = self.capture.read()
        # if not ret:
        #     exit()
        transposed_image = cv2.transpose(self.cv2_image)
        #rgb_image = cv2.transpose(self.cv2_image)
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
       #return image, gray_image
        return gray_image
        #return rgb_image



    def draw_cv2_image(self):
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
       # pg.surfarray.blit_array(self.surface, self.image)
        #cv2.imshow('img', self.image)
        self.draw_cv2_image()



    def run(self):
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_s:
                        self.save_image()
                    if i.key == pg.K_r:
                        self.record = not self.record
            #self.record_frame()
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()

if __name__ == '__main__':
    app = ArtConverter()
    app.run()



