from zipfile import ZipFile
from tkinter import *


def unzip_file(event):
    try:
        zipped_name = input_zip_file.get()
        folder_name = input_zip_folder.get()
        zipped_obj = ZipFile(zipped_name)
        zipped_obj.extractall(folder_name)
    except:
        output_label['text'] = 'Whoops, wrong file name? Have u added .zip? :('
    else:
        output_label['text'] = f'Unpacked into: {folder_name} :)'

root = Tk()

label1 = Label(width=40, text='file name to unpack (for example: sprites.zip):')
input_zip_file = Entry(width=40)
label2 = Label(width=40, text='Unpack folder name (for example: New Folder1):')
input_zip_folder = Entry(width=40)
input_button = Button(text="Unpack!")
output_label = Label(width=40)

input_button.bind('<Button-1>', unzip_file)

label1.pack()
input_zip_file.pack()
label2.pack()
input_zip_folder.pack()
input_button.pack()
output_label.pack()

root.mainloop()