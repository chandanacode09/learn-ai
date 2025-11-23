"use client";

import { useState } from "react";
import { ExplainForm } from "@/components/ExplainForm";
import { ExplanationView } from "@/components/ExplanationView";
import { Header } from "@/components/Header";
import type { ExplanationResponse } from "@/lib/types";

export default function Home() {
  const [explanation, setExplanation] = useState<ExplanationResponse | null>(null);
  const [loading, setLoading] = useState(false);

  return (
    <main className="min-h-screen">
      <Header />

      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AI Content Explainer
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            Understand technical content at any level
          </p>
          <p className="text-gray-500">
            From "Explain Like I'm 5" to expert-level analysis
          </p>
        </div>

        {/* Main Content */}
        <div className="grid gap-8">
          {/* Input Form */}
          <ExplainForm
            onExplanation={setExplanation}
            onLoadingChange={setLoading}
          />

          {/* Explanation Result */}
          {loading && (
            <div className="flex items-center justify-center py-12">
              <div className="text-center">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
                <p className="text-gray-600">Generating explanation...</p>
              </div>
            </div>
          )}

          {explanation && !loading && (
            <ExplanationView explanation={explanation} />
          )}
        </div>

        {/* Features Section */}
        {!explanation && !loading && (
          <div className="mt-16 grid md:grid-cols-3 gap-6">
            <FeatureCard
              title="Multi-Level Explanations"
              description="From ELI5 to expert level - choose your complexity"
              icon="🎯"
            />
            <FeatureCard
              title="Multiple Sources"
              description="Articles, GitHub repos, PDFs, and more"
              icon="📚"
            />
            <FeatureCard
              title="Interactive Learning"
              description="Ask follow-up questions and dive deeper"
              icon="💡"
            />
          </div>
        )}
      </div>
    </main>
  );
}

function FeatureCard({
  title,
  description,
  icon,
}: {
  title: string;
  description: string;
  icon: string;
}) {
  return (
    <div className="bg-white rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">
      <div className="text-4xl mb-3">{icon}</div>
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-gray-600 text-sm">{description}</p>
    </div>
  );
}
