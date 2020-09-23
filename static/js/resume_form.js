// CONTACT INFO DOM ELEMENTS
const contactInfoFormGroup = document.getElementById("contact-info-form-group");
// Buttons
const contactNextBtn = document.getElementById("contact-next-btn");
// Labels
const firstNameLbl = document.getElementById("first-name");
const lastNameLbl = document.getElementById("last-name");
const phoneNumberLbl = document.getElementById("phone-number");
const emailLbl = document.getElementById("email");
// Form Inputs
const firstNameInput = document.getElementById("first-name-input");
const lastNameInput = document.getElementById("last-name-input");
const phoneNumberInput = document.getElementById("phone-number-input");
const emailInput = document.getElementById("email-input");

// CONTACT INFO EVENTS
contactNextBtn.addEventListener("click", function (e) {
  e.preventDefault();
  contactInfoFormGroup.classList.add("d-none");
  educationFormGroup.classList.remove("d-none");
});
firstNameInput.addEventListener("input", function () {
  firstNameLbl.innerHTML = firstNameInput.value;
});
lastNameInput.addEventListener("input", function () {
  lastNameLbl.innerHTML = lastNameInput.value;
});
phoneNumberInput.addEventListener("input", function () {
  phoneNumberLbl.innerHTML = phoneNumberInput.value;
});
emailInput.addEventListener("input", function () {
  emailLbl.innerHTML = emailInput.value;
});

// EDUCATION DOM ELEMENTS
const educationFormGroup = document.getElementById("education-form-group");
const educationForm = document.getElementById("education-form");
const educationSection = document.getElementById("education-section");
// Buttons
const educationPrevBtn = document.getElementById("education-prev-btn");
const educationNextBtn = document.getElementById("education-next-btn");
const addEducationBtns = document.getElementsByClassName("add-education-btn");
// Labels
const majorLbl = document.getElementById("major");
const gpaLbl = document.getElementById("gpa");
// Form Inputs
const schoolNameInputs = document.getElementsByClassName("school-name-input");
const majorInput = document.getElementById("major-input");
const gpaInput = document.getElementById("gpa-input");

// EDUCATION VARIABLES
let numEducations = 0;

// EDUCATION EVENTS
educationPrevBtn.addEventListener("click", function (e) {
  e.preventDefault();
  contactInfoFormGroup.classList.remove("d-none");
  educationFormGroup.classList.add("d-none");
});
educationNextBtn.addEventListener("click", function (e) {
  e.preventDefault();
});
for (let i = 0; i < schoolNameInputs.length; i++) {
  schoolNameInputs[i].addEventListener("input", function () {
    let id = this.dataset.education;
    const schoolNameLbl = document.getElementById("school-name" + id);
    schoolNameLbl.innerHTML = schoolNameInputs[i].value;
  });
}
0;
majorInput.addEventListener("input", function () {
  majorLbl.innerHTML = majorInput.value;
});
gpaInput.addEventListener("input", function () {
  gpaLbl.innerHTML = gpaInput.value;
});
// addEducation event
for (let i = 0; i < addEducationBtns.length; i++) {
  addEducationBtns[i].addEventListener("click", function (e) {
    e.preventDefault();
    numEducations++;
    //grab the education form and duplicate it underneath the previous one
    const educationFormDuplicate = educationForm.cloneNode(true);
    educationForm.parentNode.insertBefore(
      educationFormDuplicate,
      educationForm.nextSibling
    );
    const schoolNameDuplicateInput = educationFormDuplicate.querySelector(
      "#school-name-input"
    );
    schoolNameDuplicateInput.setAttribute(
      "data-education",
      numEducations.toString()
    );
    schoolNameDuplicateInput.addEventListener("input", function () {
      let id = this.dataset.education;
      const schoolNameLbl = document.getElementById("school-name" + id);
      schoolNameLbl.innerHTML = schoolNameDuplicateInput.value;
    });
    // TODO -> edit all the data attributes of the input fields to be str(numEducations)

    //grab the education section on the resume and duplicate it underneath the previous one
    const educationSectionDuplicate = educationSection.cloneNode(true);
    educationSection.parentNode.insertBefore(
      educationSectionDuplicate,
      educationSection.nextSibling
    );
    //get the school name lbl and add numEducations to the id
    const schoolNameDuplicateLbl = educationSectionDuplicate.querySelector(
      "#school-name" + (numEducations - 1) //it is still the previous numEducations right now
    );
    schoolNameDuplicateLbl.id = "school-name" + numEducations;
  });
}
