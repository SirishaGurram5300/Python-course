#####coding for shopping mall bill
saree=450
dress=600
jeans=800
teashirt=150
tops=200
shoes=350
print("################## welcome to CMR shopping mall for women#####################")
name=input("Enter your name: ")
ph_num=int(input("Enter your phone number"))
saree_c=int(input("Enter no.of sarees:"))
tops_c=int(input("Enter no.of tops: "))
shoes_c=int(input("Enter no.of shoes you buy: "))
jeans_c=int(input("Enter the no.of jeans: "))
dress_c=int(input("Enter the no.of dresses : "))
teashirt_c=int(input("Enter the no.of tea shirts: "))
bill=(saree*saree_c)+(tops_c*tops)+(shoes_c*shoes)+(jeans*jeans_c)+(dress*dress_c)+(teashirt*teashirt_c)
if bill>=5000:
    dis=bill*35/100
elif bill>=4000:
    dis=bill*30/100
elif bill>=3000:
    dis=bill*20/100
elif bill>=2000:
    dis=bill*10/100
else:
    dis=bill*5/100
bill=bill-dis
gst=bill*12/100
totbill=bill+gst
print("############## bill amount  ###############")
print("NAME: ",name)
print("PH_NUMBER: ",ph_num)
print("discount: ",dis)
print("GST: ",gst)
print("The total bill is ",int(totbill))
print("###########################################")


