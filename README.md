# Painel ODS - Visualização e Análise de Dados

## Introdução

O Painel ODS é uma ferramenta interativa para visualização e análise de dados relacionados aos Objetivos de Desenvolvimento Sustentável (ODS) em diferentes municípios. Esta aplicação permite comparar indicadores entre municípios e analisar detalhadamente os dados ao longo dos anos, fornecendo insights valiosos para gestores públicos, pesquisadores e interessados em monitorar o progresso dos ODS.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

### `app.py`

Arquivo principal que executa a aplicação Streamlit. Ele configura a interface do usuário, carrega os dados e chama as funções de visualização dos gráficos.

### `data_processing.py`

Contém funções para carregar e processar os dados do Excel. Garante que os dados estejam no formato correto para serem utilizados pela aplicação.

### `visualization.py`

Inclui as funções responsáveis por gerar os gráficos de comparação e análise detalhada. Utiliza Plotly para criar gráficos interativos.

### `requirements.txt`

Lista de dependências necessárias para executar a aplicação. Inclui pacotes como pandas, streamlit e plotly.

## Como Utilizar

### Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas listadas em `requirements.txt`

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie um ambiente virtual e ative-o
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
pip install -r requirements.txt

### Executando a Aplicação
1. Coloque o arquivo de dados Excel (.xlsx) na raiz do projeto.

2. Execute o aplicativo Streamlit:
streamlit run app.py

3. Acesse a aplicação no seu navegador no endereço http://localhost:8501

### Uso da Interface
1. Carregar Dados
- Selecione o arquivo Excel com os dados.

## Visualização Comparativa
- Escolha os municípios e os indicadores que deseja comparar.
- Os gráficos serão gerados automaticamente mostrando a comparação dos indicadores selecionados entre os municípios.

## Análise Detalhada
- Selecione um município e os indicadores que deseja analisar ao longo do tempo.
- O gráfico mostrará a evolução dos indicadores selecionados para o município escolhido.

### Importância da Aplicação
- O Painel ODS é uma ferramenta essencial para acompanhar o progresso dos Objetivos de Desenvolvimento Sustentável (ODS) em nível municipal. Com ele, é possível:

## Identificar áreas que precisam de mais atenção e recursos.
- Monitorar o desempenho de diferentes municípios ao longo do tempo.
- Tomar decisões baseadas em dados para políticas públicas.
- Aumentar a transparência e o acesso a informações críticas para o desenvolvimento sustentável.

### Contribuição
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para adicionar funcionalidades, corrigir bugs ou melhorar a documentação.

### Licença
- Este projeto está licenciado sob a MIT License.

### Desenvolvido por João Maykon Mendes Ferreira


Este arquivo `README.md` fornece uma visão geral completa do projeto, incluindo a estrutura dos arquivos, instruções de instalação e uso, além de destacar a importância da aplicação. Sinta-se à vontade para personalizar conforme necessário!


