function render(d){
    const html = ['<div>',
    '<h2>'+d.title+'</h2>',
    '<div class="btn">'+d.id+'</div>',
    '</div>']

    return html.join('');
}


function init(){
    const project = JSON.parse(localStorage.getItem('project'))

    $('#name').text(project.name)

    //console.log(project.tasks);
    project.tasks.forEach(function(values){
        //console.log(values);
        $('#render').append(render(values));
    });

    $('#render div.btn').click(function(){
      const task_id = $(this).val();
      const key = localStorage.getItem('key');

      const data = {
        'task_id' : task_id,
        'auth_token' : key
      }
      $.ajax(
        {
          'url':'http://0.0.0.0:5000/api/v1/task',
          'method':'POST',
          'contentType':'application/json',
          'data': JSON.stringify(data),
        }).done(function(data){
          console.log(data);
        });
    });
}
$(document).ready(init);
