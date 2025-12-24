const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
document.addEventListener('DOMContentLoaded', function () {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});
