from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class mycom(GridLayout):
    def __init__(self,**kwargs):
        super(mycom,self).__init__(**kwargs)
        self.cols = 1



        self.inside = GridLayout()
        self.inside.cols = 2


        self.inside.add_widget(Label(text="firstName: " , font_size=20))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text="LastName: ", font_size=20))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: ", font_size=20))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="submit", font_size=40)
        self.submit.bind(on_press=self.mypress)

        self.add_widget(self.submit)

    def mypress(self, instance):
        name = self.firstName.text
        last = self.lastName.text
        mail = self.email.text
        print("Name:", name)
        print("Last_Name:", last)
        print("Email:", mail)
        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""




class kinapp(App):
    def build(self):
        self.icon = "calculator1.png"
        return mycom()


if __name__ == "__main__":
    com = kinapp()
    app = com
    app.run()