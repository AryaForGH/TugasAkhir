from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 10

        self.result_label = Label(text="0", font_size=150, halign="right", valign="middle", size_hint=(1, 0.3))
        self.add_widget(self.result_label)

        self.keyboard = GridLayout(cols=4)
        self.equation = ""
        self.create_buttons()

    def create_buttons(self):
        button_values = ["C", "%", "/", "*"
                         , "9", "8", "7", "+"
                         ,"4", "5", "6", "-"
                         , "1", "2", "3", "="
                         , ".", "0", "CE", "C"]

        for value in button_values:
            button = Button(text=value, font_size=30)
            button.bind(on_press=self.on_button_press)
            self.keyboard.add_widget(button)
        self.add_widget(self.keyboard)

    def on_button_press(self, button):
        if button.text == "=":
            self.calculate_result()
        elif button.text == "C":
            self.on_clear_press()
        elif button.text == "CE":
            self.on_clear_press()
        else:
            self.equation += button.text
            self.update_screen()

    def on_equal_press(self):
        self.calculate_result()

    def on_clear_press(self):
        self.equation = ""
        self.update_screen()

    def calculate_result(self):
        try:
            self.equation = str(eval(self.equation))
            self.update_screen()
        except:
            self.equation = ""
            self.update_screen()

    def update_screen(self):
        self.result_label.text = self.equation

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
