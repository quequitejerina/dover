(function(){
    const btnDelete = document.querySelectorAll(".btnDelete")

    btnDelete.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmMessage = confirm('Are you sure you want to delete this entry?');
            if (!confirmMessage){
                e.preventDefault()
            }
        });
    });
})();
