import pandas as pd
with open('fishing.data') as f:
        lst = []
        for ele in f:
            line = ele.replace('\n','').split(' ')
            sublst=[]
            
            lst.append(line)
Headers=['Fish', 'Wind', 'Air','Water','Sky']
df = pd.DataFrame(lst, columns =Headers) 

def count(data,colname,label,target):
    condition = (data[colname] == label) & (data[Headers[0]] == target)
    return len(data[condition])
total_data=14
total_yes=count(df,'Fish','Yes','Yes')
total_no=count(df,'Fish','No','No')
def probabilities(colname,param,Fish):
    if Fish=='Yes':
        param_yes=count(df,colname,param,Fish)
        return param_yes/total_yes
    if Fish=='No':
        param_no=count(df,colname,param,Fish)
        return param_no/total_no
def all_probabilities(instances):
    P_yes=float(total_yes/total_data)
    P_no=float(total_no/total_data)
    c=1
    prob_yes=1
    prob_no=1
    for inst in instances:
        prob_yes*=probabilities(Headers[c],inst,'Yes')
        prob_no*=probabilities(Headers[c],inst,'No')
        c=c+1
    
    class_yes=P_yes*prob_yes
    class_no=P_no*prob_no
    if class_yes>class_no:
        take,val= class_yes,'Yes'
    else:
        take,val= class_no,'No'
    return (take/(class_yes+class_no))*100,val

instances=['Strong','WarmAir','Cold','Sunny']
def NaiveBAyes(instances):
 return all_probabilities(instances)





 