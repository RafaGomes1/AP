import os
import cv2
import numpy as np

def extrair_frames_de_videos(pasta_videos='Package01', destino_frames='dataset_frames2', num_frames=5):
    os.makedirs(destino_frames, exist_ok=True)
    for nome_arquivo in os.listdir(pasta_videos):
        if not nome_arquivo.endswith('.mp4'):
            continue
        caminho_video = os.path.join(pasta_videos, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]
        pasta_destino = os.path.join(destino_frames, nome_base)
        os.makedirs(pasta_destino, exist_ok=True)

        cap = cv2.VideoCapture(caminho_video)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if total_frames == 0:
            print(f"Erro ao obter frames de {nome_arquivo}")
            continue

        frame_indices = np.linspace(0, total_frames - 1, num=num_frames, dtype=int)

        count = 0
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                framename = f"frame{count:04d}.jpg"
                cv2.imwrite(os.path.join(pasta_destino, frame_name), frame)
                count += 1

        cap.release()
        print(f"✅ {count} frames extraídos de {nome_arquivo}")

extrair_frames_de_videos()