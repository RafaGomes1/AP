import json

# Carregar o ficheiro da estrutura original (LabelMe)
with open("points/A40E/frame_0000.json", "r") as f:
    labelme_data = json.load(f)

# Carregar o ficheiro da estrutura de destino
with open("target.json", "r") as f:
    target_data = json.load(f)

# Indexar os pontos por label
label_points = {shape["label"]: shape["points"][0] for shape in labelme_data["shapes"]}

# Função utilitária para preencher ponto
def preencher_keypoint(label, keypoint_data):
    if label in label_points:
        x, y = label_points[label]
    else:
        x, y = 0, 0  # valor default
    keypoint_data["x"] = x
    keypoint_data["y"] = y
    keypoint_data["visibility"] = 2  # fixo

# Preencher para mãos
for hand in target_data.get("hands", []):
    for keypoint_name, keypoint_data in hand["keypoints"].items():
        label = f'{hand["label"].replace(" ", "_")}_{keypoint_name}'
        preencher_keypoint(label, keypoint_data)

# Preencher para ferramentas
for tool in target_data.get("tools", []):
    for keypoint_name, keypoint_data in tool["keypoints"].items():
        label = f'{tool["label"].replace(" ", "_")}_{keypoint_name}'
        preencher_keypoint(label, keypoint_data)

# Guardar resultado final
with open("merged_output.json", "w") as f:
    json.dump(target_data, f, indent=2)

print("Script completo. Estrutura preenchida com defaults onde necessário.")
