import React, { useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import AnalysisForm from './components/AnalysisForm';
import ScoreCard from './components/ScoreCard';
import ResultSection from './components/ResultSection';
import LearningPath from './components/LearningPath';
import { AlertCircle } from 'lucide-react';

const App = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const analyzeProfile = async (jd, resume) => {
    setLoading(true);
    setError(null);
    try {
      // Concatenate inputs as per requirement
      const concatenatedJD = `JOB DESCRIPTION:\n${jd}\n\nRESUME:\n${resume}`;

      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/analyse_resume`, {
        job_description: concatenatedJD,
        resume: "" // Backend requires this field but we put everything in JD field as per logic requirement
      });

      setResult(response.data);
      // Scroll to results
      setTimeout(() => {
        document.getElementById('results')?.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } catch (err) {
      console.error('Analysis failed:', err);
      setError('Analysis failed. Please ensure the backend is running at http://localhost:8000.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <header className="text-center mb-16 space-y-4">
          <h1 className="text-4xl md:text-5xl font-black text-slate-900 tracking-tight">
            Bridge the Gap to Your <span className="text-blue-600">Dream Career</span>
          </h1>
          <p className="text-lg text-slate-500 font-medium max-w-2xl mx-auto">
            Analyze your resume against any job description instantly. Get a fit score, identify critical gaps, and get a custom learning path.
          </p>
        </header>

        <AnalysisForm onAnalyze={analyzeProfile} isLoading={loading} />

        {error && (
          <div className="flex items-center gap-3 p-4 bg-rose-50 border border-rose-200 text-rose-700 rounded-2xl max-w-2xl mx-auto mb-8 animate-in fade-in zoom-in">
            <AlertCircle className="h-5 w-5 shrink-0" />
            <p className="font-semibold">{error}</p>
          </div>
        )}

        {result && (
          <div id="results" className="pt-16 border-t border-slate-200 space-y-20">
            <div className="flex flex-col items-center gap-6">
              <h2 className="text-3xl font-black text-slate-900">Your Analysis Results</h2>
              <ScoreCard score={result.fit_score} />
            </div>

            <ResultSection
              summary={result.summary}
              strengths={result.strengths}
              gaps={result.missing_critical_skills}
            />

            <LearningPath resources={result.recommended_resources} />

            <footer className="pt-20 pb-12 text-center text-slate-400 text-sm font-medium">
              &copy; 2026 Resume Gap Analyzer. Built with precision for career growth.
            </footer>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
