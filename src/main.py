import flet as ft
from core import TTS
from styles import *


class AudioPocket(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self._page = page

        # Motor TTS – toda la lógica de conversión vive en core.py
        self.tts = TTS(voice="es-SV-RodrigoNeural")
        self.selected_file_path = None

        page.bgcolor = background_color

        # Custom File Browser (Reemplaza al ft.FilePicker para evitar timeouts)
        from file_browser import LocalFilePicker
        self.file_picker = LocalFilePicker(self.handle_file_picked)
        self._page.overlay.append(self.file_picker)

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
            ],
        )

        # Upload (círculo clickeable → llama on_upload_click)
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
                    content=ft.Icon(
                        ft.Icons.UPLOAD_FILE, color=text_color, size=upload_icon_size
                    ),
                    on_click=self.on_upload_click,
                    ink=True,
                ),
            ],
        )

        # Label del archivo seleccionado
        self.file_label = ft.Text(
            value="Ningún archivo seleccionado",
            color=on_surface_color,
            size=body_font_size,
        )

        # Voice (campo con valor por defecto)
        self.voice_field = ft.TextField(
            label="Voz de narración",
            value="es-SV-RodrigoNeural",
            hint_text="es-SV-RodrigoNeural",
            prefix_icon=ft.Icons.VOICEMAIL,
            width=voice_field_width,
            height=voice_field_height,
            suffix=ft.IconButton(
                icon=ft.Icons.INFO,
                tooltip="Es posible cambiar la voz. Versiones disponibles en: https://tts.travisvn.com/",
            ),
            **INPUT_STYLE,
        )

        self.voice = ft.Row(
            controls=[self.voice_field], alignment=ft.MainAxisAlignment.CENTER
        )

        # Convert (botón que lanza el proceso TTS)
        self.convert = ft.Button(
            content=ft.Text("Convertir a audio", size=button_font_size),
            color=text_color,
            bgcolor=grey_color,
            width=convert_button_width,
            height=convert_button_height,
            on_click=self.on_convert_click,
        )

        # Label de estado de la conversión
        self.status_label = ft.Text(
            value="",
            size=body_font_size,
        )

        # Main content
        self.content = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.title_row,
                self.upload,
                self.file_label,
                self.voice,
                self.convert,
                self.status_label,
            ],
        )

    # ── Lifecycle ──────────────────────────────────────────

    def did_mount(self):
        super().did_mount()
        # Forzar una actualización de página luego del montado inicial 
        # para que el engine Flutter asimile bien el Flet FilePicker
        self._page.update()


    # ── Callbacks ──────────────────────────────────────────

    async def on_upload_click(self, e):
        """Abre el Flet Custom File Picker."""
        # Reset current path to HOME when opening
        from pathlib import Path
        self.file_picker.current_path = Path.home()
        self.file_picker.load_directory(update_page=False)
        
        self._page.dialog = self.file_picker
        self.file_picker.open = True
        self._page.update()

    def handle_file_picked(self, file_path: str):
        """Callback que responde a la selección o cancelación de un archivo"""
        import os
        if file_path:
            self.selected_file_path = file_path
            nombre = os.path.basename(file_path)
            self.file_label.value = f"📄 {nombre}"
            self.file_label.color = text_color
        else:
            self.selected_file_path = None
            self.file_label.value = "Ningún archivo seleccionado"
            self.file_label.color = on_surface_color

        self.status_label.value = ""
        self._page.update()

    async def on_convert_click(self, e):
        """Recoge datos de la UI y los pasa a core.TTS para procesar."""
        if not self.selected_file_path:
            self.status_label.value = "⚠ Seleccioná un archivo primero"
            self.status_label.color = warning_color
            self._page.update()
            return

        # Leer la voz
        voice_value = self.voice_field.value.strip() if self.voice_field.value else ""
        if voice_value:
            self.tts.voice = voice_value

        # Feedback
        self.status_label.value = "⏳ Generando audio..."
        self.status_label.color = on_surface_color
        self.convert.disabled = True
        self._page.update()

        try:
            # Procesar el archivo en el core
            output_path = await self.tts.generate_audio_from_file(
                self.selected_file_path
            )
            self.status_label.value = f"✅ Audio generado: {output_path}"
            self.status_label.color = success_color
        except (FileNotFoundError, ValueError) as ex:
            self.status_label.value = f"❌ {ex}"
            self.status_label.color = error_color
        except Exception as ex:
            self.status_label.value = f"❌ Error inesperado: {ex}"
            self.status_label.color = error_color
        finally:
            self.convert.disabled = False
            self._page.update()


def main(page: ft.Page):
    page.title = "AudioPocket"
    
    app = AudioPocket(page)
    page.add(app)


if __name__ == "__main__":
    ft.app(target=main)