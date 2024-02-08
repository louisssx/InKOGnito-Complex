import customtkinter as ctk
import tkinter
from tkinter import messagebox
import os
from PIL import ImageTk, Image
import pandas as pd
import csv


Landing_page = ctk.CTk()
Landing_page.title("inKOGnito")
Landing_page.geometry("1366x768")
Landing_page.iconbitmap("backgrounds\logo.ico")
ctk.set_appearance_mode('dark')

# my_background = ctk.CTkImage(light_image=Image.open('backgrounds\light.png'),
# dark_image=Image.open('backgrounds/dark.png'), size = (1920,1080))

# my_background = ctk.CTkLabel(Landing_page, text='', image= my_background)
# my_background.pack(
#     fill = "both", 
#     expand = True, 
#     anchor = "center"
# )
def go_back():
    main_frame.pack_forget()
    main_login_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

def go_back_login():
    main_register_frame.pack_forget()
    main_login_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

def login_page():
    global user_Entry, pass_Entry
    log_text = ctk.CTkFrame(
        master = login_Frame,
        fg_color = 'transparent',
        width = 450,
        height = 700
    )
    log_text.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor = tkinter.CENTER
    )
    log_Acc = ctk.CTkLabel(
        master = log_text, 
        text = "Login to your Account", 
        font = ("Segoe UI", 20, "bold")
    )
    log_Acc.place(
        x = 120, #from 145
        y = 200 
    )

    app_Welcome = ctk.CTkLabel(
        master = log_text, 
        text = "Welcome to inKOGnito!", 
        font = ("Arial", 25, "bold")
    )
    app_Welcome.place(
        x = 87, 
        y = 145
    )

    enter_User = ctk.CTkLabel(
        master = log_text, 
        text = "Username", 
        font = ("Arial", 15)
    )
    enter_User.place(
        x = 108, 
        y = 255
    )

    user_Entry = ctk.CTkEntry(
        log_text, 
        height = 40,
        width = 250, 
        placeholder_text = "Enter your Username"
    )
    user_Entry.place(
        x = 95, 
        y = 285
    )

    enter_Pass = ctk.CTkLabel(
        master = log_text, 
        text = "Password", 
        font = ("Arial", 15)
    )
    enter_Pass.place(
        x = 108, 
        y = 340
    )

    pass_Entry = ctk.CTkEntry(
        log_text, 
        height = 40, 
        width = 250, 
        placeholder_text = "Enter your Password", 
        show = "*"
    )
    pass_Entry.place(
        x = 95, 
        y = 370
    )

    login_Button = ctk.CTkButton(
        log_text,
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
        x = 170, 
        y = 440
    )

    no_Acc = ctk.CTkLabel(
        log_text, 
        text = "No Account?", 
        font = ("Helvetica", 12)
    )
    no_Acc.place(
        x = 125, 
        y = 500
    )

    registeracc_button = ctk.CTkButton(
        log_text,
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
        x = 200, 
        y = 497.5)

    def mode_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    switch_var = ctk.StringVar(value="on")
    mode_switch = ctk.CTkSwitch(
        master = log_text,
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

def register_Acc():
    main_login_frame.pack_forget()
    main_register_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )
    reg_text = ctk.CTkFrame(
        master = register_Frame,
        fg_color = 'transparent',
        width = 450,
        height = 700
    )
    reg_text.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor = tkinter.CENTER
    )

    app_Welcome = ctk.CTkLabel(
        master = reg_text, 
        text = "Welcome to inKOGnito!", 
        font = ("Arial", 25, "bold")
    )
    app_Welcome.place(
        x = 87, 
        y = 145
    )

    create_Acc = ctk.CTkLabel(
        master = reg_text, 
        text = "Create your Account", 
        font = ("Ubuntu", 20, "bold")
    )
    create_Acc.place(
        x = 120, 
        y = 200
    )

    enter_Uniqueuser = ctk.CTkLabel(
        master = reg_text, 
        text = "Enter Unique Username", 
        font = ("Ubuntu", 15)
    )
    enter_Uniqueuser.place(
        x = 108, 
        y = 255
    )

    enter_Newuser = ctk.CTkEntry(
        reg_text, 
        height = 40, 
        width = 250, 
        placeholder_text = "Create your Username"
    )
    enter_Newuser.place(
        x = 95, 
        y = 285
    )

    enter_Uniquepass = ctk.CTkLabel(
        master = reg_text, 
        text = "Enter Password", 
        font = ("Ubuntu", 15)
    )
    enter_Uniquepass.place(
        x = 108, 
        y = 340
    )

    enter_Newpass = ctk.CTkEntry(
        reg_text, 
        height = 40, 
        width = 250, 
        placeholder_text = "Create your Password", 
        show = "*"
    )
    enter_Newpass.place(
        x = 95, 
        y = 370
    )

    def write_NewUser():
        user_input = enter_Newuser.get()
        pass_input = enter_Newpass.get()

        if not user_input:
            messagebox.showerror("Registration Error", "Username cannot be empty. Please enter a username.")

        elif user_Exist(user_input):
            messagebox.showerror("Invalid Username", "Username already taken. Please choose another one.")
            
            enter_Newuser.delete(0, 'end')
            enter_Newpass.delete(0, 'end')

        elif not pass_input:
            messagebox.showerror("Registration Error", "Password cannot be empty. Please enter a password.")

            register_Acc()

        else:
            data_to_append = [[user_input, pass_input]]
            file = open("userinfo.csv", "a", newline="")
            writer = csv.writer(file)

            writer.writerows(data_to_append)

            file.close()
            
            global userData
            userData = pd.read_csv("userinfo.csv")
        
            messagebox.showinfo("Registration Success", "Account created successfully!")

            go_back_login()

    create_Button = ctk.CTkButton(
        reg_text,
        fg_color = ("#F875AA", "#8758FF"),
        hover_color = ("#AEDEFC", "#5CB8E4"),
        height = 35,
        width = 90,
        text = "Create",
        font = ("Ubuntu", 15, "bold"),
        command = write_NewUser,
    )
    create_Button.place(
        x = 170, 
        y = 440)

    have_Acc = ctk.CTkLabel(
        reg_text, 
        text = "Already have Account?", 
        font = ("Helvetica", 12)
    )
    have_Acc.place(
        x = 125, 
        y = 500
    )

    signin_Button = ctk.CTkButton(
        reg_text,
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
        x = 255, 
        y = 495.5
    )

    def mode_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    switch_var = ctk.StringVar(value="on")
    mode_switch = ctk.CTkSwitch(
        master = reg_text,
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

def read_User():
    try:
        userData = pd.read_csv("userinfo.csv")
        userData["Password"] = userData["Password"].astype(str)
        return userData
    
    except FileNotFoundError:
        print("User data file not found.")
        return None

def user_Exist(username):
    global userData
    if userData is not None:
        taken_Usernames = userData["Username"].tolist()
        return username in taken_Usernames
    else:
        return False

def authenticate_User(username, password):
    global userData
    if userData is not None:
        matches = userData.index[(userData.Username == username) & (userData.Password == password)].tolist()
        return matches
    else:
        return False

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

userData = read_User()
print(userData)

def start_button_event():
    main_login_frame.pack_forget()
    main_frame.pack(
        fill = "both", 
        expand = True, 
        anchor = "center"
    )

    # FRAME, LOGOUT, INTRO LABEL ------------------------------------------------------------------------------------------------------------------------------------
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
        relx = 0.495,
        rely = 0.15,
        anchor = tkinter.CENTER
    )

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
        relx = 0.5,
        rely = 0.5,
        anchor = tkinter.CENTER
    )
    # ------------------------------------------------------------------------------------------------------------------------------------   # Eto ung reason bakit tayo nag import ng PIL or pillow sa taas kasi eto ung module na ginagamit sa python if may images na involved
    flappy_banner = ctk.CTkImage(Image.open("Banners\Flappy bird banner.png"), size=(300, 400))

    twenty_forty_banner = ctk.CTkImage(Image.open("Banners\\2048 banner.png"), size = (300, 400))

    hungry_snake_banner = ctk.CTkImage(Image.open("Banners\hungry snake banner.png"), size=(300, 400))

    donkey_banner = ctk.CTkImage(Image.open("Banners\Donkey kong banner.png"), size = (300, 400))

    mario_banner = ctk.CTkImage(Image.open("Banners\Super mario banner.png"), size = (300, 400))

    tic_tac_toe_banner = ctk.CTkImage(Image.open("Banners\Tic tac toe banner.png"), size = (300, 400))

    bomber_banner = ctk.CTkImage(Image.open("Banners\Bomber banner.png"), size = (300, 400))

    pacman_banner = ctk.CTkImage(Image.open("Banners\Pacman banner.png"), size = (300, 400))

    tetris_banner = ctk.CTkImage(Image.open("Banners\Tetris banner.png"), size = (300, 400))
    # GAME FRAMES ------------------------------------------------------------------------------------------------------------------------------------
    game_collection_frame = ctk.CTkScrollableFrame(
        master = main_frame,
        width = 1100,
        height = 500,
        fg_color = "transparent",
        scrollbar_button_color = ("#F875AA", "#8758FF"),
        scrollbar_button_hover_color = ("#AEDEFC", "#5CB8E4"),
    )
    game_collection_frame.place(
        relx = 0.5,
        rely = 0.6,
        anchor = tkinter.CENTER
    )

    game_frame1 = ctk.CTkFrame(
        master = game_collection_frame, 
        height = 400, width = 1000, 
        fg_color = "transparent"
    )
    game_frame1.pack(
        pady=10
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
    
    # GAME EVENTS ------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game2_event():
        os.startfile("GAMES\Donkey Kong\DonkeyKong_KendraTam_PythonProgrammi.exe")

    game2 = ctk.CTkButton(
        master=game_frame1,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        image=donkey_banner,
        command=game2_event,
        text="",
    )
    game2.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game3_event():
        os.startfile("GAMES\Super Mario\dist\Mario.exe")

    game3 = ctk.CTkButton(
        master=game_frame1,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image=mario_banner,
        command=game3_event,
    )
    game3.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game4_event():
        os.startfile("GAMES\Flappy Bird\Flappy.exe")

    game4 = ctk.CTkButton(
        master=game_frame2,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image=flappy_banner,
        command=game4_event,
    )
    game4.pack(side="left", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game5_event():
        os.startfile("GAMES\\2048\\2048.exe")

    game5 = ctk.CTkButton(
        master=game_frame2,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image = twenty_forty_banner,
        command=game5_event,
    )
    game5.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game6_event():
        os.startfile("GAMES\Bomberman\dist\menu.exe")

    game6 = ctk.CTkButton(
        master=game_frame2,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image = bomber_banner,
        command=game6_event,
    )
    game6.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game7_event():
        os.startfile('GAMES\Tic-Tac-Toe-Game-In-Python-master\Tic_Tac_Toe_Game.exe')

    game7 = ctk.CTkButton(
        master=game_frame3,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image=tic_tac_toe_banner,
        command=game7_event,
    )
    game7.pack(side="left", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game8_event():
        os.startfile("GAMES\Tetris Game\dist\Tetris.exe")

    game8 = ctk.CTkButton(
        master=game_frame3,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image = tetris_banner,
        command=game8_event,
    )
    game8.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    def game9_event():
        os.startfile("GAMES\Hungry Snake\Snake.exe")

    game9 = ctk.CTkButton(
        master=game_frame3,
        height=400,
        width=300,
        fg_color=("#F875AA", "#8758FF"),
        hover_color=("#AEDEFC", "#5CB8E4"),
        text="",
        image=hungry_snake_banner,
        command=game9_event,
    )
    game9.pack(side="right", padx=20)

    # ------------------------------------------------------------------------------------------------------------------------------------
    # LIGHT AND DARK MODE SWITCH------------------------------------------------------------------------------------------------------------------------------------
    def mode_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    switch_var = ctk.StringVar(value="on")
    mode_switch = ctk.CTkSwitch(
        master=Landing_page,
        text="Dark Mode",
        button_hover_color=("#F875AA", "#8758FF"),
        progress_color=("#AEDEFC", "#191919"),
        button_color=("#F875AA", "#8758FF"),
        command=mode_event,
        variable=switch_var,
        onvalue="on",
        offvalue="off",
    )
    mode_switch.place(x=25, y=670)
    # main loop------------------------------------------------------------------------------------------------------------------------------------

main_login_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)
main_login_frame.pack(
    fill = "both", 
    expand = True, 
    anchor = "center"
)

main_register_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)

login_Frame = ctk.CTkFrame(
    master = main_login_frame,
    height = 1080,
    width = 500,
    fg_color = ("#FFF6F6", "#191919"),
    border_width = 10,
    border_color = ("#F875AA", "#8758FF"),)
login_Frame.pack(
   side = 'right'
)
register_Frame = ctk.CTkFrame(
        master = main_register_frame,
        height = 1080,
        width = 500,
        fg_color = ("#FFF6F6", "#191919"),
        border_width = 10,
        border_color = ("#F875AA", "#8758FF"),
    )
register_Frame.pack(
    side = 'right'
)


main_frame = ctk.CTkFrame(
    Landing_page, 
    fg_color = "transparent"
)

background_frame = ctk.CTkFrame(
    master = main_login_frame,
    fg_color = "black",
    corner_radius = 50,
    height = 1080,
    width = 700)
background_frame.pack(side = 'left')

my_background = ctk.CTkImage(light_image=Image.open('backgrounds\light.png'),
dark_image=Image.open('backgrounds/dark.png'), size = (1920,1080))

my_background = ctk.CTkLabel(
    master = background_frame, 
    text='', 
    image= my_background)
my_background.pack(
    fill = "both", 
    expand = True, 
    anchor = "center"
)

register_background = ctk.CTkFrame(
    master = main_register_frame,
    fg_color = "black",
    corner_radius = 50,
    height = 1080,
    width = 700
)
register_background.pack(side = 'left')

reg_background = ctk.CTkImage(light_image=Image.open('backgrounds\light.png'),
dark_image=Image.open('backgrounds/dark.png'), size = (1920,1080))

reg_bg = ctk.CTkLabel(
    master = register_background, 
    text='', 
    image= reg_background)
reg_bg.pack(
    fill = "both", 
    expand = True, 
    anchor = "center"
)


login_page()
Landing_page.mainloop()
