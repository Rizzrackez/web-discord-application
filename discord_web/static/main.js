document.getElementById("id_command").onchange = function() {showDiv("id_youtube", "label_youtube", this)};

function showDiv(divId, divId2, element)
{
    document.getElementById(divId2).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
    document.getElementById(divId).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
}

