import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_expl(df,cols):
    for col in cols:
        print("Churn distribution by {}".format(col))
        fig,axes= plt.subplots(1,2,figsize = (10,3))
        sns.histplot(
           x = df[col], 
           hue=df['Churn'], 
           multiple="stack",
           stat = 'percent',
           shrink = 0.5, 
           common_norm=False,ax = axes[0],palette=['#BBC4A9','#B1A9C4']
        )
        for val in axes[0].containers:
            axes[0].bar_label(val,label_type="center",fmt='%.f%%')

        sns.barplot(data=df,x=col,y='TotalCharges',estimator= lambda x:len(x)/len(df) * 100,ax=axes[1],palette=['#BBC4A9','#B1A9C4'],)
        for val in axes[1].containers:
            axes[1].bar_label(val,label_type="center",fmt='%.f%%')
        plt.show()
        
def cdf_plot(df,cols):
    for col in cols:
        print("Churn distribution by {}".format(col))
        sns.ecdfplot(data=df,x=col,hue='Churn',palette=['#BBC4A9','#B1A9C4'])
        plt.show()

