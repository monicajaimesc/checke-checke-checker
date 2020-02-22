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

    console.log(project.tasks);
    project.tasks.forEach(function(values){
        console.log(values);
        $('#render').append(render(values));
    })



}
$(document).ready(init);