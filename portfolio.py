import pandas as pd

def loadInvestments(filename):
    investments = pd.read_csv(f'{filename}.csv')
    investOptions= []
    
    for i in range(1, len(investments)):
        investOptions.append([investments['RegionName'].iloc[i], investments['Zhvi'].iloc[i], investments['10Year'].iloc[i]])
    
    return investOptions

def optimizeInvestments(investOptions, money):
    roi = [[0 for i in range(money + 1)] for i in range(len(investOptions) + 1)]
    
    for i in range(len(investOptions) + 1):
        for w in range(money + 1):
            if i == 0 or w == 0:
                roi[i][w] = 0
            
            elif investOptions[i-1][1] <= w:
                roi[i][w] = max(investOptions[i-1][2]
                          + roi[i-1][w - investOptions[i-1][1]],  
                              roi[i-1][w])
       
            else:
                roi[i][w] = roi[i-1][w]
    
    #Tracing back values of investments
    returnInvest = roi[len(investOptions)][money]
    print("Estimated Return on Investment is ", round(returnInvest*100, 2),"%")
    print("Actual Investments are: ") 
    
    for i in range(len(investOptions), 0, -1):
        if returnInvest <= 0:
            break

        if returnInvest == roi[i - 1][w]:
            continue
        
        else:
            print(investOptions[i - 1][0])
             
            returnInvest = returnInvest - investOptions[i - 1][2]
            w = w - investOptions[i - 1][1]


if __name__ =="__main__":
    optimizeInvestments(loadInvestments('State_Zhvi_Summary_AllHomes'), 1000000)
