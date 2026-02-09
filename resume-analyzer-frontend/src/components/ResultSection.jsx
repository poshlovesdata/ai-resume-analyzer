import React from 'react';
import { CheckCircle2, AlertCircle, Quote } from 'lucide-react';

const ResultSection = ({ summary, strengths, gaps }) => {
    return (
        <div className="space-y-12 animate-in fade-in slide-in-from-bottom-6 duration-700 delay-200">
            <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm relative overflow-hidden group">
                <div className="absolute top-0 left-0 w-2 h-full bg-blue-500" />
                <Quote className="absolute top-6 right-6 h-12 w-12 text-slate-50 opacity-10 group-hover:opacity-20 transition-opacity" />
                <h3 className="text-xl font-bold text-slate-900 mb-4">Hiring Verdict</h3>
                <p className="text-slate-600 leading-relaxed italic pr-12">
                    "{summary}"
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="bg-white p-8 rounded-3xl border border-slate-100 shadow-sm">
                    <div className="flex items-center gap-2 mb-6 text-emerald-600">
                        <CheckCircle2 className="h-6 w-6" />
                        <h3 className="text-lg font-bold">Strengths</h3>
                    </div>
                    <ul className="space-y-3">
                        {strengths.map((item, index) => (
                            <li key={index} className="flex items-start gap-3 p-3 bg-emerald-50 text-emerald-800 rounded-xl font-medium border border-emerald-100">
                                <div className="h-2 w-2 rounded-full bg-emerald-400 mt-2 shrink-0" />
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>

                <div className="bg-white p-8 rounded-3xl border border-slate-100 shadow-sm">
                    <div className="flex items-center gap-2 mb-6 text-rose-600">
                        <AlertCircle className="h-6 w-6" />
                        <h3 className="text-lg font-bold">Critical Gaps</h3>
                    </div>
                    <ul className="space-y-3">
                        {gaps.map((item, index) => (
                            <li key={index} className="flex items-start gap-3 p-3 bg-rose-50 text-rose-800 rounded-xl font-medium border border-rose-100">
                                <div className="h-2 w-2 rounded-full bg-rose-400 mt-2 shrink-0" />
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default ResultSection;
