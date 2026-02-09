import React from 'react';

const ScoreCard = ({ score }) => {
    const getScoreColor = (s) => {
        if (s >= 80) return 'text-emerald-500 border-emerald-100 bg-emerald-50';
        if (s >= 50) return 'text-amber-500 border-amber-100 bg-amber-50';
        return 'text-rose-500 border-rose-100 bg-rose-50';
    };

    const getScoreStroke = (s) => {
        if (s >= 80) return 'stroke-emerald-500';
        if (s >= 50) return 'stroke-amber-500';
        return 'stroke-rose-500';
    };

    const colorClasses = getScoreColor(score);
    const strokeClass = getScoreStroke(score);
    const radius = 36;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (score / 100) * circumference;

    return (
        <div className={`flex flex-col items-center justify-center p-8 rounded-3xl border ${colorClasses} shadow-sm w-full max-w-xs mx-auto transition-all duration-700 animate-in fade-in zoom-in slide-in-from-bottom-4`}>
            <span className="text-sm font-bold uppercase tracking-wider mb-4">Overall Fit Score</span>
            <div className="relative flex items-center justify-center">
                <svg className="w-32 h-32 transform -rotate-90">
                    <circle
                        cx="64"
                        cy="64"
                        r={radius}
                        stroke="currentColor"
                        strokeWidth="8"
                        fill="transparent"
                        className="opacity-10"
                    />
                    <circle
                        cx="64"
                        cy="64"
                        r={radius}
                        stroke="currentColor"
                        strokeWidth="8"
                        fill="transparent"
                        strokeDasharray={circumference}
                        strokeDashoffset={offset}
                        strokeLinecap="round"
                        className={`transition-all duration-1000 ease-out ${strokeClass}`}
                    />
                </svg>
                <span className="absolute text-3xl font-black">{score}%</span>
            </div>
        </div>
    );
};

export default ScoreCard;
