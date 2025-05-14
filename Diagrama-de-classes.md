# metflix

classDiagram
    class Usuario {
        +String username
        +String email
        +String password
    }
    
    class SuperUsuario {
        +adicionarJogo(nome: String, ano: int, preco: float)
        +adicionarFilmeSerie(nome: String, ano: int, genero: String, categoria: String)
        +editarJogo(jogo_id: int, nome: String, ano: int, preco: float)
        +editarFilmeSerie(filme_serie_id: int, nome: String, ano: int, genero: String, categoria: String)
        +removerJogo(jogo_id: int)
        +removerFilmeSerie(filme_serie_id: int)
    }
    
    class Jogo {
        +String nome
        +int data_lancamento
        +float preco
    }
    
    class FilmeSerie {
        +String nome
        +int data_lancamento
        +String genero
        +String categoria
    }

    class UsuarioJogo {
        +int usuario_id
        +int jogo_id
    }
    
    class UsuarioFilmeSerie {
        +int usuario_id
        +int filme_serie_id
    }

    Usuario <|-- SuperUsuario : herda
    Usuario "1" -- "0..*" UsuarioJogo : possui
    Jogo "1" -- "0..*" UsuarioJogo : adquirido por
    Usuario "1" -- "0..*" UsuarioFilmeSerie : assiste
    FilmeSerie "1" -- "0..*" UsuarioFilmeSerie : assistido por


1. Classe Usuario

Atributos:

    username: Nome de usuário único que identifica o usuário no sistema.

    email: E-mail do usuário, usado para login e comunicação.

    password: Senha do usuário, que é necessária para autenticação.

Relações:

    Um Usuário pode ter vários Jogos (relacionamento muitos para muitos), o que é representado pela classe intermediária UsuarioJogo.

    Um Usuário pode assistir a vários Filmes/Séries (relacionamento muitos para muitos), o que é representado pela classe intermediária UsuarioFilmeSerie.

2. Classe SuperUsuario

Herança:

    SuperUsuario herda de Usuario, ou seja, ele tem todos os atributos e comportamentos de um Usuario (como username, email, password), mas com permissões adicionais.

Métodos:

    adicionarJogo(): Permite que o SuperUsuario cadastre um novo jogo no sistema, fornecendo o nome, ano de lançamento e preço.

    adicionarFilmeSerie(): Permite que o SuperUsuario cadastre um novo filme ou série no sistema, fornecendo o nome, ano de lançamento, gênero e categoria.

    editarJogo(): Permite que o SuperUsuario edite um jogo existente, passando o ID do jogo e novos dados como nome, ano de lançamento e preço.

    editarFilmeSerie(): Permite que o SuperUsuario edite um filme/série existente, passando o ID do filme/série e novos dados como nome, ano de lançamento, gênero e categoria.

    removerJogo(): Permite que o SuperUsuario remova um jogo do sistema, passando o ID do jogo.

    removerFilmeSerie(): Permite que o SuperUsuario remova um filme/série do sistema, passando o ID do filme/série.

Relações:

    A classe SuperUsuario herda as funcionalidades da classe Usuario, mas com permissões extras para gerenciar o conteúdo do sistema (cadastrar, editar e remover jogos e filmes/séries).

3. Classe Jogo

Atributos:

    nome: O nome do jogo.

    data_lancamento: O ano de lançamento do jogo.

    preco: O preço do jogo.

Relações:

    O Jogo pode ser adquirido por vários Usuários. O relacionamento muitos para muitos entre Jogo e Usuario é representado pela tabela intermediária UsuarioJogo.

    Cada Jogo pode ter muitos Usuários que o adquiriram, e cada Usuário pode ter vários Jogos adquiridos.

4. Classe FilmeSerie

Atributos:

    nome: O nome do filme ou série.

    data_lancamento: O ano de lançamento do filme ou série.

    genero: O gênero do filme ou série (ex: ação, comédia, drama).

    categoria: A categoria do filme ou série (ex: longa-metragem, minissérie, etc.).

Relações:

    O Filme/Série pode ser assistido por vários Usuários. O relacionamento muitos para muitos entre FilmeSerie e Usuario é representado pela tabela intermediária UsuarioFilmeSerie.

    Cada Filme/Série pode ser assistido por vários Usuários, e cada Usuário pode assistir a vários Filmes/Séries.

5. Classe UsuarioJogo (Tabela Intermediária)

Atributos:

    usuario_id: ID do Usuário que adquiriu o jogo.

    jogo_id: ID do Jogo adquirido pelo Usuário.

Relações:

    Representa a relação muitos para muitos entre Usuário e Jogo. Cada Usuário pode ter muitos Jogos e cada Jogo pode ser adquirido por vários Usuários.

6. Classe UsuarioFilmeSerie (Tabela Intermediária)

Atributos:

    usuario_id: ID do Usuário que assistiu ao filme/série.

    filme_serie_id: ID do Filme/Série assistido pelo Usuário.

Relações:

    Representa a relação muitos para muitos entre Usuário e Filme/Série. Cada Usuário pode assistir a muitos Filmes/Séries e cada Filme/Série pode ser assistido por vários Usuários.

Resumo do Diagrama:

    Usuário é a classe base que representa os usuários do sistema. Cada Usuário pode possuir vários Jogos e assistir a vários Filmes/Séries.

    SuperUsuario é uma subclasse de Usuario com permissões extras para adicionar, editar e remover Jogos e Filmes/Séries.

    Jogo e Filme/Série representam os itens que os Usuários interagem com, podendo adquirir ou assistir, respectivamente.

    UsuarioJogo e UsuarioFilmeSerie são tabelas intermediárias que gerenciam os relacionamentos muitos para muitos entre Usuários e Jogos ou Filmes/Séries.
