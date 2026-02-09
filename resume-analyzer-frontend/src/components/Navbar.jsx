import React from 'react';
import { Briefcase } from 'lucide-react';

const Navbar = () => {
    return (
        <nav className="bg-white border-b border-slate-200">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16 items-center">
                    <div className="flex items-center gap-2">
                        <Briefcase className="h-8 w-8 text-blue-600" />
                        <span className="text-xl font-bold text-slate-900 tracking-tight">
                            Resume Gap Analyzer
                        </span>
                    </div>
                    <div className="hidden sm:flex sm:space-x-8">
                        <a href="#" className="text-slate-600 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors">
                            How it works
                        </a>
                        <a href="#" className="text-slate-600 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors">
                            Pricing
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
