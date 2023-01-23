from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.screenmanager import Screen


class SavedRecipesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.list_view = MDList()
        self.add_widget(self.list_view)

        # add some items to the list
        for recipe in self.saved_recipes:
            item = OneLineListItem(text=recipe.title)
            self.list_view.add_widget(item)
