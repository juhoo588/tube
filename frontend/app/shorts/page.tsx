async function getShorts(){
 const res=await fetch('http://localhost:8000/api/shorts/rising')
 return res.json()
}

export default async function ShortsPage(){
 const shorts=await getShorts()

 return(
<div className='p-10'>
<h1 className='text-4xl font-bold mb-8'>Rising Shorts</h1>
{shorts.map((v:any)=>(
<div key={v.title} className='border rounded-xl p-6 mb-6 shadow'>
<h2 className='text-2xl font-bold'>{v.title}</h2>
<p>Views 6h: {v.views_6h}</p>
<p>Engagement: {v.engagement}</p>
</div>
))}
</div>
)
}
