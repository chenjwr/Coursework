## Python GUI (Graphical User Interface) Development with Tkinter ("T-K-inter") -- Barron Stone -- Lynda.com

import Tkinter
import _tkinter
	## import compiled binary associated with package
Tkinter._test()
	## Run test routine


## Saying Hello to Tkinter
## Run using IDLE 

from Tkinter import *

root = Tk()
Label(root, text="Hello, Tkinter!").pack()
root.mainloop()


## Tk is an open source toolkit used to develop GUI
## Developed in '90s as an extension for a scripting language - i.e. tool command language (TCL)
## Tkinter is the standard Python interface to the Tk framework
## Widget are the controls used to interface with the program
## Each of the different types of widgets is defined as a class within the Tkinter package
## All widgets exist under a hierarchy with a single root window at the top


## Creating and configuring widgets 

from Tkinter import *
import ttk

root = Tk()

button = ttk.Button(root, text = 'Click Me')
button.pack()

print(button['text'])
button['text'] = 'Press Me'
button.config(text = 'Push Me')
print(button.config())

print(str(button))
print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()


## Always want to use the same geometry manager to organize widgets within the same master
## Event loop cannot handle multiple events simultaneously 


from Tkinter import *
import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
            ## Create widget label inside of init method; child of the master window
            ## Assign initial text value of 'Hello TKinter'
        self.label.grid(row = 0, column = 0, columnspan = 2)
            ## Store reference to label in a class variable so can access later to change its text
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()



## Displaying text and images with labels

from Tkinter import *
import ttk

root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
    ## Make label widget object display on the screen - use geometry manager 

    ## Change text after label is created
label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
    # Default = label stretches out as long as needed to be contained on a single line
label.config(wraplength = 150)
    ## wraplength = number of pixels for the text to wrap around
label.config(justify = CENTER)
    ## options = LEFT, RIGHT, CENTER
label.config(foreground = 'blue', background = 'yellow')
    ## Foreground property sets the color of the text
    ## Background property sets the color of the label area
    ## Input is a string 
label.config(font = ('Courier', 18, 'bold'))
    ## Font configuration order = font, size, modifier(s)
label.config(text = 'Howdy, Tkinter!')

    ## PhotoImage class can accept GIF, PGM, or PPM files
    ## Other file types require conversion via external library (e.g. Python Image Library)
logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
label.config(image = logo)
    ## (image = logo) is not saving a copy or reference to the 'PhotoImage' object
    ## Therefore, if 'PhotoImage' object is created inside of a function
        ## and only stored to a local variable in that function
        ## when the function is completed the 'PhotoImage' object would be garbage collected
        ## and the image would disappear from the GUI
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')

    ## Store image object to a variable location that will not be garbage collected when needed
    ## Store a reference to the 'PhotoImage' object in the TK label widget object itself
        ## since TK is holding onto that widget and preventing it from being garbage collected
label.img = logo
    ## Saved a reference to that logo inside that image variable 
label.config(image = label.img)
    ## Now can configure the label to use that image instead 

root.mainloop()


## Capturing input with buttons 

from Tkinter import *
import ttk

    ## Call TK constructor method to create top-level root window
root = Tk()

    ## Call themed TTK button constructor method
    ## Parse in its parent, which is the first parameter
    ## Configure the property for the button for 'text'
button = ttk.Button(root, text = "Click Me")
    ## Use geometry manager to add it to the window
button.pack()

    ## Create a function containing the code to execute when the button is pressed
def callback():
    print('Clicked!')

    ## Need to specify command property to make a button functional 
    ## Set the command property to the name of the function to be executed 
button.config(command = callback)
    ## Programmatically simulate a button click with 'invoke'
button.invoke()

    ## State determines whether widgets are active (can be used) or disabled (unusable)
    ## Disabled button = nothing happens when clicked
button.state(['disabled'])
    ## Check current state of a button using 'instate'
print(button.instate(['disabled']))
button.state(['!disabled'])
print(button.instate(['!disabled']))
    ## Listing of potential widget states = http://tcl.tk

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
button.config(image = logo, compound = LEFT)
    ## Resize images within TKinter
    ## Subsample function will use every Xth and every Yth pixel in each direction to create new image
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

root.mainloop()


## Presenting choices with check buttons and radio buttons 

## Check buttons can execute callback function when clicked AND store a binary value
    ## Ideal for when user needs to select or unselect options from a series of choices
## Radio buttons are similar to check buttons (i.e. maintain a value) but are not limited to only two choices 
    ## Allow users to make one selection from a series of mutually exclusive options

from Tkinter import *
import ttk

root = Tk()

checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack()

    ## Tk programs written using Tcl allow the system to indicate when a certain variable has changed
        ## so any widget referencing it can be updated (change-tracking functionality)
    ## Variable classes available in Tkinter are boolean var, double var, int var, string var

    ## Create a string variable 
spam = StringVar()
spam.set('SPAM!')
    ## Check current value of a variable
print(spam.get())

    ## Configure check button to be associated with string variable
    ## Default: selected = 1; not selected = 0
checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')
print(spam.get())

breakfast = StringVar()
    ## Each radio button is its own object tied together by that common variable
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
    ## If select 'SPAM', both radio buttons become selected since both are associated with the spam value
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
print(breakfast.get()) # Note: value will be empty if no selection is made

    ## For widgets with text property there is a text variable property 
    ## Assigning the text variable property to a string var will allow you to update the text of a label/button
        ## by just changing the value of that variable 
checkbutton.config(textvariable = breakfast)

root.mainloop()


## Entering single-line text with the Entry widget 

from Tkinter import *
import ttk

root = Tk()

    ## Entry widget allows user to enter a short text string. LIMITED to only one line
entry = ttk.Entry(root, width = 30)
    ## Width method is specified in number of characters, not pixels
        ## Does not limit the number of characters that can be entered
        ## Controls how big the field will appear on the GUI
entry.pack()

    ## Use get method to retrieve the current contents directly from the entry field
entry.get()
    ## Entry field does not have a set method
    ## Use insert/delete methods to change the contents
    ## Delete has 2 parameters = beginning and end indices of the characters to be deleted from the entry field
        ## Parameters are non-inclusive
entry.delete(0, 1)
entry.delete(0, END)
    ## Insery has 2 parameters = index of, characterwise
        ## where in that entry field to insert new text
        ## a string of the text to enter
entry.insert(0, 'Enter your password')

    ## May want to hide the characters that the user enters by config show property
    ## Asterisks = takes the string specified and replaces every character within the entry field with that string
entry.config(show = '*')
entry.state(['disabled'])
entry.state(['!disabled'])
    ## Read-only = to select/drag texts from the field but cannot enter any text
entry.state(['readonly'])

root.mainloop()


## Making selections with the combo box and spin box

from Tkinter import *
import ttk

root = Tk()

## Combo box is the basic drop down selection tool
    ## User can click on a side button that presents them with a drop down list of all the available options
## Spin box - user only sees one option at a time that represents their current selection
    ## Cycle through available choices
    ## Using for choosing from a list of options that have an inherent order

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
    ## Pass in a list of strings as values for the combo box
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.get())
month.set('Dec')
    ## Can set to a value that is not a part of the variable list
month.set('Not a month!')

year = StringVar()
    ## Spin box is only available as one of the original TK widgets
    ## Underscore in "from_" because "from" is a protected keyword in Python
        ## Used here to import modules; differentiate it from the property that it is named from
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

root.mainloop()


## Inputting values and displaying status with the Scale and Progressbar widgets

from Tkinter import *
import ttk 
    
root = Tk()

    ## length specifies the number of pixels in the longest direction
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

    ## Indeterminate mode = progress bar will show that activity is still taking place without specifying the time that remains
progressbar.config(mode = 'indeterminate')
progressbar.start()
progressbar.stop()

    ## Determinate mode = if total steps in operation is known, can calculate its progress
        ## Allow manual update of the value of the progress bar to represent steps left
    ## Default max = 100
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
progressbar.config(value = 8.0)
progressbar.step()
progressbar.step(5)

value = DoubleVar()
progressbar.config(variable = value)

    ## scale us tied to value variable 
scale = ttk.Scale(root, orient = HORIZONTAL,
          length = 400, variable = value,
          from_ = 0.0, to = 11.0)
scale.pack()
scale.set(4.2)
print(scale.get())

root.mainloop()


## Organizing widgets with frames 

from Tkinter import *
import ttk 
    
root = Tk()

frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)

    ## parent is the recently created 'frame'
    ## Use grid geometry manager instead of the pack manager
ttk.Button(frame, text = 'Click Me').grid()
frame.config(padding = (30, 15))
    ## Root window is created using pack geometry manager
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

root.mainloop()


## Creating additional top-level windows

from Tkinter import *      
    
root = Tk()

window = Toplevel(root)
window.title('New Window')

window.lower()
window.lift(root)

    ## Default state = 'normal'
    ## 'zoomed' = expand the window to its maximum allowed size
window.state('zoomed')

    ## 'withdrawn' = window will be hidden from user; not visible in the taskbar
window.state('withdrawn')

    ## 'iconic' = minimize the window so that it is still accessible in the taskbar
window.state('iconic')

window.state('normal')
print(window.state())
window.state('normal')

    ## iconify will send the window down so that it is visible in the taskbar
window.iconify()
    ## deiconify will return it back to normal state
window.deiconify()

    ## default size of window = 200 px x 200 px
    ## parameters: window.geometry('WIDTHxHEIGHT+X+Y')
window.geometry('640x480+50+100')
print(window.geometry())
    ## Indicate whether user may resize the window (X,Y)
window.resizable(False, False)
window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)

    ## Destroy all child widgets 
root.destroy()

root.mainloop()


## Separating widgets within paned windows 

from Tkinter import *
import ttk 
    
root = Tk()

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)
    ## paned window will expand the frame to fit the size vertically

frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKEN)
panedwindow.insert(1, frame3)
    ## Remove widget from paned window
    ## Does not destroy the frame; it still exists in the background so can re-add as needed
panedwindow.forget(1)

root.mainloop()


## Grouping widgeting within a tabbed notebook

from Tkinter import *
import ttk 
    
root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

    ## frame needs to be a child of the notebook that it is being added to 
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One')
    ## Add tabs to the right of existing tabs 
notebook.add(frame2, text = 'Two')
ttk.Button(frame1, text = 'Click Me').pack()
    ## All frames will be the same size

frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text = 'Three')
notebook.forget(1)
notebook.add(frame3, text = 'Three')

print(notebook.select())
    ## Determine which tab in notebook is currently selected
print(notebook.index(notebook.select()))
    ## Programmatically select particular tab
notebook.select(2)

notebook.tab(1, state = 'disabled')
    ## 'hidden' = no longer visible
notebook.tab(1, state = 'hidden')
notebook.tab(1, state = 'normal')
    ## determine text property
notebook.tab(1, 'text')
    ## determine all properties of particular tab
notebook.tab(1)

root.mainloop()


## Entering and displaying multiple lines with the Text widget 
## Adding tags, marks, images, and widgets to the text widget 

from Tkinter import *      
    
root = Tk()

    ## width and height relative to the number of characters
text = Text(root, width = 40, height = 10)
text.pack()
    ## By default the text box wraps text exactly at the end of each line and may wrap in the middle of words
    ## config options = care (character; default), none (no wrapping), word (wrap at nearest space)
text.config(wrap = 'word')

    ## Get method requires one or two input parameters, which are the indices of a place in the text
        ## One parameter = return the character at that index
        ## Two parameter = return the string of characters between those indices 
    ## Text widget needs to index characters across multiple lines which is effectively 2D space

    ## Returns the entire contents of the text widget from beginning to end
print(text.get('1.0', 'end'))
    ## Go to the index at the end of the first line 
print(text.get('1.0', '1.end'))

    ## Insert method takes two parameters with 
text.insert('1.0 + 2 lines', 'Inserted message')
    ## lineend = insert at the end of the line
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')

    ## non-inclusive delete method
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')

    ## Replace method takes 2 parameters 
text.replace('1.0', '1.0 lineend', 'This is the first line.')

    ## Disabled state prevents any modifications to the existing text field
text.config(state = 'disabled')
text.delete('1.0', 'end')
text.config(state = 'normal')

text.tag_add('my_tag', '1.0', '1.0 wordend')
    ## Most recently created tag has the highest priority when conflict arises
text.tag_configure('my_tag', background = 'yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())
text.replace('my_tag.first', 'my_tag.last', 'That was')
text.tag_delete('my_tag')

    ## Marks specify a single position which exist between two characters 
text.mark_names()
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
    ## Gravity of mark determined whether the mark will stick to the character on its left or right if things shift around
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

image = PhotoImage(file = 'python_logo.gif').subsample(5, 5) # Change path as needed
text.image_create('insert', image = image)
text.image_create('insert', image = image)

button = Button(text, text = 'Click Me')
text.window_create('insert', window = button)

root.mainloop()


## Building a hierarchical treeview

## Tree view widget can be used to display a list of items that the user can interact with and make selections from
    ## Presented on a single level or as part of a multi-tiered hierarchy

from Tkinter import *
import ttk
    
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()
    ## Each item represents a node in the tree
        ## Parameter 1 = parent node of the new item
        ## Parameter 2 = position in the list under the parent node in which to insert the item
        ## Parameter 3 = item ID
        ## Parameter 4 = text property of item (optional)
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

logo = PhotoImage(file = 'python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)

treeview.config(height = 5)
treeview.move('item2', 'item1', 'end')
    ## Default = closed position
treeview.item('item1', open = True)
treeview.item('item2', open = True)
print(treeview.item('item1', 'open'))

treeview.detach('item3')
treeview.move('item3', 'item2', '0')
treeview.delete('item3')

treeview.configure(column = ('version'))
treeview.column('version', width = 50, anchor = 'center')
treeview.column('#0', width = 150)
treeview.heading('version', text = 'Version')
treeview.set('python', 'version', '3.4')
treeview.item('python', tags = ('software'))
treeview.tag_configure('software', background = 'yellow')

def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback)

    ## Default = extended select mode i.e. allows for multiple items to be selected at once
    ## Browse select mode = allow one item to be selected at a time
    ## None select mode = does not allow any selection of items from the tree
treeview.config(selectmode = 'browse')
print(treeview.selection_add('python'))
print(treeview.selection_remove('python'))
print(treeview.selection_toggle('python'))

root.mainloop()


## Building cascading menus 
## Errors in running program -- 'add_command' parameters

from Tkinter import *

root = Tk()

root.option_add('*tearOff', False)
    ## Indicates not to create a tearable menu
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

##file.add_command(label = 'New', command = lambda:print('New File'))
##file.add_separator()
##file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
##file.add_command(label = 'Save', command = lambda: print('Saving File...'))
##
##file.entryconfig('New', accelerator = 'Ctrl+N')
##logo = PhotoImage(file = 'python_logo.gif').subsample(10, 10)
##file.entryconfig('Open...', image = logo, compound = 'left')
##file.entryconfig('Open...', state = 'disabled')
##
##file.delete('Save')
##save = Menu(file)
##file.add_cascade(menu = save, label = 'Save')
##save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
##save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

choice = IntVar()
edit.add_radiobutton(label = 'One', variable = choice, value = 1)
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)

    ## Draw file menu by passing x-y coordinates relative to entire screen
file.post(400, 300)

root.mainloop()


## Drawing a basic line on the canvas 

from Tkinter import *
    
root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)

line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
canvas.itemconfigure(line, fill = 'green')
print(canvas.coords(line))
    ## Specify three pair of coordinates 
canvas.coords(line, 0, 0, 320, 240, 640, 0)

canvas.itemconfigure(line, smooth = True)
canvas.itemconfigure(line, splinesteps = 5)
canvas.itemconfigure(line, splinesteps = 100)
canvas.delete(line)

rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill = 'yellow')
oval = canvas.create_oval(160, 120, 480, 360)
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

logo = PhotoImage(file = 'python_logo.gif') # Change path as needed
image = canvas.create_image(320, 240, image = logo)

canvas.lift(text)
canvas.lower(image)
canvas.lower(image, text)

button = Button(canvas, text = 'Click Me')
canvas.create_window(320, 60, window = button)

canvas.itemconfigure(rect, tags = ('shape'))
canvas.itemconfigure(oval, tags = ('shape', 'round'))
canvas.itemconfigure('shape', fill = 'grey')
print(canvas.gettags(oval))

root.mainloop()


## Attaching scroll bars to widgets 

from Tkinter import *
import ttk 
    
root = Tk()

text = Text(root, width = 40, height = 10, wrap = 'word')
text.grid(row=0, column=0)
scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
    ## yview method tells the widget how far the scroll bar has moved so that it can change its view accordingly
scrollbar.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand = scrollbar.set)

    ## Rather than define width/height of the canvas, define the scroll region over which the canvas will scroll
canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
        ## Translate x-y coordinates to where they actually appear on the canvas 
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

    ## Bind method = bind it to whenever the user clicks the mouse button
canvas.bind('<1>', canvas_click)

root.mainloop()


## Configuring widget styles 

from Tkinter import *
import ttk 
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

style = ttk.Style()

    ## Determine which theme system is currently using - call without any parameters
print(style.theme_use())
    ## Change the theme being used 
style.theme_use('classic')
style.theme_use('aqua')

    ## Find out name of the default style that a widget uses
print(button1.winfo_class())
style.configure('TButton', foreground = 'blue')
style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold'))
button2.configure(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])
button2.state(['disabled'])

print(style.layout('TButton'))
print(style.element_options('Button.label'))
print(style.lookup('TButton', 'foreground'))

root.mainloop()


## Prompting users with the Messagebox and dialogs

import Tkinter
import tkMessageBox

tkMessageBox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')
print(tkMessageBox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))

import tkFileDialog as filedialog
filename = filedialog.askopenfile()
print(filename.name)

import tkColorChooser
print(tkColorChooser.askcolor(initialcolor = "#FFFFFF"))


## Using the pack geometry manager

from Tkinter import *
import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(
##              fill = BOTH, expand = True)
                side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(
##              fill=BOTH)
              side = LEFT, padx = 10, pady = 10)
    ## external padding refers to number of pixels in x-y direction
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(
##              fill=BOTH, expand = True)
                side = LEFT, ipadx = 10, ipady = 10)
    ## internal padding refers to number of pixels in x-y direction
for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand = True)
        ## Print properties related to pack mnanager, not the widget properties
    print(widget.pack_info())

root.mainloop()


## Using the grid geometry manager

from Tkinter import *
import ttk        
    
root = Tk()

ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

root.mainloop()


## Using the place geometry manager 

from Tkinter import *
import ttk        
    
root = Tk()
root.geometry('640x480+200+200')

    ## Place manager - place a label at an exact location within that master window by providing x and y coordinates (absolute coordinates)
ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
    ## Place the widget in relative locations based on the current size of the parent frame
    ## Values for rele x-y are fractional values [0,1] - represent the percentage of the current width/height of the parent frame to place the widget
ttk.Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
    ## Anchor property [N, S, E, W] = change which part of the label is placed at the specified coordinates
    ## Default anchor = NW (top-left corner)
ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()


## Configuring command callbacks

from Tkinter import *
import ttk        

def callback(number):
    print(number)
    
root = Tk()

    ## lambda creates an anonymous function containing callback method
        ## Use to configure the callback command
ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()

root.mainloop()


## Binding to keyboard events 

from Tkinter import *
import ttk        

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}\n'.format(event.keycode))

def shortcut(action):
    print(action)
    
root = Tk()

    ## Bind method on the master root window
        ## Parameter 1 = string containing specially-formatted descriptions of the events
        ## Parameter 2 = name of the callback function/method to execute
    ## Need to give one input parameter that the event handler will use to parse an object containing info about the keyboard event
root.bind('<KeyPress>', key_press)
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()


## Binding to mouse events 
## Recommended to bind mouse events to individual widgets within the program 

from Tkinter import *
import ttk        

    ## Trigger event only if click on the canvas 
def mouse_press(event):
    global prev
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
        ## Coordinates are in reference to a location on the widget
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
        ## Coordinates in reference to the screen
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}\n'.format(event.y_root))
    prev = event

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event
    
root = Tk()

canvas = Canvas(root, width = 640, height = 480, 
                background = 'white')
canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()


## Binding to virtual events 
    ## Errors in running program

from Tkinter import *
import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
##entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

entry.event_delete('<<OddNumber>>')

root.mainloop()


## Binding to multiple events 

from Tkinter import *
import ttk        
    
root = Tk()

label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<BP> Label'))
label1.bind('<1>', lambda e: print('<1> Label'))

root.bind('<1>', lambda e: print('<1> Root'))

label1.unbind('<1>')
label1.unbind('<ButtonPress>')

root.bind_all('<Escape>', lambda e: print('Escape!'))

root.mainloop()


## Creating a customized widget

from Tkinter import *
import ttk
import tkMessageBox

class Feedback:

    def __init__(self, master):
        
        master.title('Explore California Feedback')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        tkMessageBox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
    
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
         
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()


