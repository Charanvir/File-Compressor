import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

label3 = sg.Text("Name of compression file")
input3 = sg.Input(key="compression_name")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="black")

window = sg.Window("File Compressor",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [label3, input3],
                       [compress_button, output_label]
                   ])
while True:
    event, values = window.read()
    print(event, values)
    compression_file_name = values["compression_name"].replace(" ", "_")
    filepaths = values["files"].split(";")
    folder_path = values["folder"]
    match event:
        case "Compress":
            make_archive(filepaths, folder_path, compression_file_name)
            window["output"].update(value="Files have been compressed")
        case sg.WINDOW_CLOSED:
            break

window.close()
