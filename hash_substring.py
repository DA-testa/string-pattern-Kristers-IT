import time
def read_input():
    
    rezims = input("Režīms:")

    if rezims.startswith('I'):
        pattern = input().rstrip()
        text = input().rstrip()
        
    elif rezims.startswith('F'):
        fails = open("./tests/" + "06", "r")
        pattern = fails.readline().rstrip()
        text = fails.readline().rstrip()
        
    return (pattern, text)
    
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    output = []
    #start_time = time.time()

    pattern_len = len(pattern)
    text_len = len(text)

    sum_ = pattern_len + text_len
    h=1
    for i in range(pattern_len-1):
        h = ((h*pattern_len)-1) % sum_

    p = 0
    t = 0
    for i in range(pattern_len):
        p = (pattern_len*p + ord(pattern[i])) % sum_
        t = (pattern_len*t + ord(text[i])) % sum_

    for i in range(text_len-pattern_len+1):
        if p == t:
            for j in range(pattern_len):
                if text[i + j] != pattern[j]:
                    break
            else:
                output.append(i)
        if i < text_len-pattern_len:
            t = (pattern_len*(t-ord(text[i])*h)) + ord(text[i+pattern_len]) % sum_

            

    #print(time.time() - start_time)
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable

    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

