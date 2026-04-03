import flet as ft
import os
from pathlib import Path
from styles import *

class LocalFilePicker(ft.AlertDialog):
    def __init__(self, on_file_selected):
        super().__init__()
        self.on_file_selected = on_file_selected
        
        # Start in user's home directory
        self.current_path = Path.home()
        self.allowed_extensions = ['.txt']

        # Label to show the current file path
        self.path_text = ft.Text(str(self.current_path), weight=ft.FontWeight.BOLD, size=14, color=text_color)
        
        # Scrollable list for directories and files
        self.files_list = ft.ListView(expand=True, spacing=5, height=350, width=500)
        
        self.title = ft.Text("Seleccionar archivo", weight=title_font_weight, size=title_font_size, color=primary_color)
        
        # Dialog main layout
        self.content = ft.Column([
            self.path_text,
            ft.Divider(color=on_surface_color),
            self.files_list
        ], tight=True)
        
        self.actions = [
            ft.TextButton("Cancelar", on_click=self.cancel)
        ]
        
        self.load_directory(update_page=False)

    def load_directory(self, update_page=True):
        self.files_list.controls.clear()
        
        # Navigate UP if not at root path
        if self.current_path.parent != self.current_path:
            self.files_list.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.FOLDER_OPEN, color=primary_color),
                    title=ft.Text("..", color=text_color),
                    on_click=lambda e: self.go_up()
                )
            )
            
        try:
            # Gather files logic
            items = os.listdir(self.current_path)
            items.sort()
            
            dirs = []
            files = []
            
            for item in items:
                if not item.startswith('.'):
                    item_path = self.current_path / item
                    try:
                        if item_path.is_dir():
                            dirs.append(item)
                        elif item_path.is_file() and item_path.suffix.lower() in self.allowed_extensions:
                            files.append(item)
                    except PermissionError:
                        pass
                        
            # Render Directories
            for d in dirs:
                self.files_list.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.FOLDER, color=on_surface_color),
                        title=ft.Text(d, color=text_color),
                        on_click=self.create_nav_handler(self.current_path / d)
                    )
                )
                
            # Render Target Files
            for f in files:
                self.files_list.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.INSERT_DRIVE_FILE, color=success_color),
                        title=ft.Text(f, color=text_color),
                        on_click=self.create_select_handler(self.current_path / f)
                    )
                )
                
        except PermissionError:
            self.files_list.controls.append(ft.Text("Sin permisos para leer este directorio.", color=error_color))
        except Exception as ex:
            self.files_list.controls.append(ft.Text(f"Error: {ex}", color=error_color))
            
        self.path_text.value = str(self.current_path)
        
        if update_page:
            try:
                self.update()
            except:
                pass

    # Scope protection for event listeners in loop
    def create_nav_handler(self, path):
        return lambda e, p=path: self.navigate_to(p)

    def create_select_handler(self, path):
        return lambda e, p=path: self.select_file(p)

    def go_up(self):
        self.current_path = self.current_path.parent
        self.load_directory()

    def navigate_to(self, new_path):
        self.current_path = new_path
        self.load_directory()

    def select_file(self, file_path):
        self.open = False
        try:
            self.update()
        except:
            pass
        
        # Fire callback to return to Main
        self.on_file_selected(str(file_path))

    def cancel(self, e):
        self.open = False
        try:
            self.update()
        except:
            pass
