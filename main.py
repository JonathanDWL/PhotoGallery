from kivy.app import App
from kivy.uix.screenmanager import Screen

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

PhotoGalleryApp().run()