from sys import stdin

def main():
    messages = [message for message in stdin]
    for i, message in enumerate(messages):
        print(f'[{i}] -> {message}', end='')

if __name__ == '__main__':
    main()
    