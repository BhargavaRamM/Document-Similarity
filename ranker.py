import glob
import math
import os
from sys import argv


class SimDocs:
    # method to build a vocabulary from file
    def __init__(self, path, file):
        self._path = path
        self._file = file
        pass

    def build_vocab(self, file_name):
        vocab = {}
        with open(file_name, 'r') as f:
            doc = f.read().replace("\n", " ")
        for word in doc.split(" "):
            if word in vocab:
                vocab[word] = vocab[word] + 1
            else:
                vocab[word] = 1
        return vocab

    # This function reads all the files in a directory and places them in a list
    # This list is later used to iterate to compute the similarities
    def read_dir(self, path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files

    # This function calculates the simple cosine distance between two documents.
    # Each document is considered as a vector and cosine similarities are calculated
    def similarity(self, vocab1, vocab2):
        val = 0
        for word, count in vocab1.items():
            if word in vocab2:
                val = val + count * vocab2[word]
        if self.document_value(vocab1) * self.document_value(vocab2) != 0:
            return val / (self.document_value(vocab1) * self.document_value(vocab2))
        else:
            return 0

    # This function reads all the documents in a directory
    def read_docs(self, path):
        files = glob.glob(path)
        doc_set = {}
        files = [f for f in os.listdir(path) if os.path.isfile(os, path.join(path, f))]
        return files

    # This function calculates the document value by considering the word frequencies.
    # A simple magnitude of each vector is calculated basing on the vocab.
    def document_value(self, vocab):
        value = 0
        for word, count in vocab.items():
            value = value + count ** 2
        return math.sqrt(value)

    # This function builds a vocabulary when a document is provided as a string rather than providing its file name

    def build_vocab_doc(self, doc):
        vocabulary = {}
        for word in doc.split(" "):
            if word in vocabulary:
                vocabulary[word] = vocabulary[word] + 1
            else:
                vocabulary[word] = 1
        return vocabulary

    def main(self):
        docs = {}
        path = argv[1]
        print path
        files = [f for f in os.listdir(self._path) if os.path.isfile(os.path.join(self._path, f))]
        docs_set = []
        for i in range(len(files)):
            file_path = self._path+str(files[i])
            print file_path
            with open(file_path,'rb') as d:
                data = d.read().replace("\n", " ")
                docs_set.append(data)
        for i in range(len(docs_set)):
            docs[i] = docs_set[i]
        docs_list = []

        doc_given = self.build_vocab(self._file)
        for i in range(len(docs)):
            sim = self.similarity(doc_given, self.build_vocab_doc(docs[i]))
            if sim != 0:
                docs_list.append(i)
        similarity_doc = {}
        for i in range(len(docs)):
            s = self.similarity(doc_given, self.build_vocab_doc(docs[i]))
            similarity_doc[i] = s
        for i, v in similarity_doc.items():
            print("Similarity between given doc and current doc is : ", (i, v))
        return similarity_doc


if __name__ == '__main__':
    print("Hello!!")
    similarity_doc_list = SimDocs(argv[1],argv[2]).main()
