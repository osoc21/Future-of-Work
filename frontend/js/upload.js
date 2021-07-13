// Define processing URL and form element

const form = document.querySelector('form');

// Listen for form submit
form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    const files = document.querySelector('[type=file]').files;
    const formData = new FormData();

  for (let i = 0; i < files.length; i++) {
    let file = files[i];

        formData.append('Population', file)
        formData.append('Attrition', file)
        formData.append('Retirement', file)
    }

  fetch('http://localhost:4000/API/upload', {
    method: 'POST',
    body: formData
  })
    .then((response) => {
      console.log(response);
    })
        .then((response) => {
            console.log(response)
        })
        .catch(err => console.error(err))
});
