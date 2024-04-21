
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}


function searchExercises() {
    var query = document.getElementById('search-input').value.trim().toLowerCase();

    const exerciseCards = document.querySelectorAll('.exercise-card');
    exerciseCards.forEach(card => {
        const title = card.querySelector('h3').innerText.toLowerCase();
        const description = card.querySelector('p:nth-child(2)').innerText.toLowerCase();
        const type = card.querySelector('p:nth-child(3)').innerText.toLowerCase();
        const bodyPart = card.querySelector('p:nth-child(4)').innerText.toLowerCase();
        const equipment = card.querySelector('p:nth-child(5)').innerText.toLowerCase();
        const level = card.querySelector('p:nth-child(6)').innerText.toLowerCase();
        const rating = card.querySelector('p:nth-child(7)').innerText.toLowerCase();
        const ratingDesc = card.querySelector('p:nth-child(8)').innerText.toLowerCase();

        if (
            title.includes(query) ||
            description.includes(query) ||
            type.includes(query) ||
            bodyPart.includes(query) ||
            equipment.includes(query) ||
            level.includes(query) ||
            rating.includes(query) ||
            ratingDesc.includes(query)
        ) {
            card.style.display = 'block'; // Show the card if it matches the query
        } else {
            card.style.display = 'none'; // Hide the card if it doesn't match the query
        }
    });
}


main();