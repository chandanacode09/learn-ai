"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import type { ExplanationResponse } from "@/lib/types";
import { formatReadTime } from "@/lib/utils";

interface ExplanationViewProps {
  explanation: ExplanationResponse;
}

export function ExplanationView({ explanation }: ExplanationViewProps) {
  const [activeTab, setActiveTab] = useState<"summary" | "detailed" | "concepts">("summary");

  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-6">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <h2 className="text-2xl font-bold mb-2">
              {explanation.original_title || "Explanation"}
            </h2>
            <p className="text-blue-100">
              {formatReadTime(explanation.estimated_read_time)} •{" "}
              {explanation.level.toUpperCase()} Level •{" "}
              {explanation.mode} Mode
            </p>
          </div>
          <div className="flex gap-2">
            <button
              className="px-4 py-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors"
              title="Export"
            >
              📥
            </button>
            <button
              className="px-4 py-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors"
              title="Share"
            >
              🔗
            </button>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <div className="flex">
          <button
            onClick={() => setActiveTab("summary")}
            className={`px-6 py-3 font-medium transition-colors ${
              activeTab === "summary"
                ? "text-blue-600 border-b-2 border-blue-600"
                : "text-gray-600 hover:text-gray-900"
            }`}
          >
            Summary
          </button>
          <button
            onClick={() => setActiveTab("detailed")}
            className={`px-6 py-3 font-medium transition-colors ${
              activeTab === "detailed"
                ? "text-blue-600 border-b-2 border-blue-600"
                : "text-gray-600 hover:text-gray-900"
            }`}
          >
            Detailed Explanation
          </button>
          <button
            onClick={() => setActiveTab("concepts")}
            className={`px-6 py-3 font-medium transition-colors ${
              activeTab === "concepts"
                ? "text-blue-600 border-b-2 border-blue-600"
                : "text-gray-600 hover:text-gray-900"
            }`}
          >
            Concepts & More
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="p-6">
        {activeTab === "summary" && (
          <div className="space-y-6">
            {/* Instant Insight */}
            <div className="bg-blue-50 border-l-4 border-blue-600 p-4 rounded">
              <h3 className="font-semibold text-blue-900 mb-2">💡 Instant Insight</h3>
              <p className="text-lg text-blue-800">{explanation.summary}</p>
            </div>

            {/* Key Takeaways */}
            <div>
              <h3 className="font-semibold text-lg mb-3">🎯 Key Takeaways</h3>
              <ul className="space-y-2">
                {explanation.key_takeaways.map((takeaway, index) => (
                  <li
                    key={index}
                    className="flex items-start gap-2 bg-gray-50 p-3 rounded"
                  >
                    <span className="text-blue-600 font-bold">•</span>
                    <span>{takeaway}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Examples */}
            {explanation.examples.length > 0 && (
              <div>
                <h3 className="font-semibold text-lg mb-3">📝 Examples</h3>
                <div className="space-y-3">
                  {explanation.examples.map((example, index) => (
                    <div key={index} className="bg-green-50 p-4 rounded border-l-4 border-green-600">
                      <p>{example}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === "detailed" && (
          <div className="prose max-w-none">
            <ReactMarkdown>{explanation.detailed_explanation}</ReactMarkdown>
          </div>
        )}

        {activeTab === "concepts" && (
          <div className="space-y-6">
            {/* Prerequisites */}
            {explanation.prerequisites.length > 0 && (
              <div>
                <h3 className="font-semibold text-lg mb-3">📚 Prerequisites</h3>
                <div className="flex flex-wrap gap-2">
                  {explanation.prerequisites.map((prereq, index) => (
                    <span
                      key={index}
                      className="bg-purple-100 text-purple-800 px-3 py-1 rounded-full text-sm"
                    >
                      {prereq}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Concepts */}
            {explanation.concepts.length > 0 && (
              <div>
                <h3 className="font-semibold text-lg mb-3">🧩 Key Concepts</h3>
                <div className="grid gap-4">
                  {explanation.concepts.map((concept, index) => (
                    <div
                      key={index}
                      className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                    >
                      <div className="flex items-start justify-between mb-2">
                        <h4 className="font-semibold text-lg">{concept.name}</h4>
                        <span className={`text-xs px-2 py-1 rounded ${
                          concept.difficulty === "beginner"
                            ? "bg-green-100 text-green-800"
                            : concept.difficulty === "intermediate"
                            ? "bg-yellow-100 text-yellow-800"
                            : "bg-red-100 text-red-800"
                        }`}>
                          {concept.difficulty}
                        </span>
                      </div>
                      <p className="text-gray-700 mb-3">{concept.description}</p>
                      {concept.prerequisites.length > 0 && (
                        <div>
                          <p className="text-sm text-gray-600 mb-1">Prerequisites:</p>
                          <div className="flex flex-wrap gap-1">
                            {concept.prerequisites.map((prereq, idx) => (
                              <span
                                key={idx}
                                className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded"
                              >
                                {prereq}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Visual Aids */}
            {explanation.visual_aids.length > 0 && (
              <div>
                <h3 className="font-semibold text-lg mb-3">📊 Visual Aids</h3>
                <div className="space-y-4">
                  {explanation.visual_aids.map((visual, index) => (
                    <div key={index} className="bg-gray-50 p-4 rounded-lg">
                      <h4 className="font-medium mb-2">{visual.type}</h4>
                      <p className="text-gray-700 text-sm mb-3">{visual.description}</p>
                      {visual.mermaid_code && (
                        <div className="bg-white p-4 rounded border border-gray-200 overflow-x-auto">
                          <pre className="text-sm"><code>{visual.mermaid_code}</code></pre>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
