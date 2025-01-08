from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from textSummarizer.entity import ModelEvaluationConfig

class Model_Evaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i + batch_size]

    def calculate_metric_on_test_data(self, dataset,metric, model,tokenizer,batch_size=2,device='cuda' if torch.cuda.is_available() else 'cpu',column_text='dialogue',column_summary='summary'):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))
        for article_batch, target_batch in tqdm(zip(article_batches, target_batches), total=len(article_batches)):
            inputs = tokenizer(article_batch, truncation=True,max_length = 1024 ,padding="max_length", return_tensors='pt')
            summaries = model.generate(input_ids = inputs['input_ids'].to(device), attention_mask = inputs['attention_mask'].to(device), max_length=128, num_beams=8, length_penalty=0.8)
            decoded_summaries = [tokenizer.decode(summary, skip_special_tokens=True, clean_up_tokenization_spaces = True) for summary in summaries]
            decoded_summaries = [summary.replace('', ' ') for summary in decoded_summaries]
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
        score = metric.compute()
        return score
    
    def evaluate(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        dataset = load_from_disk(self.config.data_path)
        rouge_names = ['rouge1', 'rouge2', 'rougeL', 'rougeLsum']
        rouge_metric = load_metric('rouge')
        score = self.calculate_metric_on_test_data(dataset['test'], rouge_metric, model, tokenizer)
        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)
        df = pd.DataFrame(rouge_dict, index=['Peagsus Model'])
        df.to_csv(self.config.metric_file_name, index=False)
