import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de inicialización con transición"
    page.bgcolor = "#FA1C28"

    # Pantalla de inicio que sirve para iniciar el proyecto
    img_local = ft.Image(
        src="https://grupoenconcreto.com/wp-content/uploads/2022/12/Taman%CC%83o-fotos-2.png",
        width=150,
        height=150
    )

    inicializando = ft.Container(
        content=ft.Column(
            [
                img_local,
                ft.Text("¡Bienvenido a nuestra aplicación!", size=24, color="white", weight=ft.FontWeight.BOLD),
                ft.TextButton("Continuar", on_click=lambda e: show_login_screen(), style=ft.ButtonStyle(color="white")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#FA1C28", "#CF1420"],
        ),
    )

    # Pantalla de inicio de sesión
    login_screen = ft.Container(
        content=ft.Column(
            [
                img_local,
                ft.Text("¡Bienvenido a Banorte Móvil!", size=20, color="white", weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("¿Eres cliente Banorte?", size=18, color="white"),
                            ft.Text("Ingresa tu número de tarjeta o cuenta para activar Banorte Móvil.", size=12, color="white"),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.TextField(
                                            label="Cuenta o tarjeta",
                                            width=200,
                                            border_color="white",
                                            keyboard_type=ft.KeyboardType.NUMBER,
                                        ),
                                        ft.Icon(ft.icons.CAMERA_ALT, color="gray")
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                border=ft.border.all(1, "gray"),
                                border_radius=ft.border_radius.all(10),
                                padding=10,
                                margin=ft.margin.symmetric(vertical=10)
                            ),
                            ft.Text("10 dígitos cuenta | 16 dígitos tarjeta", size=10, color="gray"),
                            ft.ElevatedButton("Aceptar", width=280, color="white", bgcolor="red", on_click=lambda e: show_activacion_screen()),
                        ],
                    ),
                    padding=20,
                    width=400,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Text("¿Aún no eres cliente?", size=14, color="white"),
                    alignment=ft.alignment.center,
                    padding=10
                ),
                # Agregar un separador decorativo
                ft.Container(
                    width=400,
                    height=2,
                    bgcolor="white",
                    margin=ft.margin.symmetric(vertical=20)
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#FA1C28", "#CF1420"],
        ),
    )

    # Pantalla de activación de usuario
    activacion_screen = ft.Container(
        content=ft.Column(
            [
                img_local,
                ft.Text("¡Bienvenido a Banorte Móvil!", size=20, color="white", weight=ft.FontWeight.BOLD),
                ft.Text("Email/Usuario y contraseña para entrar a Banorte Móvil", size=16, color="white"),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CAMERA_ALT, color="white"),
                                    ft.Icon(ft.icons.MAIL, color="white"),
                                    ft.Icon(ft.icons.MAIL_OUTLINE, color="white"),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Text("Email/Usuario", size=12, color="white"),
                                    ft.Text("Captura tu contraseña", size=12, color="white"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.TextField(
                                label="Email/Usuario",
                                width=280,
                                border_color="gray",
                                keyboard_type=ft.KeyboardType.TEXT,
                                helper_text="Mínimo 5 caracteres, máximo 15"
                            ),
                            ft.TextField(
                                label="Contraseña",
                                width=280,
                                border_color="gray",
                                keyboard_type=ft.KeyboardType.TEXT,
                                helper_text="Mínimo 6 caracteres",
                                password=True,
                            ),
                            ft.ElevatedButton("Olvidé mi Email/Usuario",color="white", bgcolor="red", on_click=lambda e: print("Recuperar cuenta")),
                            ft.ElevatedButton("Aceptar", color="white", bgcolor="red",on_click=lambda e: show_home_screen()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=20,
                    width=400,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#FA1C28", "#CF1420"],
        ),
    )

    home_screen = ft.Container(
        content=ft.Column(
            [
                img_local,
                ft.Text("Hola,", size=28, color="white"),
                ft.Text("¿Qué vamos a hacer?", size=18, color="white"),
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.HELP,
                                    icon_size=30, 
                                    on_click=lambda e: show_chat_screen(),  
                                    tooltip="Ayuda_chat", 
                                    icon_color= "white"
                                ),
                            ],
                        ),
                        
                        ft.Text("Menú", size=24, color="white", weight=ft.FontWeight.BOLD),
                        ft.Container(
                            width=200,
                            height=2,
                            bgcolor="white",
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    # principal menu
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=50),
                                            ft.Text("Mis cuentas", size=14),
                                            ft.Icon(ft.icons.PAYMENTS, size=50),
                                            ft.Text("Pagar o transferir", size=14),
                                            ft.Icon(ft.icons.ATM, size=50),
                                            ft.Text("Retirar dinero", size=14),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.CREDIT_CARD, size=50),
                                            ft.Text("Tarjeta Digital", size=14),
                                            ft.Icon(ft.icons.PHONE_ANDROID, size=50),
                                            ft.Text("Token Celular", size=14),
                                            ft.Icon(ft.icons.APPS, size=50),
                                            ft.Text("Más Apps", size=14),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.HELP, size=50),
                                            ft.Text("Ayuda", size=14),
                                            ft.Icon(ft.icons.SETTINGS, size=50),
                                            ft.Text("Configuraciones", size=14),
                                            ft.Icon(ft.icons.PERSON, size=50),
                                            ft.Text("Perfil", size=14),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=20,
                            width=500,
                            bgcolor="white",
                            border_radius=ft.border_radius.all(10),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#FA1C28", "#CF1420"],
        ),
    )
    chat_screen = ft.Container(
        content=ft.Column(
            [
                
                ft.Row(
                    [
                        ft.Text("KIDS", size=24, color="white", weight=ft.FontWeight.BOLD),
                        ft.TextButton("Regresar", on_click=lambda e: show_home_screen(), style=ft.ButtonStyle(color="white")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                
                ft.Row(
                    [
                        ft.TextField(
                            label="CHAT",
                            width=280,
                            border_color="gray",
                            keyboard_type=ft.KeyboardType.TEXT,
                        ),
                        ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=50, color="white"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                
                ft.Row(
                    [
                        ft.TextField(
                            label="Usuario",
                            width=280,
                            border_color="gray",
                            keyboard_type=ft.KeyboardType.TEXT,
                        ),
                        ft.Icon(ft.icons.ACCOUNT_BOX_SHARP, size=50, color="white"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    
                    
                ),
                
                ft.Row(
                    [
                        ft.TextField(
                            label="Escribe",
                            width=280,
                            border_color="gray",
                            keyboard_type=ft.KeyboardType.TEXT,
                        ),
                        ft.Icon(ft.icons.ACCOUNT_BOX_SHARP, size=50, color="white"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
           
            
            spacing=20
        ),
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#FA1C28", "#CF1420"],
        ),
    )

    # Animación para cambiar las pantallas
    animated_switcher = ft.AnimatedSwitcher(
        inicializando,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=500,
    )

    # Credencial
    def show_login_screen():
        animated_switcher.content = login_screen
        animated_switcher.update()

    # mostrar la pantalla de iniciar sesión
    def show_activacion_screen():
        animated_switcher.content = activacion_screen
        animated_switcher.update()

    # pantalla del menú
    def show_home_screen():
        animated_switcher.content = home_screen
        animated_switcher.update()

    # Esta es la del chat 1
    def show_chat_screen():
        animated_switcher.content = chat_screen
        animated_switcher.update()

    page.add(animated_switcher)

ft.app(target=main)

