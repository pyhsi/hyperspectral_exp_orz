load('/media/luo/result/hsi/extracted_data/SAdata.mat');
load('/media/luo/result/hsi_kernels_r/SA_2/exp_O\data.mat');
aa = zeros(16,1);
a(n) = max(test_acc);
for i = 0:15
    index = (test_label == i);
    result = test_prediction(index);
    num = sum(index);
    correct = sum(result == i);
    aa(i+1,1) = correct / num;
end
t_a = max(test_acc);