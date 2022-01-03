let searchbar = document.getElementById('home-set-search')

searchbar.addEventListener("input", (e) => {
    let input = searchbar.value
    let setItems = document.getElementsByClassName('home-set-card')
    for (i = 0; i < setItems.length; i++) {
        if (!setItems[i].id.toLowerCase().includes(input)) {
            setItems[i].style.display = "none";
        } else {
            setItems[i].style.display = "flex";
        }
    }
})


