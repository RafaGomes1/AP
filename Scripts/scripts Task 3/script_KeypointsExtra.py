import os
import json

def pad_tool_keypoints_preserving_names(json_dir):
    for filename in os.listdir(json_dir):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(json_dir, filename)

        with open(path, "r") as f:
            data = json.load(f)

        changed = False

        if "tools" in data:
            for tool in data["tools"]:
                existing_kpts = tool.get("keypoints", {})
                num_existing = len(existing_kpts)

                if num_existing < 6:
                    # Adicionar pontos extras mantendo os existentes
                    extras_needed = 6 - num_existing
                    for i in range(1, extras_needed + 1):
                        key_name = f"Extra{i}"
                        existing_kpts[key_name] = {
                            "x": 0,
                            "y": 0,
                            "visibility": 0
                        }
                    tool["keypoints"] = existing_kpts
                    changed = True

        if changed:
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Ajustado: {filename}")

pad_tool_keypoints_preserving_names("anotacoes/Teste/A61V")  # muda para a tua pasta
