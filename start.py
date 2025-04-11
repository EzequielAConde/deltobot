import subprocess
import os
import sys
import platform
from pathlib import Path

def get_venv_python():
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ No se encontró el entorno virtual 'venv'. ¿Lo creaste con `python -m venv venv`?")
        sys.exit(1)

    if platform.system() == "Windows":
        python_executable = venv_path / "Scripts" / "python.exe"
    else:
        python_executable = venv_path / "bin" / "python"

    if not python_executable.exists():
        print(f"❌ No se encontró el ejecutable de Python en el entorno virtual: {python_executable}")
        sys.exit(1)

    return str(python_executable)

def run_process(command, cwd, shell=False):
    return subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=None,
        text=True,
        shell=shell
    )

def main():
    python_path = get_venv_python()
    print(f"✅ Usando Python del entorno virtual: {python_path}\n")

    bot_dir = os.path.join("backend", "bot")
    api_dir = os.path.join("backend", "api")
    frontend_dir = os.path.join("frontend")

    bot_command = [python_path, "bot.py"]
    api_command = [python_path, "-m", "uvicorn", "main:app", "--reload"]
    frontend_command = ["npm", "run", "dev"]  # o ["yarn", "dev"] si usas yarn

    bot_process = run_process(bot_command, bot_dir)
    api_process = run_process(api_command, api_dir)
    frontend_process = run_process(frontend_command, frontend_dir, shell=(platform.system() == "Windows"))

    print("🚀 Iniciando DeltoBot, API y Frontend...\n")

    try:
        while True:
            bot_output = bot_process.stdout.readline()
            api_output = api_process.stdout.readline()
            frontend_output = frontend_process.stdout.readline()

            if bot_output:
                print(f"[BOT] {bot_output.strip()}")
            if api_output:
                print(f"[API] {api_output.strip()}")
            if frontend_output:
                print(f"[FRONTEND] {frontend_output.strip()}")

            if all(p.poll() is not None for p in [bot_process, api_process, frontend_process]):
                break

    except KeyboardInterrupt:
        print("\n⛔ Interrupción detectada. Cerrando...")

        for p in [bot_process, api_process, frontend_process]:
            p.terminate()
            p.wait()

        print("✅ Procesos finalizados.")

if __name__ == "__main__":
    main()
