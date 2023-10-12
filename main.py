from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display(self):
        return(images[index])
    def next(self):
        global index
        index = (index+1)%len(images)
        self.ids.image.source = images[index]
    def prev(self):
        global index
        index = (index-1)%len(images)
        self.ids.image.source = images[index]

images = ["flowah.jpg", "froggy.jpg", "lake.jpg", "man.jpg", "milky.jpg", "tree.jpg"]
index = 0

class PhotoEditorApp(App):
    pass

class MainScreen(Screen):
    def loadbase(self, image):
        if(image in images):
            self.ids.display.source = image
        else:
             self.ids.display.source = "notfound.png"
    def invert(self, image):
        if(image in images):
            img = Image.open(image)
            pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    red = 255 - pixels[x, y][0]
                    green = 255 - pixels[x, y][1]
                    blue = 255 - pixels[x, y][2]
                    pixels[x, y] = (red, green, blue)
            img.save(image[:image.index(".")] + " invert" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " invert" + image[image.index("."):]
        else:
            self.ids.display.source = "notfound.png"

    def grayscale(self, image):
        if(image in images):
            img = Image.open(image)
            pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    avg = (pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) // 3
                    pixels[x, y] = (avg, avg, avg)
            img.save(image[:image.index(".")] + " grayscale" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " grayscale" + image[image.index("."):]
        else:
            self.ids.idsplay.source = "notfound.png"

    def sepia(self, image):
        if(image in images):
            img = Image.open(image)
            pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    red = int(pixels[x, y][0] * 0.393) + int(pixels[x, y][1] * 0.769) + int(pixels[x, y][2] * 0.189)
                    green = int(pixels[x, y][0] * 0.349) + int(pixels[x, y][1] * 0.686) + int(pixels[x, y][2] * 0.168)
                    blue = int(pixels[x, y][0] * 0.272) + int(pixels[x, y][1] * 0.534) + int(pixels[x, y][2] * 0.131)
                    pixels[x, y] = (red, green, blue)
            img.save(image[:image.index(".")] + " sepia" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " sepia" + image[image.index("."):]
        else:
            self.ids.display.source = "notfound.png"

    def trippy(self, image):
        if(image in images):
            img = Image.open(image)
            pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    hue = ((pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) / 3 / 255 * 1080) % 360
                    if (hue < 60):
                        redmag = 1
                        greenmag = (60 - (60 - hue)) / 60
                        bluemag = 0
                    elif (hue < 120):
                        redmag = (120 - hue) / 60
                        greenmag = 1
                        bluemag = 0
                    elif (hue < 180):
                        redmag = 0
                        greenmag = 1
                        bluemag = (60 - (180 - hue)) / 60
                    elif (hue < 240):
                        redmag = 0
                        greenmag = (240 - hue) / 60
                        bluemag = 1
                    elif (hue < 300):
                        redmag = (60 - (300 - hue)) / 60
                        greenmag = 0
                        bluemag = 1
                    else:
                        redmag = 1
                        greenmag = 0
                        bluemag = (360 - hue) / 60
                    red = int(pixels[x, y][0] * redmag)
                    green = int(pixels[x, y][1] * greenmag)
                    blue = int(pixels[x, y][2] * bluemag)
                    pixels[x, y] = (red, green, blue)
            img.save(image[:image.index(".")] + " trippy" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " trippy" + image[image.index("."):]
        else:
            self.ids.display.source = "notfound.png"
    def lined(self, image):
        if(image in images):
            imgo = Image.open(image)
            opixels = imgo.load()
            imgn = Image.new(mode="RGB", size=imgo.size, color=(255, 255, 255))
            npixels = imgn.load()
            for x in range(1, imgo.size[0] - 1):
                for y in range(1, imgo.size[1] - 1):
                    neighbors = []
                    for xs in range(x - 1, x + 2):
                        for ys in range(y - 1, y + 2):
                            neighbors.append(opixels[xs, ys])
                    differs = []
                    for neighbor in neighbors:
                        differs.append(max([abs(neighbor[0] - opixels[x, y][0]), abs(neighbor[1] - opixels[x, y][1]),
                                            abs(neighbor[2] - opixels[x, y][2])]))
                    contrast = sum(differs) // len(differs)
                    if (contrast > 24):
                        npixels[x, y] = (0, 0, 192)
                    elif (contrast > 12):
                        npixels[x, y] = (128, 128, 255)
                    elif (contrast > 6):
                        npixels[x, y] = (192, 192, 255)
            imgn.save(image[:image.index(".")] + " line" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " line" + image[image.index("."):]
        else:
            self.ids.display.source = "notfound.png"
    def pixelate(self, image):
        if(image in images):
            img = Image.open(image)
            pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    if (x >= 0 and x <= img.size[0] - 1 and y >= 0 and y <= img.size[1] - 1):
                        pixels[x, y] = pixels[x // 10 * 10 + 5, y // 10 * 10 + 5]
            img.save(image[:image.index(".")] + " pixelate" + image[image.index("."):])
            self.ids.display.source = image[:image.index(".")] + " pixelate" + image[image.index("."):]
        else:
            self.ids.display.source = "notfound.png"

PhotoEditorApp().run()