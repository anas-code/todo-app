

document.addEventListener('DOMContentLoaded', function () {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText);
            taskInput.value = '';
        }
    });

    function addTask(taskText) {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${taskText}</span>
            <button class="delete-btn">Delete</button>
            <button class="complete-btn">Complete</button>
        `;

        listItem.querySelector('.delete-btn').addEventListener('click', function () {
            listItem.remove();
        });

        listItem.querySelector('.complete-btn').addEventListener('click', function () {
            listItem.classList.toggle('completed');
        });

        taskList.appendChild(listItem);
    }
});
