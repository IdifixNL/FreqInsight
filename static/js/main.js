document.addEventListener("DOMContentLoaded", function() {
  const configForm = document.getElementById("config-form");
  configForm.addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData(configForm);
    const data = {};

    for (const [key, value] of formData.entries()) {
      data[key] = value;
    }

    fetch('/profile/', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
      alert('Configuration saved successfully!');
    })
    .catch(error => {
      console.error('Error submitting form:', error);
      alert('Error submitting form: ' + error.message);
    });
  });
});
