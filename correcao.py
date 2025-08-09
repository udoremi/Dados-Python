import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

df['senioridade'] = df['senioridade'].replace({
    'senior': 'Sênior',
    'pleno': 'Pleno',
    'junior': 'Júnior',
    'executivo': 'Executivo'
})

df['tipo_contrato'] = df['contrato'].replace({ 
    'integral': 'Integral',
    'contrato': 'Contrato',
    'freelancer': 'Freelancer',
    'parcial': 'Parcial'
})

df['tamanho_empresa'] = df['tamanho_empresa'].replace({
    'media': 'Média',
    'grande': 'Grande',
    'pequena': 'Pequena'
})

df['remoto'] = df['remoto'].replace({
    'remoto': 'Remoto',
    'presencial': 'Presencial',
    'hibrido': 'Híbrido'
})

df.to_csv('dados_imersao_corrigidos.csv', index=False)

print("Arquivo com ortografia corrigida salvo como 'dados_corrigidos.csv'")