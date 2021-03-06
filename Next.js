const stationsList = document.getElementById('stationsList');
const searchnext = document.getElementById('searchnext');
let hpstation = [];

function all_station() {
    console.log('entering all_station')
    getStyleProp()
    console.log('entering myF.get')
    setStyleProp()
    console.log('entering myF.set')
    searchnext.addEventListener('keyup', (e) => {
        const searchString = e.target.value.toLowerCase();
        
        const filteredstation = hpstation.filter((station) => {
            return (
                station.ARRET.toLowerCase().includes(searchString) 
            );
        });
        displaystation(filteredstation)
    });
    loadstation()
};
    
document.getElementById("nexts").addEventListener("click", all_station);

const loadstation = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/Next');
        hpstation = await res.json();
        displaystation(hpstation);
    } 
    catch (err) {
        console.error(err);
    }
};

const displaystation = (station) => {
    const htmlString = station
        .map((station) => {
            return `
            <p class="charactera">
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


var r = document.querySelector('#searchWrappera');
function getStyleProp(element, property) {
    var rs = getComputedStyle(r);
    alert("The value of searchWrappera is: " + rs.getPropertyValue('display'));
}

function setStyleProp(element, property, value) {
    r.style.setProperty('display', 'block');
}
