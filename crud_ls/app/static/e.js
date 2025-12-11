let addEmpBtn=document.getElementById("addEmpBtn")
let empForm=document.getElementById("empForm")
let tBody=document.getElementById("tBody")
let allEmpsGetBtn=document.getElementById("allEmps")


function loadEmps(){
    tBody.innerHTML=""
        let allData=JSON.parse(localStorage.getItem("emps"))
    // console.log(allData,"allData")
    
    allData.forEach((x)=>{
        console.log(x)
        let Trow=document.createElement("tr")
        Trow.innerHTML=`
        <td>${x.name}</td>
        <td>${x.email}</td>
        <td>${x.salary}</td>
        `
        tBody.append(Trow)
    })
}


addEmpBtn.addEventListener("click",(e)=>{
    console.log(empForm)
    let allEmps=JSON.parse(localStorage.getItem("emps")) || [] // [{}]
    e.preventDefault()

    let newEmp={
        name: document.getElementById("empName").value ,
        email: document.getElementById("empEmail").value ,
        salary: document.getElementById("empSal").value 
    }
    // console.log(newEmp)
    fetch("/api/create_emp/",{
        method:"POST", // request
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(newEmp)
    }).then(res=>res.json()).then(res=>{
        console.log(res)
        allEmps.push(newEmp)// [{},{}]
        localStorage.setItem("emps",JSON.stringify(allEmps))
        empForm.reset()
        loadEmps()
        // alert("emp added to ls ")
    })

})



document.addEventListener("DOMContentLoaded",loadEmps)
// [{}]