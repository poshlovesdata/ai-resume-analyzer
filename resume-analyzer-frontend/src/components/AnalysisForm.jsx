import React, { useState } from 'react';
import { Loader2, Search } from 'lucide-react';

const AnalysisForm = ({ onAnalyze, isLoading }) => {
    const [jd, setJd] = useState('');
    const [resume, setResume] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!jd.trim() || !resume.trim()) return;
        onAnalyze(jd, resume);
    };

    return (
        <section className="py-12">
            <form onSubmit={handleSubmit} className="space-y-8">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div className="space-y-2">
                        <label className="text-sm font-semibold text-slate-700 block">
                            Paste Job Description
                        </label>
                        <textarea
                            className="w-full h-80 p-4 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none shadow-sm"
                            placeholder="Enter the full job description here..."
                            value={jd}
                            onChange={(e) => setJd(e.target.value)}
                            required
                        />
                    </div>
                    <div className="space-y-2">
                        <label className="text-sm font-semibold text-slate-700 block">
                            Paste Your Resume
                        </label>
                        <textarea
                            className="w-full h-80 p-4 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none shadow-sm"
                            placeholder="Paste your resume content here..."
                            value={resume}
                            onChange={(e) => setResume(e.target.value)}
                            required
                        />
                    </div>
                </div>

                <div className="flex justify-center">
                    <button
                        type="submit"
                        disabled={isLoading || !jd.trim() || !resume.trim()}
                        className="group relative flex items-center justify-center gap-3 px-8 py-4 bg-blue-600 text-white font-bold rounded-full hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-blue-200 active:scale-95 overflow-hidden"
                    >
                        {isLoading ? (
                            <>
                                <Loader2 className="h-5 w-5 animate-spin" />
                                <span>Analyzing Profile...</span>
                            </>
                        ) : (
                            <>
                                <Search className="h-5 w-5 group-hover:scale-110 transition-transform" />
                                <span>Analyze My Profile</span>
                            </>
                        )}
                    </button>
                </div>
            </form>
        </section>
    );
};

export default AnalysisForm;
