initialPrompt = """You are a recruiting and resume writing expert for software engineers with over 20 years experience. 
Based on the company name, job title, and job description provided by the user, what is the biggest challenge someone in this position would face day-to-day?"""
promptTempate = "Company Name: {}\nJob Title: {}\nJob Description: {}"

def generate_prompts(name, title, description):
    prompts = [{"role": "system", "content": initialPrompt}]
    user_prompt = promptTempate.format(name, title, description);
    prompts.append({"role": "user", "content": user_prompt})
    return prompts;