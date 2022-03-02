let searchbar = document.getElementById('searchbar')

searchbar.addEventListener("input", (e) => {
    let input = searchbar.value.toLowerCase()
    //let badgeData = document.getElementsByClassName('set-or-card-badge')
    let badges = document.querySelectorAll('.set-or-card-badge')
    let badgeData = document.querySelectorAll('.set-or-card-badge .card-header')
    for (i = 0; i < badges.length; i++) {
        if (!badgeData[i].textContent.toLowerCase().startsWith(input)) {
            badges[i].style.display = "none";
        } else {
            badges[i].style.display = "flex";
        }
    }
})


