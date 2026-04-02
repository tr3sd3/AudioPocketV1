import flet as ft

class AudioPocket(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.bg_color = "#192028"
        self.pink_color = "#cd2678"
        self.grey_color = "#7f878a"
        self.dark_grey_color = "#252d3a"
        
        page.bgcolor = self.bg_color


        # Title
        self.title_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color="white"),
                ft.Text(value="AudioPocket", color=self.pink_color, weight=ft.FontWeight.BOLD, size=20),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color="white"),
            ]
        )

        # Upload
        self.upload = ft.Stack(
            height=200,
            width=200,
            alignment = ft.alignment.center,
            controls=[
                ft.Container(
                    height=150,
                    width=150,
                    border_radius=90,bgcolor=self.pink_color,
                    content=ft.Icon(ft.Icons.UPLOAD_FILE, color="white", size=50),
                ),
            ]
        )

        # Convert
        self.convert = ft.ElevatedButton(
            text = "Convertir a audio",
            color="white",
            bgcolor=self.grey_color,
            width=200,
            height=50,
            )


        self.content = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.title_row,
                self.upload,
                # self.voice,
                self.convert,
            ]
        )

def main(page: ft.Page):
    page.title = "AudioPocket"
    app = AudioPocket(page)
    page.add(app)

if __name__ == "__main__":
    ft.app(main) # flet run should work via flet CLI, but to prevent warning we could use ft.app