function init(){
    console.log('checker1');

    if (!localStorage.getItem('key')){
        location.href="registration";
    }

    $('#form_checker1').submit(function(event){
        event.preventDefault();
        
        const key = localStorage.getItem('key');
        const project_id = $('#project_id').val();
        console.log(project_id)
        if(!project_id){
            return;
        }

        console.log(key);
        console.log(project_id);
        
        const data = {
            'project_id' : project_id,
            'auth_token' : key
        }

        $.ajax({
            'url':'http://192.168.33.12:5000/api/v1/project',
            'method':'POST',
            'contentType':'application/json',
            'data': JSON.stringify(data),
        }).done(function(data){
            console.log(data);

            localStorage.setItem('project', JSON.stringify(data));

            location.href="tasks"
        })
    })
}

$(document).ready(init);
