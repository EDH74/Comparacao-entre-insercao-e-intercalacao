# Análise de Algoritmos de Ordenação

Este repositório contém uma análise comparativa de desempenho entre os algoritmos **Ordenação por Inserção (Insertion Sort)** e **Ordenação por Intercalação (Merge Sort)**, em comparação com a função nativa `sorted()` do Python.

## Arquivos do Projeto

- `ordenacao.py`: Contém as implementações dos algoritmos de ordenação, retornando a lista ordenada e o número de comparações realizadas.
- `testes.py`: Arquivo de testes unitários que garante o funcionamento correto dos algoritmos cobrindo os piores casos e casos limítrofes.
- `medir.py`: Script principal que realiza os testes de desempenho, coleta os dados brutos de tempo/comparações e gera os gráficos.
- `RELATORIO.md`: Análise teórica baseada nos dados extraídos pela medição.

## Pré-requisitos

Para executar a aplicação, você precisará ter o **Python 3** instalado em sua máquina. Além disso, o script de medição utiliza as bibliotecas `pandas` e `matplotlib` para gerar o arquivo CSV e os gráficos de desempenho.

Para instalar as dependências necessárias, abra o terminal e execute:

```bash
pip install pandas matplotlib
```

## Como Executar

### 1. Rodar os Testes Unitários
Para garantir que as funções de ordenação estão funcionando perfeitamente em casos difíceis (listas vazias, já ordenadas, invertidas, etc.), execute o arquivo de testes:

```bash
python testes.py
```
*Se tudo estiver correto, você verá uma mensagem indicando que os testes passaram com sucesso (Ex: `Ran 2 tests in 0.001s. OK`).*

### 2. Rodar a Medição e Gerar os Gráficos
Para executar o experimento, rodar as listas aleatórias, cronometrar os algoritmos e gerar os arquivos finais, execute o arquivo principal:

```bash
python medir.py
```

### Resultados Esperados
Após rodar o `medir.py`, os seguintes arquivos serão criados ou sobrescritos na raiz do projeto:
- `dados.csv`: Contendo os dados brutos das medições (tempos médios e comparações).
- `grafico_tempos.png`: Gráfico visual mostrando o tempo de execução (s) pelo tamanho da lista (n).
- `grafico_comparacoes.png`: Gráfico visual mostrando a quantidade de comparações lógicas efetuadas pelo tamanho da lista (n).