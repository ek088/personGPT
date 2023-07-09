import os
from pdf_loader import pdf_load
from pineconeDB import search_in_pinecone_without_context

DOCS_DIR_PATH = 'docs/'
def pdf_load_cyc():
    """
    starts cycle with load PDFs menu
    """
    print('input name of pdf file from "docs" directory')
    print('or input "/exit" to return to main menu')
    while True:
        cyc_menu_value = input('file name: ')

        if cyc_menu_value == '/exit':
            break

        if os.path.isfile(f'{DOCS_DIR_PATH}{cyc_menu_value}'):

            pdf_load(f'{DOCS_DIR_PATH}{cyc_menu_value}')
        else:
            print('file not found')

def conversation_cyc():
    "starts cycle with chatGPT-pinecone chain conversation"
    print('input your query or /exit to leave chat')

    while True:
        query = input('query: ')

        if query == '/exit':
            break

        output = search_in_pinecone_without_context(query)
        print(f"\n{output}")



while True:
    print('''chose function:\n
    - [1] Load file
    - [2] Conversation
    /exit - to stop program
    ''')

    value = input('chose... ')

    if value == '/exit':
        break
    elif value == '1':
        pdf_load_cyc()
    elif value =='2':
        conversation_cyc()
    else:
        print('command does not exists')
