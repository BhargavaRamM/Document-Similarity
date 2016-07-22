import numpy as np
import math
import glob
import os
from os import walk
import operator


class SimDocs:

	"""This function builds a vocabulary of words present in a document.
	Here instead of passing document as a string, a file name is provided."""
	def build_vocb(fileName):
		vocab = {}
		with open(fileName,'r') as file:
			doc = file.read().replace("\n"," ")
		for word in doc.split(" "):
			if word in vocab:
				vocab[word] = vocab[word]+1
			else:
				vocab[word] = 1
		return vocab
	"""This function reads all the files in a directory and places them in a list. 
	This list is later used to iterate to compute the similarities"""
	def read_dir(self,path):
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
		return files

	"""This function calculates the simple cosine distance between two documents. 
	Each document is considered as a vector and cosine similarities are calculated"""
	def similarity(vocab1,vocab2):
		relevance = 0
		val = 0
		for word, count in vocab1.items():
			if word in vocab2:
				val = val + count*vocab2[word]
		if(SimDocs.document_value(vocab1)*SimDocs.document_value(vocab2)!= 0):
			return val/(SimDocs.document_value(vocab1)*SimDocs.document_value(vocab2))
		else:
			return 0
	"""This function reads all the documents in a directory"""
	def read_docs(self,path):
		files = glob.glob(path)
		doc_set = {}
		files = [f for f in os.listdir(path) if os.path.isfile(os,path.join(path, f))]
		return files

	"""This function calculates the document value by considering the word frequencies.
	A simple magnitude of each vector is calculated basing on the vocab."""
	def document_value(vocab):
		value = 0
		for word,count in vocab.items():
			value = value+count**2
		return math.sqrt(value)
	"""This function builds a vocabulary when a document is provided as a string rather than providing its file name."""
	def build_vocab_doc(doc):
		v = {}
		for word in doc.split(" "):
			if word in v:
				v[word] = v[word] + 1
			else:
				v[word] = 1
		return v
	"""All Hell Breaks Loose. This function pretty much does the heavy lifting."""
	def main():
		docs = {}
		path = "C:\\Users\\Bhargava Ram\\Documents\\GitHub\\Document-Similarity\\poem\\"
		'''docs = read_dir(path)'''		
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
		docs_set = []
		for i in range(len(files)):
			with open(files[i]) as d:
				data = d.read().replace("\n"," ")
				docs_set.append(data)
		for i in range(len(docs_set)):
			docs[i] = docs_set[i]
		vocabs = {}
		docs_list = []
		print("Provide the path to the given document:")
		document_path = input("document path: ")
		doc_given = SimDocs.build_vocb(document_path)			
		for i in range(len(docs)):
			sim = SimDocs.similarity(doc_given,SimDocs.build_vocab_doc(docs[i]))
			print("Similarity of given doc and current doc is: ",sim)
			if(sim != 0):
				print("the document relevant to the given doc is: ",i)
				docs_list.append(i)
		similarity_doc = {}
		for i in range(len(docs)):
			s = SimDocs.similarity(doc_given,SimDocs.build_vocab_doc(docs[i]))
			similarity_doc[i] = s
		for i,v in similarity_doc.items():
			print("Similarity between given doc and current doc is : ",(i, v))
		return similarity_doc

if __name__ == '__main__':
	print("Hello!!")
	doc_list = SimDocs.main()
	for i,v in doc_list.items():
		print(i,v)
	for w in sorted(doc_list, key=doc_list.get, reverse = True):
		print ("Doc Id is: ",w,"---"," and Similarity is: ", doc_list[w])
	

