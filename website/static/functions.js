function addAnswerP(data) {
  var newP = document.createElement("p");
  newP.classList.add("answer_p");

  var mydiv = document.getElementsByClassName("answer_div")[0];

  var elementExists = document.getElementsByClassName("answer_p")[0];

  if (elementExists) {

  } else {
    mydiv.appendChild(newP);
    newP.innerHTML = data;
  }

}


// function getValueFromInput() {
//   data = document.getElementsByClassName('form-control');
//   for (var i = 0; i < data.length; i++) {

//   }
// }

function delAnswerP() {
  let delAnswEl = document.getElementsByClassName("answer_p")[0];
  delAnswEl.parentElement.removeChild(delAnswEl);
}

// function addNewInput(newInput) {
//   var newInput = document.createElement("input");

//   newInput.classList.add("form-control");
//   newInput.setAttribute("id", "formGroupExampleInput");
//   newInput.setAttribute("type", "text");
//   newInput.setAttribute("placeholder", "180 00 00");

//   var mydiv = document.getElementsByClassName("form-group")
//   var elementExists = document.getElementsByClassName("form-control")[0]; 

//   if (elementExists) {

//   } else{
//     mydiv.appendChild(newInput)
//   }
// }
