from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
import base64



sec_mess = '''

Manager:
    Screen1:
    Screen2:
    Screen3:
    Screen4:

<Screen1>:
    name:"scr1"

    canvas.before:
    	Color:
    		rgba: (1,1,0,1)
    	Rectangle:
    		pos: self.pos
    		size: self.size

    BoxLayout:
        orientation:"vertical"

        MDLabel:
            text:"Message Encryption-Decryption"
            color:"red"
            halign:"center"
            bold:True
            underline:True
            font_style:"H5"

        MDTextField:
            id:user
            hint_text:"Username"
            helper_text:"*Required"
            icon_right:"account"

        MDTextField:
            id:passw
            hint_text:"Password"
            helper_text:"*Required"
            icon_right:"eye-off"

        MDLabel:
            id:lb
            text:""
            color:"red"
            halign:"center"

        Button:
            text:"---->"
            size_hint:(0.3,0.2)
        	pos_hint: {"center_x":0.5, "center_y":0.4}
        	on_release:
        	    app.validate(user,passw,lb)
        	    	    

        MDLabel:
            text:""       

<Screen2>:
    name:"scr2"

    canvas.before:
    	Color:
    		rgba: (1,1,0,1)
    	Rectangle:
    		pos: self.pos
    		size: self.size

    BoxLayout:
        orientation:"vertical"
        spacing:50

        MDLabel:
            text:"Welcome User!!!"
            color:"red"
            halign:"center"
            bold:True
            font_style:"H5"

        Image:
            source:"encrypt-decrypt.png"
            allow_stretch:True


        BoxLayout:
            orientation:"horizontal"

            Button:
                text:"ENCRYPT"
                on_release:app.root.current="scr3"

            Button:
                text:"DECRYPT"
                on_release:app.root.current="scr4"

<Screen3>:
    name:"scr3"

    canvas.before:
    	Color:
    		rgba: (1,1,0,1)
    	Rectangle:
    		pos: self.pos
    		size: self.size
    BoxLayout:
        orientation:"vertical"
        spacing:50

        MDLabel:
            text:"ENCRYPT YOUR MESSAGE!!!!"
            color:"red"
            halign:"center"
            bold:True
            font_style:"H5"

        TextInput:
            id:id1
            multiline:True

        Button:
            text:"ENCRYPT"
            size_hint:(0.3,0.4)
        	pos_hint: {"center_x":0.5, "center_y":0.4}
            on_release:app.func(id1,id2)

        TextInput:
            id:id2
            multiline:True

        Button:
            text:"<----"
            size_hint:(0.3,0.4)
        	pos_hint: {"center_x":0.5, "center_y":0.4}
            on_release:app.root.current="scr2"

        MDLabel:
            text:""  

<Screen4>:
    name:"scr4"
    
    canvas.before:
    	Color:
    		rgba: (1,1,0,1)
    	Rectangle:
    		pos: self.pos
    		size: self.size

    BoxLayout:
        orientation:"vertical"
        spacing:50

        MDLabel:
            text:"DECRYPT YOUR MESSAGE!!!!"
            color:"red"
            halign:"center"
            bold:True
            font_style:"H5"

        TextInput:
            id:id3
            multiline:True

        Button:
            text:"DECRYPT"
            size_hint:(0.3,0.4)
        	pos_hint: {"center_x":0.5, "center_y":0.4}
            on_release:
                app.func1(id3,id4)

        TextInput:
            id:id4
            multiline:True

        Button:
            text:"<----"
            size_hint:(0.3,0.4)
        	pos_hint: {"center_x":0.5, "center_y":0.4}
            on_release:app.root.current="scr2"

        MDLabel:
            text:""  




'''
class Manager(ScreenManager):
	pass

class Screen1(Screen):
	pass

class Screen2(Screen):
	pass

class Screen3(Screen):
	pass

class Screen4(Screen):
	pass

class SecretApp(MDApp):

	def build(self):
		bldr = Builder.load_string(sec_mess)
		return bldr

	
	def func(self,id1,id2):
		a=id1.text
		b=a.encode("ascii")
		c=base64.b64encode(b)
		global d 
		d= c.decode("ascii")
		id2.text=d
		

	def func1(self,id3,id4):
		f=id3.text
		g=f.encode("ascii")
		h=base64.b64decode(g)
		i=h.decode("ascii")
		id4.text = i

		


		
	def validate(self,user,passw,lb):
		if ((user.text =="admin") and (passw.text=="admin")):
			self.root.current="scr2"

		else:
			lb.text="Invalid Credentials!!!"


SecretApp().run()