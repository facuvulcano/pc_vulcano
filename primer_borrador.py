from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

import requests


class RecipeFinderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.search_input = TextInput(hint_text='Enter a recipe')
        self.search_button = Button(text='Search')
        self.search_button.bind(on_press=self.search_recipes)
        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.search_button)
        return self.layout

    def search_recipes(self, instance):
        search_term = self.search_input.text
        if not search_term:
            return

        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='Searching for recipes...'))

        
        api_key = '4f71ba8467ef49359347499517d82b38'
        api_url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={api_key}'
        response = requests.get(api_url)

        if response.status_code != 200:
            self.layout.clear_widgets()
            self.layout.add_widget(Label(text='Error fetching recipes'))
            return

        data = response.json()
        self.results = [{'title': r['title'], 'id': r['id'], 'ingredients': ', '.join(map(lambda x: x['name'], r.get('extendedIngredients', []))), 'instructions': r.get('instructions', 'Instructions not available')} for r in data['results']]

        self.layout.clear_widgets()
        if not self.results:
            self.layout.add_widget(Label(text='No recipes found'))
        else:
            self.display_results()


    def display_results(self):
        self.layout.clear_widgets()
        for result in self.results:
            btn = Button(text=result['title'], on_press=self.view_recipe)
            btn.recipe_id = result['id']
            self.layout.add_widget(btn)


    def view_recipe(self, instance):
        
        recipe_id = instance.recipe_id
        api_key = '4f71ba8467ef49359347499517d82b38'
        api_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'
        response = requests.get(api_url)
        recipe = response.json()
        instructions = recipe.get('instructions', 'Instructions not available')
        ingredients = ', '.join(map(lambda x: x['name'], recipe.get('extendedIngredients', [])))

       # Create a new BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Split the instructions into chunks of a maximum length
        chunk_size = 100
        instructions_chunks = [instructions[i:i+chunk_size] for i in range(0, len(instructions), chunk_size)]

        # Add each chunk of instructions to the layout
        for chunk in instructions_chunks:
            layout.add_widget(Label(text=chunk))
        layout.add_widget(Label(text='Ingredients: ' + ingredients))

        # Remove the current layout and add the new layout to the parent widget
        parent = self.layout.parent
        parent.remove_widget(self.layout)
        parent.add_widget(layout)
        

    def get_recipes(self, search_term):

        api_key = '4f71ba8467ef49359347499517d82b38'
        api_url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={api_key}'
        response = requests.get(api_url)
        if response.status_code != 200:
            return []
        data = response.json()
        return [{'title': r['title'], 'ingredients': ', '.join(map(lambda x: x['name'], r['extendedIngredients'])), 'instructions': r['instructions']} for r in data['results']]





if __name__ == '__main__':
    RecipeFinderApp().run()
