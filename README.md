# Painel ODS

Este projeto consiste em uma aplicação para visualização de dados relacionados aos Objetivos de Desenvolvimento Sustentável (ODS) em municípios brasileiros. A aplicação permite a comparação de indicadores entre diferentes municípios e a análise detalhada de indicadores específicos para um município.

## Estrutura do Projeto

O projeto contém os seguintes arquivos principais:

- `app.py`: Arquivo principal da aplicação. Contém a definição da interface do usuário utilizando Streamlit e a lógica para carregar e filtrar os dados.
- `utils.py`: Contém funções utilitárias para carregar e processar os dados a partir de arquivos Excel.
- `visualization.py`: Contém funções para gerar visualizações gráficas dos dados filtrados.

## Funcionalidades

A aplicação possui duas principais funcionalidades:

1. **Visualização Comparativa**:
    - Permite selecionar múltiplos municípios e comparar indicadores específicos entre eles.
    - Exibe os dados filtrados em uma tabela e um gráfico comparativo.

2. **Análise Detalhada**:
    - Permite selecionar um único município e visualizar a evolução de indicadores específicos ao longo do tempo.
    - Exibe os dados filtrados em uma tabela e um gráfico de linha mostrando a evolução dos indicadores.

## Importância dos Dados

Os dados utilizados na aplicação são cruciais para monitorar e avaliar o progresso dos municípios brasileiros em relação aos Objetivos de Desenvolvimento Sustentável. A visualização desses dados permite identificar áreas que necessitam de melhorias e orientar políticas públicas para promover um desenvolvimento sustentável e inclusivo.

## Como Utilizar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas listadas em `requirements.txt`

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/painel-ods.git
   cd painel-ods

2. Crie um ambiente virtual e instale as dependências:
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

### Execução
- Para executar a aplicação, utilize o comando:
  streamlit run app.py

### Estrutura dos Arquivos
## app.py:

- Define a interface do usuário com Streamlit.
- Carrega os dados e permite ao usuário selecionar municípios e indicadores para visualização.
- Chama funções de visualization.py para gerar gráficos.

## utils.py:

- Função load_data: Carrega os dados a partir de um arquivo Excel e os processa para uso na aplicação.

## visualization.py:

- Função generate_comparison_chart: Gera gráficos comparativos de indicadores entre municípios.
- Função generate_detailed_analysis_chart: Gera gráficos de linha mostrando a evolução de indicadores para um município.

### Contribuição
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

### Licença
Este projeto está licenciado sob a licença MIT.

### Desenvolvido por
- João Maykon Mendes Ferreira.



