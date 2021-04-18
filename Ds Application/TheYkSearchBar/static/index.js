

let input = document.querySelector('input');

let log = document.getElementById('log');



input.addEventListener("keyup", function (e) {
    let request = new XMLHttpRequest();
    request.open("POST","http://127.0.0.1:5000/search")
    request.setRequestHeader("Content-type", "application/json");

    if (e.target.value == "") {
      deleteChild()
      createDiv("No result Found")
      setTimeout(deleteChild,2000)
      
    } else {

    request.onload  = function() {
      deleteChild()
        var jsonResponse = JSON.parse(request.responseText);
    
        array = jsonResponse["result"]
        if (array.length == 0 ) {
          createDiv("No result Found")
        } else {
           for (i = 0; i < array.length; i++) {
          createDiv(array[i])
           }
    }

     };
     
    request.send(JSON.stringify({"search":e.target.value}))
     }

 

});

function createDiv(content){
  var div = document.createElement('div');
  div.id = 'sugggestion';
  div.innerHTML = content;
  div.className = 'sugggestionList';

  var element = document.getElementById("searchResults");
  element.appendChild(div);
}

function deleteChild() {
  var list = document.getElementById("searchResults");
while (list.hasChildNodes()) {  
  list.removeChild(list.firstChild);
}
}