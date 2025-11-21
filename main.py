import sys
from pathlib import Path

# Adiciona o diretório raiz ao path do Python
sys.path.insert(0, str(Path(__file__).parent))

from controlador.controlador_principal import ControladorPrincipal

if __name__ == "__main__":
    sistema = ControladorPrincipal()
    sistema.inicia_sistema()
