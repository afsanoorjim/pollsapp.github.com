function CreatePoll(){
    let CreateForm = document.getElementById('create');
    let OptoinForm = document.getElementById('option');

    if(OptoinForm.style.display = 'flex'){
        OptoinForm.style.display = 'none';
    }
   
    CreateForm.style.display = 'flex';
    
};
function CreateOption(){
    let CreateForm = document.getElementById('create');
    let OptoinForm = document.getElementById('option');

    if(CreateForm.style.display = 'flex'){
        CreateForm.style.display = 'none';
    }
    
    OptoinForm.style.display = 'flex';

};