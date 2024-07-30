import pandas as pd
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [23, 34, 45, 26],
    'Cidade': ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Curitiba']
}
df = pd.DataFrame(dados)
linha_coluna = df.loc['Bruno','Idade'] 
print(linha_coluna)