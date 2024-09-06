document.getElementById('search-button').addEventListener('click', function() {
    var query = document.getElementById('search-query').value;
    if (query) {
        fetch(`/search_results/?query=${encodeURIComponent(query)}`)
            .then(response => response.text())
            .then(data => {
                document.getElementById('search-results').innerHTML = data;
            });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const carousels = document.querySelectorAll('.container-carousel');

    carousels.forEach(function(carouselContainer) {
        const carousel = carouselContainer.querySelector('.carousel');
        const carouselItems = carousel.querySelectorAll('.carousel-item');
        let isMouseDown = false;
        let startX = 0;
        let rotation = 0;
        let rotationOffset = 0;

        const createCarousel = () => {
            const length = carouselItems.length;
            const degrees = 360 / length;
            const gap = 20; // Adjust gap between items as needed
            const tz = distanceZ(carouselContainer.offsetWidth, length, gap);

            carousel.style.width = tz * 2 + gap * length + "px";
            carousel.style.transform = `translateZ(${-tz}px) rotateY(${rotation}deg)`;

            carouselItems.forEach((item, i) => {
                const degreesByItem = degrees * i;
                item.style.transform = `rotateY(${degreesByItem}deg) translateZ(${tz}px)`;
            });
        };

        const distanceZ = (widthElement, length, gap) => {
            return (widthElement / 2) / Math.tan(Math.PI / length) + gap;
        };

        const getMouseX = (e) => {
            return e.clientX || e.touches[0].clientX;
        };

        const handleMouseDown = (e) => {
            isMouseDown = true;
            startX = getMouseX(e);
            rotationOffset = rotation;
        };

        const handleMouseMove = (e) => {
            if (!isMouseDown) return;
            const x = getMouseX(e);
            const diff = (x - startX) * 0.15; // Adjust speed of rotation
            rotation = rotationOffset - diff;
            const tz = distanceZ(carouselContainer.offsetWidth, carouselItems.length, 20);
            carousel.style.transform = `translateZ(${-tz}px) rotateY(${rotation}deg)`;
        };

        const handleMouseUp = () => {
            isMouseDown = false;
        };

        const handleMouseLeave = () => {
            isMouseDown = false;
        };

        const initEvents = () => {
            carousel.addEventListener("mousedown", handleMouseDown);
            carousel.addEventListener("mousemove", handleMouseMove);
            carousel.addEventListener("mouseup", handleMouseUp);
            carousel.addEventListener("mouseleave", handleMouseLeave);

            carousel.addEventListener("touchstart", (e) => {
                handleMouseDown(e.touches[0]);
            });

            carousel.addEventListener("touchmove", (e) => {
                handleMouseMove(e.touches[0]);
            });

            carousel.addEventListener("touchend", handleMouseUp);

            window.addEventListener("resize", createCarousel);

            createCarousel();
        };

        initEvents();

        // Optionally handle carousel navigation or item activation
        let currentItem = 0;

        function showItem(index) {
            carouselItems.forEach((item, i) => {
                item.classList.toggle('active', i === index);
            });
        }

        // Initialize the first item as active
        showItem(currentItem);

        // Navigation logic (if needed) can go here
    });
});



