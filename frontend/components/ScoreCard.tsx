export default function ScoreCard({ title, score, label }: { title: string; score: number; label: string }) {
  return (
    <div className='border rounded-xl p-6 shadow hover:shadow-lg transition-shadow'>
      <h3 className='text-lg font-semibold mb-2'>{title}</h3>
      <p className='text-3xl font-bold text-blue-600'>{score}</p>
      <p className='text-sm text-gray-500'>{label}</p>
    </div>
  )
}
