import os

def summarize(text_input, palm):
  defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
    }
  palm.configure(api_key='AIzaSyDBQ8y00dcctDrqr1GSTg4b2Kau8n8vH-g')
  summary_gen = "Give me 3 important topics with their summary with not less than 50 words: "
  summary_gen = summary_gen + text_input
  summary = palm.generate_text(**defaults,prompt = summary_gen)
  return summary.result

def generate_text(text_input, palm):
  defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
  }
  palm.configure(api_key='AIzaSyDBQ8y00dcctDrqr1GSTg4b2Kau8n8vH-g')
  text = "Give me 2 points from the given text such that it summarizes the entire text: "
  summary_gen = text + text_input
  summary = palm.generate_text(**defaults,prompt = summary_gen)
  return summary.result

def prompt_image(text_input, palm):
  defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
  }
  palm.configure(api_key='AIzaSyDBQ8y00dcctDrqr1GSTg4b2Kau8n8vH-g')
  image_prompt = "Give me a prompt(within 30 words) for each topics so that I can generate a images which summarizes it while having no text in the image: "
  image_prompt = image_prompt + text_input
  prompt = palm.generate_text(prompt = image_prompt)
  return prompt.result
    
def title_gen(text_input,palm):
  defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
  }
  title_gen = "Give me a title for this text in less than 5 words: "+text_input
  title = palm.generate_text(prompt = title_gen)
  return title.result