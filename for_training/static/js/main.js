let exercise_form = document.querySelector('.exercise-form')
let add_exercise = document.querySelector('#add-exercise');
let container = document.querySelector("#form-container")
let totalForms = document.querySelector("#id_exercises-TOTAL_FORMS")

let formNum = 0


add_exercise.addEventListener('click', addForm)
function addForm(e) {
    e.preventDefault()
    let newForm = exercise_form.cloneNode(true);
    console.log(newForm)
    let formRegex = RegExp(`exercises-(\\d){1}-`,'g') 
    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `exercises-${formNum}-`)
    container.insertBefore(newForm, add_exercise)
    totalForms.setAttribute('value', `${formNum+1}`)
}




/* group.onchange = function(e){
    e.preventDefault();
    $.ajax({
        url: '',
        type: 'post',
        data: {'group': this.value},
        success: function(data) {
            $('#id_name_exercise').replaceWith($('#id_name_exercise',data));
        }
    })
} */

/* for (let add_set of add_sets) {
    add_set.addEventListener('click', function(e) {
        $('.set').last().clone().appendTo($('.sets'));
        let parent_set = $(this).parent().find('.sets ')
        console.log(parent_set)
        for (let del_set of del_sets) {
            del_set.addEventListener('click', function(e) {
                if($('.sets').find('.set').length > 1) {
                    del_set.parentNode.parentNode.remove();
                }
            });
        }
    });
} */


/* 
$('#add-exercise').click(function() {
    $('.exercises').append(block_exercise.clone());
    let x = 1
    for (let number of exercise_number) {
        number.innerText = x;
        x++;
        for (let add_set of add_sets) {
            add_set.addEventListener('click', add_s)
        }
    };   
});


for (let add_set of add_sets) {
    add_set.addEventListener('click', add_s)
      
} 


function add_s(){
    $(this).parent().find('.sets ').append(block_set.clone());
    for (let del_set of del_sets) {
        del_set.addEventListener('click', del_s)
    }
}


function del_s(){
    if($(this).parent().parent().parent().find('.set').length > 1) {
        $(this).parent().parent().remove();
    }
} */

/* Добавить упражнение */
/* let form_total = 0
add_exercise.onclick = function(e){
    e.preventDefault();
    console.log(form_total)
    $.ajax({
        url: '',
        type: 'post',
        data: {'form_total': ++form_total},
        success: function(data) {
            
        }
    })
} */
/* console.log($('#exercises').find('.exercise ').last()) */

