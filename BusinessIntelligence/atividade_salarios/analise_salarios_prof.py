import pandas as pd
import numpy as np
import os

# Carregar dados com separador ponto-vírgula
caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'salario_prof.csv')
df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')

# Limpar espaços em branco das colunas e valores
df.columns = df.columns.str.strip()
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Converter coluna de salário: formato brasileiro (13.007,12) para float
df['Salário inicial'] = df['Salário inicial'].str.replace('.', '').str.replace(',', '.').astype(float)

# Renomear coluna para facilitar
df = df.rename(columns={'Salário inicial': 'Salario', 'UF': 'Estado'})

print("=" * 90)
print("ANÁLISE DE SALÁRIOS INICIAIS DE PROFESSORES POR ESTADO E REGIÃO")
print("=" * 90)

# 1. Estado com menor salário
print("\n1. ESTADO COM MENOR SALÁRIO:")
print("-" * 90)
estado_menor = df.loc[df['Salario'].idxmin()]
print(f"Estado: {estado_menor['Estado']:2s} | Salário: R$ {estado_menor['Salario']:>10,.2f} | Região: {estado_menor['Região']}")

# 2. Estado com maior salário
print("\n2. ESTADO COM MAIOR SALÁRIO:")
print("-" * 90)
estado_maior = df.loc[df['Salario'].idxmax()]
print(f"Estado: {estado_maior['Estado']:2s} | Salário: R$ {estado_maior['Salario']:>10,.2f} | Região: {estado_maior['Região']}")

# 3. Posição de Goiás (GO)
print("\n3. POSIÇÃO DO ESTADO DE GOIÁS (GO):")
print("-" * 90)
df_ordenado = df.sort_values('Salario', ascending=False).reset_index(drop=True)
go_data = df_ordenado[df_ordenado['Estado'] == 'GO']
if not go_data.empty:
    posicao_go = go_data.index[0] + 1
    salario_go = go_data['Salario'].values[0]
    print(f"Posição: {posicao_go}ª lugar | Salário: R$ {salario_go:,.2f}")
else:
    print("Goiás não encontrado no dataset")

# 4. Média salarial entre todos os estados
print("\n4. MÉDIA SALARIAL ENTRE TODOS OS ESTADOS:")
print("-" * 90)
media_geral = df['Salario'].mean()
print(f"Média Geral: R$ {media_geral:,.2f}")

# 5. Média salarial por estado
print("\n5. MÉDIA SALARIAL POR ESTADO:")
print("-" * 90)
media_por_estado = df.sort_values('Salario', ascending=False)[['Estado', 'Salario']].copy()
for idx, row in media_por_estado.iterrows():
    print(f"{row['Estado']}: R$ {row['Salario']:>10,.2f}")

# 6. Maior salário por região
print("\n6. MAIOR SALÁRIO POR REGIÃO:")
print("-" * 90)
maior_por_regiao = df.groupby('Região')['Salario'].max().sort_values(ascending=False)
for regiao, salario in maior_por_regiao.items():
    print(f"{regiao:20s}: R$ {salario:>10,.2f}")

# 7. Menor salário por região
print("\n7. MENOR SALÁRIO POR REGIÃO:")
print("-" * 90)
menor_por_regiao = df.groupby('Região')['Salario'].min().sort_values(ascending=True)
for regiao, salario in menor_por_regiao.items():
    print(f"{regiao:20s}: R$ {salario:>10,.2f}")

# 8. Média salarial por região
print("\n8. MÉDIA SALARIAL POR REGIÃO:")
print("-" * 90)
media_por_regiao = df.groupby('Região')['Salario'].mean().sort_values(ascending=False)
for regiao, media in media_por_regiao.items():
    print(f"{regiao:20s}: R$ {media:>10,.2f}")

# 9. Região com maior e menor média salarial
print("\n9. REGIÃO COM MAIOR E MENOR MÉDIA SALARIAL:")
print("-" * 90)
regiao_maior_media = media_por_regiao.idxmax()
valor_maior_media = media_por_regiao.max()
regiao_menor_media = media_por_regiao.idxmin()
valor_menor_media = media_por_regiao.min()
diferenca = valor_maior_media - valor_menor_media

print(f"MAIOR média salarial:  {regiao_maior_media:20s} (R$ {valor_maior_media:>10,.2f})")
print(f"MENOR média salarial:  {regiao_menor_media:20s} (R$ {valor_menor_media:>10,.2f})")
print(f"Diferença (variação):                  R$ {diferenca:>10,.2f}")

# Resumo comparativo das regiões
print("\n" + "=" * 90)
print("RESUMO COMPLETO POR REGIÃO:")
print("=" * 90)
resumo = pd.DataFrame({
    'Maior Salário': df.groupby('Região')['Salario'].max(),
    'Menor Salário': df.groupby('Região')['Salario'].min(),
    'Média': df.groupby('Região')['Salario'].mean(),
    'Qtd Estados': df.groupby('Região')['Estado'].count()
}).sort_values('Média', ascending=False)

print(resumo.to_string(float_format=lambda x: f'R$ {x:,.2f}'))

print("\n" + "=" * 90)
