/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */
import { Download, FileSpreadsheet, GraduationCap, Database } from 'lucide-react';
import { motion } from 'motion/react';

export default function App() {
  const handleDownload = () => {
    // In a real environment, we'd fetch the file. 
    // Since this is a preview, we'll trigger a download of the file path or content if possible.
    // For this specific task, the file is generated at /student_performance.csv
    window.open('/student_performance.csv', '_blank');
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 font-sans">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-2xl w-full bg-white rounded-3xl shadow-xl shadow-slate-200/50 p-8 md:p-12 border border-slate-100"
      >
        <div className="flex items-center gap-4 mb-8">
          <div className="p-3 bg-indigo-600 rounded-2xl">
            <GraduationCap className="w-8 h-8 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">
              Student Academic Performance Predictor
            </h1>
            <p className="text-slate-500 font-medium">Synthetic Dataset Generator</p>
          </div>
        </div>

        <div className="space-y-6 mb-10">
          <div className="bg-slate-50 rounded-2xl p-6 border border-slate-100">
            <h2 className="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <Database className="w-4 h-4" />
              Dataset Specifications
            </h2>
            <ul className="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-slate-600">
              <li className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                500+ Realistic Records
              </li>
              <li className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                10 Feature Columns
              </li>
              <li className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                Regression Target Variable
              </li>
              <li className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                Streamlit Web Application
              </li>
            </ul>
          </div>

          <p className="text-slate-600 leading-relaxed">
            The dataset has been generated with realistic correlations between study habits, 
            socio-economic factors, and academic outcomes. It is ready for use in machine 
            learning regression models.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-4">
          <button
            onClick={handleDownload}
            className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-4 px-6 rounded-2xl transition-all flex items-center justify-center gap-3 shadow-lg shadow-indigo-200 active:scale-[0.98]"
          >
            <Download className="w-5 h-5" />
            Download CSV Dataset
          </button>
          
          <div className="flex items-center justify-center px-6 py-4 rounded-2xl bg-slate-100 text-slate-500 font-mono text-sm border border-slate-200">
            <FileSpreadsheet className="w-4 h-4 mr-2" />
            student_performance.csv
          </div>
        </div>
      </motion.div>
      
      <p className="mt-8 text-slate-400 text-sm">
        Generated for ML Regression Project • 2026
      </p>
    </div>
  );
}
