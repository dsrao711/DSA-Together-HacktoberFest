from collections import Counter

def calc_char_freq(string):
   freq_count = Counter(string) 
   #print(freq_count)
   #print(freq_count.keys())
   for key in freq_count.keys():
      if freq_count.get(key) > 1: 
         print("(" + key + ", " + str(freq_count.get(key)) + ")")
    
myStr = 'Hello World. Let’s learn DSA '    
calc_char_freq(myStr)