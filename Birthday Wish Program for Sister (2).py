import os
import tkinter as tk
from PIL import Image, ImageTk
import vlc
import time
from threading import Thread

# --- SETTINGS ---
sister_name = "Divya"
bg_image_path = "harry potter.jpg"
birthday_video_path = "divya (2).mp4"  # <-- your video file

# --- FUNCTIONS ---
def show_birthday_wishes():
    label_status.config(
        text=(
            f"🎂 Happy Birthday, {sister_name}! 🎉\n\n"
            f"✨ Wishing you a magical year ahead filled with joy, "
            f"creativity, and endless love! ✨\n\n"
            f"💫 From all of us at Hogwarts — have a spellbinding day! 🪄"
        ),
        bg="#fff0fa",
        fg="purple",
        font=("Georgia", int(screen_height * 0.022), "bold"),
        wraplength=int(screen_width * 0.6),
        justify="center"
    )
 # --- CONTENT FRAME ---   
def content_frame():
    content_frame.pack_propagate(False)
    content_frame.pack(anchor="center")

def play_video():
    """Play video using VLC"""
    try:
        label_status.config(
            #content_frame.pack(pady=(20), anchor="center")
            text="🎬 Playing your special birthday video... 💖",
            bg="#fff0fa",
            fg="purple"
        )

        def _play():
            player = vlc.MediaPlayer(birthday_video_path)
            player.play()
            time.sleep(2)
            duration = player.get_length() / 1000
            time.sleep(duration)
            player.stop()

        Thread(target=_play, daemon=True).start()
    except Exception as e:
        label_status.config(text=f"❌ Could not play video: {e}", bg="#fff0fa")

def close_app(event=None):
    root.destroy()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🎁 Harry Potter Birthday Surprise 🎁")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Make fullscreen & hide title bar
root.attributes('-fullscreen', True)
root.bind("<Escape>", close_app)  # Press ESC to exit fullscreen

# --- BACKGROUND IMAGE WITH OPACITY ---
try:
    bg_img = Image.open(bg_image_path).convert("RGBA")
    bg_img = bg_img.resize((screen_width, screen_height))
    bg_img.putalpha(150)  # Adjust transparency
    white_bg = Image.new("RGBA", bg_img.size, (255, 255, 255, 255))
    blended = Image.alpha_composite(white_bg, bg_img)

    bg_photo = ImageTk.PhotoImage(blended)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("⚠️ Could not load background image:", e)
    root.config(bg="#cf3a75")

# --- TITLE LABEL ---
label_title = tk.Label(
    #content_frame.pack(pady=(0, 30), anchor="center")
    text=f"💌 A Magical Birthday Surprise for {sister_name}! 💌",
    font=("Garamond", int(screen_height * 0.04), "bold"),
    bg="#ffe6f0",
    fg="purple"
)
label_title.pack(pady=(0, 30))

# --- STATUS LABEL ---
label_status = tk.Label( 
    #content_frame.pack(pady=(15), anchor="center")
    text="Click below to begin your Hogwarts surprise 🎀",
    font=("Georgia", int(screen_height * 0.02)),
    bg="#ffe6f0",
    fg="black",
    wraplength=int(screen_width * 0.6),
    justify="center"
)
label_status.pack(pady=20)

# --- BUTTON STYLE FUNCTION ---
def styled_button(text, command, emoji):
    return tk.Button( text=f"{emoji}  {text}",
        font=("Georgia", int(screen_height * 0.022), "bold"),
        bg="white",
        fg="purple",
        activebackground="#f8e1f4",
        activeforeground="purple",
        relief="ridge",
        bd=3,
        padx=20,
        pady=10,
        command=command
    )

# --- BUTTONS ---
btn_wishes = styled_button("Show Wishes", show_birthday_wishes, "💖")
btn_wishes.pack(pady=15)

btn_video = styled_button("Play Video", play_video, "🎬")
btn_video.pack(pady=15)

# --- FOOTER TEXT ---
footer_label = tk.Label(
    #content_frame.pack(pady=(15), anchor="center")
    text="Press ESC to exit fullscreen ✨",
    font=("Arial", int(screen_height * 0.015)),
    bg="#fff0fa",
    fg="gray"
)
footer_label.place(relx=0.5, rely=0.96, anchor="center")

# --- RUN APP ---
root.mainloop()
