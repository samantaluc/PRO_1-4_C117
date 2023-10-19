import os
import cv2

# Diretório onde estão as imagens
path = "Images"

# Lista para armazenar os nomes dos arquivos de imagem
images = []

# Loop para encontrar arquivos de imagem no diretório
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    # Verifica se a extensão do arquivo é uma imagem válida
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = os.path.join(path, file)  # Utilize os.path.join para criar o caminho completo
        images.append(file_name)

# Obtém o número de imagens
count = len(images)

# Lê a primeira imagem para obter o tamanho
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

# Cria o objeto de gravação de vídeo
out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

# Loop para escrever as imagens no vídeo (inverso para o NASCER DO SOL)
for i in range(count - 1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)

# Libera o vídeo gerado
out.release()
print("Concluído")
