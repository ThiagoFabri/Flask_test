#ARQUIVO PYTHON PARA LER A PLANILHA FILMES E A INTELIGENCIA ARTIFICIAL E RETORNAR PARA O HTML A TABELA
#OBSERVAÇÃO ESTOU USANDO FLASK PARA EXECUTAR E CONECTAR O PYTHON COM O HTML(FLASK É UMA BIBLIOTECA PARECIDA COM O DJANGO)
import pandas as pd
from fuzzywuzzy import fuzz, process
import pickle
from flask import Flask, render_template, request, jsonify, Markup
import zipfile
import io

app = Flask(__name__, template_folder='templates')  # ISSO SERVE PARA CONECTAR AONDE ESTÁ O INDEX DO HTML

def get_recommendations_all(title_list, cosine_sim):
    # FUNÇÃO PARA FAZER A RECOMENDAÇÃO ELA PRECISA DO TITULO(S) DO(S) FILME(S), indices(DENTRO DO pickle), cosine_sim(DENTRO DO pickle)
    indices_list = [indices[title] for title in title_list]

    # Get the pairwise similarity scores of all movies with the input movies
    sim_scores = cosine_sim[indices_list].mean(axis=0)

    # Get the indices of the top most similar movies
    top_indices = sorted(range(len(sim_scores)), key=lambda i: sim_scores[i], reverse=True)#VER OS TOP 10 SORTED PARA PEGAR AS MELHORES NOTAS
    top_indices = [i for i in top_indices if i not in indices_list][:10]

    # Retorna uma lista de tuplas contendo o título
    return [(df2['title'].iloc[i], round(sim_scores[i], 2)) for i in top_indices]

def get_movie_title(input_title):#FUNÇÃO PARA TRATAR O INPUT DO USUARIO, CASO O USUARIO INSIRA UM FILME ERRONIAMENTE O CODIGO PEGARÁ OQUE FOR MAIS PARECIDO(UMA OUTRA COLUÇÃO SERIA FAZER UMA LISTA COM UM INPUT CONTAINS QUE DE AS OPÇÕES QUE TEMOS)
    # Ler dados de filmes do seu conjunto de dados aqui
    movies = df2['title']

    # Use o process.extract() para procurar correspondências com base na entrada do usuário
    matches = process.extract(input_title, movies, scorer=fuzz.token_sort_ratio)

    # Obter a correspondência com maior pontuação
    best_match = max(matches, key=lambda x: x[1])

    # Se a pontuação for menor que 50, retorne None
    if best_match[1] < 50:
        return None

    # Caso contrário, retorne o título do filme correspondente
    return best_match[0]#RETORNA O MAIS PARECIDO

# Carregar os dados dos Filmes que temos e que peguei no Kaggle(que veio completo, porem com pouca informação, e pouca especificação oque acaba afetando na precissão da IA)
df2 = pd.read_excel("Filmes.xlsx")
# # BAIXAR O QUE TEM NO PICKLE
# with open('data.pkl', 'rb') as f:#para quem não sabe o pickle é uma biblioteca que armazena em um unico arquivo variaveis do codigos antigos
#     data = pickle.load(f)
#     cosine_sim2 = data['cosine_sim']#pegando o cosine de similaridade a IA usada
#     indices = data['indices']#pegando o indice da IA uma tabela usada para o calculo do coseno de similaridade

# Carrega o arquivo zip
with open('data.zip', 'rb') as f:
    zip_data = f.read()

# Cria um objeto BytesIO a partir dos dados do arquivo zip
zipfile_obj = io.BytesIO(zip_data)

# Abre o arquivo zip usando a classe ZipFile
with zipfile.ZipFile(zipfile_obj, 'r') as zipf:
    # Lê o conteúdo do arquivo pickle diretamente do zip
    with zipf.open('data.pkl', 'r') as pickle_file:
        # Carrega as variáveis do arquivo pickle
        data = pickle.load(pickle_file)
        cosine_sim2 = data['cosine_sim']
        indices = data['indices']

@app.route('/')# conectar o app.py com o index.html
def index():
    return render_template('index.html')# renderizar isso é especifo do Flask caso usemos algo diferente teremos que mudar o Flask, mas acredito que o github tenha o Flask

@app.route('/recommend', methods=['POST'])# esse recommend o POST action que o html precisa pois ele faz uma requisição post para pegar informações do app.py e do javascript
def recommend():
    input_list = request.form['input_list'].split(',') # dividindo oque o usuario colocou por virgula para colocar em uma array no movie_tittles

    movie_titles = []#criada para ter os valores inputados pelo usuario
    for title in input_list:
        movie_title = get_movie_title(title.strip())
        if movie_title is not None:
            movie_titles.append(movie_title)

    resultado = get_recommendations_all(movie_titles, cosine_sim2)# usando a função get_recommendations_all que expliquei acima, retorna uma tupla com os valores top 10 recomendations e sua porcentagem

    # Criar um DataFrame pandas com os resultados
    df_resultado = pd.DataFrame(resultado, columns=['Movie Title', 'Similarity Score'])# tupla para dataframe(dataframe é uma tabela como se fosse o excel)

    # Converter o DataFrame em uma tabela HTML
    tabela_html = df_resultado.to_html(index=False)# o pandas(planilha) tem uma função para exportar um html

    # Retornar os títulos dos filmes inseridos e a tabela HTML
    return jsonify({
        'movie_titles': movie_titles,
        'tabela_html': tabela_html
    })

if __name__ == '__main__':
    app.run()