const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const imageDelete = document.querySelectorAll('#image_delete')

imageDelete.forEach((elem) => {
  elem.addEventListener('click', (event)=>{
    event.preventDefault()

    axios({
      method: 'POST',
      url: `/portfolios/image/${elem.dataset.pk}/delete/`,
      headers: {'X-CSRFToken': csrftoken}
    })
    .then((re)=>{console.log(re)
      const imageName = document.querySelector(`#i${elem.dataset.pk}`)
      imageName.remove()
      elem.remove()
    })          
    .catch((e)=>{console.log(e)})

  })
})
