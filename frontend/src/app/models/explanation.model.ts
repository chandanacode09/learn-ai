export enum ExplanationLevel {
  ELI5 = 'eli5',
  BEGINNER = 'beginner',
  INTERMEDIATE = 'intermediate',
  ADVANCED = 'advanced',
  EXPERT = 'expert'
}

export enum ExplanationMode {
  PERSONAL = 'personal',
  EDUCATIONAL = 'educational',
  PROFESSIONAL = 'professional'
}

export enum ContentType {
  ARTICLE = 'article',
  GITHUB_REPO = 'github_repo',
  PDF = 'pdf',
  DOCUMENTATION = 'documentation',
  CODE_SNIPPET = 'code_snippet'
}

export interface ConceptExtraction {
  name: string;
  description: string;
  difficulty: string;
  prerequisites: string[];
}

export interface VisualAid {
  type: string;
  description: string;
  mermaid_code?: string;
}

export interface ExplanationResponse {
  id: string;
  content_type: ContentType;
  original_title?: string;
  summary: string;
  detailed_explanation: string;
  key_takeaways: string[];
  concepts: ConceptExtraction[];
  prerequisites: string[];
  visual_aids: VisualAid[];
  examples: string[];
  level: ExplanationLevel;
  mode: ExplanationMode;
  estimated_read_time: number;
  created_at: string;
}

export interface ExplainRequest {
  content?: string;
  url?: string;
  github_repo?: string;
  pdf_path?: string;
  level: ExplanationLevel;
  mode: ExplanationMode;
  generate_visuals: boolean;
  include_examples: boolean;
  include_prerequisites: boolean;
}
