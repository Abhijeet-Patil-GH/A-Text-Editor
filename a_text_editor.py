#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# A Text Editor Project using Python

# 'A Text Editor' is a simple text editor like any Microsoft Text Editor which allows you to edit your text style, size, color and also provides all the editing funcitonality and environment.
# This Text Editor is efficient, easy to use, simple, cross-platform, and free to have its experience.
# The programming for 'A Text Editor' will be in the way of 'procedure oriented' and not 'OOP', hence all codes and functionality are need to be in a proper procedure and place for its working and use.


######################################################### A Text Editor Program ###########################################################


# Import Files and Modules
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os


# Create main window
main_application = tk.Tk()
main_application.geometry("1600x900")                  # Application Resolution
main_application.title("A Text Editor")
main_application.wm_iconbitmap("icon.ico")


########################################################## Main Menu ######################################################################



main_menu = tk.Menu()


# FOR FILE MENU

# Add icons for the sub-menus of Menus of Menubar using .PhotoImage Class of tkinter with icon location/name
new_icon = tk.PhotoImage(file = 'icons/new.png')
open_icon = tk.PhotoImage(file = 'icons/open.png')
save_icon = tk.PhotoImage(file = 'icons/save.png')
save_as_icon = tk.PhotoImage(file = 'icons/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons/exit.png')

# Create Menus for Main Menu along with their drop-down sub-menus with details
file = tk.Menu(main_menu, tearoff = False)


# FOR EDIT MENU

copy_icon = tk.PhotoImage(file = 'icons/copy.png')
paste_icon = tk.PhotoImage(file = 'icons/paste.png')
cut_icon = tk.PhotoImage(file = 'icons/cut.png')
clear_all_icon = tk.PhotoImage(file = 'icons/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons/find.png')

edit = tk.Menu(main_menu, tearoff = False)


# FOR VIEW MENU

tool_bar_icon = tk.PhotoImage(file = 'icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons/status_bar.png')

view = tk.Menu(main_menu, tearoff = False)


# FOR COLOR THEME

light_default_icon = tk.PhotoImage(file = 'icons/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')
red_icon = tk.PhotoImage(file = 'icons/red.png')
monokai_icon = tk.PhotoImage(file = 'icons/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff = False)

theme_choice = tk.StringVar()                                    # Since, our color theme will change after specific selection, we use radiobutton, and accpets a value 
 
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)          # Created a tuple of all image icons the use of loop

color_dict = {                                                   # The names, and color hex values are stored in dict. for using them by looping
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3d774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}


# Cascade Menus in Main Menu
main_menu.add_cascade(label = 'File', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'View', menu = view)
main_menu.add_cascade(label = 'Color Theme', menu = color_theme)



#-------------------------------------------------------- End Main Menu ------------------------------------------------------------------#



########################################################## Toolbar ########################################################################



# CREATE TOOL BAR
# The tool bar consist of many tools which can be used to edit our text.

tool_bar = ttk.Label(main_application)                    # A toolbar created without label name
tool_bar.pack(side = tk.TOP, fill = tk.X)                 # Toolbar position set using .pack()


# CREATE FONT BOX OF TOOL BAR
 
font_tuple = tk.font.families()                           # Import font families which are present in tuple
font_var = tk.StringVar()                                 # It accepts a Stirng value

font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_var, state = 'readonly')         # Font box will be a combobox in toolbar
font_box['values'] = font_tuple                           # Values of combobox
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0, column = 0, padx = 5)


# CREATE SIZE BOX OF TOOL BAR

size_var = tk.IntVar()                                    # Size box accpts a user value 

size_box = ttk.Combobox(tool_bar, width = 15, textvariable = size_var, state = 'readonly')            # Size box will be a comboox in toolbar
size_box['values'] = tuple(range(8,82,2))                 # Values of size box with step arg.
size_box.current(2)
size_box.grid(row = 0, column = 1, padx = 5)


# CREATE BOLD BUTTON

bold_icon = tk.PhotoImage(file = 'icons/bold.png')              # Image for button
bold_button = ttk.Button(tool_bar, image = bold_icon)           # Created the button on toolbar
bold_button.grid(row = 0, column = 2, padx = 5)                 # Grid button position


# CREATE ITALIC BUTTON

italic_icon = tk.PhotoImage(file = 'icons/italic.png')
italic_button = ttk.Button(tool_bar, image = italic_icon)
italic_button.grid(row = 0, column = 3, padx = 5)


# CREATE UNDERLINE BUTTON

underline_icon = tk.PhotoImage(file = 'icons/underline.png')
underline_button = ttk.Button(tool_bar, image = underline_icon)
underline_button.grid(row = 0, column = 4, padx = 5)


# CREATE FONT COLOR BUTTON

font_color_icon = tk.PhotoImage(file = 'icons/font_color.png')
font_color_button = ttk.Button(tool_bar, image = font_color_icon)
font_color_button.grid(row = 0, column = 5, padx = 5)


# CREATE LEFT ALIGN BUTTON

align_left_icon = tk.PhotoImage(file = 'icons/align_left.png')
align_left_button = ttk.Button(tool_bar, image = align_left_icon)
align_left_button.grid(row = 0, column = 6, padx = 5)


# CREATE CENTER ALIGN BUTTON

align_center_icon = tk.PhotoImage(file = 'icons/align_center.png')
align_center_button = ttk.Button(tool_bar, image = align_center_icon)
align_center_button.grid(row = 0, column = 7, padx = 5)


# CREATE RIGHT ALIGN BUTTON

align_right_icon = tk.PhotoImage(file = 'icons/align_right.png')
align_right_button = ttk.Button(tool_bar, image = align_right_icon)
align_right_button.grid(row = 0, column = 8, padx = 5)



#-------------------------------------------------------- End Tool Bar -------------------------------------------------------------------#



########################################################## Text Editor ####################################################################



# CREATE TEXT EDITOR WITH ITS SCROLL BAR
# A text editor is the interface where user is going to write his/her text

text_editor = tk.Text(main_application)                               # Create text editor using Text class
text_editor.config(wrap = 'word', relief = tk.FLAT)                   # Here,  wrap=word means, it will break line after last word fits, otherwise it will break by default of any char at new line
text_editor.focus_set()                                               # Also, relief=flat is the flat style of text in text editor, focus_set() sets the cursor default at text editor


scroll_bar = tk.Scrollbar(main_application)                           # Create scrollbar using scrollbar class

scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)                         # Set posi of scroll bar before text editor class, as it will be organized properly
text_editor.pack(expand = True, fill = tk.BOTH)


scroll_bar.config(command = text_editor.yview)                           # Scrollbar configuration at yview 
text_editor.config(yscrollcommand = scroll_bar.set)                      # Scrollbar config in text editor


# FUNCTIONALITY FOR FONT FAMILY AND FONT SIZE

current_font_family = 'Arial'                                            # Store current font family and size
current_font_size = 12


# CREATE FUNCTION FOR THE FUNCTIONALITY OF FONT FAMILY IN TEXT EDITOR

# Function for font family
def change_font(event = None) :                                               # This function takes a arg. as anything, given None as we need to pass any arg. for the working of bind class 
    global current_font_family                                                # We have changed the global var in function as everytime it should change when user choose any font
    current_font_family = font_var.get()                                      # Get user inputed value as current font value
    text_editor.configure(font = (current_font_family, current_font_size))    # Configure user text with new font family and existing font size 
# For combobox we use bind instead of command
font_box.bind('<<ComboboxSelected>>', change_font)                            # We can bind any widget with function using bind class with type of widget in angle bracs.

# Function for font size
def change_size(event = None) :                                               # Similar for size function
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family, current_font_size))

size_box.bind('<<ComboboxSelected>>', change_size)

text_editor.configure(font = (current_font_family, current_font_size))        # Configure current/default font family and size


# CREATE FUNCTION FOR THE FUNCTIONALITY OF TOOLBAR BUTTONS

# Function for bold button
def change_bold() :
    try :
        current_tags = text_editor.tag_names("sel.first")                     # Tag names are user defined/ selected tags 
        if "bold" in current_tags :                                           # If the seleted tags already have property of bold, then remove bold from 1st selected position to last selected position
            text_editor.tag_remove("bold", "sel.first", "sel.last")
        else :                                                                # If selected tags dont have bold property
            text_editor.tag_add("bold", "sel.first", "sel.last")              # Add a tag in text editior from starting posi to end posi
            bold_font = font.Font(text_editor, text_editor.cget("font"))      # Font meth. in font class on text-editor to get the font 
            bold_font.configure(weight = "bold")                              # Configure the font with bold
            text_editor.tag_configure("bold", font = bold_font)               # Configure the selected tag with bold property and its font
    except :
        return


bold_button.configure(command = change_bold)

# Function for italic button
def change_italic() :                                                         # Similarly for italic font 
    try :
        current_tags = text_editor.tag_names("sel.first")
        if "italic" in current_tags :
            text_editor.tag_remove("italic", "sel.first", "sel.last")
        else :
            text_editor.tag_add("italic", "sel.first", "sel.last")
            italic_font = font.Font(text_editor, text_editor.cget("font"))
            italic_font.configure(slant = "italic")
            text_editor.tag_configure("italic", font = italic_font)
    except :
        pass

italic_button.configure(command = change_italic)

# Function for italic button
def change_underline() :                                                      # Similarly for underline font
    try :
        current_tags = text_editor.tag_names("sel.first")
        if "underline" in current_tags :
            text_editor.tag_remove("underline", "sel.first", "sel.last")
        else :
            text_editor.tag_add("underline", "sel.first", "sel.last")
            underline_font = font.Font(text_editor, text_editor.cget("font"))
            underline_font.configure(underline = 1)
            text_editor.tag_configure("underline", font = underline_font)
    except :
        pass

underline_button.configure(command = change_underline)

# Function for font color button

def change_font_color() :
    color_var = colorchooser.askcolor()                                 # Imported colorchooser class have a method .askcolor() which gives a widget for user to choose a color and input a value which can be saved in a var
    text_editor.configure(foreground = color_var[1])                    # Configure the text_editor text(fore) color with user selected color which hex RGB value is at 1st posi. of .askcolor()

font_color_button.configure(command = change_font_color)

# Function for Align Left Button

def change_align_left() :
    text_content = text_editor.get(1.0, tk.END)                         # Get the entire content of text in text editor from 1 to end and store it in a variable
    text_editor.tag_config('left', justify = tk.LEFT)                   # Config our tag name with justification
    text_editor.delete(1.0, tk.END)                                     # Delete the previous content of the text editor
    text_editor.insert(tk.INSERT, text_content, tk.LEFT)                # Now, insert the text of text content in the left as it is align left

align_left_button.configure(command = change_align_left)

# Function for Align Center Button

def change_align_center() :
    text_content = text_editor.get(1.0, tk.END)                         # Similarly for align center
    text_editor.tag_config('center', justify = tk.CENTER)
    text_editor.delete(1.0, tk.END) 
    text_editor.insert(tk.INSERT, text_content, tk.CENTER)

align_center_button.configure(command = change_align_center)

# Function for Align Right Button

def change_align_right() :
    text_content = text_editor.get(1.0, tk.END)                         # Similarly for align right
    text_editor.tag_config('right', justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END) 
    text_editor.insert(tk.INSERT, text_content, tk.RIGHT)

align_right_button.configure(command = change_align_right)



#-------------------------------------------------------- End Text Editor ----------------------------------------------------------------#



########################################################### Status Bar ####################################################################



# CREATE A STATUS BAR FOR THE TEXT EDITOR

status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

# CREATE FUNCTION FOR THE FUNTIONALITY OF STATUS BAR

text_changed = False
def change_status_bar(event = None) :                                              # Function of status bar with event=None for bind meth.
    global text_changed
    if text_editor.edit_modified() :                                               # A Method in text editor which returns a modified/edited flag or content of text editor currently
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split(" "))                     # Since we need to count words, we use len() and get all content in text editor with 'end-1c' i.e dont count char of new line which is by default and split words with " "
        characters = len(text_editor.get(1.0, 'end-1c'))                           # Count the number of characters with spaces and end(minus)1c
        status_bar.config(text = f"Characters : {characters} Words : {words}")     # Config status bar with every value modified/typed in words, chars with this print line and values
    text_editor.edit_modified(False)                                               # After 1 word/ char is typed for the 2nd word/char modification we need to make previous false for new value get, store and print

text_editor.bind('<<Modified>>', change_status_bar)                                # Bind text editor modified after every word/cahr input with the function



#--------------------------------------------------------- End Status Bar ----------------------------------------------------------------#



########################################################## Main Menu Functionality ########################################################



# ADD COMMANDS/ SUB MENUS OF MENU IN MAIN FUNCTIONALITY since we are doing procedure oriented programming for text editor and not OOP 

url = ''                                                             # Create a global variable 'url' for the path/existence of any file for fucntionality

# FOR FILE MENU

# FOR NEW FILE

# Function for new file 
def new_file(event=None) :                                           # Event=None since we use bind() to bind with the accelators
    global url, text_changed                                         # Use two global var in func
    try :
        if text_changed :                                            # If any of our text in main text editor is changed and we click in exit
            msgbox = messagebox.askyesnocancel('Warning','Do you want to save this file ?')            # The exit function will display a message box and ask to save a file with yes, no, cancel option
            if msgbox is True :                                      # If we select yes, then value of msgbox is 1 i.e True and our if block will execute
                if url :                                             # If url already exits, save in it
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w',encoding = 'utf-8',) as fw :
                        fw.write(content)
                        text_editor.delete(1.0, tk.END)
                else :                                               # If url does not exit, create a new file and save in it
                    content_new = str(text_editor.get(1.0, tk.END))     
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
                    url.write(content_new)
                    url.close()
                    text_editor.delete(1.0, tk.END)                  # And, clear our text editor
            elif msgbox is False :                                   # If user, does select No whose value is 0 i.e False, then without saving our window will get simply destory, and it user select cancel then only our msgbox window will get destroy
                text_editor.delete(1.0, tk.END)
        else :                                                       # Else if text is not changed then, user can simply exit and window will get destroy
            text_editor.delete(1.0, tk.END)
    except :
        return

# Add the sub-menus in menu with the image icon and accelerator(shortcut) keys and compound image to LEFT 
file.add_command(label = 'New', image = new_icon, compound = tk.LEFT, accelerator = 'Ctrl+N', command = new_file)
file.add_separator()


# FOR OPEN FILE

# Fucntion for open file
def open_file(event=None) :
    global url, text_changed
    # The askopenfilename function of filedialog is used to open a new window with title and can open in given initialdir along with the types of files the window want to show and returns a string of file path with name when opened
    
    try :                                                            # Exception Handling for file not found
        if text_changed :                                            # If any of our text in main text editor is changed and we click in exit
            msgbox = messagebox.askyesnocancel('Warning','Do you want to save this file ?')            # The exit function will display a message box and ask to save a file with yes, no, cancel option
            if msgbox is True :                                      # If we select yes, then value of msgbox is 1 i.e True and our if block will execute
                if url :                                             # If url already exits, save in it
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w',encoding = 'utf-8',) as fw :
                        fw.write(content)
                        text_editor.delete(1.0, tk.END)
                    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text Files','*.txt'),('All Files','*.*')))          # This method is of tkinter allows us to open file in specific got url in a window with window name, types of files
                    with open(url, 'r') as fr :                      # Open the given path url as readonly
                        text_editor.insert(1.0, fr.read())
                else :                                               # If url does not exit, create a new file and save in it
                    content_new = str(text_editor.get(1.0, tk.END))     
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
                    url.write(content_new)
                    url.close()
                    text_editor.delete(1.0, tk.END)                  # And, clear our text editor
                    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
                    with open(url, 'r') as fr :                      # Open the given path url as readonly
                        text_editor.insert(1.0, fr.read())
            elif msgbox is False :                                   # If user, does select No whose value is 0 i.e False, then without saving our window will get simply destory, and it user select cancel then only our msgbox window will get destroy
                text_editor.delete(1.0, tk.END)
                url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
                with open(url, 'r') as fr :                      
                    text_editor.insert(1.0, fr.read())
        else :
            url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
            with open(url, 'r') as fr :                             # Open the given path url as readonly
                text_editor.insert(1.0, fr.read())        
    except FileNotFoundError :                                      # If file not found to open
        return                                                      # A return statement which returns None ends the function with except error
    except :                                                        # Else for anyother error ends the func
        return
    main_application.title(os.path.basename(url))                   # When we open the file, change the name of main app. with the name of that file with file extension

file.add_command(label = 'Open', image = open_icon, compound = tk.LEFT, accelerator = 'Ctrl+O', command = open_file)
file.add_separator()


# FOR SAVE FILE

# Function for save file 
def save_file(event=None):
    global url
    try :
        if url :                                                    # If our url exits ie our file is already saved in the directory
            content = str(text_editor.get(1.0, tk.END))             # Get all the new as well as existing content of our text editor
            with open(url, 'w', encoding = 'utf-8') as fw :         # Open with 'with' with encoding in write mode 
                fw.write(content)                                   # Write all content in the existing file
        else :
            # If url does not exits then we use .asksaveasfile which gives a window to save a new file with default extn, types of files present and in write mode and return a string of url
            url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
            content_new = str(text_editor.get(1.0, tk.END))         # Get all content of the text editor
            url.write(content_new)                                  # Write it in new created file with url
            url.close()                                            
    except :
        return                     

file.add_command(label = 'Save', image = save_icon, compound = tk.LEFT, accelerator = 'Ctrl+S',command = save_file)


# FOR SAVE AS FILE

# Function for save as file
def save_as_file(event = None) :
    global url
    try :
        # In save as, as we create a new file and save all content in it by keeping the og file, as same, so we get content of text editor,  create new url for save file and write all in it.
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
        url.write(content)                                  
        url.close()
    except :
        return         

file.add_command(label = 'Save As', image = save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S', command = save_as_file)
file.add_separator()


# FOR EXIT FILE

# Function for exit file 
def exit_file(event=None) :
    global url, text_changed                                         # Use two global var in func
    try :
        if text_changed :                                            # If any of our text in main text editor is changed and we click in exit
            msgbox = messagebox.askyesnocancel('Warning','Do you want to save this file ?')            # The exit function will display a message box and ask to save a file with yes, no, cancel option
            if msgbox is True :                                      # If we select yes, then value of msgbox is 1 i.e True and our if block will execute
                if url :                                             # If url already exits, save in it
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w',encoding = 'utf-8',) as fw :
                        fw.write(content)
                        main_application.destroy()
                else :                                               # If url does not exit, create a new file and save in it
                    content_new = str(text_editor.get(1.0, tk.END))     
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files','*.txt'),('All Files','*.*')))
                    url.write(content_new)
                    url.close()
                    main_application.destroy()                       # And, destory our application
            elif msgbox is False :                                   # If user, does select No whose value is 0 i.e False, then without saving our window will get simply destory, and it user select cancel then only our msgbox window will get destroy
                main_application.destroy()
        else :                                                       # Else if text is not changed then, user can simply exit and window will get destroy
            main_application.destroy()
    except :
        return

file.add_command(label = 'Exit', image = exit_icon, compound = tk.LEFT, accelerator = 'Ctrl+Q', command = exit_file)


# FOR EDIT MENU

# Functionality of copy, paste, cut, clear all can be done using tkinter event_generate() method as arg. for command para. which also does the accelarator key bindings
# The event_generate() method generates a event specified or passed as an arg.in it which is builtin in py tkinter module

# Copy Text
edit.add_command(label = 'Copy', image = copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C', command = lambda:text_editor.event_generate("<Control c>"))

# Paste Text
edit.add_command(label = 'Paste', image = paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V', command = lambda:text_editor.event_generate("<Control v>"))

# Cut Text
edit.add_command(label = 'Cut', image = cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X', command = lambda:text_editor.event_generate("<Control x>"))
edit.add_separator()

# Clear all Text
edit.add_command(label = 'Clear All', image = clear_all_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+X', command = lambda:text_editor.delete(1.0, tk.END))
edit.add_separator()

# FOR FIND FILE

# Function for find file
def find_text(event=None) :
    # We create window when we click find button in text editor and also define function inside function, for find/replace buttons in it
    # FUNCTIONS FOR FUNCTIONALITY OF FIND WINDOW BUTTONS 
    # Function for find
    def find() :
        word = find_entry.get()                                                                 # Get the word/string from the entry box
        text_editor.tag_remove('match', '1.0', tk.END)                                          # Remove the word/string which it matches in our text in text editor from start to end
        matches = 0
        if word :                                                                               # If we get the word
            start_pos = '1.0'                                                                   
            while True :
                start_pos = text_editor.search(word, start_pos, stopindex = tk.END)             # Search thr word from start to end in text editor
                if not start_pos :
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match', start_pos, end_pos)                                # Add the word which is match from start to end 
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'red', background = 'yellow')      # Change all the found matches fg and bg color


    # Function for replace    
    def replace() :
        find_text = find_entry.get()                                                            # Get text from find entry that we want to get replaced
        replace_text = replace_entry.get()                                                      # Get text from replace entry that we want replace
        content = text_editor.get(1.0, tk.END)                                                  # Get entire content of text editor
        new_content = content.replace(find_text, replace_text)                                  # New content is content with replaced old text with new
        text_editor.delete(1.0, tk.END)                                                         # Delete all prev. content from text editor
        text_editor.insert(1.0, new_content)                                                    # Add new content in text editor with replaced text

    
    # DESIGN OF WINDOW FOR FIND AND REPLACE USING tkinter
    find_dialogue = tk.Toplevel()                                                               # Create a window on top level
    find_dialogue.geometry('450x200+500+200')                                                   # Resolution 
    find_dialogue.title('Find & Replace')                           
    find_dialogue.resizable(0,0)                                                                # User cannot resize the window

    # CREATE FRAME IN WINDOW
    find_frame = ttk.LabelFrame(find_dialogue, text = 'Find/Replace')
    find_frame.pack(pady = 20)

    # CREATE LABELS IN THE FRAME
    find_label = ttk.Label(find_frame, text = 'Find : ')
    replace_label = ttk.Label(find_frame, text = 'Replace :')

    # CREATE ENTRIES IN FRAME
    find_entry = ttk.Entry(find_frame, width = 30)
    replace_entry = ttk.Entry(find_frame, width = 30)

    # CREATE FIND AND REPLACE BUTTONS
    find_button = ttk.Button(find_frame, text = 'Find', command =find)
    replace_button = ttk.Button(find_frame, text = 'Replace', command = replace)

    # GRID LABELS IN FRAME
    find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    replace_label.grid(row = 1, column = 0, padx = 4, pady = 4)

    # GRID ENTRIED IN FRAME
    find_entry.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_entry.grid(row = 1, column = 1, padx = 4, pady = 4)

    # GRID BUTTONS IN FRAME
    find_button.grid(row = 2, column = 0, padx = 50, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 50, pady = 4)

    
    find_dialogue.mainloop()                                                                    # Window must end when user close it

edit.add_command(label = 'Find', image = find_icon, compound = tk.LEFT, accelerator = 'Ctrl+F', command = find_text)


# FOR VIEW MENU

# FOR TOOL BAR

show_tool_bar_var = tk.BooleanVar()                                                             # Var. for tool bar/ status bar which it accepts and is a boolean value and set to True
show_tool_bar_var.set(True)

# Function for tool bar
def hide_tool_bar() :
    global show_tool_bar_var
    if show_tool_bar_var :                                                                      # If our toolbar is visible and value is True
        tool_bar.pack_forget()                                                                  # .pack_forget() will hide the value of toolbar
        show_tool_bar_var = False                                                               # Make toolbar functionality disable
    else :
        text_editor.pack_forget()                                                               # If tool bar is not visisble and disable, we need to set every thing in order, since tool bar is in top then text editor and then comes the status bar
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(expand = True, fill =tk.BOTH)
        status_bar.pack(side = tk.BOTTOM)
        show_tool_bar_var = True    

view.add_checkbutton(label = 'Tool Bar', onvalue = 1, offvalue = 0, variable = show_tool_bar_var, image = tool_bar_icon, compound = tk.LEFT, command = hide_tool_bar)              # Here,  we have added checkbuttons with their labels, on-off value for on-off the functionality, accepts a user value in var. and a command for function


# FOR STATUS BAR

show_status_bar_var = tk.BooleanVar()
show_status_bar_var.set(True)

# Function for status bar                    
def hide_status_bar() :                                                                         # Similarly, for status bar
    global show_status_bar_var
    if show_status_bar_var :
        status_bar.pack_forget()
        show_status_bar_var = False
    else :
        status_bar.pack(side = tk.BOTTOM)                                                       # Here, we only need to set our status bar since it is present at the bottom of the GUI
        show_status_bar_var = True    

view.add_checkbutton(label = 'Status Bar', onvalue = 1, offvalue = 0, variable = show_status_bar_var, image = status_bar_icon, compound = tk.LEFT, command = hide_status_bar)


# FOR COLOR THEME
# A loop which can create radiobuttons for all color themes with their image icons and its color value

# Function for change theme
def change_theme() :
    chosen_theme = theme_choice.get()                                                           # Get the value which user will input from var.
    color_tuple = color_dict.get(chosen_theme)                                                  # Get the tuple value of color by key which user has chosen in dict 
    fg_color, bg_color = color_tuple[0], color_tuple[1]                                         # Set foreground, background
    text_editor.config(foreground = fg_color, background = bg_color)

for index, key in enumerate(color_dict) :
    color_theme.add_radiobutton(label = key, image = color_icons[index], variable = theme_choice, compound = tk.LEFT, command = change_theme)



#-------------------------------------------------------- End Main Menu Functionality ----------------------------------------------------#



main_application.config(menu = main_menu)


# BIND SHORTCUT KEYS ACCELERATORS

main_application.bind("<Control-n>", new_file)                                                   # Bind a key when used, our function gets call
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit_file)
main_application.bind("<Control-f>", find_text)


main_application.mainloop()


#-------------------------------------------------------- End Text Editor Program ---------------------------------------------------------#



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Unoffocial Windows Binaries for Python Extension Packages
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze