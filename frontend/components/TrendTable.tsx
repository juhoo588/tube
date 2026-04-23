export default function TrendTable({ videos }: { videos: any[] }) {
  return (
    <table className='w-full border-collapse'>
      <thead>
        <tr className='bg-gray-100'>
          <th className='p-3 text-left'>Title</th>
          <th className='p-3 text-left'>Trend Score</th>
          <th className='p-3 text-left'>CTR</th>
          <th className='p-3 text-left'>Retention</th>
        </tr>
      </thead>
      <tbody>
        {videos.map((v) => (
          <tr key={v.title} className='border-b'>
            <td className='p-3'>{v.title}</td>
            <td className='p-3'>{v.trend_score}</td>
            <td className='p-3'>{v.ctr}%</td>
            <td className='p-3'>{(v.retention * 100).toFixed(1)}%</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
