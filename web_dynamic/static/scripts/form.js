function init(){
    console.log('init')
    $('#form_login').submit(function(event){
        event.preventDefault();
        const cod = $('#code_hb').val();
        const api = $('#api_key').val();
        const pwd = $('#pwd').val();

        if (!cod && !api && !pwd){
            return;
        }

        console.log(cod);
        console.log(api);
        console.log(pwd);
        
        data = {
            'api_key': api,
            'code_id': cod,
            'password': pwd,
        };

        $.ajax({
            'url':'http://192.168.33.12:5000/api/v1/auth',
            'method':'POST',
            'data': JSON.stringify(data),
            'contentType':'application/json'
        })
        .done(function(data){
            console.log(data);
            localStorage.setItem('key', data.auth_token);
            location.href = "project"
        })
    })    
}
$(document).ready(init);
