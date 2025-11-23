/**
 * API client for backend communication
 */
import axios from "axios";
import type { ExplainRequest, ExplanationResponse } from "./types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const explainContent = async (
  request: ExplainRequest
): Promise<ExplanationResponse> => {
  try {
    const response = await api.post<ExplanationResponse>(
      "/api/v1/explanation/explain",
      request
    );
    return response.data;
  } catch (error) {
    console.error("Error explaining content:", error);
    throw new Error("Failed to generate explanation");
  }
};

export const getExample = async (): Promise<ExplanationResponse> => {
  try {
    const response = await api.get<ExplanationResponse>(
      "/api/v1/explanation/example"
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching example:", error);
    throw new Error("Failed to fetch example");
  }
};

export const healthCheck = async (): Promise<{ status: string }> => {
  try {
    const response = await api.get("/api/v1/health");
    return response.data;
  } catch (error) {
    console.error("Health check failed:", error);
    throw new Error("API is not available");
  }
};
