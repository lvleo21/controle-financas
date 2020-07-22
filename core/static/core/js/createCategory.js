const buttonCategory = document.getElementById("buttonCreateCategory")
const buttonClose = document.getElementById("buttonCloseModal")


buttonCategory.onclick = function () {

    let nameCategory = document.getElementById("id_name")
    let errorCategory = document.getElementById("error_category")

    if (nameCategory.value === "") {
        changeInputFocus(false, nameCategory);
        errorCategory.innerHTML = "<li>Este campo é obrigatório</li>"
        errorCategory.style.display = "block"
    }

    else {
        ajaxCreateCategory();
    }
};

buttonClose.onclick = function () {

    let nameCategory = document.getElementById("id_name");
    let errorCategory = document.getElementById("error_category");

    changeInputFocus(true, nameCategory);
    errorCategory.style.display = "none";

}


function ajaxCreateCategory() {
    let formSerializer = $("#formCreateCategory").serialize();
    let message_success = document.getElementById("message_success"); 

    $.ajax({
        type: 'post',
        url: '/create-category/',
        data: formSerializer,

        success: function (data) {

            console.log(data);

            if (data.status == 200){
                var select = document.getElementById("id_category");
                var option = document.createElement('option');

                option.value = data.id;
                option.innerHTML = data.name;
                select.appendChild(option);

                select.value =  option.value;

                $('#adicionar_categoria').modal('hide');
                
                message_success.innerHTML = `Categoria <b>${data.name}</b> criada com sucesso !`;
                $('.alert').alert()
            }

            else{

            }
        }
    });
};



function changeInputFocus(state, input){
    if (state == false){
        input.className = "form-control is-invalid";
        input.focus();
    }

    else{
        input.className = "form-control";
        input.blur();
        input.value = "";

    }

    

}

