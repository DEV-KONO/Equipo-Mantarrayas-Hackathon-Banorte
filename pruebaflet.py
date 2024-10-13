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

    # Segunda pantalla de inicio, donde el usuario inicia sesión
    login_screen = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="https://grupoenconcreto.com/wp-content/uploads/2022/12/Taman%CC%83o-fotos-2.png", width=150),
                ft.Text("¡Bienvenido a Banorte Móvil!", size=20, color="white", weight=200),
                
                ft.Container(
                    content=ft.Column(
                        [
                            # Obtener la información del cliente
                            ft.Text("¿Eres cliente Banorte?", size=18),
                            ft.Text("Ingresa tu número de tarjeta o cuenta para activar Banorte Móvil.", size=12),
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
                            ft.ElevatedButton("Aceptar", width=280, color="white", bgcolor="gray", on_click=lambda e: show_activacion_screen()),
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
                ft.Text("Captura tu usuario para entrar a Banorte Móvil", size=16, color="white"),
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
                                    ft.Text("Captura tu usuario", size=12, color="white"),
                                    ft.Text("SMS de confirmación", size=12, color="white"),
                                    ft.Text("SMS de verificación", size=12, color="white"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.TextField(
                                label="Captura tu usuario",
                                width=280,
                                border_color="gray",
                                keyboard_type=ft.KeyboardType.TEXT,
                                helper_text="Mínimo 5 caracteres, máximo 15"
                            ),
                            ft.TextButton("Olvidé mi usuario", on_click=lambda e: print("Recuperar usuario")),
                            ft.TextButton("Aceptar", on_click=lambda e: show_home_screen() ),
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
                # Imagen superior con el logo y patrocinio
                ft.Image(src="https://grupoenconcreto.com/wp-content/uploads/2022/12/Taman%CC%83o-fotos-2.png", width=400),
                ft.Text("Hola,", size=28, color="white"),
                ft.Text("¿Qué vamos a hacer?", size=18, color="white"),
                
                ft.Container(
                    content=ft.Column(
                        [
                            # Menú principal
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

    # Función para mostrar la pantalla de inicio de sesión
    def show_login_screen():
        animated_switcher.content = login_screen
        animated_switcher.update()

    # Función para mostrar la pantalla de activación
    def show_activacion_screen():
        animated_switcher.content = activacion_screen
        animated_switcher.update()

    # Función para mostrar la pantalla de inicio después del login
    def show_home_screen():
        animated_switcher.content = home_screen
        animated_switcher.update()

    # Agrega el switcher a la página
    page.add(animated_switcher)

ft.app(target=main)
