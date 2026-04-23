async function getData(){
 const res=await fetch('http://localhost:8000/api/trending')
 return res.json()
}

export default async function Home(){
 const videos=await getData()

 return(
<div className='p-10'>
<h1 className='text-4xl font-bold mb-8'>TUBELENS SIGNALS</h1>

{videos.map((v:any)=>(
<div
key={v.title}
className='border rounded-xl p-6 mb-6 shadow'
>
<h2 className='text-2xl font-bold'>
{v.title}
</h2>

<p>Trend Score: {v.trend_score}</p>
<p>CTR: {v.ctr}%</p>
<p>Retention: {v.retention}</p>

</div>
))}

</div>
)
}
