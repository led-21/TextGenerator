# TextGenerator

TextGenerator é uma solução de Processamento de Linguagem Natural (NLP) desenvolvida como parte do curso "NLP Engineer" da JetBrains Academy. O principal objetivo deste projeto é prever a próxima palavra em uma sequência textual (pseudo-sentença) usando modelos estatísticos de linguagem.

## Visão Geral da Solução

O sistema utiliza modelos de n-gramas para analisar sequências de palavras e estimar, estatisticamente, a probabilidade de ocorrência da próxima palavra, considerando o contexto anterior. Esse tipo de abordagem é fundamental em tarefas como autocomplete, correção automática e geração de texto.

### Principais Funcionalidades

- Treinamento de modelos n-gramas (bigramas, trigramas, etc.) a partir de corpus textual customizado.
- Inferência: Sugestão da próxima palavra em uma sequência baseada no contexto.
- Manipulação e pré-processamento de texto (tokenização, normalização).
- Suporte a diferentes tamanhos de n-gramas configuráveis pelo usuário.

## Arquitetura e Algoritmos

O núcleo da aplicação é composto por:

- **Tokenização:** Separação do texto em unidades (tokens) para análise.
- **Construção do Modelo n-Grama:** Criação de um dicionário de frequências de n-gramas extraídos do corpus.
- **Predição:** Dada uma sequência de texto, o algoritmo busca o n-grama correspondente e sugere a próxima palavra com maior probabilidade de ocorrência.

O sistema pode ser facilmente adaptado para outros idiomas e corpus mediante alteração dos dados de entrada.

## Dependências

- Python 3.8+
- Bibliotecas: `nltk`, `numpy`, `pandas` (confirme conforme requirements.txt)

Para instalar as dependências:
```bash
pip install -r requirements.txt
```

## Uso

1. **Treinamento:**
   - Adicione seu corpus de texto ao diretório de dados.
   - Execute o script principal para treinar o modelo:
     ```bash
     python main.py --train --corpus data/meu_corpus.txt
     ```

2. **Predição:**
   - Gere a próxima palavra informando uma sequência:
     ```bash
     python main.py --predict "A inteligência artificial"
     ```

## Exemplos

```python
# Exemplo de uso em Python
from text_generator import TextGenerator

tg = TextGenerator('data/meu_corpus.txt', n=3)
tg.train()
print(tg.predict_next("A inteligência artificial"))
```

## Referências

- [Curso NLP Engineer - JetBrains Academy](https://hyperskill.org/tracks/15)
- Jurafsky, D.; Martin, J. H. - Speech and Language Processing. 3rd Edition.

## Licença

Distribuído sob a licença MIT.
