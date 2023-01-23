from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
import requests


class RecipeFinderApp(App):

    def build(self):
        # Set up a FloatLayout as the main layout
        self.layout = FloatLayout()
        
        # Add a background image to the layout
        self.layout.add_widget(Image(source='bg.jpg', allow_stretch=True, keep_ratio=False))
        
        # Add a title label
        self.title_label = Label(text='Recipe Finder', font_size=30, halign='center', pos_hint={'center_x':0.5, 'center_y':0.9}, size_hint=(0.8, 0.1))
        self.layout.add_widget(self.title_label)
        
        # Add a text input for the search term
        self.search_input = TextInput(hint_text='Enter a type of food', pos_hint={'center_x':0.5, 'center_y':0.8}, size_hint=(0.8, 0.1))
        self.layout.add_widget(self.search_input)
        
        # Add a search button
        self.search_button = Button(text='Search', size_hint=(0.2, 0.1), pos_hint={'x':0.8, 'center_y':0.8})
        self.search_button.bind(on_press=self.search_recipes)
        self.layout.add_widget(self.search_button)

        # Add a GridLayout for the filters
        self.filters_layout = GridLayout(cols=3, pos_hint={'x':0.1, 'y':0.6}, size_hint=(0.8, 0.1))
        
        # Add a dropdown menu for cuisine type
        self.cuisine_spinner = Spinner(text='All Cuisines', values=['All Cuisines', 'Italian', 'Mexican', 'Chinese', 'Indian', 'American', 'African', 'French', 'Japanese', 'Korean', 'Vietnamese', 'Thai', 'Indian', 'British', 'Irish', 'French', 'Spanish', 'Middle Eastern', 'Jewish', 'Cajun', 'Greek', 'German', 'Nordic', 'Eastern European', 'Caribbean', 'Latin American'])
        self.filters_layout.add_widget(self.cuisine_spinner)
        
        # Add a dropdown menu for dietary restrictions
        self.diet_spinner = Spinner(text='All Diets', values=['All Diets', 'Vegetarian', 'Vegan', 'Gluten-Free', 'Paleo', 'Ketogenic'])
        self.filters_layout.add_widget(self.diet_spinner)
        
        # Add a dropdown menu for cooking time
        self.time_spinner = Spinner(text='All Times', values=['All Times', '30 minutes or less', '1 hour or less', '2 hours or less'])
        self.filters_layout.add_widget(self.time_spinner)
        
        self.layout.add_widget(self.filters_layout)

        # Add a scroll view to hold the search results
        self.scroll_view = ScrollView(pos_hint={'center_x':0.5, 'center_y':0.2}, size_hint=(0.8, 0.6))
        self.layout.add_widget(self.scroll_view)

    

        return self.layout
        

    def search_recipes(self, instance):
        search_term = self.search_input.text
        cuisine_type = self.cuisine_spinner.text
        diet_type = self.diet_spinner.text
        time_type = self.time_spinner.text
        if not search_term:
            return
        
        # Show the spinner and hide the scroll view
        #self.spinner.visible = True
        self.scroll_view.visible = False
        
        api_key = '4f71ba8467ef49359347499517d82b38'
        api_url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={api_key}'
        if cuisine_type != 'All Cuisines':
            api_url += f'&cuisine={cuisine_type}'
            if diet_type != 'All Diets':
                api_url += f'&diet={diet_type}'
    
        if time_type != 'All Times':
            if time_type == '30 minutes or less':
                api_url += '&maxReadyTime=30'
            elif time_type == '1 hour or less':
                api_url += '&maxReadyTime=60'
            elif time_type == '2 hours or less':
                api_url += '&maxReadyTime=120'
    
        response = requests.get(api_url)
    
        if response.status_code != 200:
            self.spinner.text = 'Error fetching recipes'
            return
    
        data = response.json()
        self.results = [{'title': r['title'], 'id': r['id'], 'ingredients': ', '.join(map(lambda x: x['name'], r.get('extendedIngredients', []))), 'instructions': r.get('instructions', 'Instructions not available')} for r in data['results']]
    
        # Hide the spinner and show the scroll view
        #self.spinner.visible = False
        self.scroll_view.visible = True
    
        if not self.results:
            self.scroll_view.clear_widgets()
            self.scroll_view.add_widget(Label(text='No recipes found'))
        else:
            self.display_results()
        

    def display_results(self):
        self.scroll_view.clear_widgets()
    
        # Create a new GridLayout for the results
        container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make the height of the container equal to the height of all the widgets inside
        container.bind(minimum_height=container.setter('height'))
    
        # Add the result widgets to the container
        for result in self.results:
            # Create a new BoxLayout for each result
            result_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
    
            # Add a button with the recipe title
            btn = Button(text=result['title'], on_press=self.view_recipe)
            btn.recipe_id = result['id']
            result_layout.add_widget(btn)
        
            container.add_widget(result_layout)
        
        # Add the container to the scroll view
        self.scroll_view.add_widget(container)

    def view_recipe(self, instance):
        recipe_id = instance.recipe_id
        self.get_recipe(recipe_id)
    
    def get_recipe(self, recipe_id):
        api_key = '4f71ba8467ef49359347499517d82b38'
        api_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'
        response = requests.get(api_url)
        recipe = response.json()
        instructions = recipe.get('instructions', 'Instructions not available')
        ingredients = ', '.join(map(lambda x: x['name'], recipe.get('extendedIngredients', [])))
        
        # Create a new BoxLayout
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        
        # Add the recipe title
        layout.add_widget(Label(text=recipe['title'], font_size=20, halign='center'))
        
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



if __name__ == '__main__':
    RecipeFinderApp().run()


#Here are a few ideas for new features you could add to your app:

#Add a "Go Back" button to allow users to return to the search results after viewing a specific recipe. You could create the button in the view_recipe method and add it to the layout of the recipe screen.

#Allow users to filter the search results by various criteria, such as cuisine type, dietary restrictions, or cooking time. You could add a dropdown menu or a series of checkboxes to the search screen to allow users to select their desired filters.

#Allow users to save their favorite recipes to a list for easy access later. You could create a separate screen for the saved recipes list and add a "Save" button to each recipe screen that adds the recipe to the list.

#Add a feature to generate a shopping list based on the ingredients needed for a specific recipe. You could create a separate screen for the shopping list and add a "Add to Shopping List" button to each recipe screen that adds the ingredients to the list.

#Add an option to print the recipe instructions. You could create a "Print" button on the recipe screen that generates a printable version of the recipe instructions.

#Allow users to search for recipes using an image of a dish rather than a text query. You could use the Spoonacular API's "Food Visual Recognition" feature to recognize the dish in the image and return a list of matching recipes.