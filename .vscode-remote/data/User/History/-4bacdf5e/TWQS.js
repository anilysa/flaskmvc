
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


{% extends "layout.html" %}
{% block title %}Workout App{% endblock %}
{% block page %}Workout App{% endblock %}

{% block content %}
    <!-- Featured Workouts -->
    <section class="featured-workouts">
        <h2>Featured Workouts</h2>

        <!-- Search Bar -->
        <form class="navbar-form" onsubmit="searchExercises(); return false;">
            <input type="text" id="search-input" placeholder="Search for exercises...">
            <button type="submit">Search</button>
        </form>

        <div id="workouts-list" class="workout-card">
            <!-- Displayed after filtering -->
            {% for exercise in exercises %}
                <div class="exercise-card" id="exercise{{ loop.index }}">
                    <h3>{{ exercise['Title'] }}</h3>
                    <p>Description: {{ exercise['Desc'] }}</p>
                    <p>Type: {{ exercise['Type'] }}</p>
                    <p>Body Part: {{ exercise['BodyPart'] }}</p>
                    <p>Equipment: {{ exercise['Equipment'] }}</p>
                    <p>Level: {{ exercise['Level'] }}</p>
                    <p>Rating: {{ exercise['Rating'] }}</p>
                    <p>Rating Description: {{ exercise['RatingDesc'] }}</p>
                </div>
            {% endfor %}
        </div>
    </section>

    <script src="main.js"></script> <!-- Link to main.js -->
{% endblock %}


main();