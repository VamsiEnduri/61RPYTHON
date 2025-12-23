// let btn=document.getElementById("redBtn")
// let pic=document.getElementById("pic")
// // btn.onclick= function (){
// //     alert("red color")
// // }
// btn.addEventListener("click",()=>{
//     document.body.style.backgroundColor="red"
//     btn.style.fontSize="50px"
// }) // event, cab function
// // console.log(btn,"btn")
// // console.log(typeof(btn))
// pic.addEventListener("click",()=>{
//     document.getElementById("bentlyImg").style.display="block"
//     document.getElementById("bentlyImg").style.borderRadius="40px"
// })

// // how to create an element and add it to doc :
// let a=document.createElement("a")
// a.textContent="meesho"
// a.href="https://www.meesho.com/"
// a.style.textDecoration="none"
// a.target="_blank"

// document.body.appendChild(a)
// console.log(a)
document.body.style.backgroundColor="purple"
document.body.style.padding="20px"


let divC=document.getElementById("cardsContainer")
divC.style.backgroundColor="yellow"
divC.style.padding="20px"
divC.style.display="grid"
divC.style.gridTemplateColumns="repeat(4,1fr)"
divC.style.gap="10px"


// let div1=document.createElement("div")
// div1.textContent="div1"
// div1.style.fontSize="40px"
// div1.style.padding=20
// div1.style.backgroundColor="purple"

// divC.appendChild(div1)

fetch("https://fakestoreapi.com/products")
.then(res=>res.json())
.then(res=>{
    for (let i=0;i<res.length;i++){
        // console.log(res[i].title)
        
        let child=document.createElement("div")
        child.style.backgroundColor="gray"

        let img=document.createElement("img")
        img.src=res[i].image
        img.style.width="150px"

        let p= document.createElement("p")
        p.textContent=res[i].title
        p.style.backgroundColor="red"

        child.append(img,p)

        divC.append(child)
    }
})
.catch(err=>console.log(err))