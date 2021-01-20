const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/predict', {
        method: 'post',
        body: formData
    }).then(function(response) {
        return response.text();
    }).then(function(text) {
        console.log(text);
        document.getElementById('prediction-text-id').innerHTML = text;
        if (text.startsWith('Bwawhhh!')) {
            try {
                document.getElementById('prediction-text-id').classList.remove('prediction-text-good');
            } catch (e) {
                console.log(e);
            }
            document.getElementById('prediction-text-id').classList.add('prediction-text-bad')
        } else {
            try {
                document.getElementById('prediction-text-id').classList.remove('prediction-text-bad');
            } catch (e) {
                console.log(e);
            }
            document.getElementById('prediction-text-id').classList.add('prediction-text-good')
        }
    }).catch(function(err) {
        console.error(err);
    });
});