print("hello world")
df = pd.read_excel(location, sheet_name='Sheet1')
C1=df.columns[0]
C2=df.columns[1]
C3=df.columns[2]
C4=df.columns[3]
C5=df.columns[4]
C8=df.columns[7]
C9=df.columns[8]
C10=df.columns[9]

Transactor=list(df[C1])
Purpose=list(df[C2])
in_Pesos=list(df[C3])
Date=list(df[C4])
Remarks=list(df[C5])

Owner=list(df[C8])
Amount=list(df[C9])
PC=list(df[C10])

distribution=[]
transactions=[]
totalshares=[]
dist_temp=[]
