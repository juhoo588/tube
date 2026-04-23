export default function ShortsCard({ video }: { video: any }) {
  return (
    <div className='border rounded-xl p-6 mb-4 shadow hover:shadow-lg transition-shadow'>
      <h3 className='text-xl font-bold mb-2'>{video.title}</h3>
      <div className='grid grid-cols-3 gap-4 text-sm'>
        <div>
          <p className='text-gray-500'>Views (6h)</p>
          <p className='font-semibold'>{video.views_6h?.toLocaleString()}</p>
        </div>
        <div>
          <p className='text-gray-500'>Engagement</p>
          <p className='font-semibold'>{((video.likes + video.comments) / video.views * 100).toFixed(1)}%</p>
        </div>
        <div>
          <p className='text-gray-500'>Retention</p>
          <p className='font-semibold'>{(video.avg_view_percent * 100).toFixed(1)}%</p>
        </div>
      </div>
    </div>
  )
}
