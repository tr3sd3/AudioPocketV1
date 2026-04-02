import flet as ft


def main(page: ft.Page):
    page.title = "AudioPocket"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = ft.padding.all(10)
    page.window.width = 1000
    page.window.height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER



    page.add(
        
        ft.Text(

            spans=[
                ft.TextSpan(
                    text="AudioPocket",
                    style=ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900,
                    ),
                ),
            ],
        ),
        ft.Text("Carga tu documento de texto o Markdown y transforma tu contenido en audio en segundos.", text_align=ft.TextAlign.CENTER),      
        
        
        
        ft.Container(
            width=400,
            height=400,
            bgcolor=ft.Colors.GREY_900,
            border_radius=ft.BorderRadius.all(15),
            padding= 10,
            content=ft.Column(
                controls=[
                    
                    ft.Button(
                        content="traer archivo",
                        on_click=lambda _: file_picker.pick_files(allow_multiple=True),
                        height=200,
                        width=200,
                    ),
                    
                    ft.TextField(label="Voz", hint_text="es-SV-RodrigoNeural"),


                    ft.Button(
                        content="convertir a audio",    
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

if __name__ == "__main__":
    ft.run(main)