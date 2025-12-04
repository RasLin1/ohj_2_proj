'use strict'





async function pythonWaitEnemy(){

try {
  const response = await fetch('http://127.0.0.1:3000/play/')
  const pythonData = await response.json()
  console.log(pythonData.value)


}catch (error){

 console.log(error.message)

}


}


