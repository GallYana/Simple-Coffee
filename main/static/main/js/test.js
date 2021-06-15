let counterBtnQuestion = 0;

function questionAdd() {
  counterBtnQuestion++;
  const questionsContainer = document.querySelector(".test-form__questions");
  const root = document.createElement("div");

  const answersContainer = document.createElement("div");
  const answersParagraph = document.createElement("p");
  const answersFieldset = document.createElement("fieldset");
  const answersLegend = document.createElement("legend");
  const answersInput = document.createElement("input");
  const answersCheckboxLabel = document.createElement("label");
  const answersCheckbox = document.createElement("input");
  const btn = document.createElement("button");

  const fieldset = document.createElement("fieldset");
  const legend = document.createElement("legend");
  const input = document.createElement("input");

  root.className = "test-form__block";

  answersContainer.className = "test-form__answers";
  answersParagraph.innerText = "Варианты ответа";
  answersFieldset.style.marginBottom = "10px";
  answersInput.placeholder = "Вариант ответа";
  answersInput.name = "answer_name";
  answersInput.required = true;
  answersCheckboxLabel.innerText = "Верный";
  answersCheckbox.name = "answer_success";
  answersCheckbox.type = "checkbox";

  btn.type = "button";
  btn.className = "test-form__btn";

  btn.onclick = answerAdd.bind(this, counterBtnQuestion);
  btn.innerText = "Добавить вариант ответа";
  
  fieldset.style.marginBottom = "10px";
  
  input.placeholder = "Вопрос";
  input.name = "question_name";
  input.required = true;
  
  fieldset.appendChild(legend);
  fieldset.appendChild(input);

  answersFieldset.appendChild(answersLegend);
  answersFieldset.appendChild(answersInput);
  answersFieldset.appendChild(answersCheckboxLabel);
  answersFieldset.appendChild(answersCheckbox);
  answersContainer.appendChild(answersParagraph);
  answersContainer.appendChild(answersFieldset);

  root.appendChild(fieldset);
  root.appendChild(answersContainer);
  root.appendChild(btn);

  questionsContainer.appendChild(root);
}

function answerAdd(countAnswersContainer = 0) {
  const answersContainer = document.querySelectorAll(".test-form__answers")[countAnswersContainer];
  const fieldset = document.createElement("fieldset");
  const legend = document.createElement("legend");
  const input = document.createElement("input");
  const checkboxLabel = document.createElement("label");
  const checkbox = document.createElement("input");

  fieldset.style.marginBottom = "10px";
  input.placeholder = "Вариант ответа";
  input.name = `answer_name-${ countAnswersContainer }`;
  input.required = true;
  checkboxLabel.innerText = "Верный";
  checkbox.name = `answer_success-${ countAnswersContainer }-${ answersContainer.children.length }`;
  checkbox.type = "checkbox";
  
  fieldset.appendChild(legend);
  fieldset.appendChild(input);
  fieldset.appendChild(checkboxLabel);
  fieldset.appendChild(checkbox);
  answersContainer.appendChild(fieldset);
}