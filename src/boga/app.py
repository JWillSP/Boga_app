"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def button_handler(widget):
    print('toma')
    widget.app.main_window._content = widget.app.second_box
    print(dir(widget.app))


def button_handler2(widget):
    print('toma2')


class Boga(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box()
        self.second_box = toga.Box()

        button = toga.Button('Hello world', on_press=button_handler)
        button.style.padding = 50
        button.style.flex = 1

        button2 = toga.Button('Hello world', on_press=button_handler2)
        button2.style.padding = 50
        button2.style.flex = 1

        self.main_box.add(button)
        self.second_box.add(button2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


def main():
    return Boga()
