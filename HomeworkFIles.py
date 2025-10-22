homework_read = open('Codingal.txt', 'r')
print("Reading data from the file - ")
print(homework_read.read())
homework_read.close()

homework_write = open('Codingal.txt', 'w')
homework_write.write("File is now in write mode...")
homework_write.write("Hello! My name is Ahmad, I am 11 years old, and live in Islamabad, Pakistan! I love coding!")
homework_write.close()

homework_append = open('Codingal.txt', 'a')
homework_append.write("\nFile switched to append mode...")
homework_append.write(" I am Ahmad's friend, let me enter the chat.")
homework_append.close()