import pickle as pkl
alphabet_list = pkl.load(open('D:/workspace/python/ocr_detect/ocr/recognize/alphabet.pkl','rb'))
alphabet = [ord(ch) for ch in alphabet_list]
print(alphabet_list[263])
print(alphabet[263])
