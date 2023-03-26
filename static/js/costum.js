document.querySelector('.file-input').addEventListener('change', function(e) {
    document.getElementById('filename').textContent = e.target.files[0].name;
  });
  