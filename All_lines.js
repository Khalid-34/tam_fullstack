const lineList = document.getElementById('lineList');
const searchBar = document.getElementById('searchBar');
let hpstation = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredstation = hpstation.filter((station) => {
        return (
            station.LIGNE.toLowerCase().includes(searchString) 
            // LIGNE.LIGNE.DESTINATION.toLowerCase().includes(searchString)
        );
    });
    displaystation(filteredstation);
});

const loadstation = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/All_lines');
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
            <li class="character">
                <h2>${station.LIGNE}</h2>
                <p>Ligne: ${station.ARRET}</p>
                <p>Direction: ${station.DESTINATION}</p>
                <p>Horaire: ${station.HORAIRE}</p>
                
            </li>
        `;
        })
        .join('');
    lineList.innerHTML = htmlString;
};

loadstation();