document.addEventListener('DOMContentLoaded', (event) => {
    var element = document.querySelector('.small-image')

    if (element === null) {
        console.log('no such element!');
        return;
    }
    
    element.addEventListener('click', function() {
        var overlay = document.createElement('div');
        overlay.classList.add('overlay');
        var overlayContent = document.createElement('div');
        overlayContent.classList.add('overlay-content');
        var largeImage = document.createElement('img');
        largeImage.src = 'path_to_your_large_image.jpg'; // The path to the larger version of the image
        largeImage.alt = 'Image description';
        overlayContent.appendChild(largeImage);
        overlay.appendChild(overlayContent);
        document.body.appendChild(overlay);
        overlay.addEventListener('click', function() {
            overlay.remove();
        });
    });
});
