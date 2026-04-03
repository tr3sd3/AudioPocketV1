import flet as ft
from styles import (
    primary_color,
    background_color,
    text_color,
    on_surface_color,
    grey_color,
    dark_grey_color,
    surface_color,
    title_font_size,
    title_font_weight,
    button_font_size,
    upload_stack_height,
    upload_stack_width,
    upload_circle_size,
    upload_circle_border_radius,
    upload_icon_size,
    convert_button_width,
    convert_button_height,
    voice_field_width,
    voice_field_height,
    voice_field_border_radius,
    INPUT_STYLE,
)

class AudioPocket(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)

        page.bgcolor = background_color

        # Title
        self.title_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=on_surface_color),
                ft.Text(
                    value="AudioPocket",
                    color=primary_color,
                    weight=title_font_weight,
                    size=title_font_size,
                ),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=on_surface_color),
            ]
        )

        # Upload
        self.upload = ft.Stack(
            height=upload_stack_height,
            width=upload_stack_width,
            alignment=ft.Alignment.CENTER,
            controls=[
                ft.Container(
                    height=upload_circle_size,
                    width=upload_circle_size,
                    border_radius=upload_circle_border_radius,
                    bgcolor=primary_color,
                    content=ft.Icon(ft.Icons.UPLOAD_FILE, color=text_color, size=upload_icon_size),
                ),
            ]
        )

        # Convert
        self.convert = ft.Button(
            content=ft.Text("Convertir a audio", size=button_font_size),
            color=text_color,
            bgcolor=grey_color,
            width=convert_button_width,
            height=convert_button_height,
        )

        # Voice
        self.voice = ft.Row(
            controls=[
                ft.TextField(
                    label="Voz de narración",
                    hint_text="es-SV-RodrigoNeural",
                    prefix_icon=ft.Icons.VOICEMAIL,
                    width=voice_field_width,
                    height=voice_field_height,
                    suffix=ft.IconButton(
                        icon=ft.Icons.INFO,
                        tooltip="Es posible cambiar la voz. Versiones disponibles en: https://tts.travisvn.com/"
                    ),
                    **INPUT_STYLE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Main content
        self.content = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.title_row,
                self.upload,
                self.convert,
                self.voice,
            ]
        )

def main(page: ft.Page):
    page.title = "AudioPocket"
    app = AudioPocket(page)
    page.add(app)

if __name__ == "__main__":
    ft.app(main)