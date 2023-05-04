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
```
 ./env/Scripts/Activate 
```
### 4. Instale os requerimentos
```
pip install -r requirements.txt
```
### 6. Crie o arquivo "keyConfigs.py" e adicione suas keys nele
1. No diretório base do projeto crie um arquivo chamado "keyConfigs.py"
2. Vá para https://discord.com/developers/ e faça login com sua conta
3. Faça um novo aplicativo e escolha um nome
4. Vá na aba Bot e clique no botão "Reset Token"
5. Copie e cole sua chave no arquivo "keyConfig.py"
```python
discordKey = "Insira sua KEY AQUI"  # Your discord bot key
```
6. Vá para https://developer.riotgames.com e faça login com sua conta
7. Copie e cole sua chave no arquivo keyConfig.py
```python
riotKey = "Insira sua KEY AQUI"     # Your Riot API key
```
### 7. Execute o bot
```
py main.py
```
