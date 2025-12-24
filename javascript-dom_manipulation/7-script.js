const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(url)
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    for (const movie of movies) {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      document.querySelector('#list_movies').appendChild(listItem);
    }
  });
