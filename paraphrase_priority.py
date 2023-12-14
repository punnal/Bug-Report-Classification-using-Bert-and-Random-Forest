import pandas as pd
import requests

def paraphrase_text(api_key, text, num_paraphrases=5):
    api_url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    paraphrased_texts = []
    for _ in range(num_paraphrases):
        data = {
            "prompt": f"Please paraphrase the following text: '{text}'",
            "max_tokens": 120,
            "model":"gpt-3.5-turbo-instruct"
        }
        response = requests.post(api_url, headers=headers, json=data)

        # Check if the response is successful
        if response.status_code == 200:
            json_response = response.json()
            choices = json_response.get('choices', [])
            if choices:
                paraphrased_text = choices[0].get('text', '').strip()
                paraphrased_texts.append(paraphrased_text)
            else:
                print("No choices in the response.")
        else:
            print(f"Failed to get response: {response.status_code}, {response.text}")

    print(paraphrased_texts)
    return paraphrased_texts

# Load the dataset
file_path = 'priority_dataset.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Your API key
api_key = "API-KEY"  # Replace with your actual API key

# New DataFrame for paraphrased summaries
new_data = []

# Process each row
for index, row in data.iterrows():
    num_paraphrases=4
    if "P1" in row['Priority']:
        continue
    if "P2" in row['Priority']:
        continue
    if "P3" in row['Priority']:
        num_paraphrases=2
    if "P4" in row['Priority']:
        num_paraphrases=6
    if "P5" in row['Priority']:
        num_paraphrases=20
    


    paraphrased_summaries = paraphrase_text(api_key, row['Short Description'], num_paraphrases)
    for paraphrase in paraphrased_summaries:
        new_data.append({'Priority': row['Priority'], 'Short Description': paraphrase})

# Convert the list to a DataFrame
new_df = pd.DataFrame(new_data)

# Write the new DataFrame to a CSV file
output_file = 'paraphrased_summaries_priorty.csv'
new_df.to_csv(output_file, index=False)

print(f"Paraphrased summaries saved to {output_file}")
