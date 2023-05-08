function showInterest(evt, id) {
    fetch(window.location.origin + "/services/interest", {
        method: "POST",
        body: JSON.stringify({
            serviceId: id,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then((response) => console.log(response));

    evt.srcElement.classList.remove('bookmark-icon')
    evt.srcElement.classList.add('bookmark-icon-red')
}