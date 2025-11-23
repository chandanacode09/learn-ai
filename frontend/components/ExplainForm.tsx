"use client";

import { useState } from "react";
import { explainContent, getExample } from "@/lib/api";
import { ExplanationLevel, ExplanationMode, type ExplanationResponse } from "@/lib/types";

interface ExplainFormProps {
  onExplanation: (explanation: ExplanationResponse) => void;
  onLoadingChange: (loading: boolean) => void;
}

export function ExplainForm({ onExplanation, onLoadingChange }: ExplainFormProps) {
  const [inputType, setInputType] = useState<"url" | "text" | "github">("url");
  const [url, setUrl] = useState("");
  const [text, setText] = useState("");
  const [githubRepo, setGithubRepo] = useState("");
  const [level, setLevel] = useState<ExplanationLevel>(ExplanationLevel.INTERMEDIATE);
  const [mode, setMode] = useState<ExplanationMode>(ExplanationMode.PERSONAL);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    onLoadingChange(true);

    try {
      const request: any = {
        level,
        mode,
        generate_visuals: true,
        include_examples: true,
        include_prerequisites: true,
      };

      if (inputType === "url") {
        if (!url) {
          throw new Error("Please enter a URL");
        }
        request.url = url;
      } else if (inputType === "text") {
        if (!text) {
          throw new Error("Please enter some text");
        }
        request.content = text;
      } else if (inputType === "github") {
        if (!githubRepo) {
          throw new Error("Please enter a GitHub repository");
        }
        request.github_repo = githubRepo;
      }

      const explanation = await explainContent(request);
      onExplanation(explanation);
    } catch (err: any) {
      setError(err.message || "Failed to generate explanation");
      console.error(err);
    } finally {
      onLoadingChange(false);
    }
  };

  const handleTryExample = async () => {
    onLoadingChange(true);
    setError("");

    try {
      const explanation = await getExample();
      onExplanation(explanation);
    } catch (err: any) {
      setError(err.message || "Failed to load example");
    } finally {
      onLoadingChange(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Input Type Selector */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Input Type
          </label>
          <div className="flex gap-2">
            <button
              type="button"
              onClick={() => setInputType("url")}
              className={`px-4 py-2 rounded-lg ${
                inputType === "url"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
              }`}
            >
              URL
            </button>
            <button
              type="button"
              onClick={() => setInputType("text")}
              className={`px-4 py-2 rounded-lg ${
                inputType === "text"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
              }`}
            >
              Text
            </button>
            <button
              type="button"
              onClick={() => setInputType("github")}
              className={`px-4 py-2 rounded-lg ${
                inputType === "github"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
              }`}
            >
              GitHub
            </button>
          </div>
        </div>

        {/* Input Field */}
        <div>
          {inputType === "url" && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Article URL
              </label>
              <input
                type="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://example.com/article"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          )}

          {inputType === "text" && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Text Content
              </label>
              <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Paste your content here..."
                rows={6}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          )}

          {inputType === "github" && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                GitHub Repository
              </label>
              <input
                type="text"
                value={githubRepo}
                onChange={(e) => setGithubRepo(e.target.value)}
                placeholder="owner/repository or full URL"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          )}
        </div>

        {/* Explanation Level */}
        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Explanation Level
            </label>
            <select
              value={level}
              onChange={(e) => setLevel(e.target.value as ExplanationLevel)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              <option value={ExplanationLevel.ELI5}>ELI5 (Explain Like I'm 5)</option>
              <option value={ExplanationLevel.BEGINNER}>Beginner</option>
              <option value={ExplanationLevel.INTERMEDIATE}>Intermediate</option>
              <option value={ExplanationLevel.ADVANCED}>Advanced</option>
              <option value={ExplanationLevel.EXPERT}>Expert</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Mode
            </label>
            <select
              value={mode}
              onChange={(e) => setMode(e.target.value as ExplanationMode)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              <option value={ExplanationMode.PERSONAL}>Personal (Quick & Friendly)</option>
              <option value={ExplanationMode.EDUCATIONAL}>Educational (Detailed)</option>
              <option value={ExplanationMode.PROFESSIONAL}>Professional (Actionable)</option>
            </select>
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}

        {/* Submit Buttons */}
        <div className="flex gap-3">
          <button
            type="submit"
            className="flex-1 bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium"
          >
            Explain Content
          </button>
          <button
            type="button"
            onClick={handleTryExample}
            className="px-6 py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors font-medium"
          >
            Try Example
          </button>
        </div>
      </form>
    </div>
  );
}
