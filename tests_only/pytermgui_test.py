import pytermgui as ptg

def main():
    window = ptg.Window()

    input_label = ptg.Label("Enter your input:")
    input_field = ptg.InputField()

    button_ok = ptg.Button("OK")
    button_cancel = ptg.Button("Cancel")

    window.add_widget(input_label)
    window.add_widget(input_field)
    window.add_widget(button_ok)
    window.add_widget(button_cancel)

    def on_ok_clicked():
        print(input_field.get_value())

    button_ok.on_click(on_ok_clicked)

    window.run()

if __name__ == "__main__":
    main()
