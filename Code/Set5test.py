import os
i=1

for i in range(25,51):
    print(i)
    os.system(f'python eval.py --model checkpoint_bn_1_4/model_epoch_bn_{i}.pth --dataset Set5 --cuda')

    #i+=1
