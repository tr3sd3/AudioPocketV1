import flet as ft

# ============================================================
# PALETA DE COLORES
# Tema oscuro con acentos en violeta azulado/rojizo
# ============================================================

# Color principal de acento – violeta con tinte azulado
primary_color = "#7B2FBE"

# Color secundario – violeta más rojizo para complementar
secondary_color = "#A33DB5"

# Fondo general de la aplicación – negro azulado oscuro
background_color = "#0F1117"

# Color de texto principal – blanco puro
text_color = "#FFFFFF"

# Color de error – rojo suave
error_color = "#CF6679"

# Color de éxito – verde desaturado
success_color = "#4CAF82"

# Color de advertencia – ámbar cálido
warning_color = "#FFB74D"

# Superficie – fondo de tarjetas y contenedores – gris muy oscuro
surface_color = "#1A1D27"

# Texto sobre el color primario
on_primary_color = "#FFFFFF"

# Texto sobre superficies – gris claro para contraste suave
on_surface_color = "#B0B3BE"


# ============================================================
# COLORES AUXILIARES
# Grises de apoyo reutilizados en bordes, íconos, etc.
# ============================================================

# Gris medio para bordes, íconos secundarios
grey_color = "#4A4E5A"

# Gris oscuro para separadores y fondos elevados
dark_grey_color = "#252830"


# ============================================================
# TIPOGRAFÍA
# ============================================================

# Tamaño del título de la app
title_font_size = 22

# Peso del título de la app
title_font_weight = ft.FontWeight.BOLD

# Tamaño de texto de botones
button_font_size = 15

# Tamaño de texto para labels / inputs
input_font_size = 14

# Tamaño de texto general / cuerpo
body_font_size = 14


# ============================================================
# DIMENSIONES – UPLOAD CIRCLE
# ============================================================

# Tamaño del Stack contenedor del botón de upload
upload_stack_height = 200
upload_stack_width = 200

# Tamaño del círculo de upload
upload_circle_size = 150

# Radio de borde para hacerlo circular
upload_circle_border_radius = 90

# Tamaño del ícono dentro del círculo
upload_icon_size = 50


# ============================================================
# DIMENSIONES – BOTÓN CONVERTIR
# ============================================================

convert_button_width = 200
convert_button_height = 50


# ============================================================
# DIMENSIONES – CAMPO DE VOZ
# ============================================================

voice_field_width = 300
voice_field_height = 50
voice_field_border_radius = 25


# ============================================================
# ESTILOS COMPUESTOS
# Diccionarios listos para expandir con ** en los componentes
# ============================================================

# Estilo para tarjetas / contenedores con superficie elevada
CARD_STYLE = {
    "padding": 20,
    "border_radius": 15,
    "border": ft.Border.all(1, dark_grey_color),
    "bgcolor": surface_color,
}

# Estilo de texto para encabezados
TEXT_HEADER = {
    "size": title_font_size,
    "weight": title_font_weight,
    "color": primary_color,
}

# Estilo base para campos de entrada
INPUT_STYLE = {
    "color": text_color,
    "border_color": grey_color,
    "selection_color": primary_color,
    "border_radius": voice_field_border_radius,
}