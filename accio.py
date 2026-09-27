# accio.py
import time
from comandos import executar_comando

def inicializar_robot():
    print("=" * 45)
    print("🪄 [FEITIÇO DE ATIVAÇÃO] A despertar o Accio...")
    print("=" * 45)
    time.sleep(1)
    
    # Simulação do Diagnóstico de Hardware (Estilo Mark Rober)
    print("📡 A testar ligação à placa de microfones... [OK]")
    time.sleep(0.5)
    print("🚗 A verificar os encoders dos motores...     [OK]")
    time.sleep(0.5)
    print("💨 A testar a pressão da bomba de vácuo...    [OK]")
    time.sleep(0.5)
    print("🗺️ A carregar o mapa mental da casa...        [OK]")
    time.sleep(1)
    
    print("\n✨ 'Juro solenemente que não vou fazer nada de bom!' ✨")
    print("🤖 Sistema operacional. Aguardando o teu feitiço...")
    print("=" * 45)

# Arranca o diagnóstico antes de entrar no ciclo de comandos
inicializar_robot()

while True:
    comando = input("\nTu > ").strip()

    if comando == "":
        continue

    if comando.lower() in ["sair", "adeus", "exit"]:
        print("\n⚡ 'Malfeito feito!' O Accio voltou a adormecer. Até breve!")
        break

    executar_comando(comando)