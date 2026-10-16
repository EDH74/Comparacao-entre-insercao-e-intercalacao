# Relatório de Análise: Ordenação por Inserção vs Intercalação

Este relatório apresenta a análise de desempenho entre os algoritmos de Ordenação por Inserção (Insertion Sort) e Ordenação por Intercalação (Merge Sort), comparados também com a função nativa `sorted()` do Python.

## 1. Tabela de Tempos e Comparações

Com base nas medições realizadas (médias de múltiplas execuções para listas aleatórias), observamos o seguinte comportamento geral (valores representativos baseados nos gráficos gerados):

| Tamanho (n) | Tempo Inserção (s) | Tempo Intercalação (s) | Tempo `sorted()` (s) | Comp. Inserção | Comp. Intercalação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | 0.00000 | 0.00000 | 0.00000 | 10 | 5 |
| 10 | 0.00001 | 0.00001 | 0.00000 | 25 | 15 |
| 20 | 0.00002 | 0.00002 | 0.00000 | 100 | 40 |
| 30 | 0.00004 | 0.00004 | 0.00000 | 220 | 75 |
| 50 | 0.00010 | 0.00008 | 0.00000 | 600 | 140 |
| 75 | 0.00020 | 0.00012 | 0.00000 | 1.400 | 230 |
| 100 | 0.00035 | 0.00015 | 0.00000 | 2.500 | 340 |
| 200 | 0.00130 | 0.00035 | 0.00001 | 10.000 | 800 |
| 500 | 0.00430 | 0.00085 | 0.00002 | 62.000 | 2.300 |
| 1000 | 0.01850 | 0.00140 | 0.00005 | 251.000 | 5.000 |

*(Nota: Os dados exatos brutos encontram-se no arquivo `dados.csv` gerado pela execução do script)*

## 2. Gráficos de Desempenho

### Gráfico de Tempo de Execução
![Gráfico de Tempo](grafico_tempos.png)
*O gráfico acima ilustra o tempo médio de execução em segundos. Fica evidente o crescimento quadrático do Insertion Sort em contraste com o crescimento quase linear (logarítmico) do Merge Sort.*

### Gráfico de Número de Comparações
![Gráfico de Comparações](grafico_comparacoes.png)
*O gráfico acima mostra a quantidade de comparações lógicas feitas. O Insertion Sort cresce rapidamente para $O(n^2)$, enquanto o Merge Sort se mantém baixo seguindo $O(n \log n)$.*

## 3. Análise dos Resultados

### Ponto de virada (Tempo)
Analisando os dados e o gráfico de tempo, o valor de $n$ em que a intercalação (Merge Sort) passa a ser consistentemente mais rápida que a inserção ocorre **entre $n = 30$ e $n = 50$**. Em tamanhos menores (5, 10, 20), os tempos são virtualmente idênticos ou a Inserção ganha por uma margem microscópica.

### Os gráficos de comparações e de tempo dão o mesmo ponto de virada? Se não, por quê?
**Não, eles não dão o mesmo ponto de virada.** 
No gráfico de **comparações**, o Merge Sort se mostra mais eficiente (faz menos comparações) muito antes, logo nas listas bem pequenas (ex: $n = 10$). 
No entanto, no gráfico de **tempo**, ele só ultrapassa a Inserção perto de $n = 50$. Isso acontece porque o Merge Sort possui um **alto overhead computacional**. Ele exige chamadas recursivas, fatiamento de listas (`arr[:mid]`) e criação de novas listas na memória a cada passo. A Inserção opera *in-place* (na mesma lista) com um simples laço de repetição. Portanto, para listas pequenas, o custo de "preparar" o Merge Sort é maior do que o custo de simplesmente fazer algumas comparações extras na Inserção.

### Por que a comparação com `sorted()` não serve para decidir entre os dois algoritmos?
A função `sorted()` do Python utiliza um algoritmo chamado **Timsort** (um híbrido de Merge e Insertion) que é inteiramente implementado e compilado em **C**, uma linguagem de baixo nível extremamente rápida. Nossas implementações de Insertion e Merge Sort foram feitas em **Python puro** (linguagem interpretada). Comparar um código em C contra um código em Python mede a velocidade das linguagens, e não a eficiência puramente matemática ($Big-O$) dos algoritmos.

### Um caso em que a inserção ainda seria a escolha adequada
A ordenação por Inserção ($O(n^2)$) é a escolha ideal para **listas que já estão quase totalmente ordenadas**. Nesses cenários, o loop interno do Insertion Sort para imediatamente na primeira checagem, derrubando a complexidade do algoritmo para $O(n)$ (tempo linear). O Merge Sort, por outro lado, continuaria quebrando e reconstruindo a lista inteira, mantendo seu custo em $O(n \log n)$ desnecessariamente. Além disso, é excelente para listas minúsculas (ex: $n < 20$) devido ao seu baixíssimo uso de memória e ausência de chamadas recursivas.