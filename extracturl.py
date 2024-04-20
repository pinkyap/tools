import re

def extract_urls_from_file(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Use regular expressions to find URLs in the content
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)

    # Print the extracted URLs
    for url in urls:
        print(url)

if __name__ == "__main__":
    # Ask the user to enter the file path
    file_path = input("Enter the path to the text file: ")
    # Call the function to extract URLs
    extract_urls_from_file(file_path)


#how to run ?
# python extracturls.py 
#Enter the path to the text file: ferox.txt   
