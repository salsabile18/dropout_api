document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('upload-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Empêcher le formulaire de se soumettre normalement

        let formData = new FormData();
        formData.append('file', document.getElementById('file-input').files[0]);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors de la requête Fetch');
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

function displayResults(data) {
    let resultsDiv = document.getElementById('results-prediction');
    resultsDiv.innerHTML = '<h2>Résultats de la prédiction</h2>';

    let table = '<table><tr><th>ID</th><th>Prédiction</th><th>Probabilité</th><th>Commentaire</th></tr>';
    data.forEach((prediction, index) => {
        let id = index + 1; // Commencer l'ID à partir de 1
        let comment;
        let probability = prediction.probability; // Définir la variable probability
        if (probability >= 0 && probability < 0.10) {
            comment = 'Null';
        } else if (probability >= 0.10 && probability < 0.40) {
            comment = 'Faible';
        } else if (probability >= 0.40 && probability < 0.70) {
            comment = 'Probabilité importante de décrochage';
        } else {
            comment = 'Probabilité élevée de décrochage';
        }
        table += `<tr><td>${id}</td><td>${prediction.prediction}</td><td>${probability}</td><td>${comment}</td></tr>`;
    });
    table += '</table>';

    resultsDiv.innerHTML += table;
    console.log("Données reçues:", data);
}
