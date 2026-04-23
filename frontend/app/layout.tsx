export const metadata = {
  title: 'Tubelens Clone',
  description: 'AI 기반 떡상 영상 탐지 및 유튜브 성장 분석 플랫폼',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  )
}
