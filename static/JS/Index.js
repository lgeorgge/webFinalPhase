function Hide()
{
    document.getElementById("alertMessage").style.display = "none";
}

function CancelButton()
{
    window.location.replace("http://127.0.0.1:8000/ViewAdminTasks");
}

document.addEventListener('DOMContentLoaded', function() 
{
    document.querySelectorAll('#deleteTask').forEach(function(form)
    {
        form.addEventListener('submit', function(event) 
        {
            event.preventDefault();

            const taskId = form.getAttribute('data-task-id');
            const url = `/DeleteTask/${taskId}`;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, 
            {
                method: 'POST',
                headers: 
                {
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrfToken
                }
            })
            .then(response => response.json())
            .then(data => 
            {
                if (data.success) 
                {
                    const task = form.closest('#trA');
                    if (task) 
                    {
                        task.remove();
                    }
                } 
            })
        });
    });
});

function ToggleFilter() 
{
    var FilterList = document.getElementById("filterList");
    if (FilterList.style.height === "0px") 
    {
        FilterList.style.height = "252.9px";
    } 
    else 
    {
        FilterList.style.height = "0px";
    }
}

document.addEventListener('DOMContentLoaded', function() 
{
    document.querySelectorAll('#changeTaskStatus').forEach(function(form)
    {
        const checkbox = form.querySelector('#btn');
        checkbox.addEventListener('change', function(event) 
        {
            event.preventDefault();

            const taskId = form.getAttribute('data-task-id');
            const url = `/ChangeTaskStatus/${taskId}`;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, 
            {
                method: 'POST',
                headers: 
                {
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrfToken
                }
            })
            .then(response => response.json())
        });
    });
});

function ViewTaskDetails(taskId)
{
    var newURL = "http://127.0.0.1:8000/ViewTaskDetails/" + taskId;
    window.location.replace(newURL);
}

function BackButton()
{
    window.location.replace("http://127.0.0.1:8000/ViewTeacherTasks");
}
