let allCards = document.querySelectorAll('.card')

let allStatusButtons = document.querySelectorAll('.status-button');

allStatusButtons.forEach( (button) => {
    button.addEventListener('click',updateStatus)
})

let statuses = {
    "owned": {
        symbol: "✔️",
        class: "owned-button",
        classColor: "btn-success"
    },
    "not-owned": {
        symbol: "❌",
        class: "not-owned-button",
        classColor: "btn-danger"
    },
    "grailed": {
        symbol: "👑",
        class: "grailed-button",
        classColor: "btn-warning"
    }
}

function updateStatus() {
    let buttonStatus = this.classList
    let cardID = this.parentNode.parentNode.parentNode.id

    if (this.classList.contains('not-owned-button')) {
        buttonStatus.replace(statuses["not-owned"].class, statuses["owned"].class)
        buttonStatus.replace(statuses["not-owned"].classColor, statuses["owned"].classColor)
        this.innerText = statuses["owned"].symbol
        $.post("/update_db", {card_id: cardID, status:"owned"})
    } else if (this.classList.contains('owned-button')) {
        buttonStatus.replace(statuses["owned"].class, statuses["grailed"].class)
        buttonStatus.replace(statuses["owned"].classColor, statuses["grailed"].classColor)
        this.innerText = statuses["grailed"].symbol
        $.post("/update_db", {card_id: cardID, status:"grailed"})
    } else if (this.classList.contains('grailed-button')) {
        buttonStatus.replace(statuses["grailed"].class, statuses["not-owned"].class)
        buttonStatus.replace(statuses["grailed"].classColor, statuses["not-owned"].classColor)
        this.innerText = statuses["not-owned"].symbol
        $.post("/update_db", {card_id: cardID, status:"not-owned"})
    } 

}