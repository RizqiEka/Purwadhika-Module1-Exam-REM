#EXAM 1
#Contoh Pilihan Input

input1 = "Hello there how are you doing"
input2 = "   Hello    World    "
input3 = ""
input4 = "  Welcome   to   the First  Purwhadika    Exam"
input5 = "        Purwadhika      Digital      School"
#input untuk testing kondisi lebih dari 140 karakter
input6 = "    I       want       to     test     more    than    140      chars                                                                        !!!!"

#Function Construction

def Hashtag(string):

    #Pengecekan Kondisi Input & Split String based on " "
    if string == "" :
        return False
    #Pengecekan Kondisi Input & Split String lebih dari 140 karakter atau tidak
    elif len(string) > 140 :
        return False
    #Split string ke dalam list
    else:
        lst = string.split(" ")

    #Penggabungan ke dalam string diawali "#"
    hash = "#"
    for a in range(len(lst)):
        hash += str(lst[a]).capitalize()
    
    return hash

Hashtag(input4)


#EXAM 2
#Contoh Pilihan Input

input1 = [1,2,3,4,5,6,7,8,9,0]
input2 = [3,4,5,1,2,3,0,9,5,6]
input3 = [0,4,5,1.6,2.6,3.5,0,5.5,11,6] #input untuk testing kondisi integer
input4 = [-1,4,5,1,2,3,11,9,5,6] #input untuk testing range 0-9

#Function Construction

def create_phone_number(number):

    #Untuk Pengecekan Kondisi Input - Integer atau tidak
    for a in number:
        if type(a) != int:
            return "Please re-enter your number, no decimal number"
    #Untuk Pengecekan Kondisi Input - 10 Digit atau tidak
    if len(number) != 10:
        return "Please re-enter your number, 10 digits only"
    #Untuk Pengecekan Kondisi Input - antara 0 hingga 9 atau tidak 
    if max(number) > 9 and min(number) < 0:
        return "Please re-enter your number, only from 0-9"
    else:
    #Untuk Breakdown Input dan Reformat kedalam Format Phone Number
        a,b,c = number[0:3]
        d,e,f = number[3:6]
        g,h,i,j = number[6:]
    return ("({}{}{}) {}{}{}-{}{}{}{}".format(a,b,c,d,e,f,g,h,i,j))


create_phone_number(input4)


#EXAM 3
#Contoh Pilihan Input

input1 = [1,3,8,4,5,2]
input2 = [2,0,5,7,8,9,1,11]
input3 = [3,5,2,0,7,9,99,85,76,20,25,31]
input4 = []

#Function Construction

def sort_odd_even(num):
    even = []
    even_index = []
    odd = []
    odd_index = []

    #Untuk Memisahkan Ganjil dan Genap ke dalam list berbeda
    for number in num:
        if number % 2 == 0 or number == 0:
            even.append(number)
            even_index.append(num.index(number))
        else:
            odd.append(number)
            odd_index.append(num.index(number))
        
    #Untuk Mengurutkan Ganjil dan Genap, namun masih dalam list berbeda
    for i in range(len(even)):
        for j in range(i+1, len(even)):
            if even[i] < even[j]:
                even[i], even[j] = even[j], even[i]

    for i in range(len(odd)):
        for j in range(i+1, len(odd)):
            if odd[i] > odd[j]:
                odd[i], odd[j] = odd[j], odd[i]

    #Untuk Menggabungkan Ganjil dan Genap beserta indeksnya, dan mengkonversinya ke List of Tuples
    even_and_odd = even + odd
    even_and_odd_index = even_index + odd_index
    combined_list = list(zip(even_and_odd_index, even_and_odd))

    #Untuk Mengurutkan List of Tuples berdasarkan indeks Ganjil-Genap
    for i in range(len(combined_list)):
        for j in range(i+1, len(combined_list)):
            if combined_list[i] > combined_list[j]:
                combined_list[i], combined_list[j] = combined_list[j], combined_list[i]
    
    #Untuk Meng-unzip List dari List of Tuples
    return [j for i,j in combined_list]


sort_odd_even(input1)