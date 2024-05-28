import flet as ft
import datetime


def main(page: ft.Page):
    def textbox_changed(e):
        print("change")
        page.update()
        return typing(start_timer())

    page.add(
        ft.TextField(label="Type here!", multiline=True, min_lines=5, on_change=textbox_changed)

    )

    def start_timer():
        last_key = int(datetime.datetime.now().strftime("%M%S"))
        print("last key")
        return last_key

    def end_typing():
        print("over")

    def typing(last_key):
        run = True
        while run:
            current_time = datetime.datetime.now().strftime("%M%S")
            if last_key + 5 < int(current_time):
                print("fin")
                end_typing()
                run = False



ft.app(main)
