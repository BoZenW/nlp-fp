import json
import pandas as pd

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            #print('line: ', line)
            # Load each line as a JSON object
            json_data = json.loads(line.strip())
            #print('keys: ', json_data.keys())
            data.append(json_data)

    df = pd.DataFrame(data)
    return df
    #return data

# Example usage
file_path = './eval_predictions.jsonl'
#jsonl_data = read_jsonl(file_path)
df = read_jsonl(file_path)
#df = df[["id","title", "question", "answers", "predicted_answer"]]
df['id_prefix'] = df['id'].str[:24]

# Create a mask for rows where the 'predicted_answer' values are different
#mask = df.duplicated(subset=['id_prefix'], keep=False) & (df.duplicated(subset=['id_prefix', 'predicted_answer'], keep=False))
mask = (df.duplicated(subset=['id_prefix', 'predicted_answer'], keep=False))
#selected_pairs = df[df.duplicated(subset='id_prefix', keep=False)]
selected_pairs = df[mask]

#df = df[df['title'] == 'Super_Bowl_50']
#print(df.head())
print(selected_pairs.head())
# Now 'jsonl_data' is a list containing dictionaries, where each dictionary represents a JSON object from the file.
