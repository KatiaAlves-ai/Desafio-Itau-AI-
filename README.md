Este é um micro-serviço desenvolvido em Python (FastAPI) que segue os princípios de **Domain-Driven Design (DDD)**. Ele recebe prompts, persiste no banco de dados SQLite e utiliza a API do Groq (Llama 3.3) para respostas em tempo real.

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
* Python 3.9 ou superior instalado.
* Uma chave de API do [Groq Cloud](https://console.groq.com/keys).

### 2. Configuração do Ambiente
1. Clone o repositório ou extraia os arquivos.
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate     # No Windows

  ### Instalar as dependências
  <>Bash
  * pip install -r requirements.txt

### variaveis de ambiente
1.Renomeie o arquivo .env.example para .env
2 Adicione sua chave do Groq na variável OPENROUTER_API_KEY

### Execução 
Execute o servidor 
*python main.py 
* O servidor estará rodando em: http://localhost:8000

🛠️ Testando a API
A documentação interativa (Swagger) pode ser acessada em:
http://localhost:8000/docs


Exemplo de Payload (POST /v1/chat):
{
  "userId": "123",
  "prompt": "Explique brevemente o que é DDD."
}

🏗️ Arquitetura (DDD)

O projeto está dividido em camadas para garantir manutenibilidade e separação de conceitos:
Domain: Entidades de negócio e interfaces de repositório.
Services: Lógica de integração com a LLM e orquestração.
Infrastructure: Implementação do banco de dados (SQLAlchemy) e cliente HTTP.
Presentation: Endpoints da API e injeção de dependências.
