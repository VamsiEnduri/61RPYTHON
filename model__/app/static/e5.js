let addEmpBtn = document.getElementById("addEmpBtn");
// let empForm = document.getElementById("empForm");
// let tBody = document.getElementById("tBody");
// let allEmpsGetBtn = document.getElementById("allEmps");

// function loadEmps() {
//   tBody.innerHTML = "";
//   let allData = JSON.parse(localStorage.getItem("emps"));
//   // console.log(allData,"allData")

//   allData.forEach((x) => {
//     console.log(x);
//     let Trow = document.createElement("tr");
//     Trow.innerHTML = `
//         <td>${x.id}</td>
//         <td>${x.name}</td>
//         <td>${x.email}</td>
//         <td>${x.salary}</td>
//         <td>
//         <button onclick='editEmp(${x.id})'>edit</button>
//         <button onclick='deleteEmp(${x.id})'>delete</button>
//         </td>
//         `;
//     tBody.append(Trow);
//   });
// }

// function editEmp(id){
//     // alert(id,"edit")
//    let a=JSON.parse(localStorage.getItem("emps"))
//    let editableEmp=a.find((x)=>x.id ==id)
//    console.log(editableEmp)
//    document.getElementById("empName").value=editableEmp.name
//    document.getElementById("empEmail").value=editableEmp.email
//    document.getElementById("empSal").value=editableEmp.salary

//    document.getElementById("addEmpBtn").style.display="none"
//    document.getElementById("editEmpBtn").style.display="block"

//    document.getElementById("editEmpBtn").addEventListener("click",(e)=>{
//     e.preventDefault()

//      let updatedEmp = {
//     id: id,
//     name: document.getElementById("empName").value,
//     email: document.getElementById("empEmail").value,
//     salary: document.getElementById("empSal").value,
//   };

//   fetch(`/api/edit_emp/${id}/`, {
//     method: "PUT", // request
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(updatedEmp),
//   })
//     .then((res) => res.json())
//     .then((res) => {
//       console.log(res)
//        let allD=JSON.parse( localStorage.getItem("emps"))
//        let i=allD.findIndex(x=>x.id == id)
//        console.log(i)
//        allD[i]=updatedEmp

//        localStorage.setItem("emps",JSON.stringify(allD))
//        loadEmps()
//        empForm.reset()

//           document.getElementById("addEmpBtn").style.display="block"
//    document.getElementById("editEmpBtn").style.display="none"

//       // alert("emp added to ls ")
//     });

//    })

// }
// // a=[1,2,3]
// // a[2]="vamsi"

// // a=[1,2,"vamsi"]
// function deleteEmp(id) {
//   alert(id);
//   fetch(`/api/delete_emp/${id}/`, {
//     method: "DELETE",
//   })
//     .then((res) => res.json())
//     .then(res => {
//     //   e.preventDefault();
//       console.log(res);
//       let allDa = JSON.parse(localStorage.getItem("emps"));
//       let updatedFilteredData = allDa.filter((x) => x.id != id); // 2 != 2  [{id"1}]
//       localStorage.setItem("emps", JSON.stringify(updatedFilteredData));
//       loadEmps();
//     });
//   console.log("1234567");
// }
let tBody=document.getElementById("tBody")
addEmpBtn.addEventListener("click", (e) => {
  console.log(empForm);
  e.preventDefault();

  let newEmp = {
    name: document.getElementById("empName").value,
    email: document.getElementById("empEmail").value,
    salary: document.getElementById("empSal").value,
  };
  // console.log(newEmp)
  fetch("/api/create_emp/", {
    method: "POST", // request
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newEmp),
  })
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
      get_emps()
    });
});

function deleteEmp(id){
    fetch(`/api/delete_emp/${id}`,{
        method:"DELETE"
    }).then(res=>res.json()).then(res=>{
        console.log(res)
        get_emps()
    })
}




function get_emps() {
    tBody.innerHTML=""
  fetch("/api/get_emps/")
    .then((res) => res.json())
    .then((res) => {
        console.log(res)
        res.data.forEach((x)=>{
        let tRow=document.createElement("tr")
        tRow.innerHTML=`
        <td>${x.id}</td>
        <td>${x.name}</td>
        <td>${x.email}</td>
        <td>${x.salary}</td>
        <td>
         <button onclick='editEmp(${x.id})'>edit</button>
         <button onclick='deleteEmp(${x.id})'>delete</button>
        </td>
        `
        tBody.append(tRow)
        })
    })
    .catch((err) => console.log(err));
}


function editEmp(_id){
  alert(_id)
  fetch("/api/get_emps/")
    .then((res) => res.json()).then(res=>{
      console.log(res.data)
      let editableEmp=res.data.find((x)=>x.id == _id)
      console.log(editableEmp,"editableEmp")
      document.getElementById("empName").value=editableEmp.name
      document.getElementById("empEmail").value=editableEmp.email
      document.getElementById("empSal").value=editableEmp.salary

      document.getElementById("addEmpBtn").style.display="none"
      document.getElementById("editEmpBtn").style.display="block"

      document.getElementById("editEmpBtn").addEventListener("click",()=>{
        alert("edit function triggered")
        let updateEmpData={
          name: document.getElementById("empName").value,
          email:document.getElementById("empEmail").value,
          salary:document.getElementById("empSal").value
        }
        fetch(`/api/edit_emp/${_id}`,{
          method:"PUT",
          headers:{
            "Content-Type":"application/json"
          },
          body:JSON.stringify(updateEmpData)
        }).then(res=>res.json()).then(res=>{
          console.log(res)
          get_emps()
        })
      })
    })
}
document.addEventListener("DOMContentLoaded", get_emps);

// document.addEventListener("DOMContentLoaded", loadEmps);
// [{}]
