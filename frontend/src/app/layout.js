// src/app/layout.js
import { Inter } from '@next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'MediPredict — AI Symptom Checker',
  description: 'Advanced AI-powered preliminary medical assessment and triage system.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}