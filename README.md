# Discord bot feito em Python

Atualmente, esse bot tem apenas a funcionalidade de mostrar o elo do jogador nas ranqueadas do lolzinho 

## Como instalar

### 1. Clone o repositório
```
git clone https://github.com/Jonatas00/Python-Discord-bot.git
```
### 2. Crie um ambiente virtual (Virutal Environment)
```
Python -m venv env
```

### 3. Ative o ambiente virtual
```python
 ./env/Scripts/Activate  # Windows
```
### 4. Instale os requerimentos
```
pip install -r requirements.txt
```
### 5. Adicione suas keys em keyConfig.py

1. Vá para https://discord.com/developers/ e faça login com sua conta
2. Faça um novo aplicativo e escolha um nome
3. Vá na aba Bot e clique no botão "Reset Token"
4. Copie e cole sua chave no arquivo keyConfig.py
```python
discordKey = "Insira sua KEY AQUI"  # Your discord bot key
```
5. Vá para https://developer.riotgames.com e faça login com sua conta
6. Copie e cole sua chave no arquivo keyConfig.py
```python
RiotKey = "Insira sua KEY AQUI"     # Your Riot API key
```
