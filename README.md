# Blog com Container Apps em Python

Este projeto consiste em um blog simples executado em um ambiente de contêineres, utilizando tráfego HTTPS, NGINX como proxy reverso e uma aplicação Python para gerenciar postagens.

## Arquitetura

1. **Tráfego HTTPS** → Configurado para garantir comunicação segura.
2. **NGINX** → Atua como proxy reverso, roteando as requisições para a aplicação.
3. **App Python** → Aplicação principal para gerenciar postagens do blog.
   - **ListPost**: Endpoint para listar postagens.
   - **CreatePost**: Endpoint para criar novas postagens.

## Tecnologias Utilizadas

- Docker
- NGINX
- Python (Flask ou FastAPI)
- HTTPS (SSL/TLS)

## Estrutura do Projeto
```
blog-container-apps/
│-- app/
│   ├── main.py  # Código da aplicação
│   ├── requirements.txt  # Dependências
│   ├── Templates/
│   │   ├── create_post.html  # Página para criação de postagens
│   │   ├── index.html  # Página inicial do blog
│   │   ├── post-detail.html  # Página de detalhes de uma postagem
│-- nginx/
│   ├── default.conf  # Configuração do NGINX
│-- Dockerfile
│-- docker-compose.yml
│-- README.md
```

## Como Executar

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/blog-container-apps.git
   cd blog-container-apps
   ```

2. Construa e inicie os contêineres:
   ```sh
   docker-compose up --build
   ```

3. Acesse a aplicação via HTTPS:
   ```
   https://localhost
   ```

## Endpoints

- **GET** `/posts` → Lista todas as postagens.
- **POST** `/posts` → Cria uma nova postagem (dados JSON no corpo da requisição).

## Configuração de HTTPS

O HTTPS pode ser configurado utilizando certificados autoassinados ou um serviço como Let’s Encrypt. Para um ambiente local, gere um certificado com:
```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx/ssl.key -out nginx/ssl.crt
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

