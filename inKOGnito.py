# Import necessary libraries and modules.
import customtkinter as ctk         # Customized version of the tkinter library.
import tkinter                      # Standard GUI package for Python in creating GUI elements.
from tkinter import messagebox      # Provides message boxes that can show warnings and informations.
import os                           # Allows to interact with the operating system to read and write to the file system.
from PIL import ImageTk, Image      # Provides tools used in PIL images in tkinter for handling images.
import pandas as pd                 # Allows you to read and manipulate the CSV data.
import csv                          # Provides functionality to both read from and write to CSV files.

# Creates the main window of application.
Landing_page = ctk.CTk()
Landing_page.title("inKOGnito")
Landing_page.geometry("1366x768")
Landing_page.iconbitmap("Banners\logo.ico")

# Sets the appearance mode of the application.
ctk.set_appearance_mode('dark')

# Function that go back to the main login page after the confirmation logout
def go_back():
    main_frame.pack_forget()
    main_login_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

# Function that go back to the main login page after the creation of account.
def go_back_login():
    main_register_frame.pack_forget()
    main_login_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

# Function that show/display the login interface.
def login_page():
    global user_Entry, pass_Entry
    log_Acc = ctk.CTkLabel(
        master = login_Frame, 
        text = "Login to your Account", 
        font = ("Segoe UI", 20, "bold")
    )
    log_Acc.place(
        x = 145, 
        y = 100
    )

    app_Welcome = ctk.CTkLabel(
        master = login_Frame, 
        text = "Welcome to inKOGnito!", 
        font = ("Arial", 25, "bold")
    )
    app_Welcome.place(
        x = 112, 
        y = 45
    )

    enter_User = ctk.CTkLabel(
        master = login_Frame, 
        text = "Username", 
        font = ("Arial", 15)
    )
    enter_User.place(
        x = 133, 
        y = 155
    )

    user_Entry = ctk.CTkEntry(
        login_Frame, 
        height = 40,
        width = 250, 
        placeholder_text = "Enter your Username"
    )
    user_Entry.place(
        x = 120, 
        y = 185
    )

    enter_Pass = ctk.CTkLabel(
        master = login_Frame, 
        text = "Password", 
        font = ("Arial", 15)
    )
    enter_Pass.place(
        x = 133, 
        y = 240
    )

    pass_Entry = ctk.CTkEntry(
        login_Frame, 
        height = 40, 
        width = 250, 
        placeholder_text = "Enter your Password", 
        show = "*"
    )
    pass_Entry.place(
        x = 120, 
        y = 270
    )

    login_Button = ctk.CTkButton(
        login_Frame,
        fg_color = ("#F875AA", "#8758FF"),
        text_color = "#000000",
        height = 35,
        width = 90,
        text = "Login",
        font = ("Arial", 15, "bold"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        command = authentication,
    )
    login_Button.place(
        x = 195, 
        y = 340
    )

    no_Acc = ctk.CTkLabel(
        login_Frame, 
        text = "No Account?", 
        font = ("Helvetica", 12)
    )
    no_Acc.place(
        x = 150, 
        y = 400
    )

    registeracc_button = ctk.CTkButton(
        login_Frame,
        fg_color = "transparent",
        text_color = ("#F875AA", "#8758FF"),
        height = 35,
        width = 30,
        text = "Create a New One",
        hover_color = ("#AEDEFC", "#5CB8E4"),
        font = ("Helvetica", 12, "bold"),
        command = register_Acc,
    )
    registeracc_button.place(
        x = 225, 
        y = 397.5)

    def mode_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    switch_var = ctk.StringVar(value="on")
    mode_switch = ctk.CTkSwitch(
        master = Landing_page,
        text = "Dark Mode",
        button_hover_color = ("#F875AA", "#8758FF"),
        progress_color = ("#AEDEFC", "#191919"),
        button_color = ("#F875AA", "#8758FF"),
        command = mode_event,
        variable = switch_var,
        onvalue = "on",
        offvalue = "off",
    )
    mode_switch.place(
        x = 25, 
        y = 670
    )

# Function that show/display the register account interface.
def register_Acc():
    main_login_frame.pack_forget()
    main_register_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

    register_Frame = ctk.CTkFrame(
        master = main_register_frame,
        height = 500,
        width = 500,
        corner_radius = 50,
        fg_color = ("#FFF6F6", "#191919"),
        border_width = 10,
        border_color = ("#F875AA", "#8758FF"),
    )
    register_Frame.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor = tkinter.CENTER
    )

    app_Welcome = ctk.CTkLabel(
        master = register_Frame, 
        text = "Welcome to inKOGnito!", 
        font = ("Arial", 25, "bold")
    )
    app_Welcome.place(
        x = 112, 
        y = 45
    )

    create_Acc = ctk.CTkLabel(
        master = register_Frame, 
        text = "Create your Account", 
        font = ("Ubuntu", 20, "bold")
    )
    create_Acc.place(
        x = 145, 
        y = 100
    )

    enter_Uniqueuser = ctk.CTkLabel(
        master = register_Frame, 
        text = "Enter Unique Username", 
        font = ("Ubuntu", 15)
    )
    enter_Uniqueuser.place(
        x = 133, 
        y = 155
    )

    enter_Newuser = ctk.CTkEntry(
        register_Frame, 
        height = 40, 
        width = 250, 
        placeholder_text = "Create your Username"
    )
    enter_Newuser.place(
        x = 120, 
        y = 185
    )

    enter_Uniquepass = ctk.CTkLabel(
        master = register_Frame, 
        text = "Enter Password", 
        font = ("Ubuntu", 15)
    )
    enter_Uniquepass.place(
        x = 133, 
        y = 240
    )

    enter_Newpass = ctk.CTkEntry(
        register_Frame, 
        height = 40, 
        width = 250, 
        placeholder_text = "Create your Password", 
        show = "*"
    )
    enter_Newpass.place(
        x = 120, 
        y = 270
    )

    # Function to write a new data in the CSV database.
    def write_NewUser():
        user_input = enter_Newuser.get()
        pass_input = enter_Newpass.get()

        # Condition that checks if the username is empty.
        if not user_input:
            messagebox.showerror("Registration Error", "Username cannot be empty. Please enter a username.")

        # Condition that checks if the username is already existing in the database file.
        elif user_Exist(user_input):
            messagebox.showerror("Invalid Username", "Username already taken. Please choose another one.")
            
            enter_Newuser.delete(0, 'end')
            enter_Newpass.delete(0, 'end')

        # Condition that checks if the password is empty.
        elif not pass_input:
            messagebox.showerror("Registration Error", "Password cannot be empty. Please enter a password.")

            register_Acc()

        # Adds the new user data to the CSV database.
        else:
            data_to_append = [[user_input, pass_input]]
            file = open("userinfo.csv", "a", newline="")
            writer = csv.writer(file)

            writer.writerows(data_to_append)

            file.close()
            
            # Read and update the user data in the CSV database.
            global userData
            userData = pd.read_csv("userinfo.csv")
        
            messagebox.showinfo("Registration Success", "Account created successfully!")

            go_back_login()

    create_Button = ctk.CTkButton(
        register_Frame,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        height = 35,
        width = 90,
        text = "Create",
        font = ("Ubuntu", 15, "bold"),
        command = write_NewUser,
    )
    create_Button.place(
        x = 195, 
        y = 340)

    have_Acc = ctk.CTkLabel(
        register_Frame, 
        text = "Already have Account?", 
        font = ("Helvetica", 12)
    )
    have_Acc.place(
        x = 150, 
        y = 400
    )

    signin_Button = ctk.CTkButton(
        register_Frame,
        fg_color = "transparent",
        text_color = ("#F875AA", "#8758FF"),
        height = 35,
        width = 30,
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "Sign In",
        font = ("Helvetica", 12, "bold"),
        command = go_back_login,
    )
    signin_Button.place(
        x = 280, 
        y = 395.5
    )

# Function that reads the user data from the CSV file.
def read_User():
    try:
        userData = pd.read_csv("userinfo.csv")
        userData["Password"] = userData["Password"].astype(str)
        return userData
    
    except FileNotFoundError:
        print("User data file not found.")
        return None

# Function that check if the username is already existing in the database.
def user_Exist(username):
    global userData
    if userData is not None:
        taken_Usernames = userData["Username"].tolist()
        return username in taken_Usernames
    else:
        return False

# Function that authenticates the user data based from username and password.
def authenticate_User(username, password):
    global userData
    if userData is not None:
        matches = userData.index[(userData.Username == username) & (userData.Password == password)].tolist()
        return matches
    else:
        return False

# Function that handles the authentication process.
def authentication():
    global userData
    username = user_Entry.get()
    password = pass_Entry.get()
    print(username, password)

    authenticated = authenticate_User(username, password)

    if authenticated:
        start_button_event()
        print("Login successful!")
    else:
        messagebox.showerror("Authentication Error", "Invalid username or password. Please try again.")

        user_Entry.delete(0, 'end')
        pass_Entry.delete(0, 'end')

# Reads and prints the user data.
userData = read_User()
print(userData)

# Function that handles the homepage of the app after having a successfu login.
def start_button_event():
    main_login_frame.pack_forget()
    main_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

    # Configuration and initializing the frame, introduction label, and logout in the main window.
    frame = ctk.CTkFrame(
        master = main_frame,
        height = 150,
        width = 400,
        fg_color = ("#FFF6F6", "#181818"),
        corner_radius = 15,
        border_width = 8,
        border_color = ("#F875AA", "#8758FF"),
    )
    frame.place(
        x = 485, 
        y = 30
    )

    # Function that confirms if you want to logout on the logged account in homepage.
    def confirm_logout():
        result = messagebox.askquestion("Logout", "Are you sure you want to log out?")
        if result == "yes":
            go_back()  

    logout = ctk.CTkButton(
        master = main_frame,
        text = 'Logout',
        font = ("Ubuntu", 16, "bold"),
        command = confirm_logout,
        fg_color = ('#F875AA', '#8758FF'),
        hover_color = ('#AEDEFC', '#5CB8E4')
    )
    logout.place(
        x = 15, 
        y = 30
    )

    Intro = ctk.CTkLabel(
        master = frame, 
        text = "inKOGnito", 
        font = ("UbuntuS", 50, "bold")
    )
    Intro.place(
        x = 80, 
        y = 50
    )
    
    # Calling out the banners from the local file sby using a file handling method.
    flappy_banner = ctk.CTkImage(Image.open("Banners\Flappy bird banner.png"), size = (300, 400))

    twenty_forty_banner = ctk.CTkImage(Image.open("Banners\\2048 banner.png"), size = (300, 400))

    hungry_snake_banner = ctk.CTkImage(Image.open("Banners\hungry snake banner.png"), size = (300, 400))

    donkey_banner = ctk.CTkImage(Image.open("Banners\Donkey kong banner.png"), size = (300, 400))

    mario_banner = ctk.CTkImage(Image.open("Banners\Super mario banner.png"), size = (300, 400))

    tic_tac_toe_banner = ctk.CTkImage(Image.open("Banners\Tic tac toe banner.png"), size = (300, 400))

    bomber_banner = ctk.CTkImage(Image.open("Banners\Bomber banner.png"), size = (300, 400))

    pacman_banner = ctk.CTkImage(Image.open("Banners\Pacman banner.png"), size = (300, 400))

    tetris_banner = ctk.CTkImage(Image.open("Banners\Tetris banner.png"), size = (300, 400))

    # Initializing and Configurations of the game frames and scrollable window.
    game_collection_frame = ctk.CTkScrollableFrame(
        master = main_frame,
        width = 1100,
        height = 500,
        fg_color = "transparent",
        scrollbar_button_color = ("#F875AA", "#8758FF"),
        scrollbar_button_hover_color = ("#AEDEFC", "#5CB8E4"),
    )
    game_collection_frame.place(
        x = 130,
        y = 220
    )

    # Game frames for games.
    game_frame1 = ctk.CTkFrame(
        master = game_collection_frame, 
        height = 400, 
        width = 1000, 
        fg_color = "transparent"
    )
    game_frame1.pack(
        pady = 10
    )

    game_frame2 = ctk.CTkFrame(
        master = game_collection_frame, 
        height = 400, 
        width = 1000, 
        fg_color = "transparent"
    )
    game_frame2.pack(
        pady = 10
    )

    game_frame3 = ctk.CTkFrame(
        master = game_collection_frame, 
        height = 400, 
        width = 1000, 
        fg_color = "transparent"
    )
    game_frame3.pack(
        pady = 10
    )

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Game Event/Button for Game 1 (Pacman).
    def game1_event():
        os.startfile("GAMES\Pacman\PacMan-Python-master\PacMan\main.exe")

    game1 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        image = pacman_banner,
        command = game1_event,
        text = "",
    )
    game1.pack(
        side = "left", 
        padx = 20
    )

    # Game Event/Button for Game 2 (Donkey Kong).
    def game2_event():
        os.startfile("GAMES\Donkey Kong\DonkeyKong_KendraTam_PythonProgrammi.exe")

    game2 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        image = donkey_banner,
        command = game2_event,
        text = "",
    )
    game2.pack(
        side = "right", 
        padx = 20)

    # Game Event/Button for Game 3 (Super Mario).
    def game3_event():
        os.startfile("GAMES\Super Mario\dist\Mario.exe")

    game3 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = mario_banner,
        command = game3_event,
    )
    game3.pack(
        side = "right", 
        padx = 20
    )

    # Game Event/Button for Game 4 (Flappy Bird).
    def game4_event():
        os.startfile("GAMES\Flappy Bird\Flappy.exe")

    game4 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = flappy_banner,
        command = game4_event,
    )
    game4.pack(
        side = "left", 
        padx = 20
    )

    # Game Event/Button for Game 5 (2048).
    def game5_event():
        os.startfile("GAMES\\2048\\2048.exe")

    game5 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = twenty_forty_banner,
        command = game5_event,
    )
    game5.pack(
        side = "right", 
        padx = 20
    )

    # Game Event/Button for Game 6 (Bomberman).
    def game6_event():
        os.startfile("GAMES\Bomberman\dist\menu.exe")

    game6 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = bomber_banner,
        command = game6_event,
    )
    game6.pack(
        side = "right", 
        padx = 20
    )

    # Game Event/Button for Game 7 (Tic Tac Toe).
    def game7_event():
        os.startfile('GAMES\Tic-Tac-Toe-Game-In-Python-master\Tic_Tac_Toe_Game.exe')

    game7 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = tic_tac_toe_banner,
        command = game7_event,
    )
    game7.pack(
        side = "left", 
        padx = 20
    )

    # Game Event/Button for Game 8 (Tetris).
    def game8_event():
        os.startfile("GAMES\Tetris Game\dist\Tetris.exe")

    game8 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = tetris_banner,
        command = game8_event,
    )
    game8.pack(
        side = "right", 
        padx = 20
    )

    # Game Event/Button for Game 9 (Hungry Snake).
    def game9_event():
        os.startfile("GAMES\Hungry Snake\Snake.exe")

    game9 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        text = "",
        image = hungry_snake_banner,
        command = game9_event,
    )
    game9.pack(
        side = "right", 
        padx = 20
    )

    # Function that enables the dark and light mode of the application.
    def mode_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    switch_var = ctk.StringVar(value="on")
    mode_switch = ctk.CTkSwitch(
        master = Landing_page,
        text = "Dark Mode",
        button_hover_color = ("#F875AA", "#8758FF"),
        progress_color = ("#AEDEFC", "#191919"),
        button_color = ("#F875AA", "#8758FF"),
        command = mode_event,
        variable = switch_var,
        onvalue = "on",
        offvalue = "off",
    )
    mode_switch.place(
        x = 25, 
        y = 670
    )


# Main loop event of the program.

# Main Login Frame
main_login_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)
main_login_frame.pack(
    fill = "both", 
    expand = True, 
    anchor = "center"
)

# Main Register Frame
main_register_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)

# Login Frame
login_Frame = ctk.CTkFrame(
    master = main_login_frame,
    height = 500,
    width = 500,
    corner_radius = 50,
    fg_color = ("#FFF6F6", "#191919"),
    border_width = 10,
    border_color = ("#F875AA", "#8758FF"),
)
login_Frame.place(
    relx = 0.5, 
    rely = 0.5, 
    anchor = tkinter.CENTER
)

# Main Frame
main_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)

# Calls the login_page function.
login_page()

# Starts the main event loop.
Landing_page.mainloop()
