# python3
import sys
#import time

def read_input():
    
    rezims = input("Režīms:")
    
    if rezims.startswith('I'):
        pattern = input().rstrip()
        text = input().rstrip()
        
    elif rezims.startswith('F'):
        fails = open("./tests/" + "06", "r")
        pattern = fails.readline().rstrip()
        text = fails.readline().rstrip()
   
    if 1 <=len(pattern) <= len(text) <= 5*10**5:
        if all([c.isalpha() and ord(c) < 128 for c in pattern]) or all([i.isalpha() and ord(i) < 128 for i in text]):   
            return (pattern, text)
        else: 
            print("wrong input")
            sys.exit()
    else:
        print("wrong input")
        sys.exit()

    
def print_occurrences(output):
   
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    output = []
    pattern_len = len(pattern)
    text_len = len(text)

    p = 0
    t = 0
    sum_pattern = 0

    for i in range(pattern_len):
        p = p * 256 + ord(pattern[i])
        t = t * 256 + ord(text[i])
    
    for i in range(text_len-pattern_len+1):
        if p == t:
            if text.startswith(pattern,i):
                output.append(i)
                sum_pattern = sum_pattern + 1
        if i < text_len-pattern_len:
            t = (t - ord(text[i]) * 256**(pattern_len-1)) * 256 + ord(text[i+pattern_len])

    if sum_pattern > 10**8:
        print("wrong input")
        sys.exit()
    else: 
        return output

if __name__ == '__main__':
    #start_time = time.time()
    print_occurrences(get_occurrences(*read_input()))
    #print(time.time() - start_time)

