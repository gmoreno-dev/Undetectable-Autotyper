# 👻 GhostTyper - Undetectable AutoTyper

<div align="center">

<!-- Coloque aqui sua logo maneira -->
<img src="logo.png" alt="GhostTyper Logo" width="200"/>

### O AutoTyper que finge ser humano melhor que você (ou não)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Quase%20Indetect%C3%A1vel-success)](https://github.com/seuuser/undetectable-autotyper)

**Python-based undetectable autotyper with human-like typing simulation | AutoTyper indetectável com simulação de digitação humana**

</div>

---

## 🤔 O que é isso?

Sabe quando você precisa digitar aquele textão gigante e sua mão já tá doendo só de pensar? GhostTyper é um autotyper com interface gráfica que simula digitação humana.

**Spoiler:** Nada é 100% indetectável, mas eu tentei.

## 🤖 Features que te fazem parecer humano

- **Delays Aleatórios**: Entre 10-50ms por caractere
- **Erros de Digitação**: 5% de chance de errar e corrigir (sim, igual você faz na vida real)
- **Pausas Aleatórias**: Aquele momento de "eeehhh o que eu ia escrever mesmo?"
- **Movimento do Mouse**: Porque até digitando você mexe o mouse às vezes

## ❓ Como usar

### Instalação
```bash
# Clone o repo (ou baixe o ZIP, sem julgamentos aqui)
git clone [https://github.com/gmoreno-dev/Undetectable-Autotyper.git]
cd Undetectable-Autotyper

# Instala as dependências
pip install -r requirements.txt

# Roda
python autotyper.py
```

### Uso

1. **Escreve o texto** no campo grande ali
2. **Posiciona o cursor** onde você quer digitar (ex: campo de texto no Chrome)
3. **Clica em "Iniciar"** ou aperta F9
4. **Conta até 3** e deixa a mágica acontecer
5. **Usa F10** se quiser parar no meio

## ⚠️ Isso realmente funciona?

**TL;DR:** Depende.

### ✅ Funciona bem contra:
- Sites simples com pouca/média proteção anti-bot
- Campos de texto básicos
- Formulários comuns
- Aquela tarefa chata que o professor passou

### ❌ Não funciona contra:
- Google e redes sociais (eles são espertos demais)
- Sites com CAPTCHA avançado
- Detecção por IP ou fingerprinting
- O olhar desconfiado do seu chefe

### 🔬 Técnicas usadas:
```python
# Velocidade humana
human_like_delay(0.01, 0.05)  

# Simula aquele erro clássico
simulate_typing_error()  # 5% de chance

# Pausa pra "pensar"
random_pause()  # 10% de chance

# Mexe o mouse que nem você faz sem querer
move_mouse_slightly()  # 5% de chance
```

## 📋 Requirements
```
pyautogui==0.9.54
pillow==10.0.0
pynput==1.7.6
```

## 🛣️ Roadmap (se eu tiver tempo)

- [ ] Suporte a múltiplos arquivos de texto
- [ ] Perfis de velocidade (Lerdo, Normal, Flash)
- [ ] Integração com clipboard
- [ ] Modo "Super Paranóico" com ainda mais variações
- [ ] Estatísticas de digitação em tempo real
- [ ] Tema customizável

## ⚖️ Disclaimer (a parte chata mas necessária)

Este projeto foi criado para fins **educacionais e de automação pessoal**. Use com responsabilidade e bom senso:

- ❌ NÃO use para spam
- ❌ NÃO use para burlar sistemas de segurança importantes
- ❌ NÃO use para atividades ilegais ou antiéticas
- ✅ Use para automatizar tarefas repetitivas legítimas
- ✅ Use para aprender sobre automação
- ✅ Use para economizar suas mãos de digitar demais

**Se você for banido de algum lugar usando isso, não foi culpa minha.**

## 🤝 Contribuindo

PRs são bem-vindos! Se você tem ideias pra tornar isso ainda mais indetectável (ou apenas mais legal), manda ver.

## 📝 Licença

MIT - Faça o que quiser, só não me culpe depois.

---

<div align="center">

**Feito com ☕ e muita procrastinação**

Se isso te ajudou, deixa uma ⭐ aí!

</div>
