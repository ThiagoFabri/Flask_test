# IA de recomendação de Filmes
A Inteligência Artificial(IA) tem com o objetivo é mostrar o funcionamento do cosseno de similaridade que será no produto da empresa sem a necessidade do usuário inserir algo, porém como estamos construindo um site para melhorar o marketing da empresa, e uma demonstração seria o ideal para isso, pensando nisso a Crigma pensou em criar uma IA básica para isso.
No projeto de demonstração, o cosseno de similaridade é utilizado para medir o quão semelhantes são os filmes com base em seus atributos. O algoritmo compara os filmes inseridos pelo usuário com uma matriz de similaridade previamente calculada. Em seguida, os filmes com as maiores similaridades são selecionados e retornados como recomendações. O objetivo é fornecer ao usuário uma lista de filmes similares aos que ele inseriu, com base em características como gênero, elenco, diretor e avaliação do filme.
A base de dados é muito importante para o resultado final do projeto, o cosseno de similaridade é uma faca de dois gumes, quanto mais detalhes você colocar mais preciso ele será porém, maior a base de dados será requisitado já que a porcentagem de similaridade será afetada.
No projeto usamos uma Base de Dados pequena encontrada no Kaggle com 5 mil filmes, muito abaixo do que realmente existe, e consequentemente não pudemos colocar informações mais específicas dos gêneros oque seria essencial no futuro da empresa. Mas qual seria o efeito disso?
O efeito seria que filmes, por exemplo, de dark-comedy não seriam diferenciados dos comedy’s comuns, outro exemplo seria a idade classificatória que não estava disponível no Dataframe(Planilha). Mesmo assim, este é o Dataframe mais completo em relação a cast(elenco), gênero, rating, data de criação etc que levamos em consideração e o resultado foi satisfatório, basicamente para melhorar o modelo apenas incluindo mais linhas e mais colunas mencionadas acima.
A IA irá mostrar filmes parecidos baseado nas colunas do nosso banco de dados usamos para esse cálculo de similaridade os três principais nomes do cast(elenco), o nome do diretor, as keywords(palavras chaves), o gênero, uma classificação de filmes mais recentes, e uma classificação baseada na média da nota do imdb, como é possível ver abaixo
![image](https://github.com/ThiagoFabri/Flask_test/assets/91853113/fadca3e5-0fab-47cd-b918-46f55303b093)

 É possível observar a estrutura da base, que usa a classificação ano de lançamento, como argumentos mais fracos em comparação ao gênero e keywords usando o cosseno de similaridade.
No final é colocando isso em um site para a elaboração do protótipo o usuário irá usar essa IA no site de marketing como uma demonstração(demo)  para uma campanha, por isso nesse caso não iremos usar o histórico do usuário baseado em outras plataformas.
Com isso esclarecido o usuário deverá inserir o nome(s) do(s) filme(s) que viu e receberá uma recomendações baseadas nesse(s) nome(s). Além disso a IA mostrará a porcentagem de similaridade baseadas nas colunas acima como é possível ver na imagem abaixo:
![image](https://github.com/ThiagoFabri/Flask_test/assets/91853113/821c66bc-bb17-48c4-a91b-16489d79d00f)

Como é possível observar mesmo se o usuário escrever o nome de forma incorreta também usamos outra inteligência para conseguir buscar o nome mais similar que existe no nosso banco de dados
![image](https://github.com/ThiagoFabri/Flask_test/assets/91853113/7a1313d6-10b4-429f-97c6-b45ad203d7bf)


Referências
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata - Base de Dados

