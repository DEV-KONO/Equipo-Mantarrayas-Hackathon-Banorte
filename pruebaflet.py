import json
from arrow import get
import flet as ft
from httpx import request
import requests
import os
import dotenv

dotenv.load_dotenv()

URL = os.getenv("URL")

class Message:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"

    def join_chat_click(e):
        login_req = requests.post(f"{URL}login", json={"mail": join_user_name.value, "password" : contraseña.value})
        try:
            if not login_req.json()["error"]:
                r = requests.get(f"{URL}all_hist", json={"mail": join_user_name.value }) #todo llamar toda la historia del correo especificado
                print((r.json()))

                if not join_user_name.value:
                    join_user_name.error_text = "Name cannot be blank!"
                    join_user_name.update()
                else:
                    page.session.set("user_name", join_user_name.value)
                    page.dialog.open = False
                    new_message.prefix = ft.Text(f"{join_user_name.value}: ")
                    page.pubsub.send_all(
                        Message(
                            user_name=join_user_name.value,
                            text=f"{join_user_name.value} has joined the chat.",
                            message_type="login_message",
                        )
                    )
                    for req in r.json():
                        rj = json.loads(req.replace("\'", "\""))

                        if len(rj["message"]) > 150:
                            for i in range(0,len(rj["message"])//150):
                                rj["message"] = rj["message"][:150*(i+1)] + "\n" + rj["message"][150*(i+1):]

                        if rj["role"] == "user":
                            page.pubsub.send_all(
                                Message(
                                    user_name=join_user_name.value,
                                    text=rj["message"],
                                    message_type="chat_message"
                                )
                            )
                        else:
                            page.pubsub.send_all(
                                Message(
                                    user_name="Norty",
                                    text=rj["message"],
                                    message_type="chat_message"
                                )
                            )

                    page.update()
        except:
            join_user_name.error_text = "Usuario o contraseña incorrectos"
            join_user_name.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.get("user_name"),
                    new_message.value,
                    message_type="chat_message",
                )
            )

            r = requests.get(f"{URL}gemini_call", json={"mail":page.session.get("user_name"), "message":new_message.value})
            print(r.json())
            
            rj = r.json()

            if len(rj["message"]) > 150:
                rj["message"] = rj["message"][:150] + "\n" + rj["message"][150:]

            page.pubsub.send_all(
                Message(
                    user_name="Norty",
                    text=rj["message"],
                    message_type="chat_message"
                )
            )

            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # A dialog asking for a user display name
    join_user_name = ft.TextField(
        label="Correo",
        autofocus=True,
        on_submit=join_chat_click,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        width=280,
        border_color="gray",
        keyboard_type=ft.KeyboardType.TEXT,
        helper_text="Mínimo 6 caracteres",
        password=True,
    )

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Container(
                    content=ft.Column(
                        [
                            join_user_name,
                            contraseña,
                            ft.ElevatedButton("Aceptar", color="white", bgcolor="red",on_click=join_chat_click),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
        ),
        # content=ft.Column([join_user_name], width=300, height=70, tight=True),
    )

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )


ft.app(target=main)