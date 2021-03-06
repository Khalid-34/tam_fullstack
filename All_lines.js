const linesList = document.getElementById('linesList');
const searchall = document.getElementById('searchall');
let hpsline = [];

searchall.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredline = hpsline.filter((line) => {
        return (
            line.ARRET.toLowerCase().includes(searchString) 
        );
    });
    displayline(filteredline);
});

const loadline = async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/All_lines');
        hpsline = await res.json();
        displayline(hpsline);
    } 
    catch (err) {
        console.error(err);
    }
};

const displayline = (line) => {
    const htmlString = line
        .map((line) => {
            return `
            <p class="character">
                <h2>${line.LIGNE}</h2>
                <p id="lines">
                    <sub id="line">Ligne</sub>${line.ARRET}
                    <sub id="dest">Direction</sub>${line.DESTINATION}
                    <sub id="horaire">Horaire</sub>${line.HORAIRE}
                </p>
            </p>
        `;
        })
        .join('');
    linesList.innerHTML = htmlString;
};

loadline();