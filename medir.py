# medir.py
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from ordenacao import insertion_sort, merge_sort

def executar_medicoes():
    tamanhos = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
    repeticoes = 20
    
    dados = []

    print("A executar medições de tempo e comparações...")

    for n in tamanhos:
        tempo_ins_tot = 0.0
        tempo_mrg_tot = 0.0
        tempo_srt_tot = 0.0
        
        comp_ins_tot = 0
        comp_mrg_tot = 0

        for rep in range(repeticoes):
            random.seed(n * 1000 + rep)
            lista_original = [random.randint(1, 100000) for _ in range(n)]

            # Insertion Sort
            t_inicio = time.perf_counter()
            _, c_ins = insertion_sort(lista_original)
            t_fim = time.perf_counter()
            tempo_ins_tot += (t_fim - t_inicio)
            comp_ins_tot += c_ins

            # Merge Sort
            t_inicio = time.perf_counter()
            _, c_mrg = merge_sort(lista_original)
            t_fim = time.perf_counter()
            tempo_mrg_tot += (t_fim - t_inicio)
            comp_mrg_tot += c_mrg

            # sorted() do Python (Timsort em C)
            t_inicio = time.perf_counter()
            _ = sorted(lista_original)
            t_fim = time.perf_counter()
            tempo_srt_tot += (t_fim - t_inicio)

        dados.append({
            'n': n,
            'tempo_insercao_s': tempo_ins_tot / repeticoes,
            'tempo_intercalacao_s': tempo_mrg_tot / repeticoes,
            'tempo_sorted_s': tempo_srt_tot / repeticoes,
            'comparacoes_insercao': comp_ins_tot / repeticoes,
            'comparacoes_intercalacao': comp_mrg_tot / repeticoes
        })

    # Guardar DataFrame em dados.csv
    df = pd.DataFrame(dados)
    df.to_csv("dados.csv", index=False)
    print("Ficheiro dados.csv gerado com sucesso!")

    # --- Gráfico 1: Tempos de Execução ---
    plt.figure(figsize=(10, 6))
    plt.plot(df['n'], df['tempo_insercao_s'], marker='o', color='crimson', label='Ordenação por Inserção (Insertion Sort)')
    plt.plot(df['n'], df['tempo_intercalacao_s'], marker='s', color='navy', label='Ordenação por Intercalação (Merge Sort)')
    plt.plot(df['n'], df['tempo_sorted_s'], marker='^', color='forestgreen', label='sorted() do Python (Timsort)')
    plt.title('Comparação do Tempo de Execução (Segundos)', fontsize=14, fontweight='bold')
    plt.xlabel('Tamanho da Lista (n)', fontsize=12)
    plt.ylabel('Tempo Médio (s)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig("grafico_tempos.png", dpi=300)
    plt.close()
    print("Gráfico grafico_tempos.png gerado com sucesso!")

    # --- Gráfico 2: Número de Comparações ---
    plt.figure(figsize=(10, 6))
    plt.plot(df['n'], df['comparacoes_insercao'], marker='o', color='crimson', label='Ordenação por Inserção (Insertion Sort)')
    plt.plot(df['n'], df['comparacoes_intercalacao'], marker='s', color='navy', label='Ordenação por Intercalação (Merge Sort)')
    plt.title('Comparação do Número de Comparações de Chaves', fontsize=14, fontweight='bold')
    plt.xlabel('Tamanho da Lista (n)', fontsize=12)
    plt.ylabel('Número Médio de Comparações', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig("grafico_comparacoes.png", dpi=300)
    plt.close()
    print("Gráfico grafico_comparacoes.png gerado com sucesso!")

if __name__ == "__main__":
    executar_medicoes()
