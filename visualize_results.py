import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import platform

def generate_dashboard():
    # 1. Carregar os dados gerados pelo Projeto #3
    file_name = 'system_performance.png'
    csv_file = 'system_history.csv'
    
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{csv_file}' não foi encontrado.")
        print("Certifique-se de rodar o seu script principal (Projeto #3) primeiro para gerar os dados!")
        return

    # 2. Configuração Visual (Estilo Solarpunk/Tech)
    sns.set_theme(style="darkgrid")
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # --- GRÁFICO 1: NÍVEL DE ÁGUA (Eixo Esquerdo) ---
    color_water = '#0077b6' # Azul oceano
    ax1.set_xlabel('Tempo (Carimbo de Data/Hora)', fontweight='bold')
    ax1.set_ylabel('Nível da Caixa d\'Água (L)', color=color_water, fontweight='bold')
    
    # Plotando a linha de água
    sns.lineplot(data=df, x='Timestamp', y='Water_L', ax=ax1, color=color_water, linewidth=3, label='Nível de Água')
    ax1.tick_params(axis='y', labelcolor=color_water)
    
    # Melhorar a visualização das datas no eixo X
    plt.xticks(rotation=35, ha='right')

    # --- GRÁFICO 2: ENERGIA SOLAR (Eixo Direito) ---
    ax2 = ax1.twinx() # Cria o segundo eixo compartilhado
    color_solar = '#ffb703' # Amarelo solar
    ax2.set_ylabel('Radiação Solar (W/m²)', color=color_solar, fontweight='bold')
    
    # Preenchendo a área solar (Visual estilo "montanha")
    ax2.fill_between(df['Timestamp'], df['Solar_W'], color=color_solar, alpha=0.3, label='Energia Solar')
    ax2.tick_params(axis='y', labelcolor=color_solar)

    # 3. Títulos e Estética
    plt.title('JesFer JesFer AI: Monitoramento de Autonomia Hídrica (48h)', fontsize=18, pad=20, fontweight='bold')
    
    # Ajuste fino para não cortar as legendas
    fig.tight_layout()
    
    # 4. SALVAR E GERAR LINK
    plt.savefig(file_name, dpi=300) # Salva com alta qualidade para o GitHub
    
    # Gerar o link absoluto para o terminal
    full_path = os.path.abspath(file_name)
    path_with_slashes = full_path.replace('\\', '/')
    formatted_path = f"file:///{path_with_slashes}"
    
    print("\n" + "="*50)
    print("🎨 DASHBOARD GERADO COM SUCESSO!")
    print("="*50)
    print(f"\n🔗 LINK CLICÁVEL (Segure Ctrl + Clique):")
    print(f"{formatted_path}")
    print("\n" + "="*50)

    # 5. Abertura Automática (Dependente do Sistema Operacional)
    try:
        if platform.system() == "Windows":
            os.startfile(file_name)
        elif platform.system() == "Darwin": # macOS
            os.system(f"open {file_name}")
        else: # Linux
            os.system(f"xdg-open {file_name}")
    except Exception as e:
        print(f"Nota: Não foi possível abrir a imagem automaticamente ({e}), mas ela foi salva no diretório.")

if __name__ == "__main__":
    generate_dashboard()