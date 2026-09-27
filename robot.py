# robot.py
import time
# Importamos as funções de segurança e localização do mapa mental
from mapa import obter_posicao_atual, atualizar_posicao

# Coordenadas dos teus objetos na grelha da casa (ex: mesa, sofá, etc.)
CHIPS_DOS_OBJETOS = {
    "telemovel": {"id": "BT_ID_TELEMOVEL_99", "coordenada": [1, 5]},
    "comando": {"id": "BT_ID_COMANDO_TV_01", "coordenada": [3, 1]},
    "chaves": {"id": "BT_ID_CHAVES_CASA_02", "coordenada": [2, 2]}
}

def accio_buscar_objeto(objeto):
    print(f"\n⚡ [Feitiço Accio Ativado] Alvo: {objeto}")
    
    if objeto not in CHIPS_DOS_OBJETOS:
        print(f"🤖 O objeto '{objeto}' não tem nenhum chip registado no meu sistema.")
        return

    destino = CHIPS_DOS_OBJETOS[objeto]["coordenada"]
    id_chip = CHIPS_DOS_OBJETOS[objeto]["id"]
    
    print(f"🧠 Localização do chip [{id_chip}] encontrada no mapa: {destino}")
    print(f"📍 Posição inicial do Accio: {obter_posicao_atual()}")
    time.sleep(1)

    print("\n🗺️ A planear rota segura através do mapa mental...")
    time.sleep(1)
    
    # Navegação passo a passo até ao objeto
    while obter_posicao_atual() != destino:
        atual = obter_posicao_atual()
        proxima_linha = atual[0]
        proxima_coluna = atual[1]
        
        if proxima_linha < destino[0]: proxima_linha += 1
        elif proxima_linha > destino[0]: proxima_linha -= 1
        elif proxima_coluna < destino[1]: proxima_coluna += 1
        elif proxima_coluna > destino[1]: proxima_coluna -= 1
        
        # Executa o movimento consultando a matriz de segurança
        movimento_seguro = atualizar_posicao(proxima_linha, proxima_coluna)
        if not movimento_seguro:
            print("🚨 Rota abortada por risco de colisão física! O robô recusa-se a bater na parede.")
            return
            
        print(f"🚗 Motores avançam para: {obter_posicao_atual()}")
        time.sleep(0.6)

    # Ativação da garra de sucção ao chegar
    print(f"\n🎯 Posição {destino} alcançada com precisão milimétrica!")
    print("🦾 Ventosa posicionada sobre o alvo.")
    print("💨 Bomba de vácuo ativada. Pressão negativa criada... Objeto seguro!")
    time.sleep(1.5)
    print("↩️ A calcular rota de regresso à base pelo mapa mental... Entrega efetuada! 🎁")


def vir_ter_comigo():
    print("\n⚡ [Feitiço Supremo Ativado] 'Accio Accio!'")
    print("🎤 Placa de Microfones Reativa Ativada... A ouvir ondas sonoras...")
    time.sleep(1)
    
    # Definimos o ângulo e a coordenada onde tu estás ficticiamente (ex: Linha 4, Coluna 4)
    angulo_da_voz = 45
    coordenada_dono = [4, 4]
    
    print(f"🔊 [ÂNGULO DETETADO]: Voz vinda a {angulo_da_voz}°!")
    print("📡 [FUSÃO DE SENSORES]: Trancando posição no mapa mental...")
    time.sleep(1)
    
    # Navegação segura até ti
    while obter_posicao_atual() != coordenada_dono:
        atual = obter_posicao_atual()
        proxima_linha = atual[0]
        proxima_coluna = atual[1]
        
        if proxima_linha < coordenada_dono[0]: proxima_linha += 1
        elif proxima_linha > coordenada_dono[0]: proxima_linha -= 1
        elif proxima_coluna < coordenada_dono[1]: proxima_coluna += 1
        elif proxima_coluna > coordenada_dono[1]: proxima_coluna -= 1
            
        movimento_seguro = atualizar_posicao(proxima_linha, proxima_coluna)
        if not movimento_seguro:
            print("🚨 Rota interrompida! Há um obstáculo no caminho.")
            return
            
        print(f"🚗 Accio a avançar em direção à tua voz... Posição: {obter_posicao_atual()}")
        time.sleep(0.6)
        
    print("\n🤖 [Magia Concluída] Parei exatamente à tua frente!")