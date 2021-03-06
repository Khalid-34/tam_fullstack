const travelsList = document.getElementById('travel');
const searchone = document.getElementById('searchone');
let hpstravel = [];

function ftravel() {
    console.log('entering travel')
    getStyleProp()
    console.log('entering myF.get')
    setStyleProp()
    console.log('entering myF.set')
    searchone.addEventListener('keyup', (e) => {
        const searchString = e.target.value.toLowerCase();
        
        const filteredtravel = hpstravel.filter((travel) => {
            return (
                travel.ARRET.toLowerCase().includes(searchString) 
            );
        });
        displaytravel(filteredtravel);
    });
    loadtravel()
};
    
    document.getElementById("prochain").addEventListener("click", ftravel);

const loadtravel = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/prochain');
    hpstravel = await res.json();
        displaytravel(hpstravel);
    } 
    catch (err) {
        console.error(err);
    }
};

const displaytravel = (travel) => {
    const htmlString = travel
        .map((travel) => {
            return `
            <li class="characterb">
                <h2>${travel.ARRET}</h2>
                <p>Ligne: ${travel.ARRET}</p>
                <p>Direction: ${travel.DESTINATION}</p>
                <p>Horaire: ${travel.HORAIRE}</p>
                
            </li>
        `;
        })
        .join('');
    travelsList.innerHTML = htmlString;
};


var r = document.querySelector('#searchWrapperb');
function getStyleProp(element, property) {
    var rs = getComputedStyle(r);
    alert("The value of searchWrapperb is: " + rs.getPropertyValue('display'));
}

function setStyleProp(element, property, value) {
    r.style.setProperty('display', 'block');
}
