const form = document.getElementById('uploadForm');
const statusDiv = document.getElementById('status');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById('resume');
  const file = fileInput.files[0];

  if (!file) {
    statusDiv.textContent = "Please select a file.";
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch('https://22rb9lj5mj.execute-api.ap-south-1.amazonaws.com/Dev/main', {
      method: 'POST',
      body: formData,
    });

    const result = await response.json();

    if (response.ok) {
      statusDiv.style.color = 'green';
      statusDiv.innerHTML = `<strong>✅ Success:</strong> ${result.message}<br><br>`;

      const parsed = result.parsed;
      if (parsed) {
        statusDiv.innerHTML += `<strong>Name:</strong> ${parsed.name}<br>`;
        statusDiv.innerHTML += `<strong>Email:</strong> ${parsed.email}<br>`;
        statusDiv.innerHTML += `<strong>Phone:</strong> ${parsed.phone}<br><br>`;

        const sections = parsed.sections || {};
        for (const section in sections) {
          statusDiv.innerHTML += `<strong>${section}:</strong><br><pre>${sections[section]}</pre><br>`;
        }
      }
    } else {
      statusDiv.style.color = 'red';
      statusDiv.textContent = `❌ Error: ${result.error || "Upload failed."}`;
    }

  } catch (error) {
    console.error(error);
    statusDiv.style.color = 'red';
    statusDiv.textContent = "❌ Upload failed. Check console.";
  }
});
