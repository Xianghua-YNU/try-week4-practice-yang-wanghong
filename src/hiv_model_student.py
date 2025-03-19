import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        # TODO: 初始化模型参数
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta


    def viral_load(self, time):
        # TODO: 计算病毒载量
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

def plot_model(self, time):
        # TODO: 绘制模型曲线
        viral_load = self.viral_load(time)
        plt.plot(time, viral_load)
        plt.xlabel('Time (days)')
        plt.ylabel('Viral Load')
        plt.title('HIV Viral Load Model')
        plt.show()

def load_hiv_data(filepath):
    # TODO: 加载HIV数据
    try:
        data = np.loadtxt(filepath)
        return data['time_in_days'], data['viral_load']
    except:
        return np.loadtxt(filepath, delimiter=',', unpack=True)

def main():
    # TODO: 主函数，用于测试模型
   # 初始化模型参数
    model = HIVModel(A=1000, alpha=0.5, B=500, beta=0.1)
    
    # 生成时间序列
    time = np.linspace(0, 10, 100)
    
    # 计算并绘制模型曲线
    model.plot_model(time)
    
    # 加载实验数据
    time_data, load_data = load_hiv_data('data/HIVseries.npz')
    
    # 绘制实验数据
    plt.scatter(time_data, load_data, label='Experimental Data')
    plt.legend()
    plt.show()

if __name__ == "__main__":
        main()
