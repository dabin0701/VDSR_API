import torch
import torch.nn as nn
from math import sqrt
"""
class Conv_ReLU_Block_0519(nn.Module):
    def __init__(self):
        super(Conv_ReLU_Block, self).__init__()
        self.conv = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1=nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        
    def forward(self, x):
        return self.relu(self.bn1(self.conv(x)))
"""   
class Conv_ReLU_Block(nn.Module):
    def __init__(self):
        super(Conv_ReLU_Block, self).__init__()
        self.conv = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1=nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        
    def forward(self, x):
        return self.relu(self.bn1(self.conv(x)))  
        
class Conv_ReLU_Block_RES(nn.Module):
    def __init__(self):
        super(Conv_ReLU_Block_RES, self).__init__()
        self.conv = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1=nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        
    def forward(self, x):
    
        temp = x
        """
        x = self.conv(x)
        x = self.bn1(x)
        x = self.relu(x)
        return x 
        """
        x = self.relu(self.bn1(self.conv(x)))    
        x = temp + x
        return x

        
         
class Net(nn.Module):
    def __init__(self, my_experiment, residual_bn):
        super(Net, self).__init__()
        if my_experiment == 1:
            self.repeat_num = 18
        elif my_experiment == 2:
            self.repeat_num = 24
        elif my_experiment == 3:
            self.repeat_num = 12
        elif my_experiment == 4:
            self.repeat_num = 30
        
        if residual_bn == 0:
            self.residual_layer = self.make_layer(Conv_ReLU_Block, self.repeat_num)
        elif residual_bn == 1:
            self.residual_layer = self.make_layer(Conv_ReLU_Block_RES, self.repeat_num)
        self.input = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        self.output = nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1, bias=False)
        self.relu = nn.ReLU(inplace=True)
    
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, sqrt(2. / n))
                
    def make_layer(self, block, num_of_layer):
        layers = []
        for _ in range(num_of_layer):
            layers.append(block())
        return nn.Sequential(*layers)

    def forward(self, x):
        residual = x
        out = self.relu(self.input(x))
        out = self.residual_layer(out)
        out = self.output(out)
        out = torch.add(out,residual)
        return out
 
