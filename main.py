import os
EMAIL = os.environ['KQEMAIL']
PASSWORD = os.environ['KQPASS']

def main():
    print EMAIL
    print PASSWORD

if __name__ == '__main__':
    main()