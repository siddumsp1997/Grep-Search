#import the necessary packages
import sys  
import os
import time
from subprocess import Popen
from subprocess import PIPE
from nltk.tokenize import word_tokenize

#main function
def main():  


   	queries = open("IR_Assignment1/query.txt",'r')

	for query in queries:

		#print(query)
		start_time = time.time()

		#query = query.rstrip('\n') 
		result = set()

		cnt = 0

		#tokens = word_tokenize(query)
		tokens = query.split(' ')

		query_no = int(tokens[0])

		#Removing the first element in the list
		tokens.pop(0)

		#print(tokens)

		for token in tokens:

			grep_search =Popen(["grep",'-lr',token,'IR_Assignment1/alldocs'],stdout=PIPE)

			grep_result =str(grep_search.stdout.read())

			#print(grep_result)

			#splitting it line by line 
			record = grep_result.split("\n")

			if cnt != 0:
				result = result & set(record)

			else:
				result = set(record)
				cnt = cnt + 1


		final_result = list(result)

		end_time = time.time()
		time_diff = end_time - start_time

		#open output file in append mode
		output_file1 = open('grep_time_calc.txt','a')
		output_file2 = open('grep_output.txt','a')

		output_file1.write(str(query_no)+"  Query search time = "+str(time_diff)+" secs\n")

		print("Query = '"+query+"' | Execution time = "+str(time_diff)+"\n")
		#output_file1.write("Grep search results:\n")
    	
		result_count = 0
		for results in final_result :

			if results != "":

        		#take out the filepath
				filepath = results.split("/")
        		#the last element is the file name
				filename = str(filepath[-1]) 

				#output_file1.write(str(query_no)+"  "+filename+"\n")
				output_file2.write(str(query_no)+"  "+filename+"\n")

				result_count += 1
		
		#if result_count==0:
		#	output_file1.write("--empty--\n")

		output_file1.close()
		output_file2.close()
		

	queries.close()




if __name__ == '__main__':  
	main()
