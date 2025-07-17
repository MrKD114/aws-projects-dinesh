const API_URL = 'https://lg0cj9zjm1.execute-api.ap-south-1.amazonaws.com/Dev/feedback';

document.getElementById('feedback-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const message = document.getElementById('message').value.trim();

  if (!name || !message) return alert("Please fill in both fields!");

  const response = await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, message })
  });

  const result = await response.json();
  alert(result.message || result.error);

  document.getElementById('name').value = '';
  document.getElementById('message').value = '';
  loadFeedback(); // refresh list
});

document.getElementById('refresh').addEventListener('click', loadFeedback);

async function loadFeedback() {
  const response = await fetch(API_URL);
  const feedbacks = await response.json();

  const list = document.getElementById('feedback-list');
  list.innerHTML = '';

  feedbacks.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  feedbacks.forEach(fb => {
    const div = document.createElement('div');
    div.className = 'feedback-item';
    div.innerHTML = `
      <strong>${fb.name}</strong>
      <small>${new Date(fb.timestamp).toLocaleString()}</small>
      <p>${fb.message}</p>
    `;
    list.appendChild(div);
  });
}

loadFeedback(); // auto-load on page load
