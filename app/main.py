import sys,os

if len(sys.argv) > 1:
    curr_fold = 0
    if str(sys.argv[1]) == 'init':
        curr_fold = os.getcwd()
        os.system(f"python {curr_fold}\init_data.py")
    elif str(sys.argv[1]) == 'start':
        curr_fold = os.getcwd()
        os.system(f"uvicorn web:app --reload && cd {curr_fold}")
    else:
        print(sys.argv)
        print(f'''
            Ouch!

            I don't know such a parameter
        ''')
else:
    print(f'''
        Sorry, i need some parameter:
        - init (to initialize data)
        - start (to start web-app)

        Nice to see u
    ''')
