import torch
import numpy as np

x = torch.ones(2,2, dtype=torch.double)
print(x.dtype)

x = torch.tensor([2.5,0.1])
print(x)
y = torch.rand(2,2)
print(y)

z = x+y # elementwise addition
print(z)

z = torch.add(x,y) # same as x+y
print(z)

y.add_(x) # trailing underscore = inplace operation
print(y)

x = torch.randn(5,3)
print(x)
print(x[:,0]) # first column of all rows
print(x[1,:]) # second row of all columns
print(x[:,1]) # second column of all rows
print(x[1,1]) # second element of second row
print(x[1,1].item()) # second element of second row

x = torch.rand(4,4)
y = x.view(16)
print(y)
y = x.view(-1,8)
print(y.size())

a = torch.ones(5)
print(a)
b = a.numpy() #convert tensor to numpy array
print(b)
print(type(b))