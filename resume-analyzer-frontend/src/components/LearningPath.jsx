import React from 'react';
import { ExternalLink, GraduationCap, Clock, Award } from 'lucide-react';

const LearningPath = ({ resources }) => {
    if (!resources || resources.length === 0) return null;

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-700 delay-400">
            <div className="flex items-center gap-3">
                <div className="p-3 bg-blue-100 rounded-2xl text-blue-600">
                    <GraduationCap className="h-6 w-6" />
                </div>
                <div>
                    <h3 className="text-2xl font-black text-slate-900">Custom Learning Path</h3>
                    <p className="text-slate-500 font-medium">Curated resources to bridge your career gaps</p>
                </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {resources.map((res, index) => (
                    <div key={index} className="group bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl hover:border-blue-200 transition-all duration-300 flex flex-col h-full">
                        <div className="flex justify-between items-start mb-4">
                            <span className="px-3 py-1 bg-slate-100 text-slate-600 text-xs font-bold rounded-lg uppercase tracking-wider">
                                {res.provider || 'Featured'}
                            </span>
                            <span className={`px-3 py-1 text-xs font-bold rounded-lg uppercase tracking-wider ${res.level === 'Beginner' ? 'bg-emerald-100 text-emerald-600' :
                                    res.level === 'Intermediate' ? 'bg-blue-100 text-blue-600' :
                                        'bg-purple-100 text-purple-600'
                                }`}>
                                {res.level || 'All Levels'}
                            </span>
                        </div>

                        <h4 className="text-lg font-bold text-slate-900 mb-2 line-clamp-2 leading-snug group-hover:text-blue-600 transition-colors">
                            {res.title}
                        </h4>

                        <div className="flex items-center gap-4 mt-auto pt-6">
                            <a
                                href={res.url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="w-full inline-flex items-center justify-center gap-2 px-6 py-3 bg-slate-900 text-white font-bold rounded-2xl hover:bg-blue-600 transition-all active:scale-95"
                            >
                                Start Learning
                                <ExternalLink className="h-4 w-4" />
                            </a>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default LearningPath;
