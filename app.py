from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter

img_resized = None

# --- Setup window ---
app = customtkinter.CTk()
app.geometry("1000x700")
app.title("CTk example")

# --- Functions ---

def resize(img, height):
    fixed_height = height
    orig_width, orig_height = img.size
    new_width = int((fixed_height / orig_height) * orig_width)
    return img.resize((new_width, fixed_height))

def add_image():
    global img_file, my_image, my_label, img_resized
    img_file = filedialog.askopenfilename()
    if not img_file:
        return  # user cancelled
    img = Image.open(img_file)
    img_resized = resize(img,550)
    width, height = img_resized.size
    my_image = customtkinter.CTkImage(light_image=img_resized, dark_image=img_resized, size=(width, height))
    # Create label if it doesn't exist
    try:
        my_label.configure(image=my_image)
    except NameError:
        my_label = customtkinter.CTkLabel(app, text="", image=my_image)
        my_label.pack(pady=10)

def add_logo():
    global img_resized, my_image, my_label
    if img_resized is None:
        messagebox.showinfo(title="Information", message="Please add an image first!")
        return
    logo_file = filedialog.askopenfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")])
    if not logo_file:
        return
    logo = Image.open(logo_file)
    logo = resize(logo,50)
    # Paste logo at (15, 15)
    img_resized.paste(logo, (15, 15), logo)
    width, height = img_resized.size
    my_image = customtkinter.CTkImage(light_image=img_resized, dark_image=img_resized, size=(width, height))
    try:
        my_label.configure(image=my_image)
    except NameError:
        my_label = customtkinter.CTkLabel(app, text="", image=my_image)
        my_label.pack(pady=10)

def save():
    global img_resized
    if img_resized is None:
        messagebox.showinfo(title="Information", message="Please add an image first!")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
    if not save_path:
        return
    if save_path.lower().endswith(('.jpg', '.jpeg')):
        rgb_image = img_resized.convert('RGB')
        rgb_image.save(save_path)
        messagebox.showinfo(title="Information", message="Image saved!")
    else:
        img_resized.save(save_path)
        messagebox.showinfo(title="Information", message="Image saved!")


# --- GUI ---
btn_frame = customtkinter.CTkFrame(app)
btn_frame.pack(pady=10)

customtkinter.CTkButton(btn_frame, text="Add Image", command=add_image).pack(side="left", padx=5)
customtkinter.CTkButton(btn_frame, text="Add Logo", command=add_logo).pack(side="left", padx=5)
customtkinter.CTkButton(btn_frame, text="Save",command=save).pack(side="left", padx=5)

# --- Run the app ---
app.mainloop()