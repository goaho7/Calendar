const group = document.getElementById('id_group');
const add_sets = document.getElementsByClassName('add_set');
const del_sets = document.getElementsByClassName('del_set');
const sets = document.getElementsByClassName('sets');

group.onchange = function(e){
    e.preventDefault();
    $.ajax({
        url: '',
        type: 'post',
        data: {'group': this.value},
        success: function(data) {
            $('#id_name_exercise').replaceWith($('#id_name_exercise',data));
        }
    })
}

for (let add_set of add_sets) {
    add_set.addEventListener('click', function(e) {
        $('.set').last().clone().appendTo($('.sets'));
        for (let del_set of del_sets) {
            del_set.addEventListener('click', function(e) {
                console.log(1)
                if($('.sets').find('.set').length > 1) {
                    del_set.parentNode.remove();
                }
            });
        }
    });
}
