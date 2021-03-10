const LineList = document.getElementById('LineList');
const searchall = document.getElementById('searchall');
let hpslines = [];

function all_line() {
    console.log('entering all_line')
    getStyleProp()
    console.log('entering myF.get')
    setStyleProp()
    console.log('entering myF.set')
    searchall.addEventListener('keyup', (e) => {
        const searchString = e.target.value.toLowerCase();

        const filteredligne = hpslines.filter((ligne) => {
            return (
                ligne.LIGNE.toLowerCase().includes(searchString) 
            );
        });
    displayligne(filteredligne);
    });
};

document.getElementById("all").addEventListener("click", all_line);

const loadligne = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/All_lines');
        hpslines = await res.json();
        displayligne(hpslines);
    } 
    catch (err) {
        console.error(err);
    }
};

const displayligne = (ligne) => {
    const htmlString = ligne
        .map((ligne) => {
            return `
            <li class="charactera">
                <h2>${ligne.LIGNE}</h2>
                <p>Ligne: ${ligne.ARRET}</p>
                <p>Direction: ${ligne.DESTINATION}</p>
                <p>Horaire: ${ligne.HORAIRE}</p>
                
            </li>
        `;
        })
        .join('');
    LineList.innerHTML = htmlString;
};

loadligne();

var r = document.querySelector('#searchWrapper');
function getStyleProp(element, property) {
    var rs = getComputedStyle(r);
    alert("The value of searchWrapper is: " + rs.getPropertyValue('display'));
}

function setStyleProp(element, property, value) {
    r.style.setProperty('display', 'block');
}
