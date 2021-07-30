function addAnswerP() {
  var newP = document.createElement("p");
  newP.classList.add("answer_p");

  var mydiv = document.getElementsByClassName("answer_div")[0];
  var data = document.getElementsByClassName("form-control")[0].value;

  var elementExists = document.getElementsByClassName("answer_p")[0];

  if (elementExists) {

  } else {
    mydiv.appendChild(newP);

    newP.innerHTML = data;
  }

}

function delAnswerP() {
  let delAnswEl = document.getElementsByClassName("answer_p")[0];
  delAnswEl.parentElement.removeChild(delAnswEl);
}

function createInput() {
  var newInput = document.createElement("input");

  newInput.classList.add("form-control");
  newInput.setAttribute("id", "formGroupExampleInput");
  newInput.setAttribute("type", "text");
  newInput.setAttribute("placeholder", "180 00 00");

  return newInput
}

function addNewInput(newInput) {
  var mydiv = document.getElementsByClassName("form-group")
  var elementExists = document.getElementsByClassName("form-control")[0]; 

  if (elementExists) {

  } else{
    mydiv.appendChild(newInput)
  }
}
