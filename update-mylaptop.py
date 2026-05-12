#!/usr/bin/env python3

import sys
import platform
import subprocess
from datetime import datetime

# ── Configuración ──────────────────────────────────────────────
PATHS = {
    "Linux":   "/home/dennishnf/Desktop/dennishnf.github.io",
    "Windows": r"C:\Users\Dennis\Desktop\dennishnf.github.io",
}
# ───────────────────────────────────────────────────────────────

def run(cmd, description=""):
    """Ejecuta un comando y detiene el script si falla."""
    print(f"\n▶ {description or cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n✗ Error al ejecutar: {cmd}")
        print("  El proceso se detuvo para evitar subir contenido incorrecto.")
        sys.exit(result.returncode)
    print(f"  ✓ OK")

def main():
    os_name = platform.system()          # 'Linux' o 'Windows'
    site_path = PATHS.get(os_name)

    if not site_path:
        print(f"✗ Sistema operativo no soportado: {os_name}")
        sys.exit(1)

    print(f"═══════════════════════════════════════")
    print(f"  OS detectado : {os_name}")
    print(f"  Ruta del site: {site_path}")
    print(f"═══════════════════════════════════════")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    run("git pull",                                        "Actualizando repo local")
    run(f'python3 md2html.py "{site_path}"',               "Generando HTML desde Markdown")
    run("git add -A",                                      "Añadiendo cambios al stage")
    run(f'git commit -m "update {timestamp}"',             "Haciendo commit")
    run("git push origin main",                            "Subiendo a GitHub")

    print(f"\n✓ Sitio actualizado correctamente ({timestamp})\n")

if __name__ == "__main__":
    main()
