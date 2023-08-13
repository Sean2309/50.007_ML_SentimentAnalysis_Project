import math

class BeamSearchSentimentAnalyzer:
    def __init__(self, beam_width=5):
        self.beam_width = beam_width
        self.word_sentiment_probs = {}
    
    def processFile(file: list):
        return [word[:len(word)-1] for word in file]

    def getSentences(input_data):
        return [sentence for sentence in [group.split('\n') for group in '\n'.join(input_data).split('\n\n')] if sentence != ['']]
        
    def load_sentiment_data(self, data_path):
        with open(data_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) >= 2:
                    word = parts[0]
                    sentiment = parts[1]
                    self.word_sentiment_probs[word] = {sentiment: 1.0}  # Set initial probability to 1.0
                else:
                    print(f"Skipped line: {line}")  # Print a message for lines with less than 2 parts


    def beam_search_predict(self, text, tags):
        sequences = [([], 0.0)]

        for word in text.split(" "):
            new_sequences = []
            for sequence, score in sequences:
                for sentiment in tags:
                    new_score = score + (1.0 if self.word_sentiment_probs.get(word) == sentiment else 0.0)
                    new_sequences.append((sequence + [(word, sentiment)], new_score))
            
            new_sequences.sort(key=lambda x: x[1], reverse=True)
            sequences = new_sequences[:self.beam_width]
        
        best_sequence, _ = sequences[0]
        return best_sequence

if __name__ == "__main__":
    beam_search_model = BeamSearchSentimentAnalyzer(beam_width=5)
    beam_search_model.load_sentiment_data('Data/ES/train')  # Replace with your sentiment data file


    with open("Data/ES/train", "r", encoding="utf-8") as f:
        raw_data = f.readlines()
        processed_data = [word[:len(word)-1] for word in raw_data]
        sentiment_data = ' '.join([item.split()[0] for item in processed_data if item])
        
    print(sentiment_data[0:100])
    tags = ["O","B-positive","B-neutral","B-negative","I-positive","I-neutral","I-negative"]
    
    best_sequence = beam_search_model.beam_search_predict(sentiment_data, tags)
    for word, sentiment in best_sequence:
        print(f"Word: {word}, Sentiment: {sentiment}")
