Sistema de Gestão de Estoque e Controle de Acesso

Um sistema interativo em linha de comando (CLI) desenvolvido em Python com SQLite3, projetado para gerenciar usuários (Clientes, Colaboradores e Cargos) e realizar o controle completo de produtos em estoque com controle de acesso baseado em funções (RBAC).

🚀 Funcionalidades

Gerenciamento de Usuários e Acessos:

Cadastro de Clientes com validação de dados de contato e endereço.

Cadastro de Colaboradores associados a cargos específicos.

Criação dinâmica de Cargos (Ex: Administrador, Estoquista, Caixa).

Autenticação e validação de login (Email/Senha).

Controle de acesso às funcionalidades do menu de acordo com o cargo do colaborador.

Controle de Estoque:

Cadastro de produtos com nome, descrição, preço unitário, quantidade e código de barras único.

Listagem detalhada de itens cadastrados no inventário.

Cálculo e verificação do total de itens disponíveis em estoque.

Auditoria e Logs:

Registros de logs automáticos (Logs_save/sistema_login.txt) armazenando erros de validação e eventos importantes do sistema com data e hora.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

Banco de Dados: SQLite3

Manipulação de Arquivos e Datas: Módulos nativos pathlib e datetime

📁 Estrutura do Projeto

.
├── main.py                    # Ponto de entrada da aplicação (menus e fluxo principal)
├── Core/
│   ├── Codigo_Estoque.py      # Operações da classe de Estoque
│   └── Funções_Estoque.py     # Funções de validação para produtos
├── Login/
│   ├── Codigo_Login.py        # Classes para Cadastro, Cargo e Colaborador
│   └── Funções_Login.py       # Funções de login, validação de inputs e logs
├── Db/
│   ├── classe.py              # Conexão e gerenciamento do SQLite
│   ├── create_tables.py       # Script de inicialização das tabelas do BD
│   ├── delete.py              # Scripts utilitários de limpeza/reset
│   └── update.py              # Scripts utilitários de atualização
└── Logs_save/
    └── sistema_login.txt      # Arquivo de histórico de logs


🗄️ Modelo do Banco de Dados

O banco de dados SQLite é estruturado com as seguintes tabelas e relacionamentos principais:

Clientes: Dados cadastrais e endereço do cliente.

Cargos: Tipos de privilégios/cargos do sistema.

Colaboradores: Funcionários vinculados a um cargo (FK: Id_cargo).

login: Autenticação e vínculo com cliente ou colaborador.

Armazenamento: Cadastro do estoque com regras de integridade (Preco_unitario > 0, Quantidade >= 0 e Codigo_de_barra UNIQUE).

Vendas / Itens_vendas: Módulos preparados para o registro de transações.

⚙️ Como Executar o Projeto

Pré-requisitos

Python 3.8 ou superior instalado.

Instalação e Execução

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


Inicialize as tabelas do banco de dados:
Antes de rodar o sistema pela primeira vez, execute o script para criar a estrutura do banco SQLite:

python Db/create_tables.py


Execute a aplicação:

python main.py


📝 Exemplo de Uso

Ao abrir o sistema, crie um Cargo (Ex: Administrador ou Estoquista).

Cadastre um Colaborador e associe-o ao cargo criado.

Faça o Login com o e-mail e senha cadastrados.

Acesse o menu de estoque para Cadastrar novos produtos, Listar itens ou Verificar quantidade total.
