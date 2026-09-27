import os
import shutil

# Ficheiros que queremos guardar na pasta principal (o coração do Accio)
FICHEIROS_MAGICOS = ["accio.py", "comandos.py", "robot.py", "mapa.py"]

def faxina_de_natal():
    print("🧹 [ACCIO LIMPEZA] A iniciar a remoção de excessos...")
    
    # Cria uma pasta para guardar as coisas antigas (caso queiras consultar mais tarde)
    pasta_backup = "backup_antigo"
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)
        print(f"📁 Pasta de segurança '{pasta_backup}' criada.")

    # Listar todos os ficheiros da pasta atual
    ficheiros = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    for ficheiro in ficheiros:
        # Se for o próprio script de limpeza ou um dos ficheiros principais, não mexe!
        if ficheiro == "limpar_projeto.py" or ficheiro in FICHEIROS_MAGICOS:
            continue
            
        # Ignora ficheiros ocultos do sistema ou do git
        if ficheiro.startswith('.'):
            continue
            
        # Move o ficheiro para o backup
        try:
            shutil.move(ficheiro, os.path.join(pasta_backup, ficheiro))
            print(f"📦 Movido para o backup: {ficheiro}")
        except Exception as e:
            print(f"⚠️ Não consegui mover {ficheiro}: {e}")

    print("\n✨ Limpeza concluída! A tua pasta principal agora só tem robótica a sério.")

if __name__ == "__main__":
    faxina_de_natal()