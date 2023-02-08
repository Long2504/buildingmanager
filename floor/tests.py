from django.test import TestCase

# Create your tests here.
A = "static/image/floor/t1.as"
b = A.split("/")[1] + "/" + A.split("/")[2] + "/" + A.split("/")[3]
print(b)