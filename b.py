

n_num = [12,14,14,15,16,17,18]
n = len(n_num)
if n%2 == 0:
   median1 = n_num[n//2]
   median2 = n_num[n//2-1]
   median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("median is:" + str(median))
