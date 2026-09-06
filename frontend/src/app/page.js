// src/app/page.js
"use client";

import { useState } from "react";
import axios from "axios";
import { Loader2, AlertTriangle, ClipboardList, ShieldCheck, Activity, Sparkles } from "lucide-react";

export default function Home() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!symptoms.trim()) {
      setError("Please describe your symptoms first.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/predict`, {
        symptoms: symptoms,
      });
      setResult(response.data);
    } catch (err) {
      setError("Failed to connect to the AI server. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  const getTriageColor = (triage) => {
    if (!triage) return "bg-slate-100 text-slate-800 border-slate-200";
    if (triage.includes("Emergency")) return "bg-red-50 text-red-700 border-red-200";
    if (triage.includes("Consult")) return "bg-orange-50 text-orange-700 border-orange-200";
    if (triage.includes("Schedule")) return "bg-blue-50 text-blue-700 border-blue-200";
    return "bg-teal-50 text-teal-700 border-teal-200";
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 to-slate-100 text-slate-800 flex flex-col items-center">
      
      {/* Header */}
      <header className="w-full max-w-5xl flex justify-between items-center p-6">
        <div className="flex items-center gap-2">
          <svg viewBox="0 0 100 100" className="w-10 h-10">
            <defs>
              <linearGradient id="medGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#2563eb" />
                <stop offset="100%" stopColor="#0d9488" />
              </linearGradient>
            </defs>
            <path d="M40 15 L60 15 L60 40 L85 40 L85 60 L60 60 L60 85 L40 85 L40 60 L15 60 L15 40 L40 40 Z" fill="url(#medGradient)" />
            <path d="M10 50 L30 50 L38 35 L46 65 L54 40 L60 50 L90 50" stroke="white" strokeWidth="4" fill="none" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          <span className="text-xl font-bold tracking-tight">Medi<span className="text-blue-600">Predict</span></span>
        </div>
        <div className="hidden md:flex items-center gap-2 text-sm text-slate-600 bg-white px-4 py-2 rounded-full border border-slate-200 shadow-sm">
          <ShieldCheck className="w-4 h-4 text-teal-600" />
          AI-Powered Triage
        </div>
      </header>

      {/* Hero Section */}
      <section className="text-center mt-12 mb-10 px-4 max-w-3xl">
        <div className="inline-flex items-center gap-2 bg-blue-50 text-blue-700 px-4 py-1.5 rounded-full text-sm font-medium mb-4 border border-blue-100">
          <Sparkles className="w-4 h-4" />
          Advanced Medical AI
        </div>
        <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight text-slate-900 leading-tight">
 Understand Your Symptoms <br className="hidden md:block"/> with <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-teal-600">AI Precision</span>
        </h1>
        <p className="text-slate-600 mt-4 text-lg max-w-xl mx-auto">
          Describe how you feel in your own words. Our system analyzes context and medical patterns to provide instant triage recommendations.
        </p>
      </section>

      {/* Main App Card */}
      <section className="w-full max-w-2xl px-4 mb-12">
        <div className="bg-white rounded-3xl shadow-xl border border-slate-100 p-8">
          
          <label className="block text-sm font-semibold text-slate-700 mb-3 flex items-center gap-2">
            <ClipboardList className="w-4 h-4 text-blue-600" />
            Describe Your Symptoms
          </label>
          
          <textarea
            className="w-full h-36 p-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none outline-none text-slate-700 placeholder-slate-400 text-base"
            placeholder="e.g., My eyes are seeing blurry and I can't focus on distant objects."
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
          />

          {error && (
            <div className="mt-4 flex items-center gap-2 text-red-600 text-sm bg-red-50 p-3 rounded-lg border border-red-100">
              <AlertTriangle className="w-4 h-4" />
              {error}
            </div>
          )}

          <button
            onClick={handlePredict}
            disabled={loading}
            className="mt-6 w-full bg-gradient-to-r from-blue-600 to-teal-600 hover:from-blue-700 hover:to-teal-700 text-white font-semibold py-4 px-4 rounded-2xl transition-all shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-lg"
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Analyzing Symptoms...
              </>
            ) : (
              "Analyze Symptoms"
            )}
          </button>
        </div>
      </section>

      {/* Results Dashboard */}
      {result && (
        <section className="w-full max-w-2xl px-4 mb-12 animate-in fade-in duration-700">
          <div className="bg-white rounded-3xl shadow-xl border border-slate-100 p-8">
            <div className="flex items-center gap-3 mb-6">
               <div className="p-2 bg-blue-50 rounded-lg">
                 <Activity className="w-6 h-6 text-blue-600" />
               </div>
               <h2 className="text-2xl font-bold text-slate-900">Assessment Results</h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
              <div className="bg-slate-50 p-5 rounded-2xl border border-slate-100">
                <p className="text-sm text-slate-500 mb-2 font-medium">Possible Condition</p>
                <p className="text-xl font-bold text-slate-900">{result.predicted_disease}</p>
              </div>

              <div className={`p-5 rounded-2xl border ${getTriageColor(result.triage_level)}`}>
                <p className="text-sm opacity-80 mb-2 font-medium">Recommended Action</p>
                <p className="text-xl font-bold">{result.triage_level}</p>
              </div>
            </div>

            <div className="flex items-start gap-3 text-sm text-slate-600 bg-amber-50 p-4 rounded-xl border border-amber-100">
              <AlertTriangle className="w-5 h-5 mt-0.5 flex-shrink-0 text-amber-500" />
              <p className="font-medium">{result.disclaimer}</p>
            </div>
          </div>
        </section>
      )}

      {/* Footer */}
      <footer className="w-full max-w-5xl border-t border-slate-200 mt-auto py-6 px-4 text-center text-sm text-slate-500">
        <p>© {new Date().getFullYear()} MediPredict. For educational purposes only. Not a substitute for professional medical advice.</p>
      </footer>

    </main>
  );
}