# 📄 Resume Parser AI

Projeto em Python para extração automática de informações de currículos utilizando Expressões Regulares (Regex).

O sistema lê arquivos `.txt` contendo currículos e identifica automaticamente dados importantes como nome, e-mail, telefone, experiência profissional e habilidades.

---

# 🚀 Funcionalidades

* Extração automática de nome
* Identificação de e-mail
* Captura de telefone e celular
* Leitura de experiência profissional
* Extração de habilidades
* Processamento de currículos em texto
* Uso de Regex para análise inteligente

---

# 🛠 Tecnologias utilizadas

* Python
* Regex (`re`)

---

# ▶ Como executar

## Clone o repositório

```bash
git clone SEU_LINK_GITHUB
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Execute o projeto

```bash
python main.py
```

---

# 📂 Exemplo de currículo

```txt
Nome: João Silva
Email: joao@gmail.com
Telefone: (11) 99999-9999
Experiência: Desenvolvedor Python
Habilidades: Python, SQL, Automação
```

---

# 📌 Exemplo de saída

```python
{
    'nome': 'João Silva',
    'email': 'joao@gmail.com',
    'telefone': '(11) 99999-9999',
    'experiencia': 'Desenvolvedor Python',
    'habilidades': 'Python, SQL, Automação'
}
```

---

# 📖 Objetivo

Automatizar a leitura e extração de informações de currículos para sistemas de RH, automações e análise de candidatos.

