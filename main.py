import subprocess
import os
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

is_retina = True

uploaded_image_path = None

def wait_for_button(image_path, scale_factor=2, timeout=60, confidence=.99):
    start_time = time.time()
    button = None

    while time.time() - start_time < timeout:
        try:
            button = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if button:
                x, y = button.left / scale_factor, button.top / scale_factor
                print(f"Coordinates divided by {scale_factor}: ({x}, {y})")
                
                pyautogui.moveTo(x, y)
                pyautogui.click(button='left')
                return True
        except pyautogui.ImageNotFoundException:
            pass
        
        print(f"Waiting for {image_path} to appear...")
        time.sleep(.1)
    
    print(f"Button not found within {timeout} seconds: {image_path}")
    return False

def open_tribot():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_path = os.path.join(desktop_path, "Tribot")

    subprocess.call(["open", shortcut_path])
    print("Tribot opened")
    if wait_for_button('image/launch.png', scale_factor=1 if is_retina else 2):
        print("Launch button clicked")

def new_client():
    if wait_for_button('image/new_client.png', scale_factor=1 if is_retina else 2):
        print("New Client button clicked")

def script():
    if wait_for_button('image/script.png', scale_factor=1 if is_retina else 2):
        print("Script button clicked")
        
def auto_relog():
    if wait_for_button('image/auto_relog.png', scale_factor=1 if is_retina else 2):
        print("Auto Relog button clicked")
        
def quests():
    if wait_for_button('image/quests.png', scale_factor=1 if is_retina else 2):
        print("Quests button clicked")
        
def aio():
    if wait_for_button('image/aio.png', scale_factor=1 if is_retina else 2):
        print("AIO button clicked")

def aio_start():
    if wait_for_button('image/aio_start.png', scale_factor=1 if is_retina else 2):
        print("AIO Start button clicked")
        
def profile():
    if wait_for_button('image/profile.png', scale_factor=1 if is_retina else 2):
        print("Profile button clicked")
        
def last():
    if wait_for_button('image/last.png', scale_factor=1 if is_retina else 2):
        print("Last button clicked")
        
def load():
    if wait_for_button('image/load.png', scale_factor=1 if is_retina else 2):
        print("Load button clicked")
        
def start_tab():
    if wait_for_button('image/start_tab.png', scale_factor=1 if is_retina else 2):
        print("Start tab clicked")
        
def profile_start():
    if wait_for_button('image/profile_start.png', scale_factor=1 if is_retina else 2):
        print("Profile Start button clicked")

def account_image():    
    global uploaded_image_path
    if uploaded_image_path:
        if wait_for_button(uploaded_image_path, scale_factor=1 if is_retina else 2):
            print("Account Image button clicked")
    else:
        print("No image uploaded.")

def start_sequence():
    open_tribot()
    new_client()
    script()
    auto_relog()
    account_image()
    quests()
    aio()
    aio_start()
    profile()
    last()
    load()
    start_tab()
    profile_start()
    
def toggle_retina():
    global is_retina
    is_retina = not is_retina
    print(f"Retina display toggle is now {'ON' if is_retina else 'OFF'}")

def upload_image():
    global uploaded_image_path
    uploaded_image_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )
    if uploaded_image_path:
        print(f"Image uploaded: {uploaded_image_path}")
    else:
        print("No image uploaded.")

def create_gui():
    root = tk.Tk()
    root.title("Tribot Automation")

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    start_button = ttk.Button(frame, text="Start", command=start_sequence)
    start_button.grid(row=0, column=0, padx=5, pady=5)

    retina_toggle = ttk.Checkbutton(frame, text="Retina Display", command=toggle_retina)
    retina_toggle.grid(row=1, column=0, padx=5, pady=5)

    upload_button = ttk.Button(frame, text="Upload Image", command=upload_image)
    upload_button.grid(row=2, column=0, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
