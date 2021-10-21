# 4. Write a program that can perform a letter frequency attack on any monoalphabetic 
# substitution cipher without human intervention. Your software should produce possible
# plain text in rough order of likelihood. It would be good if your user interface allows user to specify " 
# Give me top 10 possible plain texts"


import copy

def letter_frequency_attack(S, N):
  
  plain_Text = [None] * 10       # Variable to store first 10 possible deciphered plain texts
  
  freq = [0] * 26               # Variable to store the frequency of each letter in cipher text
  
  decending_frequency = [None] * 26      
 
  used_words = [0] * 26

  for i in range(N):
      if S[i] != ' ':
          freq[ord(S[i]) - 65] += 1
      
  decending_frequency=copy.deepcopy(freq)

  decending_frequency.sort(reverse = True)
  # T Stores the string formed from concatanating the english letter in the decreasing frequency in the
  # english language    
  T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
 
  for i in range(10):
      ch = -1
      
      for j in range(26):
          if decending_frequency[i] == freq[j] and used_words[j] == 0:
              used_words[j] = 1
              ch = j
              break
      if ch == -1:
          break
     
      x = ord(T[i]) - 65
      
      x = x - ch        # Calculate the probable shift used_words
                        # in monoalphabetic cipher
      
      new_plain_text = ""
      # Generate the probable ith plain_Text
      # string using the shift calculated above
      for k in range(N):
          # Insert whitespaces as it is
          if S[k] == ' ':
              new_plain_text += " "
              continue
          # Shift the kth letter of the
          # cipher by x
          y = ord(S[k]) - 65
          y += x
          if y < 0:
              y += 26
          if y > 25:
              y -= 26
          # Add the kth calculated/shifted
          # letter to temporary string    
          new_plain_text += chr(y + 65)
      plain_Text[i] = new_plain_text
  return plain_Text
def main():
    encrypted_word = input("\nEnter the encrypted message: ")
    print("\nFirst 10 possible plain texts are : ")
    text_list=letter_frequency_attack(encrypted_word,len(encrypted_word))
    print(*text_list,sep='\n')
if __name__ == '__main__':
    main()
