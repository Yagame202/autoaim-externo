 # Arduino Auto-Aim Aimbot

Este projeto detecta inimigos por cor na tela (vermelho), calcula a posição e move a mira automaticamente usando Arduino Leonardo/Micro com HID.

## Estrutura

- `python/aimbot.py`: código Python com OpenCV + MSS.
- `arduino/aimbot_autoaim.ino`: código para Arduino que recebe movimentos via Serial e move o mouse.
- `requirements.txt`: bibliotecas Python necessárias.

## Uso

1. Conecte o Arduino e envie `aimbot_autoaim.ino`.
2. Instale dependências Python:

```bash
pip install -r requirements.txt
