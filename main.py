import re

# Função para extrair informações do currículo
def extrair_informacoes(cv):
    informacoes = {}
    
    # Procurando nome do candidato
    nome = re.search("(?i)nome: (.+)", cv)
    if nome:
        informacoes["nome"] = nome.group(1).strip()
    
    # Procurando endereço de e-mail
    email = re.search("(?i)[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", cv)
    if email:
        informacoes["email"] = email.group(0).strip()
        
    # Procurando experiência de trabalho
    experiencia = re.search("(?i)experiência(.+)", cv)
    if experiencia:
        informacoes["experiencia"] = experiencia.group(1).strip()
        
    # Procurando telefone
    telefone = re.search("(?i)telefone(.+)", cv)
    if telefone:
        informacoes["telefone"] = telefone.group(1).strip()
        
    # Procurando celular
    celular = re.search("(?i)celular(.+)", cv)
    if celular:
        informacoes["celular"] = celular.group(1).strip()
        
    # Procurando contato
    contato = re.search("(?i)contato(.+)", cv)
    if contato:
        informacoes["contato"] = contato.group(1).strip()
        
    # Procurando habilidades
    habilidades = re.search("(?i)habilidades(.+)", cv)
    if habilidades:
        informacoes["habilidades"] = habilidades.group(1).strip()
    
    
    return informacoes

# Lendo arquivo de currículo
with open("untitled.txt", "r") as f:
    cv = f.read()
    
# Extraindo informações do currículo
informacoes = extrair_informacoes(cv)

# Imprimindo informações
print(informacoes)
