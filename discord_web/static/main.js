
document.getElementById("id_command").onchange = function() {showDiv("id_youtube", "label_youtube", "double_arrow", this)};

function showDiv(divId, divId2, divID3, element)
{
    document.getElementById(divID3).style.display = element.value === "Конвертер валют" ? 'block' : 'none';
    document.getElementById(divId2).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
    document.getElementById(divId).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
}


