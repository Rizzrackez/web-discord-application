
document.getElementById("id_command").onchange = function() {showDiv("id_youtube", "label_youtube", "double_arrow", "label_weather","id_weather", this)};

function showDiv(divId, divId2, divID3, divId4, divId5,element)
{
    // document.getElementById(divId4).style.display = element.value === "Погода" ? 'block' : 'none' ;

    document.getElementById(divId5).style.display = element.value === "Погода" ? 'block' : 'none';
    document.getElementById(divId4).style.display = element.value === "Погода" ? 'block' : 'none';
    document.getElementById(divID3).style.display = element.value === "Конвертер валют" ? 'block' : 'none';
    document.getElementById(divId2).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
    document.getElementById(divId).style.display = element.value === "Конвертация видео с ютуб в m4a файл" ? 'block' : 'none';
}


