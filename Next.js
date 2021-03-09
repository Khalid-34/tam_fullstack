const stationsList = document.getElementById('stationsList');
const searchBar = document.getElementById('searchBar');
let hpstation = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredstation = hpstation.filter((station) => {
        return (
            station.ARRET.toLowerCase().includes(searchString) 
            // LIGNE.LIGNE.DESTINATION.toLowerCase().includes(searchString)
        );
    });
    displaystation(filteredstation);
});

const loadstation = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/Next');
        hpstation = await res.json();
        displaystation(hpstation);
    } catch (err) {
        console.error(err);
    }
};

const displaystation = (station) => {
    const htmlString = station
        .map((station) => {
            return `
            <p class="character">
                <h2>${station.ARRET}</h2>
                <p id="lines">
                    <sub id="ligne">Ligne</sub>${station.LIGNE}
                    <sub id="dest">Direction</sub>${station.DESTINATION}
                    <sub id="horaire">Horaire</sub>${station.HORAIRE}
                </p>
            </p>
        `;
        })
        .join('');
    stationsList.innerHTML = htmlString;
};

loadstation();