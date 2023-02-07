import PySimpleGUI as sg

sg.change_look_and_feel("DarkAmber")

text_entry = sg.Multiline(key="text_written", size= (68, 21), font=["Times New Roman", 20])
save_button = sg.Button("Save", key="save")
selector_button = sg.FilesBrowse("Choose File Name", key="select")

layout = [[text_entry], [save_button, selector_button]]

window = sg.Window("WordChad", layout=layout, size=(1000, 700))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "save":
        fileWrite = values["text_written"]
        filepath = values["select"]
        if fileWrite == "":
            sg.popup("Your content is empty!")
            continue
        if filepath == "":
            sg.popup("Please pick a file to save your content in!")
            continue

        with open(filepath, "w") as file:
            file.writelines(fileWrite)
    if event == sg.WIN_CLOSED:
        break

window.close()