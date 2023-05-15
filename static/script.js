const form = document.querySelector('form');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    const inputList = document.getElementById('input_list').value;
    const formData = new FormData();
    formData.append('input_list', inputList);

    fetch('/recommend', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Limpa os resultados anteriores
        resultsDiv.innerHTML = '';

        // Exibe os títulos dos filmes inseridos
        const movieTitles = data.movie_titles;
        const movieTitlesElement = document.createElement('p');
        movieTitlesElement.textContent = 'Valores inseridos pelo usuário: ' + movieTitles.join(', ');
        resultsDiv.appendChild(movieTitlesElement);

        // Exibe a tabela HTML com os resultados
        const tabelaHtml = data.tabela_html;
        resultsDiv.innerHTML += tabelaHtml;
    })
    .catch(error => {
        console.error('Ocorreu um erro:', error);
    });
});

// Alternar o dark-mode quando o botão for clicado
const toggleButton = document.getElementById('toggle-dark-mode');

toggleButton.addEventListener('click', function() {
    document.documentElement.classList.toggle('dark-mode');
});
