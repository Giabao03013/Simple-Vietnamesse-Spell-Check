import pickle
import re
data = pickle.load(open('Data/Data.pkl','rb'))

alphabet = '^[ _abcdefghijklmnopqrstuvwxyz0123456789áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ!\"\',\-\.:;?_\(\)]+$'
training_data=[]
vocab_to_int = {}
count = 0


for character in data:
    if character not in vocab_to_int:
        vocab_to_int[character] = count
        count += 1

codes = ['<PAD>','<EOS>','<GO>']
for code in codes:
    vocab_to_int[code] = count
    count += 1
vocab_size = len(vocab_to_int)
print(len(data), len(set(i for i in data)))
print(len(training_data))

print("The vocabulary contains {} characters.".format(vocab_size))
print(sorted(vocab_to_int))