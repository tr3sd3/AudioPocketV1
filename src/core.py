import asyncio 
import edge_tts
from pathlib import Path


# /// 
# ///
# ///

class TTS:
    """
    Clase encargada de la lógica de procesamiento de archivos y TTS.
    Centraliza la configuración de voz y rutas.
    """
    def __init__(self, voice: str = "es-SV-RodrigoNeural"):
        self.voice = voice
        self.rate = "+5%"
        self.pitch = "-5Hz"

    def get_output_path(self, input_path: str) -> Path:
        """
        Toma un path de archivo .txt y devuelve un Path objeto .mp3
        en la misma carpeta con el mismo nombre.
        """
        path_obj = Path(input_path)
        # .with_suffix('.mp3') cambia la extensión automáticamente
        return path_obj.with_suffix('.mp3')

    async def generate_audio_from_file(self, file_path: str):
        """
        Lee el contenido de un txt y genera el audio en la misma ubicación.
        """
        input_path = Path(file_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

        # Obtener el path de salida (.mp3)
        output_path = self.get_output_path(file_path)

        # Leer el texto del archivo
        with open(input_path, "r", encoding="utf-8") as f:
            texto = f.read()

        if not texto.strip():
            raise ValueError("El archivo de texto está vacío.")

        # Proceso de TTS
        communicate = edge_tts.Communicate(
            text=texto, 
            voice=self.voice, 
            rate=self.rate, 
            pitch=self.pitch
        )
        
        await communicate.save(str(output_path))
        return str(output_path)

# Ejemplo de us o (esto iría en tu main o en un bloque de prueba)
#if __name__ == "__main__":
    # Supongamos que recibes esto desde un FilePicker de Flet
    #test_path = "C:/usuarios/proyecto/mi_guion.txt"
    
    #generator = TTS()
    
    # Para ejecutarlo fuera de Flet (prueba rápida)
    # asyncio.run(generator.generate_audio_from_file(test_path))