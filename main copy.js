let AccOption = document.querySelectorAll('select');
let fromText = document.querySelector('.fromText');
let TransText = document.querySelector('.totrans');

AccOption.forEach((get, con) => {
   for(let countryCode in accent){

let selected ;
if (con == 0 && countryCode == "N"){
    selected = "selected"
}
else if (con == 1 && countryCode == "G"){
    selected = "selected"
}
    let option = `<option value = "${countryCode}" ${selected}>${accent[countryCode]}</option> `
    get.insertAdjacentHTML(`beforeend` , option)
   } 
})

fromText.addEventListener('click' , function() {
    let content = fromText.value ;
    fromContent = AccOption[0].value;
    transContent = AccOption[1].value;

   

})