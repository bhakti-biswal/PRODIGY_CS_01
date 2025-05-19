def caesar_cipher(text,shift_value,mode):
    result=""
    if mode=="encrypt":
        for i in text:
            if i.isalpha():
                base=ord("A") if i.isupper() else ord("a")
                result=result+chr(((ord(i) - base) + shift_value )%26 + base)
            else:
                result=result+i
    else :
        for i in text:
            if i.isalpha():
                base=ord("A") if i.isupper() else ord("a")
                result=result+chr(((ord(i) - base) - shift_value )%26 + base)
            else:
                result=result+i
    return result

def main():
    text=input("Enter text:")
    shift_value=int(input("Enter shift value :"))
    mode=input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt text:").lower()
    if mode not in ["encrypt","decrypt"]:
        print("Invalid mode selection")
        return 
    final_result=caesar_cipher(text,shift_value,mode)
    print(final_result)
    
if __name__=='__main__':
    main()

    


