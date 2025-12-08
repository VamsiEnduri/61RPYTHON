// let h1Tag=document.body.querySelector("h1") #
// // console.log(h1Tag)
// h1Tag.style.backgroundColor="green"
// h1Tag.style.padding="25px"
// h1Tag.style.borderRadius="40px"
// h1Tag.style.color="white"
// h1Tag.style.fontSize="3.5rem"

// let bodyTag=document.body
// bodyTag.style.backgroundColor="yellow"
// bodyTag.style.padding="25px"
// bodyTag.style.borderRadius="40px"
// bodyTag.style.maxHeight="100px"

// #selecting 1
// let h1Tag=document.querySelector("h1")
// let pTag=document.querySelector(".p__")
// let aTag=document.querySelector("#anchor")
// h1Tag.style.backgroundColor="orange"

// #selecting 2 :--
// by id :--
// let h1Tag=document.getElementById("h1tag")
// let pTag=document.getElementById("p__")
// let aTag=document.getElementById("anchor")
// h1Tag.style.backgroundColor="red"
// pTag.style.backgroundColor="yellow"
// aTag.style.backgroundColor="green"

let addEmpBtnVar = document.getElementById("addEmpBtn");
let div = document.querySelector("#div1");
// let h1 = document.querySelector("#h1name");
// let p = document.querySelector("#pEmail");
// let span = document.querySelector("#sSpan");

addEmpBtnVar.addEventListener("click", (ev) => {
  ev.preventDefault();
  let n = document.getElementById("name").value;
  let e = document.getElementById("email").value;
  let s = document.getElementById("salary").value;
  console.log(n, e, s);//   h1.textContent = n;//   p.textContent = e;
//   span.textContent = s;
div.innerHTML=`
<h1>${n}</h1>
<p>${e}</p>
<span>${s}</span>
`

});
