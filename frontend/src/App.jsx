import { useState,useEffect } from 'react'
import Login from './components/Login'


function App() {
  const [data , setData] = useState([])
  useEffect(()=>{
    async function fetchData(){
      console.log(import.meta.env.VITE_API_URL)
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}`)
        if (!response.ok){
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        console.log('data recieved :',result);
        setData(result);
      } catch (error) {
        console.error('Error fetching data:',error);
      }
      
    }
    fetchData();
  },[])

  return (
    <>
      <ul>
        {data.map((item, index) => (
          <li key={index}>{item.title}</li>
        ))}
      </ul>
      
      <Login/>
    </>
  )
}

export default App
