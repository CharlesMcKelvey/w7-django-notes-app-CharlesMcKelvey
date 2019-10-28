document.querySelectorAll('delete').addEventListener('click', event => {
    event.preventDefault()

})

document.querySelectorAll('edit').addEventListener('click', event => {
    event.preventDefault()

})

anime({
    targets: '.note',
    rotate: '1turn',
    easing: 'easeInOutCubic',
    autoplay: true,
})