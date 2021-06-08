data = "From abc@gmail.com Sat Jul 6 5:03:56 2021"
at = data.find("@")
print(at)
space = data.find(" ",at)
print(space)
provider = data[at+1 : space]
print(provider)

#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

#Option 1

text = "X-DSPAM-Confidence:    0.8475"
dot = text.find("0")
a=text[23:]
print(float(a))

#Option 2

text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(":")
print(ipos)
piece = text[ipos1+:]
print(piece)
value = float(piece)
print(value)


