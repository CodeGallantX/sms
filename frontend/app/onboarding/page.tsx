"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

const steps = [
  { id: 1, title: "Basics", description: "Institution info" },
  { id: 2, title: "Structure", description: "Levels and Classes" },
  { id: 3, title: "Staff", description: "Invite team" },
  { id: 4, title: "AI & Finance", description: "Final configuration" },
];

export default function OnboardingPage() {
  const [currentStep, setCurrentStep] = useState(1);

  const nextStep = () => setCurrentStep((prev) => Math.min(prev + 1, steps.length));
  const prevStep = () => setCurrentStep((prev) => Math.max(prev - 1, 1));

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center py-20">
      <div className="w-full max-w-4xl px-4">
        {/* Stepper */}
        <div className="flex justify-between mb-12">
          {steps.map((step) => (
            <div key={step.id} className="flex flex-col items-center">
              <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold ${currentStep >= step.id ? 'bg-primary text-white' : 'bg-gray-200 text-gray-500'}`}>
                {step.id}
              </div>
              <div className="mt-2 text-sm font-medium">{step.title}</div>
            </div>
          ))}
        </div>

        {/* Content */}
        <div className="bg-white rounded-2xl shadow-xl p-10 min-h-[500px] flex flex-col">
          <AnimatePresence mode="wait">
            <motion.div
              key={currentStep}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="flex-grow"
            >
              <h2 className="text-3xl font-bold mb-4">{steps[currentStep-1].title}</h2>
              <p className="text-gray-500 mb-8">{steps[currentStep-1].description}</p>

              {currentStep === 1 && (
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium mb-1">Institution Name</label>
                    <input className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-primary" placeholder="e.g. Greenwood Academy" />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-1">Subdomain</label>
                    <div className="flex">
                      <input className="flex-grow p-3 border rounded-l-lg" placeholder="greenwood" />
                      <span className="p-3 bg-gray-100 border border-l-0 rounded-r-lg">.schoolos.com</span>
                    </div>
                  </div>
                </div>
              )}

              {/* Add other steps placeholders */}
              {currentStep > 1 && <div className="p-20 text-center text-gray-400">Step {currentStep} implementation details...</div>}
            </motion.div>
          </AnimatePresence>

          <div className="flex justify-between mt-10">
            <button onClick={prevStep} disabled={currentStep === 1} className="px-6 py-2 border rounded-lg disabled:opacity-50">Back</button>
            <button onClick={nextStep} className="px-6 py-2 bg-primary text-white rounded-lg">
              {currentStep === steps.length ? 'Complete Setup' : 'Next Step'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
