document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/ipos/')
        .then(response => response.json())
        .then(data => {
            const ipoData = document.getElementById('ipo-data');
            data.forEach(ipo => {
                ipoData.innerHTML += `
                    <div class="ipo-card">
                        <img src="${ipo.company_logo}" alt="${ipo.company_name}" class="img-fluid">
                        <h3>${ipo.company_name}</h3>
                        <p>Price Band: ${ipo.price_band}</p>
                        <p>IPO Price: ${ipo.ipo_price}</p>
                        <p>Listing Price: ${ipo.listing_price}</p>
                    </div>
                `;
            });
        });
});
