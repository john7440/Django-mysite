export interface Choice {
  id: number;
  choice_text: string;
  votes?: number;
}

export interface Question {
  id: number;
  question_text: string;
  pub_date: string;
  choices: Choice[];
 }
