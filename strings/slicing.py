def slic(var, delimit):
    i = var.find(f"{delimit}")
    sflo = var[i+1:]
    print(sflo)


if __name__ == "__main__":
    slic('X-DSPAM-Confidence:0.8475',":" )

# str = 'X-DSPAM-Confidence:0.8475'
# i = str.find(":")
# print(i, len(str))
# sflo = str[19:]
# print(sflo)