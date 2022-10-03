import pandas as pd

data = pd.read_csv (r'C:\Users\Админ\Desktop\Папки\кредитный скоринг\credit_train.csv')
df = pd.DataFrame(data, columns= ['Loan ID','Customer ID','Loan Status','Current Loan Amount','Term','Credit Score','Annual Income','Years in current job','Home Ownership','Purpose','Monthly Debt','Years of Credit History','Months since last delinquent','Number of Open Accounts','Number of Credit Problems','Current Credit Balance','Maximum Open Credit','Bankruptcies','Tax Liens'])
print (df)

