import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of program")
num = []
sum = 0
for i in range(3):
    logging.debug(f"i = {i}")
    print("Enter a number to add:")
    n = int(input())
    logging.debug(f"{n} added.")
    num.append(n)
    logging.debug(f"num is {num}")
    sum += num[i]
    logging.debug(f"sum = {sum}")
    

logging.debug("End of program")
