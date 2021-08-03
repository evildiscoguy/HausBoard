import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
from pygame import mixer


# Function to play sound passed by button
def play_sound(sound):
    mixer.music.load(sound)
    mixer.music.play()


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the ttk theme for the app
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Set the title for the window and set window to be non-resizable
        self.title("HausBoard")
        self.resizable(False, False)

        # Open the pygame mixer ready to play sounds
        mixer.init()

        # Create a frame to "contain" all the seperate frames
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Load all the frames into the "container" frame on top of each other
        self.frames = {}
        for F in (StartPage, JamesWillems, EylseWillems, BruceGreene, LawrenceSonntag):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew")

        # Set the "StartPage" frame as the starting frame
        self.show_frame("StartPage")

    # Command to change the frame
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the "HausBoard" logo
        self.logo_img_load = ImageTk.PhotoImage(Image.open("img/logo.png"))
        lbl_logo = ttk.Label(self, image=self.logo_img_load)
        lbl_logo.pack(pady=10)

        # Set up frames for new page
        frm_links = ttk.Frame(self)
        frm_links.pack(
            side="bottom",
            pady=5)

        frm_james = ttk.Frame(self)
        frm_james.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5)

        frm_eylse = ttk.Frame(self)
        frm_eylse.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5)

        frm_bruce = ttk.Frame(self)
        frm_bruce.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5)

        frm_lawrence = ttk.Frame(self)
        frm_lawrence.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5)

        # Load and show all the photos
        self.links_img_load = ImageTk.PhotoImage(Image.open("img/links_logo.png"))
        lbl_links_logo = ttk.Label(image=self.links_img_load, master=frm_links)
        lbl_links_logo.pack()

        self.james_img_load = ImageTk.PhotoImage(Image.open("img/james_willems.png"))
        lbl_james_img = tk.Label(
            frm_james,
            image=self.james_img_load)
        lbl_james_img.pack()

        self.eylse_img_load = ImageTk.PhotoImage(Image.open("img/elyse_willems.png"))
        lbl_eylse_img = tk.Label(
            frm_eylse,
            image=self.eylse_img_load)
        lbl_eylse_img.pack()

        self.bruce_img_load = ImageTk.PhotoImage(Image.open("img/bruce_greene.png"))
        lbl_bruce_img = tk.Label(
            frm_bruce,
            image=self.bruce_img_load)
        lbl_bruce_img.pack()

        self.lawrence_img_load = ImageTk.PhotoImage(Image.open("img/lawrence_sonntag.png"))
        lbl_lawrence_img = tk.Label(
            frm_lawrence,
            image=self.lawrence_img_load)
        lbl_lawrence_img.pack()

        # Set up and show all the buttons
        btn_funhaus = ttk.Button(
            frm_links,
            text="Funhaus @ YT",
            command=lambda: webbrowser.open("https://www.youtube.com/funhaus", new=2))
        btn_funhaus.pack(
            side="left",
            padx=15,
            pady=5)

        btn_twitter = ttk.Button(
            frm_links,
            text="@evildiscoguy",
            command=lambda: webbrowser.open("https://twitter.com/evildiscoguy", new=2))
        btn_twitter.pack(
            side="left",
            padx=15,
            pady=5)

        btn_james = ttk.Button(
            frm_james,
            text="James Willems",
            command=lambda: controller.show_frame("JamesWillems"))
        btn_james.pack(fill="both")

        btn_eylse = ttk.Button(
            frm_eylse,
            text="Eylse Willems",
            command=lambda: controller.show_frame("EylseWillems"))
        btn_eylse.pack(fill="both")

        btn_bruce = ttk.Button(
            frm_bruce,
            text="Bruce Greene",
            command=lambda: controller.show_frame("BruceGreene"))
        btn_bruce.pack(fill="both")

        btn_lawrence = ttk.Button(
            frm_lawrence,
            text="Lawrence Sonntag",
            command=lambda: controller.show_frame("LawrenceSonntag"))
        btn_lawrence.pack(fill="both")


# Create a class frame to hold the sounds for James Willems
class JamesWillems(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Set logo for "James Willems"
        self.logo_img_load = ImageTk.PhotoImage(Image.open("img/james_logo.png"))
        lbl_logo = ttk.Label(self, image=self.logo_img_load)
        lbl_logo.pack(pady=10)

        # Set up frames for new page
        frm_home = ttk.Frame(self)
        frm_home.pack(side="bottom", pady=10)

        frm_col1 = ttk.Frame(self)
        frm_col1.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        frm_col2 = ttk.Frame(self)
        frm_col2.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        # Set up all the buttons
        btn_home = ttk.Button(
            frm_home,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"))
        btn_home.pack(fill="both")

        # Each button for the sounds passes an ogg file to a method
        btn_play_semen = ttk.Button(
            frm_col1,
            text="If you eat a lot of pineapple",
            command=lambda: play_sound("media/eat_semen.ogg"))
        btn_play_semen.pack(fill="both")

        btn_play_gank = ttk.Button(
            frm_col1,
            text="Smoke dat straight GANK",
            command=lambda: play_sound("media/straight_gank.ogg"))
        btn_play_gank.pack(fill="both")

        btn_play_dollars = ttk.Button(
            frm_col1,
            text="Can I borrow $5?",
            command=lambda: play_sound("media/can_i_borrow_five_dollars.ogg"))
        btn_play_dollars.pack(fill="both")

        btn_play_tricked = ttk.Button(
            frm_col1,
            text="The game tricked us",
            command=lambda: play_sound("media/game_tricked_us.ogg"))
        btn_play_tricked.pack(fill="both")

        btn_play_gay = ttk.Button(
            frm_col2,
            text="You don't have to be gay",
            command=lambda: play_sound("media/dont_have_to_be_gay.ogg"))
        btn_play_gay.pack(fill="both")

        btn_play_gender = ttk.Button(
            frm_col2,
            text="I don't see gender",
            command=lambda: play_sound("media/i_dont_see_gender.ogg"))
        btn_play_gender.pack(fill="both")
        
        btn_play_cumrags = ttk.Button(
            frm_col2,
            text="Cumrags...",
            command=lambda: play_sound("media/cumrags.ogg")
        )

        btn_play_cumrags.pack(fill="both")

        btn_play_tampon = ttk.Button(
            frm_col2,
            text="Tampon Bucket's full",
            command=lambda: play_sound("media/tampon_bucket.ogg")
        )
        btn_play_tampon.pack(fill="both")


# Create a class frame to hold the sounds for Eylse Willems
class EylseWillems(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Set logo for "Eylse Willems"
        self.logo_img_load = ImageTk.PhotoImage(Image.open("img/eylse_logo.png"))
        lbl_logo = ttk.Label(self, image=self.logo_img_load)
        lbl_logo.pack(pady=10)

        # Set up frames for new page
        frm_home = ttk.Frame(self)
        frm_home.pack(side="bottom", pady=10)

        frm_col1 = ttk.Frame(self)
        frm_col1.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        frm_col2 = ttk.Frame(self)
        frm_col2.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        # Each button for the sounds passes an ogg file to a method
        btn_home = ttk.Button(
            frm_home,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"))
        btn_home.pack(fill="both")

        btn_play_jack = ttk.Button(
            frm_col1,
            text="Jack!",
            command=lambda: play_sound("media/jack.ogg"))
        btn_play_jack.pack(fill="both")

        btn_play_blowjobs = ttk.Button(
            frm_col1,
            text="Your father gives better BJs",
            command=lambda: play_sound("media/father_better_blowjobs.ogg"))
        btn_play_blowjobs.pack(fill="both")

        btn_play_eylse = ttk.Button(
            frm_col1,
            text="E for Eylse",
            command=lambda: play_sound("media/e_for_eylse.ogg"))
        btn_play_eylse.pack(fill="both")

        btn_play_clit = ttk.Button(
            frm_col2,
            text="Clit or Miss Situation",
            command=lambda: play_sound("media/clit_or_miss.ogg"))
        btn_play_clit.pack(fill="both")

        btn_play_pussy = ttk.Button(
            frm_col2,
            text="Pussy bonus",
            command=lambda: play_sound("media/pussy_bonus.ogg"))
        btn_play_pussy.pack(fill="both")


# Create a class frame to hold the sounds for Bruce Greene
class BruceGreene(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Set logo for "Bruce Greene"
        self.logo_img_load = ImageTk.PhotoImage(Image.open("img/bruce_logo.png"))
        lbl_logo = ttk.Label(self, image=self.logo_img_load)
        lbl_logo.pack(pady=10)

        # Set up frames for new page
        frm_home = ttk.Frame(self)
        frm_home.pack(side="bottom", pady=10)

        frm_col1 = ttk.Frame(self)
        frm_col1.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        frm_col2 = ttk.Frame(self)
        frm_col2.pack(side="left",
                      fill="both",
                      expand=True,
                      padx=5)

        # Each button for the sounds passes an ogg file to a method
        btn_home = ttk.Button(
            frm_home,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"))
        btn_home.pack(fill="both")

        btn_play_ska = ttk.Button(
            frm_col1,
            text="Ska came before reggae",
            command=lambda: play_sound("media/ska_before_reggae.ogg"))
        btn_play_ska.pack(fill="both")

        btn_play_leia = ttk.Button(
            frm_col1,
            text="Why's Leia so fat?",
            command=lambda: play_sound("media/leia_fat.ogg"))
        btn_play_leia.pack(fill="both")

        btn_play_gooses = ttk.Button(
            frm_col1,
            text="Bruce's Gooses",
            command=lambda: play_sound("media/bruces_gooses.ogg"))
        btn_play_gooses.pack(fill="both")

        btn_play_getit = ttk.Button(
            frm_col2,
            text="We get it and that's that!",
            command=lambda: play_sound("media/we_get_it.ogg"))
        btn_play_getit.pack(fill="both")

        btn_play_notgay = ttk.Button(
            frm_col2,
            text="I'm not gay!",
            command=lambda: play_sound("media/im_not_gay.ogg"))
        btn_play_notgay.pack(fill="both")


# Create a class frame to hold the sounds for Lawrence Sonntag
class LawrenceSonntag(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Set logo for "Bruce Greene"
        self.logo_img_load = ImageTk.PhotoImage(Image.open("img/lawrence_logo.png"))
        lbl_logo = ttk.Label(self, image=self.logo_img_load)
        lbl_logo.pack(pady=10)

        # Set up frames for new page
        frm_home = ttk.Frame(self)
        frm_home.pack(side="bottom", pady=10)

        frm_col1 = ttk.Frame(self)
        frm_col1.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        frm_col2 = ttk.Frame(self)
        frm_col2.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5)

        # Each button for the sounds passes an ogg file to a method
        btn_home = ttk.Button(
            frm_home,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"))
        btn_home.pack(fill="both")

        btn_play_butthole = ttk.Button(
            frm_col1,
            text="Never seen my own butthole",
            command=lambda: play_sound("media/butthole.ogg"))
        btn_play_butthole.pack(fill="both")

        btn_play_stfu = ttk.Button(
            frm_col1,
            text="Shut the fuck up!",
            command=lambda: play_sound("media/stfu.ogg"))
        btn_play_stfu.pack(fill="both")

        btn_play_alcoholic = ttk.Button(
            frm_col1,
            text="Functional alcoholic",
            command=lambda: play_sound("media/functioning_alcoholic.ogg"))
        btn_play_alcoholic.pack(fill="both")

        btn_play_boner = ttk.Button(
            frm_col2,
            text="It gives me a boner",
            command=lambda: play_sound("media/gives_me_a_boner.ogg"))
        btn_play_boner.pack(fill="both")

        btn_play_running = ttk.Button(
            frm_col2,
            text="Imagine running so fast...",
            command=lambda: play_sound("media/running_so_fast.ogg"))
        btn_play_running.pack(fill="both")


# Keep the app running until the user closes it
if __name__ == "__main__":
    app = App()
    app.mainloop()
